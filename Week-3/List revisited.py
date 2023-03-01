#!/user/bin/env python3
#This is camel case
# my favourite fruit
#Name:wilma wanjiku
#email:wilmawanjiku@gmail.com
#Date:20th Feb 2023
#File:operaters.py
myFavouriteFruits=["lime","orange","mango","banana","avocado"]
for fruit in myFavouriteFruits:
    print(fruit)
    #len number of elements in a list
    print(len(fruit))

friends=["Nazra","Resh","dayster","rooney","mary"]
friends[0]="Tuwei"
print(friends)
print("--------------")
new_friend=friends.copy()
print(new_friend)
new_friend.sort()
print(new_friend)

new_friend=friends.pop()
print(new_friend)