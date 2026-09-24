print("--------------Create Dic (1) ------------------")
emp={
    "empname":"Sanika",
    "department":"Marketing",
    "location":"Mumbai",
    "salary":31500
}
print(emp)

print("--------------Create Dic (1) ------------------")
stud=dict(studname='sharayu',course='core java',feespaid=False)
print(stud)
print(type(stud))


print("--------------List in Dic ------------------")
e={
    "empnm":"Yogita",
    "department":"development",
    "skillset":["asp.net core","sql server","azure"],
    "location":"dubai"
}
print(e)
print(type(e))



player={
    "playernm":"Dominik Szoboszlai",
    "club":"Liverpool",
    "position":"midfielder",
    "healthparam":{
        "age":26,
        "height":175,
        "weight":64
    },
    "contractends":"June 2027"

}

print(player)
print(type(player))


k=['patnm','age','city']
v=['john doe','47','chicago']
patient=dict(zip(k,v))
print(patient)

patient['age']=47
print(patient)
