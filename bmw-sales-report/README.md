# BMW Sales Report Automation 🚙

This project automates the creation of an Excel sales report and visualizations from the BMW Worldwide Sales (2010–2024) dataset.
It generates pivot-like summaries across multiple dimensions (year, region, model, fuel type) and produces charts for quick insights.

---

## 📂 Project Structure
- `BMW sales data (2010-2024).csv` → Raw dataset downloaded from Kaggle  
- `ExcelAutomationwithPython.py` → Script for automated report generation and visualization  
- `bmw_sales_report.xlsx` → Final Excel report (multi-sheet: yearly sales, region, top models, fuel type)  
- `yearly_sales.png` → Line chart of BMW yearly sales volumes  
- `sales_by_region.png` → Bar chart of regional sales comparison  
- `top_10_models.png` → Bar chart of top 10 BMW models by sales volume  
- `avg_price_by_fuel.png` → Bar chart of average car price grouped by fuel type

---

## 🛠 Tech Stack
- **Python**   
- **Pandas** → Data wrangling & Excel export  
- **OpenPyXL** → Excel automation  
- **Matplotlib** → Charts and visualizations
  
---

## 🚀 Features
- **Data Cleaning & Transformation**  
  - Handles missing values and converts numeric fields (`Year`, `Sales_Volume`, `Price_USD`).
- **Automated Reports**  
  - Yearly Sales Trends  
  - Regional Sales Comparison  
  - Top 10 BMW Models by Sales  
  - Average Price by Fuel Type
- **Excel Export**  
  - All results saved into `bmw_sales_report.xlsx` with multiple sheets.
- **Data Visualization**  
  - Line chart: Yearly sales volume  
  - Bar charts: Sales by region, Top 10 models, Avg. price by fuel type  

---

# 📊 BMW Sales Visualizations

You can find visual summaries generated from the **BMW Sales Report Automation** project.  
Each chart highlights different business insights derived from the dataset *(2010–2024)*.

---

## 1️⃣ Yearly Sales Trend
<img width="1418" height="788" alt="yearly_sales" src="https://github.com/user-attachments/assets/173b61f6-bde6-46b6-b84c-31260415ef6e" />
📌 *BMW sales show the yearly trend, helping identify growth or decline periods.*

## 2️⃣ Sales by Region
<img width="1422" height="842" alt="sales_by_region" src="https://github.com/user-attachments/assets/55951e19-11aa-45c1-86fc-07489be4e175" />
📌 *Reveals which regions contribute most to BMW’s global sales volume.*

## 3️⃣ Top 10 Models by Sales
<img width="1419" height="878" alt="top_10_models" src="https://github.com/user-attachments/assets/390cd161-9473-4b11-8184-e7370d1b070a" />
📌 *Highlights the most popular BMW models worldwide, showcasing customer preferences.*

## 4️⃣ Average Price by Fuel Type
<img width="1275" height="698" alt="avg_price_by_fuel" src="https://github.com/user-attachments/assets/f705401a-9a06-499c-885d-996bdd6de384" />
📌 *Compares the pricing across petrol, diesel, electric, and hybrid BMWs, showing clear pricing tiers.*

## Notes
- All charts were created automatically using **Matplotlib**.  
- They are directly linked to the CSV dataset and will update whenever new data is added.  
- These visualizations complement the Excel report (`bmw_sales_report.xlsx`) for a more **data-driven business overview**.

---
## ▶️ How to Run
```bash
# Install dependencies
pip install pandas openpyxl matplotlib
# Ensure the CSV is named
BMW sales data (2010-2024) (1).csv
# Run scraper 
python ExcelAutomationwithPython.py





