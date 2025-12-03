import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df["trigger_time"] = pd.to_datetime(df["trigger_time"])
    return df

def compute_status_rates(df):
    status_counts = df["status"].value_counts()
    total = len(df)

    return {
        "success": status_counts.get("success", 0) / total * 100,
        "failure": status_counts.get("failed", 0) / total * 100,
        "cancelled": status_counts.get("cancelled", 0) / total * 100,
    }

def average_duration(df):
    return df["duration_seconds"].mean()

def daily_status_counts(df):
    return (
        df.groupby(df["trigger_time"].dt.date)["status"]
        .value_counts()
        .unstack(fill_value=0)
    )

def failures_by_author(df):
    return df[df["status"] == "failed"].groupby("author").size()

def author_daily_failures(df):
    return (
        df[df["status"] == "failed"]
        .groupby(["author", df['trigger_time'].dt.date])
        .size()
    )

def find_anomalies(df):
    threshold = df["duration_seconds"].mean() + 2 * df["duration_seconds"].std()
    return df[df["duration_seconds"] > threshold]