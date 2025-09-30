# 📚 Advanced Web Scraping – Books to Scrape  

This project shows advanced **web scraping with Python**, targeting the [Books to Scrape](https://books.toscrape.com) demo website.  
The scraper collects detailed product information (books) and exports results into multiple structured files for further analysis.  

---

## Project Description  
- Crawls all book pages from `books.toscrape.com`.  
- Extracts structured data including:  
  - **Title**  
  - **Price (incl. tax)**  
  - **Rating (converted to numeric 1–5)**  
  - **Number of Reviews**  
  - **Availability (in stock or not)**  
  - **UPC**  
  - **Product Type**  
  - **Description**  
- Exports the results into:  
  - Excel file (`export.xlsx`)  
  - Text log files with URLs and errors  
  - Individual HTML snapshots of product pages  
  - Image URLs  

---

## ⚙️ Tech Stack  
- **Python**  
- **Libraries:** `requests`, `lxml`, `pandas`, `tqdm`, `openpyxl`, `re`, `time`, `random`  

---

## 📂 Output Files  
- `export.xlsx` → Main dataset with all book details.  
- `url_unit.txt` → List of all scraped product URLs.  
- `error_log.txt` → Captures failed requests and errors.  
- `2_data_unit_urls.txt` → Duplicate export of collected URLs.  
- `3_data_unit_urls.html` → Clickable list of scraped product pages.  
- `5_image_urls.txt` → Collected image URLs of books.  

---

## ▶️ How to Run  

```bash
# Install dependencies
pip install requests lxml pandas tqdm openpyxl

# Run the scraper
books-to-scrape.py
