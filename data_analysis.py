import pandas as pd

def calculate_market_share(df):
    total_market = df["Revenue"].sum()
    df["Market Share (%)"] = (df["Revenue"] / total_market) * 100
    return df

def project_revenue(df, growth_rate):
    df["Projected Revenue"] = df["Revenue"] * (1 + growth_rate)
    return df

def tam_sam_som(total_population, penetration_rate, capture_rate, avg_price):
    tam = total_population * avg_price
    sam = tam * penetration_rate
    som = sam * capture_rate
    return {
        "TAM": round(tam, 2),
        "SAM": round(sam, 2),
        "SOM": round(som, 2)
    }
