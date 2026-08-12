# Olist E-Commerce Business Intelligence & Customer Analytics Platform

## 1. Project Overview

This project develops an end-to-end Business Intelligence, Customer
Analytics, Operations Analytics, and Machine Learning solution using
the Olist Brazilian E-Commerce Public Dataset.

The dataset contains approximately 100,000 real, anonymized commercial
orders from 2016–2018 and provides information across customers,
orders, products, sellers, payments, reviews, delivery, and
geographic dimensions.

The objective of this project is to transform raw multi-table
e-commerce data into actionable business insights that can support
revenue growth, customer retention, product and seller performance,
delivery operations, and customer experience.

---

## 2. Business Context

Olist is an e-commerce marketplace that connects sellers with customers
through online marketplaces in Brazil.

The business generates data across multiple operational areas:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Payments
- Reviews
- Delivery
- Customer Locations
- Product Categories
- Geolocation

Management needs an integrated analytical view of this information to
understand business performance and identify opportunities for
improvement.

---

## 3. Business Problem

The business needs to answer:

- What are the major drivers of revenue and sales?
- Which customers generate the greatest business value?
- How effectively does the company retain customers?
- Which products and categories perform best?
- Which sellers perform best?
- Which sellers or regions experience delivery issues?
- Does delivery performance affect customer satisfaction?
- Which products and categories receive poor customer ratings?
- What factors are associated with customer dissatisfaction?
- Can customer behavior be used for segmentation and prediction?

---

## 4. Project Objectives

The project aims to:

1. Analyze revenue and sales performance.
2. Understand customer behavior and retention.
3. Identify high-value customer segments.
4. Evaluate product and category performance.
5. Evaluate seller performance.
6. Analyze payment and order behavior.
7. Measure delivery and operational performance.
8. Analyze customer reviews and satisfaction.
9. Perform cohort and retention analysis.
10. Build customer segmentation using RFM and K-Means.
11. Develop appropriate predictive machine learning models.
12. Build interactive Power BI dashboards.
13. Translate analytical findings into actionable business recommendations.

---

## 5. Key Business Questions

### 5.1 Revenue & Sales Performance

- What is total sales/revenue?
- How does revenue change over time?
- What is the average order value?
- Which product categories generate the most revenue?
- Which regions generate the most revenue?
- Are there seasonal sales patterns?
- What are the major order-status trends?

### 5.2 Customer Analytics

- How many unique customers are there?
- How many customers make repeat purchases?
- What is the average customer spend?
- What is the customer purchase frequency?
- Who are the highest-value customers?
- Which customer segments generate the most revenue?
- Which customer cohorts have better retention?
- Which customers appear to be becoming inactive?

### 5.3 Product Analytics

- Which products sell the most?
- Which product categories generate the most revenue?
- Which categories have the highest order volume?
- Which categories receive the best and worst reviews?
- Which products have high freight costs?
- Which categories have longer delivery times?

### 5.4 Seller Analytics

- Which sellers generate the most revenue?
- Which sellers process the most orders?
- Which sellers have the best review scores?
- Which sellers have delivery-performance issues?
- Is seller performance associated with customer satisfaction?

### 5.5 Delivery & Operations

- What is the average delivery time?
- What percentage of orders are delivered late?
- Which sellers experience the most delays?
- Which regions experience longer delivery times?
- Which product categories have longer delivery times?
- Does late delivery affect customer review scores?

### 5.6 Customer Experience

- What is the average customer review score?
- Which categories receive the lowest ratings?
- Which sellers receive poor ratings?
- Does delivery delay affect customer satisfaction?
- What patterns are associated with negative reviews?
- What topics appear frequently in negative review text?

### 5.7 Advanced Analytics & Machine Learning

- Can customers be grouped into meaningful segments?
- Which customers are high-value?
- Which customers appear at risk of becoming inactive?
- Can historical customer behavior help predict future behavior?
- Can historical sales data support forecasting?
- Can review text be analyzed using NLP?

---

## 6. Expected Business Outcomes

The project should help identify:

- Major revenue drivers
- High-value customers
- Customer retention opportunities
- Important customer segments
- High-performing products and categories
- High-performing sellers
- Delivery bottlenecks
- Customer satisfaction drivers
- Products/categories associated with poor reviews
- Opportunities for data-driven business improvement

---

## 7. Key Analytical Modules

### Module 1 — Sales & Revenue Analytics

Analyze:

- Revenue
- Orders
- Items sold
- Average Order Value
- Monthly sales
- Sales growth
- Category performance
- Geographic performance

### Module 2 — Customer Analytics

Analyze:

- Customer frequency
- Customer spending
- Repeat purchases
- Customer value
- RFM metrics
- Customer segments
- Retention

### Module 3 — Product & Category Analytics

Analyze:

- Product sales
- Category revenue
- Order volume
- Product pricing
- Freight
- Customer ratings

### Module 4 — Seller Analytics

Analyze:

- Seller revenue
- Seller order volume
- Seller ratings
- Seller delivery performance

### Module 5 — Delivery Analytics

Analyze:

- Delivery duration
- Estimated vs actual delivery
- Late deliveries
- Delivery performance by seller
- Delivery performance by region

### Module 6 — Customer Experience Analytics

Analyze:

- Review scores
- Review distribution
- Low-rated orders
- Delivery vs review relationship
- Review text

### Module 7 — Customer Segmentation

Use:

- RFM Analysis
- K-Means Clustering

Potential segments:

- High-value customers
- Loyal customers
- New customers
- Potential loyalists
- At-risk/inactive customers

### Module 8 — Predictive Analytics

Evaluate appropriate machine learning approaches such as:

- Logistic Regression
- Random Forest
- XGBoost

The final model will be selected based on the business problem,
data suitability, and model performance.

---

## 8. Key KPIs

### Sales KPIs

- Total Revenue
- Total Orders
- Total Items Sold
- Average Order Value
- Monthly Revenue
- Revenue Growth

### Customer KPIs

- Unique Customers
- Repeat Customer Rate
- Average Customer Spend
- Purchase Frequency
- Customer Value
- Retention Rate

### Product KPIs

- Revenue by Category
- Units Sold
- Average Product Price
- Average Review Score
- Freight Cost

### Seller KPIs

- Seller Revenue
- Orders per Seller
- Average Review Score
- Delivery Performance

### Operations KPIs

- Average Delivery Time
- On-Time Delivery Rate
- Late Delivery Rate
- Average Freight Value

### Customer Experience KPIs

- Average Review Score
- Low-Rating Rate
- Review Score by Category
- Review Score by Seller
- Review Score vs Delivery Performance

---

## 9. Technology Stack

### Data Analytics

- SQL
- Python
- Pandas
- NumPy
- Statistics

### Business Intelligence

- Power BI
- DAX
- Data Modeling

### Machine Learning

- Scikit-learn
- K-Means
- Logistic Regression
- Random Forest
- XGBoost

### Data Platforms

- Snowflake
- Azure / Microsoft Fabric

### Development

- VS Code
- Jupyter Notebook
- Git
- GitHub

---

## 10. Project Architecture

Raw Olist Data
        ↓
Data Quality Assessment
        ↓
Data Cleaning & Transformation
        ↓
SQL Database / Data Warehouse
        ↓
Analytical Data Model
        ↓
Python Exploratory Data Analysis
        ↓
Business Analytics
        ↓
Customer Segmentation
        ↓
Predictive Analytics
        ↓
Power BI Dashboards
        ↓
Business Recommendations

---

## 11. Power BI Dashboard Structure

### Dashboard 1 — Executive Overview

- Revenue
- Orders
- Customers
- Average Order Value
- Sales Trends
- Top Categories
- Geographic Performance

### Dashboard 2 — Customer Analytics

- Customer value
- RFM segments
- Repeat customers
- Retention
- Cohort analysis

### Dashboard 3 — Product & Seller Analytics

- Product performance
- Category performance
- Seller performance
- Revenue
- Ratings

### Dashboard 4 — Delivery & Operations

- Delivery time
- Late deliveries
- Seller performance
- Geographic delivery patterns
- Estimated vs actual delivery

### Dashboard 5 — Customer Experience

- Review scores
- Low-rated orders
- Category satisfaction
- Seller satisfaction
- Delivery vs review relationship

### Dashboard 6 — Predictive Analytics

- Customer segments
- Prediction results
- Model performance
- Key ML insights

---

## 12. Data Sources

### Primary Dataset

Olist Brazilian E-Commerce Public Dataset.

The dataset contains approximately 100,000 anonymized commercial
orders from 2016–2018.

The primary datasets include:

- olist_customers_dataset
- olist_orders_dataset
- olist_order_items_dataset
- olist_order_payments_dataset
- olist_order_reviews_dataset
- olist_products_dataset
- olist_sellers_dataset
- olist_geolocation_dataset
- product_category_name_translation

### Optional Additional Dataset

Olist also provides a separate Marketing Funnel dataset.

If incorporated, it will be clearly documented as an additional
data source and analyzed separately from the core transactional data.

---

## 13. Data Limitations

The analysis will only use metrics that are supported by the available
data.

For example:

- True product profit cannot be calculated because reliable product
  cost data is not available.
- Customer demographics will only be analyzed where available.
- Marketing analytics will only be included if the Olist Marketing
  Funnel dataset is incorporated.
- Churn will be defined analytically using customer inactivity rather
  than treated as a confirmed business-provided churn label.

All assumptions and derived metrics will be documented.

---

## 14. Final Deliverables

The project will include:

- Cleaned analytical datasets
- SQL database/schema
- Advanced SQL analysis
- Python EDA
- Customer segmentation
- Cohort and retention analysis
- Predictive ML analysis
- Power BI dashboards
- Data dictionary
- Data architecture
- Business recommendations
- GitHub documentation

---

## 15. Project Success Criteria

The project will demonstrate the ability to:

1. Work with real-world multi-table business data.
2. Identify and resolve data-quality issues.
3. Build relationships between business datasets.
4. Perform advanced SQL analysis.
5. Perform exploratory analysis using Python.
6. Build a professional Power BI data model.
7. Develop meaningful business KPIs.
8. Perform customer segmentation and retention analysis.
9. Build and evaluate appropriate ML models.
10. Communicate analytical findings clearly.
11. Translate data insights into business recommendations.

---

## 16. Final Business Outcome

The final solution will demonstrate an end-to-end Data Analyst workflow:

Business Understanding
→ Data Collection
→ Data Quality
→ SQL
→ Python
→ Data Modeling
→ Business Intelligence
→ Advanced Analytics
→ Machine Learning
→ Visualization
→ Business Recommendations

The objective is to demonstrate practical Data Analytics and
business problem-solving skills using real-world e-commerce data.