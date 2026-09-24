s1=["sanika kale",451,91.0,"A",451,"mahesh"]

#print type of object/variable
print(type(s1))

#display data
print(s1)


#get size/length of list object
print(len(s1))

#get specific data from List object
print(s1[0])      #sanika kale
# print(s1[5])    #IndexError: list index out of range


#add new element at specific position/ add element in between list -> right shift operation
s1.insert(3,"rahul")
print(s1)

#add multiple new elements at the end
s1.extend([10,"mahesh","ganesh","B"])
print(s1)

#remove data from list -> pop(), pop(index), remove(object/element)
#remove element from last position
s1.pop()
print(s1)

#remove data from specific index -> left shift operation
s1.pop(3)
print(s1)

#remove specific element -> left shift operation
s1.remove("mahesh")
print(s1)

