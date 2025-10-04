### INF601 - Advanced Programming in Python
### Jamie Smith
### Mini Project 2
 
 
# Project Title
 
MiniProject 2 - Vulnerability Charts
 
## Description
 
This project analyzes a dataset of reported security vulnerabilities using Python, Pandas, and Matplotlib. The dataset contains information such as vulnerability title, date, severity, summary, and reference link.

The primary goal of the project is to answer the questions:
“How have security vulnerabilities trended over time, and how do they break down by severity?”

To explore this question, the program:

- Loads the dataset into a Pandas DataFrame for structured analysis.

- Cleans the data by handling missing values and standardizing severity labels.

- Generates basic statistics on vulnerabilities by severity and over time.

- Creates a variety of visualizations that help interpret the data, including:

- A horizontal bar chart showing vulnerability counts by severity.

- A pie chart showing the distribution of vulnerabilities by severity.

- A vertical bar chart showing severity counts with color coding.

- A line chart showing the monthly trend of reported vulnerabilities.

- A bar chart showing monthly counts for easier comparison.

- Saves all charts as .png images in a dedicated charts/ folder.

- Pauses briefly between charts so the user can view each visualization.

This project demonstrates working with external data sources, cleaning and analyzing data in Python, and visualizing results with Matplotlib. It provides both statistical summaries and visual insights that make the patterns in the vulnerability data clear and easy to understand.
 
## Getting Started
 
### Dependencies
 
* Please install the pip requirements
```
pip install -r requirements
```

### Executing program
 
* Download the Security Vulnerabilities Dataset from https://www.kaggle.com/datasets/ighoshsubho/security-vulnerabilities-dataset
* Extract the Security Vulnerabilities.csv file located inside the .zip file
* Copy Security Vulnerabilities.csv into a folder within the project. Ensure the folder is named data
* Then run:
```
python main.py
```

## Authors
 
Jamie Smith
 
## Version History
 
* 0.1
    * Initial Release
 
# Acknowledgments
 
Inspiration, code snippets, etc.
* [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)
* chatgpt using the HutchCC business subscription - Chat available upon approved request