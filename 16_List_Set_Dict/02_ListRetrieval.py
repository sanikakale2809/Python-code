films=['the matrix','pk','speed','mission impossible']
actors=['keanu reeves','amir khan','tom cruise']

#add multiple new elements at the end
films.extend(actors)
print(films)

# print variable according to index
print(films[5])
# list slicing
print(films[1:5])
print(films[2:])
print(films[:4])
print(films[-1])

# Reverse List(1)
print(films[::-1])

# Reverse List(2)
films.reverse()
print(films)