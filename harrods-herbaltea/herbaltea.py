"""
Advanced Web Scraping with Python
Exercise 12
Advanced scraping
"""

"""
Task: Your task is to open the following website with the help of Selenium:
    https://www.harrods.com/en-gb/tea

Follow the steps to scrape the latest "Tea Bags" sub-category using Selenium:
    - Check for pre-requisites to scrape
    - Click away the cookie notice
    - Use the filter menu of the website to select the category "Tea Bags"
    - Then sort the selection by "Newest".
    - After this filtering, regularly scrape all the remaining results using Selenium.

Attributes are:
    - title_string
    - brand_string
    - price_gbp_float
    - color_string
    - size_string
    - url_product_string

Finally, export the data as an Excel file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm.auto import tqdm
import time, random, pandas as pd
from urllib.parse import urljoin

# Variables
url_start = "https://www.harrods.com/en-gb/tea"
url_base = "https://www.harrods.com"
url_list = [] # list of product URLs (will be filled below)

log_error = [] # keeps request / element failures
data = [] # will hold one dict per product
next_page = True # checks if there is a next page button
page_index = 1 # page index for pagination

time_sleep_min = 1 # min. pause between requests (sec)
time_sleep_max = 3 # max. pause between requests (sec)


# Start Selenium
driver = webdriver.Chrome()
wait = WebDriverWait(driver,15)
driver.get(url_start)

# Click away cookie notices
try:
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="didomi-notice-agree-button"]')))
    driver.find_element(By.XPATH,'//*[@id="didomi-notice-agree-button"]').click()
except:
    pass

# Click category herbal teas
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filter-category-body"]/div/div[1]/ul/li[2]/a')))
driver.find_element(By.XPATH, '//*[@id="filter-category-body"]/div/div[1]/ul/li[2]/a').click()
time.sleep(3)

# Click selector option newest
driver.find_element(By.XPATH, '//*[@id="plp-body"]/div/div[1]/div[2]/div[2]/div/select/option[3]').click()
time.sleep(3)
# Wait until the product grid is visible
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="plp-body"]')))

# Get full page dimensions
full_page_height = driver.execute_script("return document.body.scrollHeight")
full_page_width = driver.execute_script("return document.body.scrollWidth")

# Set browser window to full page size
driver.set_window_size(full_page_width, full_page_height)

# Save screenshot
driver.save_screenshot("herbal_tea.png")
print("Screenshot saved: herbal_tea.png")

# Crawling
print("\n Crawling")
page_url = url_start
while next_page:

    print(f"\n Crawling page: {page_index}")

    if page_index == 1:
        pass
    else:
        try:
            driver.get(page_url)
        except Exception as e:
            log_error.append({
                'step': "Crawling",
                'timestamp': pd.Timestamp.now(),
                'url': page_url,
                'exception': e
            })
            print(log_error[-1])
            page_index += 1
            time.sleep(random.randint(time_sleep_min,time_sleep_max))
            continue

# Wait for product boxes to be present
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="plp-body"]')))
    # Filter for all product boxes urls
    product_boxes = driver.find_elements(By.XPATH, '//article[@class="flex h-full w-[177px] flex-col sm:w-[232px] lg:w-[235px] xl:w-[306px]"]/a')
    # Extract URLs from product boxes
    for tag in product_boxes:
        href = tag.get_attribute("href")
        if href:
            url_list.append(urljoin(url_base, href))

 # Check for the next page button
    try:
        next_text = driver.find_element(By.XPATH, '(//span[@data-test-id="headline"])[last()]').text.strip()

        if next_text == "NEXT":
            wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@aria-current="page"])[last()]')))
            next_button = driver.find_element(By.XPATH, '(//a[@aria-current="page"])[last()]')

            next_button_url = next_button.get_attribute("href")
            page_url = urljoin(url_base, next_button_url)
        else:
            next_page = False
            print("\n No more pages to crawl.")
    except Exception as ex:
        log_error.append(f"Next page button not found: {ex}")
        print(log_error[-1])
        next_page = False

    page_index += 1
    time.sleep(random.randint(time_sleep_min,time_sleep_max))

print("\n url_list: \n", url_list)
print(f"\n Number of Data Unit URLs: {len(url_list)}")
print(f' First product url: {url_list[0] if url_list else "No products found"}')
print(f' Last product url: {url_list[-1] if url_list else "No products found"}')


# Parsing
print("\n Parsing:")

for data_unit_url in tqdm(url_list, "Parsing"):
    try:
        driver.get(data_unit_url)
    except Exception as e:
        log_error.append({
            'step': "Parsing",
            'timestamp': pd.Timestamp.now(),
            'url': data_unit_url,
            'exception': e
        })
        print(log_error[-1])
        time.sleep(random.randint(time_sleep_min,time_sleep_max))
        continue

    # Wait for the page to load
    try:
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/div/div/section')))
    except Exception as e:
        pass

# 1) Extract product_title
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/h1/span[2]')))
        title_string = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/h1/span[2]').text.strip()
    except Exception as e:
        title_string = None

    # 2) Extract brand
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/h1/span[1]')))
        brand_string = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/h1/span[1]').text.strip()
    except Exception as e:
        brand_string = None

    # 3) Extract price_gbp
    import re

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/div/div/p/span/span[2]')))
        price_text = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/div/div/p/span/span[2]').text.strip()
        price_gbp_float = float(re.sub(r"[^\d.]", "", price_text))
    except Exception as e:
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/div/div/p/span/span[1]')))
            price_text = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[1]/div/div/div/p/span/span[1]').text.strip()
            price_gbp_float = float(re.sub(r"[^\d.]", "", price_text))
        except Exception as e:
            price_gbp_float = None

    # 4) Extract color
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[2]/div[1]/div/span')))
        color_string = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/div/section/div[1]/div[2]/div/div[2]/div[1]/div/span').text.strip()
    except Exception as e:
        color_string = None

    # 5) Extract size
    try:
        select_size = wait.until(EC.visibility_of_element_located((By.XPATH, '//select[starts-with(@id, "select-")]')))
        size_string = ", ".join(
            opt.text.strip() for opt in select_size.find_elements(By.XPATH, ".//option") if opt.text.strip())
    except Exception as e:
        size_string = None

    # Extract Quantity
    try:
        quantity_select = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//select[starts-with(@id, "select-")]')))[1]
        quantity_options = [opt.text.strip() for opt in quantity_select.find_elements(By.TAG_NAME, "option") if opt.text.strip()]
    except Exception as e:
        quantity_options = None


    # Create a dictionary for the current product
    data_unit_dict = {
        "title_string": title_string,
        "brand_string": brand_string,
        "price_gbp_float": price_gbp_float,
        "color_string": color_string,
        "size_string": size_string,
        "url_product_string": data_unit_url,
        "quantity_options": quantity_options
    }

    # Append the dictionary to the data list
    data.append(data_unit_dict)

    # Sleep to avoid overwhelming the server
    time.sleep(random.randint(time_sleep_min, time_sleep_max))

# DataFrame generation
df1 = pd.DataFrame(data)
print(df1.head()) # sadece ilk 5 ürün için bunu kullan
# print(df1) tüm ürünleri görmek için bunu kullan

# Export as an Excel file
df1.to_excel("export_herbaltea.xlsx", index=False)

# Print data unit URLs
print("\n--- Data Unit URLs ---")
print(f"Total URLs collected: {len(url_list)}")

if url_list:
    print(f"First URL: {url_list[0]}")
    print(f"Last URL: {url_list[-1]}")
else:
    print("No product URLs collected.")

# Print error log
print("\n--- Error Log ---")
print(f"Total errors: {len(log_error)}")

if log_error:
    for error in log_error:
        print(error)
else:
    print("No errors encountered.")

# Error file
filename = "1_error_log.txt"

with open(filename, "w", encoding="utf-8") as f:
    if log_error:
        for error in log_error:
            f.write(str(error) + "\n")
    else:
        f.write("No errors occurred.")

print(f"Error log saved to: {filename}")

# data unit url txt
filename = "2_data_unit_urls.txt"

with open(filename, "w", encoding="utf-8") as f:
    for url in url_list:
        f.write(url + "\n")

print(f"Data unit URLs saved to: {filename}")

# data unit html
# Create a DataFrame from the URL list
df = pd.DataFrame(url_list, columns=["product_url"])

# Save to HTML with index and no header
df.to_html("3_data_unit_urls.html", index=True, header=False)

print("Data unit URLs saved to: 3_data_unit_urls.html")
