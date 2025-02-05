import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Ratings = []
Descriptions = []

# Flipkart may block bot-like requests, so we add headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

for i in range(1, 12):  # Loop through 11 pages
    url = f"https://www.flipkart.com/search?q=mobiles+under+20000&page={i}"
    r = requests.get(url, headers=headers)  # Send request with headers
    soup = BeautifulSoup(r.text, "lxml")

    # Find the main container
    box = soup.find("div", class_="DOjaWF gdgoEp")  # Update class as per Flipkart HTML

    if not box:
        print(f"Page {i}: No box found. Skipping...")
        continue  # Skip this page if box is not found

    # Extract Product Names
    names = box.find_all("div", class_="KzDlHZ")
    for name in names:
        Product_name.append(name.text.strip())

    # Extract Prices
    prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for price in prices:
        Prices.append(price.text.strip())

    # Extract Descriptions
    desc = box.find_all("ul", class_="G4BRas")
    for des in desc:
        Descriptions.append(des.text.strip())

    # Extract Ratings
    rating = box.find_all("div", class_="XQDdHH")
    for rate in rating:
        Ratings.append(rate.text.strip())

# Create DataFrame
df = pd.DataFrame({"Product Name": Product_name, "Price": Prices, "Ratings": Ratings, "Descriptions": Descriptions})

# Save to CSV file


#print(df)
print((len(Product_name), len(Prices), len(Ratings), len(Descriptions))
)
df.to_csv("flipkart_mobiles.csv", index=False, encoding="utf-8")
