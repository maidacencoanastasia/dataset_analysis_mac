import pandas as pd
from ydata_profiling import ProfileReport
import warnings

warnings.filterwarnings("ignore")
df = pd.read_csv("dataset/menu.csv")
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("ydata_profiling_report.html")
