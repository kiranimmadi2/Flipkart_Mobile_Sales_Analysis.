import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

flipkart_mobile_brands_data = pd.read_csv('/content/Flipkart_mobile_brands_data.csv')

flipkart_mobile_brands_data.head()

flipkart_mobile_brands_data['Rating'].plot(kind='hist', bins=20, title='Rating')
plt.gca().spines[['top', 'right',]].set_visible(False)

flipkart_mobile_brands_data['Selling Price'].plot(kind='hist', bins=20, title='Selling Price')
plt.gca().spines[['top', 'right',]].set_visible(False)

flipkart_mobile_brands_data['Brand'].groupby(flipkart_mobile_brands_data['Memory']).count().sort_values(ascending=False)

sns.pairplot(flipkart_mobile_brands_data, hue='Brand')

sns.displot(flipkart_mobile_brands_data, x='Selling Price',bins=5, hue='Brand',aspect=1.2 )

fig, ax = plt.subplots(figsize=(15,3))
ax=sns.countplot(x="Brand", data=flipkart_mobile_brands_data )

round(flipkart_mobile_brands_data.groupby('Brand')['Selling Price'].mean(),0).sort_values(ascending=False)

plt.figure(figsize=(9,7))
sns.scatterplot(data=flipkart_mobile_brands_data ,x='Rating', y='Selling Price',hue="Brand")
plt.show()

"""**Conclusion :-**
The availability of Low Range Phones Should be Increased as most buyers buy phones in 15000 range
Vivo is providing more rated products and are value for money.
It is not true that only higher selling price products have a higher rating maximum mobiles lying between 0 to 25000 also have a good rating
"""
