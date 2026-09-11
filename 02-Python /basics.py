# class 01 python basics ( varibles and its types)          4 sept 2026

# --- String Variable Basics ---

name = "shree ganeshay namah"

# Just by writing name of variable and running it, it will give you the content inside
name 

# Type will tell us type of variable right now
type(name) 

print(name)


# --- Numerical Variables & Operations ---

pizza = 100
samosa = 20
slize = 30.01

total = pizza + samosa + slize

total

type(total)

# This > operator means "is total greater than 200"
total > 200

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 02 (numbers)
base = 10
height = 8
area = 1/2 *base*height  
area  # ouput = 40

type(area)  # by this we will know the area 

x=30
y=7

x+y = 37
x*y = 210
x/y = 4.285714285714286
x//y = 4  # it is a integer divison 
x**y = 21870000000 #x to the power y 

sci = 1.2e+2 # 120
sci2 = 1e-2  # 0.01 

food = 3
water = 5
Total = food + water #8

food = "3"
water = "5"
total = food + water  # but in this case it will give output "35" , now to tackle this problem 

total = float(food) + float(water) # this is called type casting 

# this is how we import this library 
import math 
x=16 
math.sqrt(x)  # output is 4 

format (5 ,'b')  # it will convert to binary 
format (10 ,'b') # 1010

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class -03 (strings)

first = "Mohan"
last = "sharma"

name =first + " " + last  # WE CAN ADD LIKE THIS 
#output = Mohan sharma 

name = f"{first} {last}"  # this is also an method in python for adding a string , varible should be in {}

# this is how indexing works 
name[0] = m
name[1] = o

# slice operator
name[0:4] # SLICE operator = it will give you sliced string out of this (o to 4)
# "moha"

name[6:12]  # 6 included and 12 exlcuded (6,7,8,9,10,11)
# sharma 

name[-2] # this in only in python , where -2 is saaying second element from last 

len(name) # to get size of string 

food_Story = " i am 'banana' "  # when we have to use single quotes , we will use double quotes in outer 
s = ' they have "oops" moment ' # when we have to use double quotes , we will use single quotes in outer 


recipi = ''' \n veg biryani with saffron , cardamom , and cloves , garnished with fried onions 
'''
# these 3 quoation is for paragraph 

print(recipi)  #veg biryani with saffron , cardamom , and cloves , garnished with fried onions 

spice = "cardamom"
spice in recipi # true

"milk" in recipi # false 

print(recipi.replace("veg","non-veg") ) # it will print , but it will not change the orignal string 
nw = recipi.replace("veg","non-veg") # replace funcion will give a entire new string and changes happen in new striing 

recipi.upper() # simliraly lower s also there

recipi.index("garnished") # this will give the starting index of given word or striig

text = "my age is :"
age = 38

text + age  # this will give a error ,  so convert int into string '38' or str(age)
text + str(age) # now it will work 


tickers="AAPL|NVDIA|RIL|GOGL"
tickers.split("|")  # ['AAPL', 'NVDIA', 'RIL' ,'GOGL']
tickers.split("|" , maxsplit = 2) #['AAPL', 'NVDIA', 'RIL|GOGL']

data = " helloo we are doing the same thing again and again "
data.strip() # it removes the extra spaces and trailing spaces from your body 

file_name = "report.pdf"

file_name.endswith(".pdf")  # usally these are used in checking of the format of file 

# Create a variable and store the string “The Himalayas are one of the youngest mountain ranges on the planet.”

# 01 Print ‘The Himalayas’ using slice operator
# 02 Print “mountain range” using a negative index
# 03 Print “The Himalayas on the planet” using slice as well as f-string

st = "The Himalayas are one of the youngest mountain ranges on the planet"

print(st[0:13])  # 13 is not included 
print(st[-29:-14])
print(st[0:13],st[54:67]) 
print(st[0:13],st[-13:])
#outputs
# The Himalayas
# mountain ranges
# The Himalayas on the planet
# The Himalayas on the planet
------------------------------
# Q2
# You have created a string variable called string= ”There are 9 planets in the solar system”.
# After some time, you have realized that your sentence is incorrect and there are only 8 planets, 
# now correct your sentence by replacing the incorrect words. (Bonus: Try to do it in one line)

st = "There are 9 planets in the solar system"
nw = st.replace("9","8")
nw

# output
# There are 8 planets in the solar system'

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class - 04 (list)

# list is something array , but in python list in not homogenious which means we can have diffrent data type in same lists 

# syntax of list 
items = ["bread" , "jam" , "essence" , "milk" , "water"] 
items
# output = ['bread', 'jam', 'essence', 'milk', 'water']

items[0] # bread
items[0:2]  # using slice operator output = bread , jam 

# append 
items.append("butter") # insertion at last ['bread', 'jam', 'essence', 'milk', 'water' , 'butter']

# remove 
items.remove("butter") # remove from last 

# insertion at particular position 
items.insert(1,"butter") # (index where u want to insert , what you want to insert )


# checking 
'rice' in items  # false 

expenses = [2000 , 190 , 40 , 300 , 498]

expenses.sort() # this will sort the given order 
expenses.sort(reverse = True) # this will reversed the sorted order 
expenses


bakery = ['biscuit' , 'sprite']

# we can add both array by just + operatr 

bakery_items = bakery + items

bakery_items.sort() # Python compares the strings character by character, starting from the first character , A space comes before letters in the character ordering, so ' cheese' gets placed first.

bakery_items # [' cheese', 'almonds', 'biscuit', 'bread', 'jam', 'sprite']

len(items) # size of array 
dir(items) #all the mehtods avilable for list 

items.clear() # it will clear all the items 

Q7.
What will be the output of the following code?

lst = [1, [2, 3], 4, [5, [6, 7]]]
print(lst[3][1][0])
# ouput is 6

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 05 (if - else) 11 sept 2026 

# Taking input from user ( we have to specify the input because of type casting )
from email import message

# n = input("enter number here ")  (it will give error)

n = int(input("enter number here "))   # Yes, input() always returns a string (str) by default. What you type: 25 -> What Python receives: "25" (String)
print(type(n))
if n%2 == 0 :
     print("even number")
else:
     print("odd ")

# short way
message = "number is even" if n%2 ==0  else "number is odd"

#reverse way
m= int(input("enter number here "))
if not n%2 == 0 :
     print("odd number")
else:
     print("even")


x=10
if x>10 and x%2==0 :   # try with OR , AND
    print("yay")
else :
    print("no")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class -06 (loops)

 expenses = [1000 , 1200 ,2000 ,5000]
 total_expense = 0
#
#  way -01
for expense in expenses :
  total_expense += expense
  print(total_expense)

# way -02
for i in range(len(expenses)) :
    expense = expenses[i]
    print(f" month {i} ->  {expense}" )
    total_expense += expense

#way -03
for i , expense in enumerate(expenses) :
    print(f" month {i} ->  {expense}")
    total_expense += expense
#
# break in loops
monthly_Sales = [42 , 34 , 33 , 38 ,40 ,45]
threshold = 35

for sales_amount in monthly_Sales :
    if sales_amount < threshold :
        print(f"sales amount {sales_amount} is lesser than threshold")
        break
    else:
        print(f" {sales_amount} is greater than ")


# using zip ( enumerate() pairs index numbers with items from one list, zip()
# pairs corresponding elements from multiple lists based on their position.)
# monthly_Sales = [42 , 34 , 33 , 38 ,40 ,45]
# threshold = 35
# months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
#
# for sales_amount , month in zip (monthly_Sales ,months):
#     print(month,sales_amount)



# using continue

for i in range (1,11):
    if i%2 == 0 :
        continue
    else :
        print(i)

# we can use else with for loop , but it only means that after completing the for loop the execution goes to else


# nested loops
products = ["iphone",'ipad','macbook']
regions = ["usa",'ind','uk']
revenue = [20,23,45,56,12,34,13,44,34,31,39]

i=0
for product in products :
    for region in regions :
        rev = revenue[i]
        i=i+1
        print(f"{product} -> {region} -> {rev}")


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)











