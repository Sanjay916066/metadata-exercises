# 📊 Mini Data Quality Audit

## 📌 Overview
This project performs a structured data quality audit on a messy customer transactions dataset using Python in Google Colab.

## 📂 Dataset
- week2_customer_transactions_messy.csv

## 🧠 Business Use Case
The dataset can be used for:
- Sales tracking
- Customer behavior analysis
- Financial reporting
- Fraud detection

## 🔍 Data Quality Dimensions
The audit evaluates:
- Completeness
- Uniqueness
- Validity
- Consistency
- Integrity

## 📈 KPIs
- Completeness Rate
- Duplication Rate
- Error Rate

## ⚙️ Validation Rules
- Transaction amount must be positive
- Customer ID must not be missing
- Payment methods must be valid and consistent

## 📋 Key Findings
- Invalid transaction amounts (zero or negative)
- Missing customer IDs
- Inconsistent categorical values (payment method, currency, region)
- Mixed date formats

## 🧹 Recommended Cleaning Actions
- Handle missing values
- Remove duplicates
- Standardize categorical values
- Fix date formats
- Validate numerical fields

## 🚀 Tools Used
- Python
- Pandas
- Google Colab
