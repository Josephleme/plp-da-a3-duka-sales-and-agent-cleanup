# Retail Sales Analytics and Mobile Money Agent Cleanup

## Workspace Summary
This repository contains two data engineering and analysis projects. The first explores a six-month sales dataset for Duka Electronics to rank branch performance and identify key product drivers. The second implements an automated cleaning pipeline to audit, normalize, and validate unreliable transaction logs from a mobile money agent network across five counties.

## Project Structure
* `duka_sales_exploration.ipynb`: The notebook containing sales metrics, filtered datasets, and derived columns.
* `agent_cleanup.ipynb`: The notebook executing the transaction audit engine and county distribution tables.
* `cleaning_pipeline.py`: A reusable script that houses the programmatic data cleaning function.
* `generate_data.py`: The background script used to build the original uncleaned source files.
* `excel/duka_branch_summary.xlsx`: The spreadsheet summary containing SUMIFS tables and XLOOKUP mapping formulas.
* `outputs/premium_online_coast_capital.csv`: Filtered premium online sales records from Nairobi and Mombasa branches.
* `outputs/agent_transactions_clean.csv`: The finalized clean mobile money dataset.

## How to Regenerate Data and Run Notebooks
1. Install the required system packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the generator script to create the base datasets:
   ```bash
   python generate_data.py
   ```
3. Open Jupyter or Google Colab and run every notebook from top to bottom.

## Duka Electronics Executive Summary
* Duka Electronics generated an aggregate total revenue of KES 72,077,600 during the first half of 2026.
* Operational volume reached exactly 1,000 completed orders across all sales channels.
* The Nairobi Central branch stood out as the primary location, managing 368 total orders.
* Financial and transactional performance tracking spanned a continuous timeline of 6 months.
* The business successfully managed consumer market demand across 5 unique product categories.

## Agent Cleanup Record Tracking
* **Initial Raw Transaction Volume:** 612 rows
* **Final Clean Validated Volume:** 601 rows
