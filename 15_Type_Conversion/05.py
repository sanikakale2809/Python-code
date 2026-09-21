#Convert string to list
text = "Python"
char_list = list(text)
print(char_list)

text = "I love Python"
word_list = text.split()
print(word_list)

text = "Apple,Banana,Mango"
fruit_list = text.split(",")
print(fruit_list)

text = input("Enter words: ")
word_list = text.split()
print("List:", word_list)