import requests
import json
API_KEY = "sRG5lgwCHbQhNxh8rYXscXegp7BtLSVq9UQAuxxk"
SEARCH_QUERY = "pepperoni" #Replace with the food. Will add a loop later on.

search_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
search_params = {
    "api_key": API_KEY,
    "query": SEARCH_QUERY,
    "pageSize": 1
}

search_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
search_params = {
    "api_key": API_KEY,
    "query": SEARCH_QUERY,
    "pageSize": 1
}

search_response = requests.get(search_url, params=search_params)
search_data = search_response.json()


fdc_id = search_data["foods"][0]["fdcId"]


detail_url = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}"
detail_params = {"api_key": API_KEY}
detail_response = requests.get(detail_url, params=detail_params)
detail_data = detail_response.json()

#nutrients are expandable
target_nutrients = [
    "Energy", 
    "Protein", 
    "Total lipid (fat)", 
    "Carbohydrate, by difference",
    "Fiber, total dietary"
]

nutrients = {}

for nutrient in detail_data.get("foodNutrients", []):
    name = nutrient.get("nutrient", {}).get("name")
    amount = nutrient.get("amount")
    unit = nutrient.get("nutrient", {}).get("unitName")

    if name in target_nutrients:
        nutrients[name] = f"{amount} {unit}"

#display
print(f"\n🥄 Nutritional Info for: {SEARCH_QUERY}")
for n in target_nutrients:
    print(f"{n}: {nutrients.get(n, 'N/A')}")
