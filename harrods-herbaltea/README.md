# ☕ Advanced Web Scraping – Harrods Herbal Tea

This project shows advanced web scraping techniques with **Selenium** and **LXML** to extract product data from the Harrods online shop.  

---

## 📂 Project Structure
- `herbaltea.py` → Scraper for Harrods Herbal Tea  
- `export_herbaltea.xlsx` → Example output file for Herbal Tea  
- `herbal_tea.png` → Screenshot of filtered product page  
- `1_error_log.txt` → Log file that records scraping errors (failed requests, missing elements, etc.) with timestamps  
- `2_data_unit_urls.txt` → Text file containing all product URLs collected during the crawling phase  
- `3_data_unit_urls.html` → HTML file with clickable links to all scraped product URLs for easy manual inspection  

---

## ⚙️ Tech Stack
- **Python**  
- **Selenium** (browser automation)  
- **lxml** (HTML parsing)  
- **pandas** (data processing & export)  
- **openpyxl** (Excel export)  

---

## 📊 Features
- Pre-requirement checks (robots.txt, TOS, cookies)  
- Automatic filtering for **Herbal Tea** categories  
- Sorting by *Newest*  
- Crawling all product pages  
- Extracting product attributes:
  - `title_string`
  - `brand_string`
  - `price_gbp_float`
  - `color_string`
  - `size_string`
  - `url_product_string`  
- Exporting clean dataset to **Excel**

---

## Example Screenshots

### Filtered Herbal Tea Page
<img width="3840" height="1380" alt="herbal_tea_filtered" src="https://github.com/user-attachments/assets/bdc43c40-b027-423c-970d-49eeea88cbd5" />


### Herbal Tea Product Listing
<img width="2400" height="1292" alt="herbal_tea_listing" src="https://github.com/user-attachments/assets/53b7a506-cd2a-4438-bc61-47378419997b" />

---

## Example Output
Sample of the exported dataset (`export_herbaltea.xlsx`):

| title_string         | brand_string | price_gbp_float | color_string | size_string | url_product_string |
|----------------------|--------------|-----------------|--------------|-------------|--------------------|
| Herbal Tea Classic   | Harrods      | 12.00           | Green        | 20 bags     | https://...        |
| Herbal Tea Selection | Twinings     | 15.50           | -            | 40 bags     | https://...        |

---

## ▶️ How to Run
```bash
# Install dependencies
pip install selenium lxml pandas openpyxl tqdm

# Run scraper (choose one)
python herbaltea.py
