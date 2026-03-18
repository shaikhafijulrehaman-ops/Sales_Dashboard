

import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)


x=[1,2,3,4]
y=[20,30,40,50]
plt.plot(x,y)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [20, 30, 40, 50]
f1=plt.figure(figsize=(4, 3), facecolor='w')

plt.plot(x, y)
plt.legend(loc=9)
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

-import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [20, 30, 40, 50]

f1 = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, y, label="Line")   # Added label
plt.legend(loc=9)              # loc=9 means 'top center'
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()

#1Q
import matplotlib.pyplot as plt
Days=[1,2,3,4,5]
Temparature=[30,32,31,29,33]
plt.grid()
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperature Graph")
plt.plot(Days,Temparature,marker='s',ms=20,mec='r',mfc='y')

#2
import matplotlib.pyplot as plt
Months=["jan","feb","mar","apr","may"]
Sales=[200,250,300,200,350]
plt.plot(Months,Sales,marker='s',ms =10,mec='y',mfc='r',linestyle="dashed",color='g',label='Monthly sales')
plt.legend(loc=9)
plt.grid(True)
plt.legend(loc=9)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("sales Graph")

#3
import matplotlib.pyplot as plt
days=[1,2,3,4,5]
product_A=[50,60,55,70,65]
product_B=[40,45,50,55,60]
plt.plot(days,product_A,marker='s',ms=11,mec='r',mfc='y',linestyle="dotted",color='b',label="SALES OF A")
plt.plot(days,product_B,marker='h',ms=13,mec='y',mfc='r',linestyle="dashed",color='g',label="SALES OF B")
plt.legend(loc="upper left")
plt.grid(True)
plt.xlabel("sales")
plt.ylabel("days")
plt.title("TOTAL SALES")

#1 .scatter plot
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 70, 80]

plt.scatter(hours, marks, marker='o', color='blue',s=100,label='data points')
plt.legend()
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Hours vs Marks")
plt.show()

#2.scatter plot
import matplotlib.pyplot as plt
students_A=[60,70,75,80,85]
students_B=[55,65,70,78,82]
hours=[2,3,4,5,6]
plt.scatter(students_A,hours,marker='o',color='b',s=100,label='students_A')
plt.scatter(students_B,hours,marker='s',color='r',s=100,label='students_B')
plt.xlabel("students")
plt.ylabel("hours")
plt.title("students vs hours")
plt.legend()
plt.show()