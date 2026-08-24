# Vendor Performance Analysis

An end-to-end data analytics project focused on analyzing vendor sales, purchasing, profitability, inventory performance, and vendor contribution using Python, SQL, and Power BI.

##  Project Overview

The objective of this project is to analyze vendor-level sales and purchase data to identify high-performing and low-performing vendors, understand profitability, evaluate inventory efficiency, and generate actionable business insights.

The project covers the complete data analytics workflow, including data ingestion, data cleaning, exploratory data analysis, statistical analysis, SQL-based analysis, and interactive dashboard development.

##  Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- SQL
- SQLite
- Power BI
- Jupyter Notebook

##  Project Workflow

1. Data ingestion and database creation
2. Data cleaning and preprocessing
3. SQL-based data aggregation
4. Vendor performance analysis
5. Exploratory Data Analysis (EDA)
6. Statistical analysis
7. Visualization using Python
8. Interactive Power BI dashboard development
9. Business insights and report generation

##  Key Analysis Performed

### Vendor Performance
- Identified the top vendors based on total sales.
- Identified low-performing vendors based on sales performance.
- Compared purchase and sales performance across vendors.
- Analyzed vendor-level gross profit and profit margins.

### Purchase Contribution Analysis
- Calculated each vendor's contribution to total purchases.
- Created cumulative contribution analysis using Pareto analysis.
- Identified the vendors contributing the largest share of total purchases.

### Brand Analysis
- Identified top-performing brands based on sales.
- Analyzed brand-level performance.
- Compared high-performing and low-performing brands.

### Profitability Analysis
- Calculated gross profit and profit margin.
- Compared profit margins between high-performing and low-performing vendors.
- Performed a two-sample t-test to determine whether the difference in profit margins between vendor groups was statistically significant.
- Calculated 95% confidence intervals for vendor profit margins.

### Inventory Analysis
- Analyzed stock turnover to evaluate inventory efficiency.
- Identified vendors with lower stock turnover.
- Examined sales-to-purchase ratios to understand inventory movement.

### Order & Pricing Analysis
- Analyzed purchase prices and actual selling prices.
- Examined unit purchase prices across different order sizes.
- Studied purchasing and sales quantities.

##  Power BI Dashboard

An interactive Power BI dashboard was created to provide a consolidated view of vendor and brand performance.

The dashboard includes:

- Total Sales
- Total Purchases
- Gross Profit
- Profit Margin
- Unsold Capital
- Purchase Contribution %
- Top Vendors by Sales
- Top Brands by Sales
- Low Performing Vendors
- Low Performing Brands
- Vendor/Brand performance analysis

##  Key Insights

The analysis helped identify:

- Vendors contributing the highest share of total sales and purchases.
- Vendors with relatively low sales performance.
- Brands with strong and weak sales performance.
- Differences in profitability between high-performing and low-performing vendors.
- Vendors with inefficient inventory turnover.
- The amount of capital tied up in unsold inventory.
- The concentration of purchase contributions among major vendors.


├── reports/
│   └── Vendor_Performance_Report.pdf
│
├── README.md
└── requirements.txt
