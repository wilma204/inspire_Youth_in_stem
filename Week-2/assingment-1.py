#write a programme to calculate arithmetic progression of numbers 1-20
n=20
a=1
d=input("enter the difference")
arithmeticprogression=int(a)+(n-1)*int(d)
print(arithmeticprogression)
#formula a.n =nth termin the sequence,a=first term of the sequence
 #write a programme to list all odd numbers from 1-100
print("the values below are odd numbers")
for odd_numbers in range(1,101):
    if(odd_numbers%2 !=0):
        print(odd_numbers)
#write a programme to list all even numbers from 1-100
print("the values below are even numbers")
for even_numbers in range (1,100):
    if(even_numbers%2 == 0):
        print(even_numbers)
#write a programme to list all prime numbers from 1-100
print("the values below are prime numbers")
for prime_numbers in range(1,101):
    if prime_numbers >1:
        for i in range(2,prime_numbers):
            if (prime_numbers% i) == 0:
                 break
        else:
            print(prime_numbers)