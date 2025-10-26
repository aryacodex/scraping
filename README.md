1️⃣ Choose the website and target page

We picked Snapdeal and a specific category: laptops.
The URL we used:

https://www.snapdeal.com/search?keyword=laptop&page=1


keyword=laptop → tells Snapdeal we want laptops

page=1 → page number (we loop through multiple pages)

2️⃣ Send a request to the website
response = requests.get(url, headers=headers)


We ask Snapdeal for the HTML content of the page.

headers with User-Agent makes it look like a real browser (prevents blocks).

3️⃣ Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")


BeautifulSoup converts raw HTML into a structured object we can search.

4️⃣ Find all product blocks
products = soup.find_all("div", class_="product-tuple-listing")


Every product is inside a <div> with a specific class.

find_all returns a list of all products on the page.

5️⃣ Extract product details

For each product:

name = product.find("p", class_="product-title").text.strip()
price = product.find("span", class_="lfloat product-price").text.strip().replace("₹","").replace(",","")
rating_tag = product.find("div", class_="filled-stars")
link = product.a["href"]


name → Product name

price → Product price (₹ removed for analysis)

rating → Extracted from the width percentage of stars (style attribute)

link → Direct product URL

Try/except blocks handle missing data gracefully (so code doesn’t crash).

6️⃣ Save data into a CSV
writer.writerow([name, price, rating, link])


Each product is written as a row in snapdeal_laptops_full.csv

CSV is easy to load into Pandas for EDA.

7️⃣ Handle multiple pages
for page in range(1, 21):


Loops through pages 1 to 20

Fetches more products → bigger dataset → better for EDA

8️⃣ Be polite
time.sleep(1)


Pauses 1 second between page requests

Prevents your IP from being blocked by the website

✅ End result

CSV file with columns: Product Name, Price, Rating, Link

You can now use this data for:

Price distribution

Rating analysis

Top brands

Correlations between price & rating
