import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/josuecampos/downloads/product_sales.csv')

print(data.info())

#replace typo's in 'sales_method' column
data['sales_method'] = data['sales_method'].str.replace('email', 'Email')
data['sales_method'] = data['sales_method'].str.replace('em + call', 'Email + Call')

#drop all rows for NA's in revenue column, less than 10% of rows
data = data.dropna(subset='revenue')

print(data.groupby('sales_method')['nb_sold'].sum())
print(data.groupby('sales_method')['revenue'].sum())
print(data.groupby('nb_site_visits')['revenue'].sum())
print(data.groupby('state')['revenue'].sum())

#customers/sales by sales method
sns.countplot(data, x='sales_method')
plt.title('Sales by Sales Method')
plt.ylabel('Sales')
plt.show()

#Revenue spread by sales method
sns.barplot(data=data, x='sales_method', y='revenue', estimator=sum)
plt.title('Total Revenue by Sales Method')
plt.ylabel('Revenue')
plt.show()

sns.boxplot(data=data, x='sales_method', y='revenue')
plt.title('Revenue by Sales Method')
plt.ylabel('Revenue')
plt.show()

#revenue line graph over time by method_
sns.lineplot(x='week', y='revenue', data=data, hue='sales_method', estimator=sum)
plt.title('Revenue Over Time')
plt.xlabel('Week')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

#revenue by years as customers

plt.figure(figsize=(12, 6))
sns.barplot(data=data, x='years_as_customer', y='revenue', estimator=sum)
plt.title('Total Revenue by Years as Customer')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#revenue by number of site visits
plt.figure(figsize=(12, 6))
sns.barplot(data=data, x='nb_site_visits', y='revenue', estimator=sum)
plt.title('Total Revenue by site visits')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()