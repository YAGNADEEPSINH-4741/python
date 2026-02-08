import os
import requests

def get_github_streak(username):
    token = input("Enter GitHub Token: ").strip()

    if not token:
        print("GITHUB_TOKEN not found in environment variables")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    query = """
    query($login:String!) {
      user(login:$login) {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """

    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": {"login": username}},
        headers=headers
    )

    if response.status_code != 200:
        print("GitHub API error")
        return

    data = response.json()
    weeks = data["data"]["user"]["contributionsCollection"][
        "contributionCalendar"
    ]["weeks"]

    days = []
    for week in weeks:
        for day in week["contributionDays"]:
            days.append(day["contributionCount"])

    # Longest streak
    longest = 0
    temp = 0
    for c in days:
        if c > 0:
            temp += 1
            longest = max(longest, temp)
        else:
            temp = 0

    # Current streak
    current = 0
    for c in reversed(days):
        if c > 0:
            current += 1
        else:
            break

    print(f"GitHub Username : {username}")
    print(f"🔥 Current Streak : {current} days")
    print(f"🏆 Longest Streak : {longest} days")


# ---- RUN ----
username = input("Enter GitHub username: ").strip()
get_github_streak(username)
