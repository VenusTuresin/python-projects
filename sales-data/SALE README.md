# 📊 Retail Sales – Real-Life Data Analysis 

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

## 📊 Visualizations & Insights
- **Revenue vs. Profit
<img width="639" height="525" alt="Revenue Profit" src="https://github.com/user-attachments/assets/c1a90c89-0db8-4d04-8c7d-b0e49ffc43d8" />

- There is a strong positive correlation between revenue and profit. High-revenue transactions also generate high profit.
  
- **Top Selling Age Groups
<img width="1033" height="576" alt="Top Selling Age Groups" src="https://github.com/user-attachments/assets/837e665a-ed9a-4f30-9211-3722eecf2ddf" />

- Adults (35–64) form the largest customer group. Young Adults (25–34) follow as the second most important group, while Youth (<25) contribute less to total sales.
  
- **Profit by Age Group

<img width="911" height="567" alt="Profit Age Group" src="https://github.com/user-attachments/assets/57d00c17-2d6e-4423-9d6f-e619d0b0fb1c" />

- Profit distribution shows that Adults (35–64) and Young Adults (25–34) generate the highest profit. Youth and Seniors (64+) contribute significantly less.
  
- **Profit Distribution
  
<img width="1031" height="448" alt="Ekran Resmi 2025-09-26 15 49 28" src="https://github.com/user-attachments/assets/71c0bc8b-223a-4763-b6ad-fa7c3200821a" />

- Profit values are heavily concentrated at lower levels, with a few outliers generating very high profit. This indicates that a small share of transactions contributes disproportionately to total profit (Pareto effect).
  
- **Age Group Distribution
  
<img width="611" height="440" alt="Ekran Resmi 2025-09-26 15 49 42" src="https://github.com/user-attachments/assets/5e332ace-1a2d-4f31-a519-08f8e9450479" />

- The customer base is dominated by Adults (35–64), while Youth (<25) and Seniors (64+) represent smaller market segments.

  
## Output Files
- `Real Life data analysis.ipynb` – main notebook with full workflow  
- `sales_data.csv` – raw dataset (source: FreeCodeCamp) 

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn
# open the notebook and run all cells 
