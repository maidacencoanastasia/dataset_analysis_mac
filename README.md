# McDonald's Menu Nutritional Analysis

A multi-tool exploratory data analysis (EDA) project examining the nutritional content of McDonald's menu items. The project demonstrates five different analysis approaches — from manual custom visualizations to automated profiling libraries — all applied to the same dataset.

## Dataset

**File:** `dataset/menu.csv`

Contains nutritional information for McDonald's menu items across multiple food categories (Breakfast, Beef & Pork, Chicken & Fish, Salads, Snacks & Sides, Desserts, Beverages, etc.).

| Column | Description |
|---|---|
| `Category` | Menu category (e.g. Breakfast, Salads) |
| `Item` | Name of the menu item |
| `Serving Size` | Serving size in oz / g |
| `Calories` | Total calories |
| `Calories from Fat` | Calories derived from fat |
| `Total Fat` | Total fat in grams |
| `Total Fat (% Daily Value)` | Total fat as % of daily value |
| `Saturated Fat` / `(% DV)` | Saturated fat amount and % DV |
| `Trans Fat` | Trans fat in grams |
| `Cholesterol` / `(% DV)` | Cholesterol amount and % DV |
| `Sodium` / `(% DV)` | Sodium amount and % DV |
| `Carbohydrates` / `(% DV)` | Carbohydrates amount and % DV |
| `Dietary Fiber` / `(% DV)` | Dietary fiber amount and % DV |
| `Sugars` | Sugars in grams |
| `Protein` | Protein in grams |
| `Vitamin A / C / Calcium / Iron (% DV)` | Micronutrient % daily values |

## Project Structure

```
├── dataset/
│   └── menu.csv                    # McDonald's menu nutritional dataset
│
├── manual_analysis.py              # Custom EDA with pandas, seaborn, matplotlib, plotly
├── sweetviz_analysis.py            # Automated EDA report using SweetViz
├── ydata_profiling_analysis.py     # Automated profiling using ydata-profiling
├── autoviz_analyze.ipynb           # AutoViz automated visualization notebook
├── pygwalker_analysis.ipynb        # PyGWalker interactive drag-and-drop analysis
├── oh-mcdonald-s-i-know-all-d.ipynb  # Full exploratory notebook
│
├── SWEETVIZ_REPORT.html            # Generated SweetViz HTML report
├── ydata_profiling_report.html     # Generated ydata-profiling HTML report
│
└── requirements.txt                # Python dependencies
```

## Analysis Approaches

### 1. Manual Analysis (`manual_analysis.py`)
Custom visualizations built from scratch using pandas, seaborn, matplotlib, and plotly. Covers:
- Distribution of food items by category
- Average calories and cholesterol per category
- Average total fat and saturated fat per category
- Mean carbohydrates and dietary fiber per category
- KDE distribution plots for nutrient pairs (Calories/Cholesterol, Total Fat/Cholesterol, Carbohydrates/Dietary Fiber, Vitamins, Calcium/Iron)
- Pearson correlation heatmap across all nutritional features

### 2. SweetViz (`sweetviz_analysis.py`)
Generates a standalone HTML report (`SWEETVIZ_REPORT.html`) with feature statistics, correlations, and distributions in a single command.

### 3. ydata-profiling (`ydata_profiling_analysis.py`)
Produces a detailed HTML profiling report (`ydata_profiling_report.html`) including missing value analysis, univariate distributions, and correlation matrices.

### 4. AutoViz (`autoviz_analyze.ipynb`)
Uses the AutoViz library to automatically select and render the most relevant visualizations for the dataset.

### 5. PyGWalker (`pygwalker_analysis.ipynb`)
Renders an interactive Tableau-style drag-and-drop interface directly inside the Jupyter notebook for ad-hoc exploration.

## Setup & Installation

### Prerequisites
- Python 3.8–3.10 recommended (required by pinned dependency constraints)
- pip

### Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The `requirements.txt` pins specific version ranges for compatibility (e.g. `pandas<2.0`, `matplotlib<=3.7.4`, `xgboost>=0.82,<1.7`). It is recommended to use a virtual environment.

### Create a virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Running the Analyses

### Manual Analysis
```bash
python manual_analysis.py
```

### SweetViz Report
```bash
python sweetviz_analysis.py
# Opens / generates SWEETVIZ_REPORT.html
```

### ydata-profiling Report
```bash
python ydata_profiling_analysis.py
# Generates ydata_profiling_report.html
```

### Jupyter Notebooks
```bash
jupyter notebook
```
Open any of the `.ipynb` files:
- `autoviz_analyze.ipynb`
- `pygwalker_analysis.ipynb`
- `oh-mcdonald-s-i-know-all-d.ipynb`

## Key Dependencies

| Package | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `matplotlib` / `seaborn` | Static plotting |
| `plotly` | Interactive charts |
| `sweetviz` | Automated EDA HTML report |
| `ydata-profiling` | Detailed profiling HTML report |
| `autoviz` | Automatic visualization selection |
| `pygwalker` | Interactive visual analytics in notebooks |
| `scikit-learn` | ML utilities |
| `statsmodels` | Statistical analysis |
| `xgboost` | Gradient boosting (used by AutoViz) |
| `wordcloud` | Word cloud generation |

## Generated Reports

Pre-generated HTML reports are included in the repository and can be opened directly in any browser without running the scripts:

- **[SWEETVIZ_REPORT.html](SWEETVIZ_REPORT.html)** — SweetViz feature summary
- **[ydata_profiling_report.html](ydata_profiling_report.html)** — ydata-profiling detailed report
