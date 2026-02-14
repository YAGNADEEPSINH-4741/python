# Write a program to find countries whose area is greater than a given area

country_area = {
    "Russia": 17098242,
    "Canada": 9984670,
    "China": 9596961,
    "United States": 9833517,
    "Brazil": 8515767,
    "Australia": 7692024,
    "India": 3287263,
    "Argentina": 2780400,
    "Kazakhstan": 2724900,
    "Algeria": 2381741
}

try:
    min_area = int(input("Enter minimum area: "))

    print("\nCountries with area greater than", min_area, ":\n")

    found = False

    for country, area in country_area.items():
        if area > min_area:
            print(f"{country:<15} {area}")
            found = True

    if not found:
        print("No countries found.")

except ValueError:
    print("Please enter a valid number.")
