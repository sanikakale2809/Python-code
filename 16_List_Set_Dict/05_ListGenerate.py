print("-----------------Generate list-----------------")
lst=[3,12,45,9,15,26,13]
sq=[]

for n in lst:
  sq.append(n*n)

print(sq)


lst=[3,12,45,9,15,26,13]
cubes=[n**3 for n in lst]
print(cubes)


nms=['sanika','gauri','pavan','achal']
u=[nm.upper() for nm in nms]
print(u)


lst=[9,13,26,1,45,10,30,15,18,25]
odd=[x for x in lst if x%2==1]
print(odd)

lst=[9,13,26,1,-45,-10,30,15,-18,25]
neg=[x for x in lst if x<0]
print(neg)

lst=[9,13,26,1,45,10,30,15,18,25]
res=[x for x in lst if x%3==0]
print(res)


l1=[3,14,26,55,15]
l2=[1,5,13,2,9,26,14]
common=[x for x in l1 if x in l2]
print(common)


l1=['java','python','sql','spring','spark','docker']
l2=['azure','aws','java','oracle','cpp']
res=[x for x in l1 if x not in l2]
res2=[x for x in l2 if x not in l1]
res.extend(res2)
print(res)