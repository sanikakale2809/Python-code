student={"studnm":"Sanika","course":"spark","fees":12500,"mode":"live online"}
print(student)

print(student["studnm"])  # Output : Sanika
print(student["course"])
print(student.get("mode"))
print(student.get("mobile"))
print(student.get("qualification","Not Available"))



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

print(player["healthparam"]["age"])