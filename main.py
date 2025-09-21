### INF601 - Advanced Programming in Python
### Jamie Smith
### Mini Project 2



# This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question. This will get you familar with working with datasets and asking questions, researching APIs and gathering datasets. If you get stuck here, please email me!
#
# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

#import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#Define dataframe
df = pd.read_csv("./data/Security Vulnerabilities.csv", index_col=0)

# Variable for columns from df
date_col = "Date"
sev_col = "Severity"

# Create data folder if it does not exist
data = Path('data')
if not data.exists():
    Path(r'data').mkdir()

# Consistent colors for severity levels
severity_colors = {
    "CRITICAL": "red",
    "HIGH": "orange",
    "MODERATE": "gold",
    "LOW": "green"
}

#Display number of vulnerabilities of each severity.
severity = (df[["Severity"]]).value_counts()
critical = severity["Critical"]
high = severity["High"]
moderate = severity["Moderate"]
low = severity["Low"]

# Function to save charts as .png files
# def chart(name):
#     plt.savefig (f'charts/{name}.png')
#     plt.show()

# Create charts folder if it does not exist
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

# Save graphs in directory named charts
def chart(name):
    # Makes the labels fit in the picture
    plt.tight_layout()
    # Saves the chart in the charts directory
    plt.savefig (f'charts/{name}.png')
    # Displays the chart
    plt.show()
    # Closes the chart
    plt.close()

# Count by severity
if sev_col in df.columns:
    # Create new figure 8" W X 5" H
    plt.figure(figsize=(8,5))

    # Count severities
    counts = (
        df[sev_col]
        .astype(str).str.strip().str.upper()
        .replace("", np.nan)
        .dropna()
        .value_counts()
        .sort_index())
    # Match bar colors to severity (fallback to gray if not in dictionary)
    bar_colors = [
    severity_colors.get(sev, "gray")
    for sev in counts.index
    ]

    # Plot with custom colors
    counts.plot(kind="barh", rot=0, color=bar_colors)
    plt.title("Count by Severity")
    plt.title("Count by Severity")
    plt.xlabel("Count"); plt.ylabel("Severity")
    chart("counts_by_severity_horizontal_bar_chart")

if sev_col in df.columns:
    # Create new figure 8" W X 5" H
    plt.figure(figsize=(8,5))

    # Count severities
    counts = (
        df[sev_col]
        .astype(str).str.strip().str.upper()
        .replace("", np.nan)
        .dropna()
        .value_counts()
        .sort_index())

    # Match bar colors to severity (fallback to gray if not in dictionary)
    bar_colors = [
    severity_colors.get(sev, "gray")
    for sev in counts.index
    ]

    # Plot with custom colors
    counts.plot(kind="bar", rot=0, color=bar_colors)
    plt.title("Count by Severity")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    chart("counts_by_severity_bar_chart")

# Monthly count over time
if date_col:
    # Convert Date column to datetime
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    #Drop any rows that are missing dates
    d = df.dropna(subset=[date_col]).copy()
    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    # Filter the data set this chart builds from
    d = df[df["Date"] >= "2022-12-01"]
    if not d.empty:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        monthly = d.groupby("Date").size()
        # Make the chart
        plt.figure(figsize=(9,5))
        monthly.plot(kind="line")
        plt.title("Vulnerabilities Over Time (Monthly)")
        plt.xlabel("Month"); plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        chart("Monthly_over_time")

if date_col:
    # Convert Date column to datetime
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    #Drop any rows that are missing dates
    d = df.dropna(subset=[date_col]).copy()
    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    # Filter the data set this chart builds from
    d = df[df["Date"] >= "2023-08-15"]
    if not d.empty:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        monthly = d.groupby("Date").size()
        # Make the chart
        plt.figure(figsize=(9,5))
        monthly.plot(kind="bar")
        plt.title("Vulnerabilities Over Time (Monthly)")
        plt.xlabel("Month"); plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        chart("Monthly_over_time")
# https://realpython.com/pandas-plot-python/