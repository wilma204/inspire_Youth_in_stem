#!/user/bin/env python3
#This is camel case
# my favourite celeb
#Name:wilma wanjiku
#email:wilmawanjiku@gmail.com
#Date:20th Feb 2023
#File:operaters.py



#copy the list to a new list called celeb
#sort the list
#pop out 2 celebrities
#count the remaining celeb
myFavouriteMusicians=[]
myFavouriteMusicians=["drake","h.e.r","rihanna","21savage","doja cat"]
for musician in myFavouriteMusicians:
    print(musician)
updateMusicians =myFavouriteMusicians + ["anne marie","lil durk","selena","playboi carti"]
for musician in updateMusicians:
    print(musician)
celebs = updateMusicians.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop()
print(celebs)
celebs.count()
print(celebs)








