# Remove duplicate values from a list

numbers=[1,2,2,2,3,4,5,5,6,7,7,7,8]
unique_numbers=list(set(numbers))
print(unique_numbers)


# Membership testing

allowed_users={'praffull','sharayu','shailaja'}

user=input('Enter UserID : ')

if user in allowed_users:
  print('access granted')
else:
  print('access denied')

visited=set()
itemcodes=[1,2,3,2,1,4,3,5,2]

for item in itemcodes:
  if item not in visited:
    print(f'Procession orders for {item}')
    visited.add(item)


# Frozenset - immutable set

fs=frozenset([1,2,3,4,5,2])
print(fs)


# Membership testing -> set O(1)  list tuple O(n)
l1=[1,2,3,4,5]
l2=[5,6,7,3,8]

exclusive_l1=list(set(l1).difference(l2))
print(exclusive_l1)