import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import pygame
import time
import os
from datetime import date

# ---------------- CONFIG ---------------- #

# File to track last played date
TRACK_FILE = "last_played.txt"

# Delay after laptop start (5 minutes = 300 seconds)
START_DELAY = 300

# Rashi → URL mapping (Divya Bhaskar)
RASHI_URLS = {
    "mesh": "https://www.divyabhaskar.co.in/rashifal/13/today",
    "vrushabh": "https://www.divyabhaskar.co.in/rashifal/2/today",
    "mithun": "https://www.divyabhaskar.co.in/rashifal/3/today",
    "kark": "https://www.divyabhaskar.co.in/rashifal/4/today",
    "sinh": "https://www.divyabhaskar.co.in/rashifal/5/today",
    "kanya": "https://www.divyabhaskar.co.in/rashifal/6/today",
    "tula": "https://www.divyabhaskar.co.in/rashifal/7/today",
    "vrushchik": "https://www.divyabhaskar.co.in/rashifal/8/today",
    "dhanu": "https://www.divyabhaskar.co.in/rashifal/9/today",
    "makar": "https://www.divyabhaskar.co.in/rashifal/10/today",
    "kumbh": "https://www.divyabhaskar.co.in/rashifal/11/today",
    "meen": "https://www.divyabhaskar.co.in/rashifal/12/today",
}

# ---------------- UTIL FUNCTIONS ---------------- #

def already_played_today():
    if not os.path.exists(TRACK_FILE):
        return False
    with open(TRACK_FILE, "r") as f:
        return f.read().strip() == str(date.today())

def mark_played_today():
    with open(TRACK_FILE, "w") as f:
        f.write(str(date.today()))

# ---------------- MAIN LOGIC ---------------- #

def play_rashi_bhavishya():
    # 1️⃣ Decide Chandra Rashi (user input)
    rashi = input(
        "Enter your Chandra Rashi (mesh, vrushabh, mithun, kark, sinh, kanya,\n"
        "tula, vrushchik, dhanu, makar, kumbh, meen): "
    ).strip().lower()

    if rashi not in RASHI_URLS:
        print("Invalid rashi.")
        return

    # 2️⃣ Decide URL
    url = RASHI_URLS[rashi]
    print(f"Fetching horoscope for {rashi.title()}...")

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Failed to fetch data.")
            return

        # 3️⃣ Extract data
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find("div", class_="a6b3d8fe")

        if not content:
            print("Horoscope content not found.")
            return

        text = content.text.strip()

        # 4️⃣ Text-to-Speech
        tts = gTTS(text=text, lang="gu", slow=False)
        tts.save("rashi.mp3")

        # 5️⃣ Play sound
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load("rashi.mp3")
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play()

        print("Playing Rashi Bhavishya...")
        while pygame.mixer.music.get_busy():
            time.sleep(1)

        pygame.mixer.music.stop()
        mark_played_today()
        print("Done.")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)

# ---------------- STARTUP CONTROL ---------------- #

if __name__ == "__main__":
    if already_played_today():
        print("Rashi Bhavishya already played today.")
    else:
        #print("Waiting 5 minutes after system start...")
        #time.sleep(START_DELAY)
        play_rashi_bhavishya()
