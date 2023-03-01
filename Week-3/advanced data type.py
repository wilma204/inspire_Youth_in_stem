#advanced data types
#mutable vs immutable
#mutagle data that can be changed during pragrame life cycle
#immutable data types that cannot be edited during programme life cycle
#1)list (mutable)
friends=["nazra","resh","dayster"]
#or friends = [] for empty list
#add--->append(),extend()
#remove-->pop()
students=["mary","rooney","goreti"]
friends.extend(students)
friends.append(students)

#2)tuples
#type of list that are immutable
stationaries =("pens","pencil","calculater")
for stationery in stationaries:
    print(stationery)

    numbers = (1,2,3,4,5,6)
#you can be allowed to replace


#3)dictioneries
#uses key and value pair to store data
student ={"name" :"willy", "age" :13,"gender":"male"}

print(student["name"])
print(student["age"])
print(student["gender"])
#"name": "willy" --> name(key) willy(value)
#create a dictionery of your friends
friends ={"favourite colour":"nude pink","hobby":"swimming","course":"law","weight":"50kg",}
print(friends["favourite colour"])
print(friends["hobby"])
print(friends["favourite colour"])
#sets