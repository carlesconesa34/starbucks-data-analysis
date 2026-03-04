# Starbucks Data Analysis

A beginner data analysis project exploring Starbucks business data through Python and SQL, combining exploratory analysis, cleaning and reporting.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Results & Reports](#results--reports)
- [License](#license)

---

## Disclaimer

This project was built as a **learning exercise** by a beginner in data analysis. It may contain errors, suboptimal approaches, or incomplete analyses. It is **not intended to be taken as a serious or professional-grade analysis** in any context.

If you are a recruiter or evaluator reviewing this project, please keep in mind that the primary goal was to practice and develop skills in Python, SQL, and data analysis workflows — not to produce production-ready work.

Feedback and suggestions are always welcome!

---

## Overview

This project performs a basic data analysis on Starbucks datasets, covering data ingestion, cleaning, SQL querying, and insight generation. The goal is to extract meaningful business patterns and trends from raw data, producing structured reports that can support data-driven decision-making.

---

## Project Structure

```
starbucks-data-analysis/
│
├── data/
│   └── raw/                  # Raw input datasets (CSV, JSON, etc.)
│
├── src/                                   # Python source code
│   ├── starbucks_cleaning.py              # Data cleaning script.
│   └── starbucks_exploration.py           # Data exploration script.
│
│
├── sql/                      # SQL query files
│   └── starbucks_cleaning.sql                 # Queries for modifying dataset columns.
│
├── report/                   # Output report and visualizations.
│
├── .vscode/                  # VSCode workspace settings
├── .gitignore
├── requirements.txt          # Python dependencies
└── README.md
```

---

## Tech Stack

| Layer         | Tools / Libraries                        |
|---------------|------------------------------------------|
| Language      | Python                                   |
| Data Analysis | Pandas                                   |
| Visualization | Power BI                                 |
| Database      | SQL (DuckDB)                            |
| Environment   | VSCode                                   |

---

## Getting Started

### Prerequisites

- Python
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/carlesconesa34/starbucks-data-analysis.git
cd starbucks-data-analysis
```

2. **Create and activate a virtual environment** *(recommended)*

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the data processing scripts from the `src/` folder:

```bash
python src/starbucks_exploration.py
python src/starbucks_cleaning.py
```
2. Execute SQL queries found in the `sql/` folder.

3. Generated reports and visualizations will be saved in the `report/` directory.

---

## Data

The `data/raw/` directory contains the source dataset used in this project.

Dataset Source

The dataset used in this project is Starbucks Customer Ordering Patterns, publicly available on Kaggle:

https://www.kaggle.com/datasets/likithagedipudi/starbucks-customer-ordering-patterns

It contains information about customer ordering behaviour at Starbucks, including order patterns and related variables used throughout the analysis.

---

## Results & Reports

All analytical outputs — including charts, tables, and summary reports — are saved in the `report/` directory after running the pipeline.

Key areas of analysis may include:

- Sales trends
- Customer segmentation insights
- Geographic distribution of stores

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

> Built in Python by [carlesconesa34](https://github.com/carlesconesa34)