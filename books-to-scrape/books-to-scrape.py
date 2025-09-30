"""
Advanced Web Scraping with Python
"""
from pydoc import html

"""
# 1
# Scrape all the books from the website https://books.toscrape.com and export them to an Excel file.
# Required variables: title, price, rating, reviews, available, available_copies, upc, type, description.
# Hint: At the end of this task, you should have a Pandas DataFrame containing all this information.
# Hint: Be careful with correctly encoding the data unit server r1.


# 2 - Optional
# Check the DataFrame for errors using the Pandas df.describe() method.
# Google for the ydata-profiling module and install it. Check the required Python version before.
# Export an HTML profile report to get a dataset overview.
"""

# importing the necessary libraries for web scraping, parsing, regular expressions, data handling (with pandas),
# progress tracking (tqdm), delays (time), and Excel exporting (openpyxl).

from lxml import html
import re
import pandas as pd
from tqdm.auto import tqdm
import time
import random
import openpyxl
from urllib.parse import urljoin
import requests

url_list = [] # will store all product URLs
data = [] # will store parsed book data
start_url = "https://books.toscrape.com"
limit_crawling = 1  # to limit pages during testing
sleep_time_min = 1
sleep_time_max = 2
error_log = []

#  Initial request to get page structure and total number of pages
try:
    r1 = requests.get(start_url)
    tree1 = html.fromstring(r1.content)
except requests.RequestException as e:
    print(f"Error during initial request: {e}")
    error_log.append({
        "url": start_url,
        "error": str(e),
        "timestamp": pd.Timestamp.now(),
    })
    exit()
time.sleep(random.randint(sleep_time_min, sleep_time_max))
max_pages = int(tree1.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[1]/text()')[0].strip().split()[-1])
print(f"Max pages found: {max_pages}\n")

# Crawling
# looping over all product listing pages
# The URL format changes only after the first page, so i handle page 1 differently.
for page_id in tqdm(range(1, min(max_pages, limit_crawling) + 1)):
    if page_id == 1:
        page_url = start_url
    else:
        page_url = f"{start_url}/catalogue/page-{page_id}.html"

    try:
        r2 = requests.get(page_url)
        tree2 = html.fromstring(r2.content)
    except requests.RequestException as e:
        print(f"Error during request for page {page_id}: {e}")
        error_log.append({
            "url": page_url,
            "error": str(e),
            "timestamp": pd.Timestamp.now(),
        })
        continue
    # If the request fails, the error is logged and the loop continues to the next page.
    # From each page, I extract product links using XPath, convert them to full URLs, and store them.
    products = tree2.xpath('//h3/a/@href')
    for product_url in products:
        product_url_full = urljoin(page_url, product_url)
        url_list.append(product_url_full)

    time.sleep(random.randint(sleep_time_min, sleep_time_max)) # pausing between requests using time.sleep() to mimic human behavio

print(f"\n{len(url_list)} product URLs found.")
print(f"First product URL: {url_list[0]}")
print(f"Last product URL: {url_list[-1]}")

with open("url_unit.txt", "w", encoding="utf-8") as f:
    for url in url_list:
        f.write(url + "\n")

# Parsing
# sending requests to each individual product page. Errors are caught and skipped.
for product_url_full in tqdm(url_list):
    try:
        r3 = requests.get(product_url_full)
        tree3 = html.fromstring(r3.content)
    except requests.RequestException as e:
        print(f"Error during request for product {product_url_full}: {e}")
        error_log.append({
            "url": product_url_full,
            "error": str(e),
            "timestamp": pd.Timestamp.now(),
        })
        continue

    data.append({
        "title": tree3.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1')[0].text.strip(),
        "price": float(tree3.xpath('//th[text()="Price (incl. tax)"]/following-sibling::td/text()')[0].replace('£', '').strip()),
        "rating": {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}.get(tree3.xpath('//p[contains(@class, "star-rating")]/@class')[0].split()[-1], None),
        "reviews": int(tree3.xpath('//th[text()="Number of reviews"]/following-sibling::td/text()')[0]),
        "available": True if tree3.xpath('//i[contains(@class, "icon-ok")]') else False,
        "available_copies": product_url_full,
        "upc": tree3.xpath('//th[text()="UPC"]/following-sibling::td/text()')[0],
        "type": tree3.xpath('//th[text()="Product Type"]/following-sibling::td/text()')[0],
        "description": tree3.xpath('//div[@id="product_description"]/following-sibling::p[1]/text()')[0].strip(),
        }) # All data is stored in a dictionary and added to the data list.

    time.sleep(random.randint(sleep_time_min, sleep_time_max))

# Export to Excel
# converting the data list into a Pandas DataFrame and export it to an Excel file called export.xlsx.
print("\nExporting to Excel...")
df1 = pd.DataFrame(data)
df1.to_excel("export.xlsx", index=False)
print("Export complete.")

with open("error_log.txt", "w", encoding="utf-8") as f:
    if error_log:
        for error in error_log:
            f.write(f"{error['timestamp']} - {error['url']} - {error['error']}\n")
    else:
        f.write("No errors encountered.\n")

with open("2_data_unit_urls.txt", "w", encoding="utf-8") as f:
    for url in url_list:
        f.write(url + "\n")

with open("3_data_unit_urls.html", "w", encoding="utf-8") as f:
    f.write("<html><body><ul>\n")
    for url in url_list:
        f.write(f"<li><a href='{url}'>{url}</a></li>\n")
    f.write("</ul></body></html>")

for idx, url in enumerate(url_list):
    try:
        r = requests.get(url)
        with open(f"4_data_unit_{idx}.html", "w", encoding="utf-8") as f:
            f.write(r.text)
        time.sleep(random.randint(sleep_time_min, sleep_time_max))
    except Exception as e:
        print(f"Error saving HTML for {url}: {e}")

image_urls = []
for url in url_list:
    try:
        r = requests.get(url)
        tree = html.fromstring(r.content)
        img_src = tree.xpath('//div[@class="item active"]/img/@src')[0]
        full_img_url = urljoin(url, img_src)
        image_urls.append(full_img_url)
    except Exception as e:
        print(f"Error getting image from {url}: {e}")

with open("5_image_urls.txt", "w", encoding="utf-8") as f:
    for img in image_urls:
        f.write(img + "\n")

print("\n All files created successfully.")






