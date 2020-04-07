print("User defined list")
list1 =[]                                       #initially make a empty list
n=int(input("enter the number of elements:"))       # user defined number
for i in range(0,n):
    element=int(input())                          #defined for values of element
    list1.append(element)                          # adding new element at last
print("input :",end = " ")
print("list1",list1)                              #print user defined input in a form of list

print("\n")                                   # space between input & output


print("output : ",end=" ")                          #output statement for user defined list
for j in list1:
  if j>=0:                                          #elements must be positive
    print(j," ",end=" ")                       #print  required output
print("thank you")
