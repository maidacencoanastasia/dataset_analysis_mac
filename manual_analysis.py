import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import plotly.offline as py

# Suppress unnecessary output
warnings.filterwarnings('ignore')

# Initialize Plotly (optional, comment out if not using)
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go

# Read CSV data
df = pd.read_csv('dataset/menu.csv')

# Print initial data (optional)
print(df.head())
print(df.describe())

# Check for missing values
print(df.isnull().any())
print('-' * 70)

# Check data shape
print(df.shape)
print('-' * 70)

# Category Distribution
sns.set(font_scale=2)
plt.figure(figsize=(15, 10))
sns.countplot(y='Category', data=df)
plt.title("Distribution of Food Items by Category")
# plt.show()  # Uncomment to display plot

# Mean Calories and Cholesterol per Category
f, ax = plt.subplots(1, 2, figsize=(15, 12))  # Adjusted figure size

average_calories = {}
average_cholesterol = {}
for category in df['Category'].unique():
    average_calories[category] = int(df[df['Category'] == category]['Calories'].mean())
    average_cholesterol[category] = int(df[df['Category'] == category]['Cholesterol (% Daily Value)'].mean())

# Plot average calories
pd.Series(average_calories).sort_values(ascending=True).plot.barh(
    width=0.8, color=sns.color_palette('RdYlGn', 10), ax=ax[0])
ax[0].set_title("Average Calories per Category")
ax[0].set_xlabel("Calories")  # Add X-axis label

# Plot average cholesterol
pd.Series(average_cholesterol).sort_values(ascending=True).plot.barh(
    width=0.8, color=sns.color_palette('RdYlGn', 10), ax=ax[1])
ax[1].set_title("Average Cholesterol (% Daily Value) per Category")
ax[1].set_xlabel("% Daily Value")  # Add X-axis label

plt.subplots_adjust(wspace=0.5)
# Remove grid lines (optional)
ax[0].grid(False)
ax[1].grid(False)

# plt.show()  # Uncomment to display plot

# Average Total Fat and Saturated Fat per Category (similar structure)

f, ax = plt.subplots(1, 2, figsize=(15, 12))

average_total_fat = {}
average_saturated_fat = {}
for category in df['Category'].unique():
    average_total_fat[category] = int(
        df[df['Category'] == category]['Total Fat (% Daily Value)'].mean())
    average_saturated_fat[category] = int(
        df[df['Category'] == category]['Saturated Fat (% Daily Value)'].mean())

# Plot average total fat
pd.Series(average_total_fat).sort_values(ascending=True).plot.barh(
    width=0.8, color=sns.color_palette('inferno', 10), ax=ax[0])
ax[0].set_title("Average Total Fat (% Daily Value)")
ax[0].set_xlabel("% Daily Value")  # Add X-axis label

# Plot average saturated fat
pd.Series(average_saturated_fat).sort_values(ascending=True).plot.barh(
    width=0.8, color=sns.color_palette('inferno', 10), ax=ax[1])
ax[1].set_title("Average Saturated Fat (% Daily Value)")
ax[1].set_xlabel("% Daily Value")  # Add X-axis label

plt.subplots_adjust(wspace=0.5)
plt.show()

# # Mean Vitamins and Minerals per Category
# categories = df['Category'].unique()
#
# for category in categories:
#     category_data = df[df['Category'] == category]
#     fig, axes = plt.subplots(1, 2, figsize=(15, 8))  # Adjusted figure size for each category
#
#     # Mean Vitamin C and Vitamin A
#     sns.barplot(x='Vitamin C (% Daily Value)', y='Item', data=category_data,
#                 ax=axes[0], color='skyblue')
#     axes[0].set_title(f"Mean Vitamin C (% Daily Value) - {category}")
#     axes[0].set_xlabel("% Daily Value")
#     axes[0].set_ylabel("Item")
#     axes[0].tick_params(axis='y')  # Rotate y-axis labels for better readability
#
#     sns.barplot(x='Vitamin A (% Daily Value)', y='Item', data=category_data,
#                 ax=axes[1], color='lightcoral')
#     axes[1].set_title(f"Mean Vitamin A (% Daily Value) - {category}")
#     axes[1].set_xlabel("% Daily Value")
#     axes[1].set_ylabel("Item")
#     axes[1].tick_params(axis='y')  # Rotate y-axis labels for better readability
#
#     plt.tight_layout(pad=3.0)  # Increase padding between subplots for better readability
#     plt.show()

# Mean Carbohydrates and Dietary Fiber per Category (similar structure)

f, ax = plt.subplots(1, 2, figsize=(15, 12))

MeanCarbohydrates = {}
MeanDietaryFiber = {}
for category in df['Category'].unique():
    mean = int(df[df['Category'] == category]['Carbohydrates (% Daily Value)'].mean())
    MeanCarbohydrates[category] = mean
    mean = int(df[df['Category'] == category]['Dietary Fiber (% Daily Value)'].mean())
    MeanDietaryFiber[category] = mean

# Plot average carbohydrates
pd.Series(MeanCarbohydrates).sort_values(ascending=True).plot.barh(
    width=0.8, color=sns.color_palette('viridis', 10), ax=ax[0])
ax[0].set_title("Mean Carbohydrates % Daily Value)")
ax[0].set_xlabel("% Daily Value")  # Add X-axis label

# Plot average dietary fiber
pd.Series(MeanDietaryFiber).sort_values(ascending=True).plot.barh(
    width=0.8, color=sns.color_palette('viridis', 10), ax=ax[1])
ax[1].set_title("Mean Dietary Fiber % Daily Value")
ax[1].set_xlabel("% Daily Value")  # Add X-axis label

plt.subplots_adjust(wspace=0.5)
plt.show()





# Distribution of Calories and Cholesterol
sns.set(font_scale=1)
f, ax = plt.subplots(2, 2, figsize=(10, 10), sharex=False, sharey=False)

x = df['Calories'].values
y = df['Cholesterol (% Daily Value)'].values
sns.kdeplot(x=x, y=y, cmap="viridis", shade=True, ax=ax[0, 0])  # Adjust colormap and add shading
sns.rugplot(x, color='g', alpha=0.7, ax=ax[0, 0])  # Adjust rugplot alpha for better visibility
sns.rugplot(y, vertical=True, color='g', alpha=0.7, ax=ax[0, 0])  # Adjust rugplot alpha

ax[0, 0].set(xlim=(-200, 1000), ylim=(-10, 40), title='Calories and Cholesterol Distribution')

# The distribution of Total Fat and Cholesterol (similar structure)
x = df['Total Fat (% Daily Value)'].values
y = df['Cholesterol (% Daily Value)'].values
sns.kdeplot(x=x, y=y, ax=ax[0, 1])
sns.rugplot(x, color='g', alpha=0.7, ax=ax[0, 1])
sns.rugplot(y, vertical=True, color='g', alpha=0.7, ax=ax[0, 1])
ax[0, 1].set(xlim=(-20, 70), ylim=(-10, 40), title='Total Fat and Cholesterol')

# The distribution of Carbohydrates and Dietary Fiber
x = df['Carbohydrates (% Daily Value)'].values
y = df['Dietary Fiber (% Daily Value)'].values
sns.kdeplot(x=x, y=y, cmap="viridis", shade=True, ax=ax[1, 0])  # Adjust colormap and add shading
sns.rugplot(x, color='g', alpha=0.7, ax=ax[1, 0])  # Adjust rugplot alpha for better visibility
sns.rugplot(y, vertical=True, color='g', alpha=0.7, ax=ax[1, 0])  # Adjust rugplot alpha
ax[1, 0].set(xlim=(-20, 100), ylim=(-10, 40), title='Carbohydrates and Dietary Fiber Distribution')

# The distribution of Vitamin C and Vitamin A (similar structure)
x = df['Vitamin C (% Daily Value)'].values
y = df['Vitamin A (% Daily Value)'].values
sns.kdeplot(x=x, y=y, cmap="viridis", shade=True, ax=ax[1, 1])  # Adjust colormap and add shading
sns.rugplot(x, color='g', alpha=0.7, ax=ax[1, 1])  # Adjust rugplot alpha for better visibility
sns.rugplot(y, vertical=True, color='g', alpha=0.7, ax=ax[1, 1])  # Adjust rugplot alpha
ax[1, 1].set(xlim=(-20, 100), ylim=(-10, 40), title='Vitamin C and Vitamin A Distribution')

# The distribution of Calcium and Iron (similar structure)
x = df['Calcium (% Daily Value)'].values
y = df['Iron (% Daily Value)'].values
sns.kdeplot(x=x, y=y, cmap="viridis", shade=True, ax=ax[1, 0])  # Adjust colormap and add shading
sns.rugplot(x, color='g', alpha=0.7, ax=ax[1, 0])  # Adjust rugplot alpha for better visibility
sns.rugplot(y, vertical=True, color='g', alpha=0.7, ax=ax[1, 0])  # Adjust rugplot alpha
ax[1, 0].set(xlim=(-20, 100), ylim=(-10, 40), title='Calcium and Iron Distribution')

plt.show()

# Pearson Correlation Heatmap
sns.set(font_scale=1.5)
plt.figure(figsize=(15, 10))
corr = (df.corr())
# Consider using a sequential colormap for correlations (e.g., 'coolwarm')
cmap = sns.diverging_palette(220, 20, as_cmap=True)  # Adjust colormap as needed
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values,
            annot=True, fmt='.2f', annot_kws={'size': 13, 'weight': 'bold', 'color': 'black'})
plt.title("Pearson Correlation Coefficients of Nutrients")  # More accurate title
plt.show()