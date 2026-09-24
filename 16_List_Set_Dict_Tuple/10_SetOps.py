a={1,2,3,4,5}
b={4,5,6,7,8}

# union - combine all values from both the sets
res=a.union(b)
print(res)

# intersection - common values from the sets
res=a.intersection(b)
print(res)

# difference - values in the first set but not in second
res=a.difference(b)
print(res)

# symmetric difference
res=a.symmetric_difference(b)
print(res)



amazon={'iPhone','Airpods','MacBook','iPad','Samsung TV','Dell Laptop'}
flipkart={'Samsung TV','iPhone','XBox','PlayStation','Dell Laptop','HP Printer'}
print(amazon)
print(flipkart)


all=amazon.union(flipkart)
print(all)


# show categories exclusively available on amazon
amazon_exclusive=amazon.difference(flipkart)
print(amazon_exclusive)


# categories exclusively available on flipkart
flipkart_exclusive=flipkart.difference(amazon)
print(flipkart_exclusive)


# All exclusive product categories
all_exclusive=amazon.symmetric_difference(flipkart)
print(all_exclusive)

# product categories on both platforms
common=amazon.intersection(flipkart)
print(common)

# Multiple sets
microsoft={'Windows','Office','Cloud','XBox','LinkedIn','GitHub','Teams','Search'}
google={'Search','Gmail','Cloud','Drive','Maps','Android'}
apple={'iPhone','Mac','iPad','Cloud','Maps','Music','Watch'}

# Intersection &
common_services=microsoft & google & apple
print(common_services)

# Union |

all_services=microsoft | google | apple
print(all_services)

# difference
microsoft_exclusive=microsoft - google - apple
print(microsoft_exclusive)

# symmetric difference ^
only_exclusive= microsoft ^ google
print(only_exclusive)

# subsetting membership
a={1,2,3}
b={1,2,3,4,5}
print(a<=b)
print(a.issubset(b))
print(b.issubset(a))
print(b.issuperset(a))