friends=[]
cho=''

while cho.lower()!='no':
  nm=input('Enter friend name : ')
  friends.append(nm)
  cho=input('Do you want to add more friends? (yes/no) : ')
else:
  print(friends)


s=input('Enter name : ')
if s in friends:
  print('friend found')
else:
  print('friend not found...added')
  friends.append(s)

print(friends)