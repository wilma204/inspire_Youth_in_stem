#Import module
from tabulate import tabulate

#assign data
mydata=[
    ["Nairobi,Kenya"]
    ["Mumbai,India"]
    ["washington DC;america"]
    ["dubai,united states of america"]
]
#create header
head=["Capital city;country"]
#display table
print(tabulate(mydata,headers=head,tablefint="grid"))
