import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL for laptops (can change category)
base_url = "https://www.snapdeal.com/search?keyword=laptop&page={}"

headers = {"User-Agent": "Mozilla/5.0"}

filename = "snapdeal_laptops_full.csv"
csv_file = open(filename, "w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["Product Name", "Price", "Rating", "Link"])

for page in range(1, 21):  # Scrape first 20 pages (adjustable)
    print(f"Scraping page {page}...")
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    products = soup.find_all("div", class_="product-tuple-listing")
    if not products:
        print("No more products found.")
        break

    for product in products:
        try:
            name = product.find("p", class_="product-title").text.strip()
        except:
            name = "N/A"

        try:
            price = product.find("span", class_="lfloat product-price").text.strip().replace("₹","").replace(",","")
        except:
            price = "N/A"

        try:
            rating_tag = product.find("div", class_="filled-stars")
            rating = rating_tag["style"].split(":")[1].replace("%","") if rating_tag else "N/A"
        except:
            rating = "N/A"

        try:
            link = product.a["href"]
        except:
            link = "N/A"

        writer.writerow([name, price, rating, link])

    time.sleep(1)  # Be polite, avoid blocking

csv_file.close()
print("Scraping complete! Check snapdeal_laptops_full.csv")
