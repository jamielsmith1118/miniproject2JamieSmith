### INF601 - Advanced Programming in Python
### Jamie Smith
### Mini Project 2
 
 
# Project Title
 
Simple overview of use/purpose.
 
## Description
 
This project analyzes a dataset of reported security vulnerabilities using Python, Pandas, and Matplotlib. The dataset contains information such as vulnerability title, date, severity, summary, and reference link.

The primary goal of the project is to answer the question:
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

 
### Installing
 
* Download the Security Vulnerabilities Dataset from https://www.kaggle.com/datasets/ighoshsubho/security-vulnerabilities-dataset
* Extract file
* Copy Security Vulnerabilities.csv into a folder named data
 
### Executing program
 
* How to run the program
* Step-by-step bullets
```
python main.py
```
 
## Help
 
Any advise for common problems or issues.
```
command to run if program contains helper info
```
 
## Authors
 
Jamie Smith
 
## Version History
 
* 0.1
    * Initial Release
 
# Acknowledgments
 
Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)