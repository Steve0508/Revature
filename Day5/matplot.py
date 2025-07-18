import matplotlib.pyplot as plt

#basic line plot


# x=[1,2,3,4,5]
# y=[2,4,6,8,10]

# plt.plot(x,y)
# plt.title("Line Chart ")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid(True)
# plt.show()



#Barchart

# categories=['A','B','C']
# values=[10,20,15]

# plt.bar(categories,values)
# plt.title("Bar Chart")
# plt.show()

#Scatter plot
x=[1,2,3,4,5]
y=[2,4,1,8,7]

plt.scatter(x,y,color='red')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()