import pandas as pd


# l=[["bimal",19],["kl",22]]
# l1=pd.DataFrame(l,columns=["name","age"])
# print(l1)



# l={'name':['naruto','shaske','itachi'],'age':[11,12,13]}
# l1=pd.DataFrame(l,index=[100,101,102])
# print(l1[1:])


# l={'name':['naruto','shaske','itachi'],'age':[11,12,13]}
# l1=pd.DataFrame(l,index=[100,101,102])
# print(l1['name'])

# l={'name':['naruto','shaske','itachi'],'age':[11,12,13]}
# l1=pd.DataFrame(l,index=[100,101,102])
# print(l1['age'])


# l=[{"name":"bimal","age":19},{"name":"kl","age":22}]
# l1=pd.DataFrame(l)
# print(l1)


# summation=lambda v1,v2:v1+v2
# print("the sum of 7 + 10 =",summation(7,10))


# summation=lambda v1,v2:v1*v2
# print("the sum of 7 * 10 =",summation(7,10))

# def fahrenheit(T):
#     return ((float(9)/5)*T + 32 )
# def celcius(T):
#     return (float(5)/9) * (T - 32 )

# temp =(15,10,25,66)
# f=list(map(fahrenheit,temp))
# c=list(map(celcius,temp))
# print(f)
# print(c)


# celcius =[1,2,3,4]
# fahrenheit =map(lambda x:(float(9)/5)*x+32,celcius)

# for x in fahrenheit:
#     print(x)

# fib =[0,1,1,2,3,5,8,13,21,34,55]

# result =list(filter(lambda x: x%2==0,fib))
# for x in result:
#     print(x)



import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
print(np.add(a,b))
print(np.subtract(a,b))

