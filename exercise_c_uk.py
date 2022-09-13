united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
for places in united_kingdom:
    if places["name"] == "Wales":
        places["capital"] = "Cardiff"

print(united_kingdom)


# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
new_country = {
    "name": "Norther Ireland",
    "population": 1811000,
    "capital": "Belfast",
}

united_kingdom.append(new_country)
print(united_kingdom)


# 3. Use a loop to print the names of all the countries in the UK.
for places in united_kingdom:
    print(places["name"])

# 4. Use a loop to find the total population of the UK.
total_pop = 0

for places in united_kingdom:
    total_pop += places["population"]

print(total_pop)
