














#write a programme that calcultes quadratic equatoin
#using for loop draw a diamond ,triangle and pascals triangle

import cmath

first_coefficient = int(input("Enter the first coefficient:"))
second_coefficient = int(input("Enter the second coefficient:"))
constant = int(input("Enter the constant:"))

ans1 =abs(second_coefficient) - cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)
ans2 = abs(second_coefficient) + cmath.sqrt((second_coefficient**2)-(4*first_coefficient*constant))/(2*first_coefficient)


print("The answers "+str(ans1)+" and " +str(ans2))


#using a for loop draw a diamond
R=int(input("Enter the range:"))
for diamond in range(R):
    print(" " * (R - diamond), "*" *(2 * diamond +1))
    for diamond in range(R-2,-1,-1):
        print(" "*(R-diamond), " *" * (2 * diamond +1))


print("---------------------------")

#using a for loop draw pascals triangle
for i in range(1, R+1):
    for j in range(0, R-i+1):
        print('', end='')


        #using Binomial Coefficient
        c = c * (i - j) // j
        print()





my_set={"banana","lemon","orange",}
print(set)
print(type(my_set))
print(len(my_set))
