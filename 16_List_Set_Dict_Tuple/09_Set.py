tech={'java','python','jpa','spring','pandas','openai','spring','jpa'}
print(tech)
print(type(tech))
print(len(tech))
print(max(tech))
print(min(tech))


#Check for presence of element
print(tech.__contains__('pandas'))
print('pandas' in tech)  # Output: True ()

# ------Adding Elements (add/update)----------
#Add Single Element
tech.add(105)
print(tech)

# Add multiple elements
tech.update(["mahesh","suresh"])
print(tech)


# ------Removing Elements(remove/discard)----------
tech.remove('java')
print(tech)

tech.discard(200)
print(tech)

s2=tech.pop()
print(s2)
print(tech)      #remove any random element from set


#copy set
s3=tech.copy()
print(s3)

#sorting
s4={50,20,10,40,20,20}
print(s4)
print(sorted(s4))

s4=sorted(s4)    #reinitialization
print(s4)


#delete/clear all data from set obj
tech.clear()
print(len(tech))

#delete set object
del tech

print("------Print all data using for each loop-----")
for i in s4:
    print(i)