# BMW Sales Report Automation 🚙

This project automates the creation of an Excel sales report and visualizations from the BMW Worldwide Sales (2010–2024) dataset.
It generates pivot-like summaries across multiple dimensions (year, region, model, fuel type) and produces charts for quick insights.

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

## 🛠 Tech Stack
- **Python** 🐍  
- **Pandas** → Data wrangling & Excel export  
- **OpenPyXL** → Excel automation  
- **Matplotlib** → Charts and visualizations  

---

## 📂 Folder Structure
- `BMW sales data (2010-2024).csv` → Raw dataset downloaded from Kaggle  
- `ExcelAutomationwithPython.py` → Script for automated report generation and visualization  
- `bmw_sales_report.xlsx` → Final Excel report (multi-sheet: yearly sales, region, top models, fuel type)  
- `yearly_sales.png` → Line chart of BMW yearly sales volumes  
- `sales_by_region.png` → Bar chart of regional sales comparison  
- `top_10_models.png` → Bar chart of top 10 BMW models by sales volume  
- `avg_price_by_fuel.png` → Bar chart of average car price grouped by fuel type

---

## ▶️ How to Run

### 1) Create & activate virtual environment (optional but recommended)

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

