import pandas as pd
import numpy as np

def clean_agent_data(txns_df, agents_df):
    df = txns_df.copy()
    master_agents = agents_df.copy()
    log = {}
    
    initial_rows = len(df)
    df = df.drop_duplicates()
    log["duplicates_removed"] = initial_rows - len(df)
    
    df["txn_type"] = df["txn_type"].astype(str).str.strip().str.capitalize()
    
    df["txn_date"] = df["txn_date"].astype(str).str.replace("/", "-")
    df["txn_date"] = pd.to_datetime(df["txn_date"], format="%Y-%m-%d")
    
    df["amount"] = df["amount"].replace(["N/A", "nan", "None", ""], np.nan)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    
    missing_mask = df["amount"].isna()
    log["missing_amounts_imputed"] = missing_mask.sum()
    
    median_amounts = df.groupby("txn_type")["amount"].transform("median")
    df["amount"] = df["amount"].fillna(median_amounts)
    df["amount_imputed"] = missing_mask
    
    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df["is_outlier"] = (df["amount"] < lower_bound) | (df["amount"] > upper_bound)
    log["outliers_tagged"] = df["is_outlier"].sum()
    
    clean_df = pd.merge(df, master_agents, on="agent_id", how="left")
    log["unknown_agent_transactions"] = clean_df["county"].isna().sum()
    
    return clean_df, log
