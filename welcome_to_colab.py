import matplotlib.pyplot as plt

Months = ['Jan','Feb','Mar','Apr','May','Jun']
Sales_A = [200, 250, 300, 280, 350, 400]
Sales_B = [180, 220, 260, 300, 330, 370]

Ad_Spend = [10, 20, 30, 40, 50, 60]
Sales_Scatter = [100, 150, 200, 260, 300, 360]

Categories = ['Electronics','Clothing','Food','Furniture']
Revenue = [500, 300, 400, 350]

Regions = ['North','South','East','West']
Region_Sales = [30, 25, 20, 25]

plt.figure(figsize=(12,8))

# 1. Line Chart 
plt.subplot(2,2,1)
plt.plot(Months, Sales_A, marker='o', label="Product A")
plt.plot(Months, Sales_B, marker='s', linestyle='--', label="Product B")
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid()

# 2. Scatter Plot 
plt.subplot(2,2,2)
plt.scatter(Ad_Spend, Sales_Scatter, color='red', marker='x', label="Ad vs Sales")
plt.title("Ad Spend vs Sales")
plt.xlabel("Ad Spend")
plt.ylabel("Sales")
plt.legend()
plt.grid()

# 3. Bar Chart 
plt.subplot(2,2,3)
plt.bar(Categories, Revenue, color='green')
plt.title("Revenue by Category")
plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.grid(axis='y')

# 4. Pie Chart
plt.subplot(2,2,4)
plt.pie(Region_Sales, labels=Regions, autopct='%1.1f%%')
plt.title("Regional Sales Distribution")

# Suptitle
plt.suptitle("Sales Performance Dashboard", fontsize=16)

plt.tight_layout()
plt.show()
