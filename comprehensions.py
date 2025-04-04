numbers=[1,2,3,4,5,6,7]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
print(even)
# List comprehension
even=[i for i in numbers if i%2==0]
print(even)
print(numbers)
squares=[i**2 for i in numbers]
print(squares)
# Set comprehension
s =set([1,2,3,4,5,6,7,2,3,1,4])
print(s)
even = (i for i in s if i%2==0)
for i in even:
    print(i)

# Dictionary comprehension
cities=["Mubai","New York","Paris"]
countries=["India","USA","France"]
z=zip(cities,countries)
for a in z:
    print(a)

d={city:country for city,country in zip(cities,countries)}
print(d)
print(d["Mubai"])