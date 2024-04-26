import pandas as pd
import sweetviz as sv
df = pd.read_csv("dataset/menu.csv")

my_report = sv.analyze(df)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"