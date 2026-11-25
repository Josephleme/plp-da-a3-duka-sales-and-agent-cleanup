import numpy as np
import pandas as pd

def generate_datasets():
    rng_duka = np.random.default_rng(2026)
    n_duka = 1000
    
    duka_branches = ["Nairobi Central", "Mombasa CBD", "Kisumu Mega", "Nakuru West", "Kiambu Town"]
    duka_products = {
        "Premium Laptop": 85000, "Midrange Smartphone": 32000, 
        "Budget Phone": 12000, "Wireless Earbuds": 6500, "Smart Watch": 15000
    }
    prod_names = list(duka_products.keys())
    
    duka_sales = pd.DataFrame({
        "order_id": [f"DK{i:04d}" for i in range(1, n_duka + 1)],
        "branch": rng_duka.choice(duka_branches, n_duka, p=[0.4, 0.2, 0.15, 0.15, 0.10]),
        "product": rng_duka.choice(prod_names, n_duka, p=[0.15, 0.30, 0.25, 0.15, 0.15]),
        "units": rng_duka.integers(1, 5, n_duka),
        "channel": rng_duka.choice(["In-Store", "Online"], n_duka, p=[0.6, 0.4]),
        "order_date": (pd.to_datetime("2026-01-01") + 
                       pd.to_timedelta(rng_duka.integers(0, 181, n_duka), unit="D")).strftime("%Y-%m-%d")
    })
    
    product_base_prices = duka_sales["product"].map(duka_products)
    duka_sales["unit_price"] = (product_base_prices * rng_duka.uniform(0.9, 1.05, n_duka)).round(-2)
    duka_sales.to_csv("duka_sales.csv", index=False)
    print("✔ duka_sales.csv generated successfully.")

    rng = np.random.default_rng(44)
    n = 600
    
    agents = pd.DataFrame({
        "agent_id": [f"AG{i:03d}" for i in range(1, 21)],
        "county": rng.choice(["Nairobi", "Kiambu", "Nakuru", "Mombasa", "Kisumu"], 20),
        "onboarded": pd.date_range("2024-01-01", periods=20, freq="MS").strftime("%Y-%m-%d"),
    })
    
    txns = pd.DataFrame({
        "txn_id": [f"TX{i:05d}" for i in range(1, n + 1)],
        "agent_id": rng.choice(agents["agent_id"], n),
        "txn_type": rng.choice(["Deposit", "withdrawal", "DEPOSIT ", "Withdrawal", "deposit"], n),
        "amount": rng.lognormal(7.5, 0.8, n).round(0).astype(str),
        "txn_date": (pd.to_datetime("2026-03-01") + pd.to_timedelta(rng.integers(0, 60, n), unit="D")).strftime("%Y-%m-%d"),
    })
    
    idx = rng.choice(n, 30, replace=False)
    txns.loc[idx[:15], "amount"] = np.nan
    txns.loc[idx[15:20], "amount"] = "N/A"
    txns.loc[idx[20:25], "amount"] = "250000"
    txns.loc[idx[25:], "txn_date"] = txns.loc[idx[25:], "txn_date"].str.replace("-", "/")
    txns = pd.concat([txns, txns.sample(12, random_state=1)], ignore_index=True)
    txns.loc[rng.choice(len(txns), 8, replace=False), "agent_id"] = "AG099"
    
    agents.to_csv("agents.csv", index=False)
    txns.to_csv("agent_transactions.csv", index=False)
    print("✔ agents.csv and agent_transactions.csv generated successfully.")

if __name__ == "__main__":
    generate_datasets()
