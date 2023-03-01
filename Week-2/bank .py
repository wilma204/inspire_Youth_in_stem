#!/user/bin/env python3

#This is asingle line comment
#Python programme to calculate gross income
#Name:wilma wanjiku
#email:wilmawanjiku@gmail.com
#Date:17th Feb 2023
#File:operaters.py

#write a programme that calculate
#16% if ranging between 100k-150k
#19% if tax income is between 150k-300k
#30% if tax income is above 300k
#5% if income is less than 100k

#print gross income and net income 

#Formulae gross_income= net income + taxes
net_income = int(input("Enter your net income"))

#above 300k
if(net_income>=300000):
    gross_income= net_income + ((30/100)*net_income)
    print("Since Your Net income is{} your Gross inccome is{}".format (net_income, int(gross_income)))

#150k to less than 
elif(net_income >= 100000) & (net_income < 150000):
    gross_income = net_income + ((15/100)*net_income)
    print("Since your net is{} your gross income is {}".format(net_income, int(gross_income)))

#from 1 to less than 100k
elif(net_income >= 1) & (net_income <100000):
    gross_income = net_income + ((5/100)*net_income)
    print("Since Your Net income is {} your Gross income is {}".format(net_income, int(gross_income)))
else:
    print("Invalid argument")



