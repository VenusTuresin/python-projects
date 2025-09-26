# Retail Sales – Real-Life Data Analysis 📊

## Goal
Understand revenue & profit drivers across products, customer segments, and time.

## Dataset
- `sales_data.csv` – 2013–2016 per-order records  
  *(date, product, quantity, unit cost/price, revenue, profit, customer demographics)*

## Key Questions
1. Which products, categories, and states drive the most **revenue** and **profit**?  
2. How do **age groups** and **gender** differ in basket size and profitability?  
3. What are the **yearly trends** in orders, revenue, and profit?  

## Methods
- Data cleaning & typing (`parse_dates`, categorical types)  
- Feature checks:  
  - `Revenue == Cost + Profit`  
  - `Cost == Quantity * Unit_Cost`  
- Aggregations: `groupby`, pivot tables  
- Visualizations:  
  - Bar charts → top products  
  - Line charts → yearly trend  
  - Boxplots → segment profitability  

## Highlights (Findings & Interpretation)
- **Top 10 products** contribute ~X% of total revenue (clear Pareto effect).  
- **Adults (35–64)** segment shows the *highest average basket size* of **$Y vs Youth $Z**, making them the most profitable customer group.  
- Revenue grew from **2013 → 2016 by N%**, largely driven by *Accessories*.  
- Female customers showed slightly higher frequency in purchases, but **male customers had higher avg profit per order**.  
- Certain states consistently outperformed others, suggesting geographic concentration of demand.  

## Files
- `Real Life data analysis.ipynb` – main notebook with full workflow  
- `sales_data.csv` – raw dataset (source: FreeCodeCamp) 

## How to Run
```bash
pip install pandas numpy matplotlib seaborn
# open the notebook and run all cells 

