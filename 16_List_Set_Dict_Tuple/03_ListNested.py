lst=['java','python','spring','pandas',['Sanika','Yogita']]
print(lst)

# add element at last position
lst.append('spark')
print(lst)

lst[4].append('Gauri')
print(lst)

profiles=[
    ['Sanika','bhavesh','sanem'],
    ['core java','python','spring boot'],
    ['9 june','13 january','1 january'],
    [23,10,5],
    ['london','dubai','pune']
]

#print(profiles)
for items in profiles:
  print(items)


print(profiles[1][2])