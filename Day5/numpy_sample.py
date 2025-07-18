import numpy as np

a= np.array([1,2,3])
b= np.array([1,2],[3,4])

c=np.zeros((2,3))      #2x3 array of zero
print(c)
d=np.ones((3,2))          #3x2 array of ones
print(d)
e=np.eye(3)               #3x3 identity matrix
print(e)
f=np.full((2,2),7)        #2x2 filled with 7
print(f)
g=np.arange(0,10,2)       #[0,2,4,6,8]
print(f)
h=np.linspace(0,1,5)      #5 values between  0 and 1 
print(h)

#array attributes

arr =np.array([[1,2],[3,4]])


arr.shape       #(2,2)
arr.ndim  #2
arr.size    #4
arr.dtype   #data type (eg: int 64)




#indexing and slicing

arr=np.arry([[1,2,3],[4,5,6]])
arr[0,1]#2
arr[:,1]    #[2,5] (all rows , column 1)
arr[1,:]        #[4,5,6] (row 1)


#mathematical operations

a=np.array([1,2,3])
b=np.array([4,5,6])

a+b   #[5 7 9]
a*b         #[4 10 18] element wise
x=np.dot(a,b)  #32 (dot product)

print(x)

a1=np.mean(a)
b1=np.std(b)
c1=np.sum(a)

d1=np.max(b)


#Reshaping and flattening 

arr=np.array([[1,2],[3,4]])

arr.reshape(4,1)


#broadcasting (allows aruthmetic between arrays of different shapes)
a=np.array([[1],[2],[3]])
b=np.array([10,20,30])

a+b

