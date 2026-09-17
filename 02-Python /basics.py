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

# -------------------------------------------------------------------------------------------------------------------------------------------
# class = 07 (functions)

'''
important points

01 function = In Python, a function is defined using the def keyword
->The code inside the function must be indented. Python uses indentation to define code blocks.

02 function name rules -> Function names are case-sensitive (myFunction and myfunction are different)

03 function return -> If a function doesn't have a return statement, it returns None by default.

04 pass statment -> Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
-> Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

05 -> parameter vs argument

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter (because it can be a variable)
  print("Hello", name)

my_function("Emil") # "Emil" is an argument (because it is exact name )

If your function expects 2 arguments, you must call it with exactly 2 arguments.

06 -> positional vs keyword arguments

positional -> just a nomral arguments , order is important here
keyword -> key - value pair arguments , in this order is not important

ou can mix positional and keyword arguments in a function call.

However, positional arguments must come before keyword arguments:

'''

# function for finding a volume of cylinder

def vol_cylinder (radius, height):
    vol = 3.14* (radius**2) * height
    print(f"volume of given cylinder with radius {radius} and height {height} is : {vol}")
    return vol

vol_cylinder(10,7)

# if i use extra parameter than givne (it will give error to them)
# vol_cylinder(10,7,4)

# if i use less parameter than given ( it will give error of missing argument)
# vol_cylinder(10)

# this is positional argument so you have to be careful about order of agrument first radius -> then height

# here we use keyword argument
def vol_keyword (rad , hei=7 ) :
    vol = 3.14 * (rad ** 2) * hei
    print(f"volume of given cylinder with radius {rad} and height {hei} is : {vol}")
    return vol

vol_keyword(hei=7 , rad = 10) # here we shuffled the order but it will run fine

vol_keyword(rad=7)  # it will use default argument , if we didnt give them a height

# if we are not sure how many argument it will take
def sum_all (*args) :  # by writing this *args i specified that , it can have any number of argument                   
    total = 0          # When you want a function to handle any number of inputs (e.g., adding numbers, concatenating strings)
    for num in args :
        print(num)
        total += num
    print(total)
    return total

sum_all(1,2,3,4,5,6,7,8)


# using kwargs
# suppose i want to give this argument company_info (name='resurgence pvt ltd' , valuation ='2000 bd' , revenue= 50 crd) , and i can add anyhting new in this

def company_info (**kwargs) :   # When you want to pass named properties without predefining every single parameter in the function header.
Python
    for info in kwargs :
        print(info ,":->", kwargs[info])

company_info (name='resurgence pvt ltd' , valuation ='2000 bd' , revenue= 50)
# now i wanna add new details in arguments

company_info (name='resurgence pvt ltd' , valuation ='2000 bd' , revenue= 50 , product='AI-SOFT-ELC')


# f you use standard positional arguments, *args, and **kwargs together, Python requires them to be in this exact order:
# Python

# using lamba expression (lambda expression is a quick way to define a function in a single line )
# def sqr (x)
#     return x**2

# now by using lamda expression
x= lambda a : a*a   #lambda input :  return output
print(x(5))

y = lambda a,b : a+b
print(y(2,3))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 08 (tuples )
# tuples are collection of ordered elements , tuple is immutable
# we cannot change directly in the tuples

points_2d = (2,3)
points_3d = (3,4,5)

def find_pe_pb_Ratio (price ,eps ,book_value) :
    pe = price/eps
    pb = price/book_value
    return pe,pb  # we can return multiple values in python as a list


# this is called unpacking
# Function Call karte waqt (Unpacking):
# *my_list ya *my_tuple kisi list/tuple ko khol kar individual values me spread kar deta hai
# **my_dict kisi dictionary ko khol kar individual key=value arguments me spread kar deta hai.
pe_ratio,pb_ratio = find_pe_pb_Ratio(3,4,5)
print(pe_ratio)
print(pb_ratio)


# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 09 (dictionary)
# In python dictionary is a implementation of hashmap
# lets assume there is a list of tuples
contcts = [('arpit','ind'),('sharon','uk'),('alice','can')]

# now we will dictionary of this

d = {
    'arpit':'ind',
    'sharon':'uk',
    'alice':'can'
}

print(d)
print(type(d))

# accesing
print(d['arpit'])

# to get all keys
x = d.keys()
print(x)

y = d.values()
print(y)

z= d.items()
print(z)

d.get('aaditya',-1)  # this will not throw error , just simply return none
#d['aaditya']  # this will definelty give error

# adding
d['bitto'] = 'dewas'
print(d)

# using IN operator
print('bitto' in d)  # this will return true
print('aadi' in d) # this will return false

# using for loop (only keys)
for name in d :
    print(name)

# this will return both keys and values
for name,number in d.items() :
    print(name,number)

d.keys()
d.values()
d.items()

# we can have nested dictionary as well
apple_revenues = {
    'usa' : { "iphone":20,
             'ipad':4,
             'iwatch':10
           },


    'ind' : {'iphone': 24,
             'ipad': 25,
             'iwatch':23
            }


}

for country,product_Data in apple_revenues.items() :
    for product,rev in product_Data.items():
        print(f"{country} {product}")



# example for using both args and kwrgs 
'''
def make_pizza(size, *toppings, **order_details):
    print(f"Pizza Size: {size}")
    
    print("\nToppings (*args packed as Tuple):")
    for topping in toppings:
        print(f" - {topping}")
        
    print("\nOrder Details (**kwargs packed as Dict):")
    for key, value in order_details.items():
        print(f" - {key}: {value}")


# Function Call
make_pizza(
    "Large",                                   # 1. Standard Argument
    "Pepperoni", "Mushrooms", "Extra Cheese",   # 2. *args (Positional values)
    customer="Srinivas", address="Indore", pay_mode="UPI" # 3. **kwargs (Key=Value pairs)
)

'''
# output
# Pizza Size: Large

# Toppings (*args packed as Tuple):
#  - Pepperoni
#  - Mushrooms
#  - Extra Cheese

# Order Details (**kwargs packed as Dict):
#  - customer: Srinivas
#  - address: Indore
#  - pay_mode: UPI



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 10 (file handling)
# file handling 
f = open('funny.txt' ,'r')

for line in f:
    print(line)

# using with it works as context 
with open('funny.txt','r') as f:  # here you dont have to close it , it will automaticlly got closed after executiow
    for line in f:
        print(line)

with open('funny.txt', 'a') as f  : # here i am appending something 
 f.write("i am feeling so sad and sleepy")

player_scores = {}
with open ('scores.csv','r') as fl:
    for line in fl:
        player , _,score = line.split(",")   # humne value nikali hai yha se 
        score = int(score.strip())
        if player in player_scores :   # if player is already in that , just apeend its scores 
            player_scores[player].append(score)
        else :
            player_scores[player] = [score]
           
        
player_scores

''' 
{'rohit': [9, 120, 105, 140, 130],
 'shakib': [56, 78, 102, 72],
 'babar': [56, 45, 120, 5, 67]}
'''

for player ,score_list  in player_scores.items() :
    min_score = min(score_list)
    max_score = max(score_list)
    print(f"{player} {min_score} {max_score}")

''' output 
rohit 9 140
shakib 56 102
babar 5 120
'''


''' 
file handling questions with solutions for understanding 




Task 1
You are given a file called customers.txt that contains the name of the customer and total amount they spent. Read this file line by line and save the customer name and total amount in a dictionary.

For example, customers.txt file will content the data in the following format,

Srinivas,120
John,250
Maria,150
Smith,510
Anjali,45
You will read this and build a dictionary like this,

{
    "Srinivas": 120,
    "John": 250,
    "Maria": 150,
    "Smith": 510,
    "Anjali": 45
}

solution ->

d = {}
with open ('customers.txt','r') as f :
   for line in f :
       name , amount = line.split(',')
       d[name] = int(amount.strip())

print(d)


Step 1 (Line lao): for line in f: File se ek raw text line uthao ("Srinivas,120\n").
Step 2 (Clean karo): line.strip() Clean textual line banao ("Srinivas,120")
.Step 3 (Tukde karo): .split(',') Comma se tod do ("Srinivas" aur "120").
Step 4 (Dict me dalo): d[name] = int(amount) Key-value pair bana kar type convert karo.



'''
# 

'''
'r' (Read) -> Reads existing content
'w' (Write) -> Erases/Overwrites all existing content	
'a' (Append)-> Preserves existing content; adds to en
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 11 (classes)
# syntax of defining a class
import datetime
class cricket_player:
    team_Size = 11    # this is for every one
    def __init__(self,fname,lname,birth_year,team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []


    def add_Scores (self,score):
     self.scores.append(score)

    def get_avg (self):
     return sum(self.scores)/len(self.scores)

    def get_age (self) :
     now = datetime.datetime.now() # this is how you calculate current year
     return now.year - self.birth_year

    # this is function thorugh which we can represent object in string
    def __str__(self):
       return f"{self.first_name} {self.last_name} ,the cricket player from {self.team}"

virat = cricket_player("virat","virat",1999,'IND')
virat.add_Scores(27)
virat.add_Scores(149)
virat.add_Scores(87)

print(virat.get_age())
print(virat.get_avg())


# example - 02

class Student:
    # Constructor: Runs when an object is created
    def __init__(self, name, age, marks):
        self.name = name     # Attribute
        self.age = age       # Attribute
        self.marks = marks   # Attribute

    # Method: Action that the object can perform
    def display_info(self):
        return f"Student: {self.name}, Age: {self.age}, Marks: {self.marks}"

    def is_passed(self):
        return self.marks >= 40


# Creating Objects (Instances of Class Student)
s1 = Student("Srinivas", 22, 85)
s2 = Student("Rahul", 21, 35)

# Accessing Attributes and Methods
print(s1.display_info())  # Output: Student: Srinivas, Age: 22, Marks: 85
print(s1.is_passed())     # Output: True
print(s2.is_passed())     # Output: False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class -12 (exceptional handelling)
# if on any line , code gets exception then the code below that line will not be executed
# so we have to handle this exception using try and except

x= input("enter a number")
y = input("enter a number")

ans = 0
ans_2 = 0
try:
    ans = int(x)/int(y)
    ans_2 = 'hellow' + 18

except ZeroDivisionError as ze:
    print('exception occured : ', ze)

except TypeError as te:
    print('exceptions occured :',  te)

#If you don't know the exact error type in advance, you can catch the generic Exception object to get its details
except Exception as e:  # this is actualy genric expections , it can handle anything if we forget to specify  , but as a good data engineer use specific exception
    print('exeption occured :' , e)




# finally => finally will get executed no matter what , even if exeption comes or not
finally:
    print('i will be executed at any situation')

balance = 0
def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError('amount must be greater than 0') #You can trigger an error intentionally using the raise keyword when custom conditions aren't met:
    balance += amount

deposit(100)
print(balance)

def credit (amount):
    global balance
    if amount>balance :
        raise ValueError('insuffcient funds')
    balance = balance - amount

credit(120)
print(balance)


# exercise questions of oops soltuion 
'''
# 1. Base Parent Class
class LibraryItem:

    def __init__(self, title, is_borrowed=False):
        self.title = title
        self.is_borrowed = is_borrowed

    def borrow_item(self):
        if self.is_borrowed:
            raise Exception(f"The item '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"Successfully borrowed '{self.title}'.")


# 2. Child Class (Book)
class Book(LibraryItem):

    def __init__(self, title, author, is_borrowed=False):
        super().__init__(title, is_borrowed)
        self.author = author


# 3. Task 4 Execution
# Step A: Object creation
book_1 = Book("Jeet Aapki", "Shiv Kheda", is_borrowed=False)

# Step B: First borrow attempt (Succeeds)
print("--- First Attempt ---")
try:
    book_1.borrow_item()
except Exception as e:
    print("Error:", e)

# Step C: Second borrow attempt (Triggers Exception)
print("\n--- Second Attempt ---")
try:
    book_1.borrow_item()
except Exception as e:
    print("Caught Exception successfully:", e)

'''

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 13 (pandas library , dataframe)

'''
import pandas as pd

df = pd.read_csv('data.csv')  # Loads CSV file into a DataFrame

df.head(5)                    # Views the first 5 rows
df.info()                    # Displays column names, non-null counts, and dtypes
df.describe()                # Calculates mean, std, min, max, and quartiles for numeric columns
df.shape                     # Returns (rows, columns) tuple

'''
import pandas as pd # pandas is widely used by data analysts , data sceintists

df = pd.read_csv('movies.csv')
print(df) 

df.head(5)
df.tail(3)
df[2:6]

# for avg imdb reading 
df.imdb_rating  # it is series 

df.imdb_rating.min(),  df.imdb_rating.max() , df.imdb_rating.mean() # we can do many operations 

# for only bollywood industry (understand syntax through gpt)
df_b = df[df.industry == "Bollywood"]
df_h = df[df.industry == "Hollywood"]

df_b.imdb_rating.min() , df_h.imdb_rating.max()

''' data frame basics use from here '''

df.columns # it will tell you all coloum of data frame 

df.industry.unique() # for how many industry in it 

df.language.unique() 

mvd = df['language'].unique()

df.industry.value_counts()

# how many movies are there for each of these languages 
df.language.value_counts()

# subset of data set (coloum fitering)
df_subset = df[["title","language","imdb_rating","industry"]]  # this is how we can get the subset of our data frame , if we want to work on it we can save it in diffrent varialble

# we want movies which have release_year should be greater than 2000
df[df.release_year>2000]

# we want movies which have release_year should be between 2000 and 2010
df[(df.release_year>2000) & (df.release_year<2010)]

# WANT to see only marvel movies 
df[df.studio == "Marvel Studios"]  # row level filtering 

df.describe()  # this actually give us the basic analytics of our dataframe 

df.info() # give us infor about our dataframe , how many colums and all 

# movie with max rating 
df[df.imdb_rating == df.imdb_rating.max()]

'''
# bollywood movie  with highest rating 
# df[ df.imdb_rating == df.imdb_rating.max() & df.industry == 'bollywood'] (wrong )

# way -01 
#ntop_movie = df[(df.industry == 'bollywood') & (df.imdb_rating == df[df.industry == 'bollywood'].imdb_rating.max())]

# way -02  using subset  
bwd = df[df.industry == 'Bollywood'] # created a subset from dataframe
BMV = bwd[bwd.imdb_rating == (bwd.imdb_rating.max())] # now filtering the row 
BMV.head(1)
'''

df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())]

# we want to calculate the age of the movie 
# relase_year - current_year
# we can use diffrent ways for it 

#way -01 ( adding the new coloum )
df['age'] = df['release_year'].apply(lambda x : 2026-x)  
df.head(10)

# way -02 
def calculate_age(release_year):
    return 2026 - release_year
# Step 2: Pass the function name to .apply()
df['age'] = df['release_year'].apply(calculate_age)   # this apply function works as loop , and works as row by row 
df.head(10)

# way -03
df['age'] = 2026 - df['release_year']
df.head(10)


# now we want to calculate profit 
# way -01  
df['profit'] = df.apply(lambda x : x['revenue'] - x['budget'] , axis=1) # axis=1 means going row by row 
df.head(4)

# way -02
def calprf (budget,revenue):
    return revenue-budget
df['profit'] = calprf(df['budget'],df['revenue'])
df.head(4)

# we will study about index 
df.index  # it will show you the index from where to where 

# now if we want to change the index
df.set_index("title",inplace = True) # this inplace true depict that it will change in df 
df.index

df.head(3) # without changing index it has s.no but after changing index it has starting from titledf

df.loc['Pather Panchali']  # uou will get info of a row as a hashmap or you can say as a disctionary fromat  , but we can only do this by after setting an index

df.loc[["Pather Panchali","Doctor Strange in the Multiverse of Madness"]]  # for multiple index 

df.iloc[0] # it is integer based loacation
df.iloc[2:5]

df.reset_index(inplace=True)
df.head(4)

'''
doubts for single bracket or double bracket 

01 You are selecting only one column to perform simple math or series operations.
# Returns a Series
max_rating = df['imdb_rating'].max()
df['age'] = 2026 - df['release_year']

02 Use Double Brackets df[['col1', 'col2']] when: You need to select two or more columns at the same time.
# Must use double brackets for multiple columns
df_subset = df[['movie_title', 'industry', 'imdb_rating']]

03 You are selecting one column, but you want the result to stay formatted as a DataFrame table rather than a Series array.
# Returns a 1-column DataFrame instead of a Series
df_table = df[['imdb_rating']]

'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 14 (reading csv files)

'''
     format    Read function         write function                                       Best used for 
     
01   CSV	     pd.read_csv()	       df.to_csv('file.csv', index=False)	               Plain text, universal compatibility

02   Excel     pd.read_excel()	  df.to_excel('file.xlsx', sheet_name='Sheet1')	     Spreadsheets (.xlsx)

03   JSON	     pd.read_json()	       df.to_json('file.json')	                         Web APIs and nested data


Exporting Clean Data
When exporting DataFrames back to disk, set index=False to prevent Pandas from writing the default integer row numbers into your output file as an extra column:
Python

'''

import pandas as pd
df = pd.read_csv("stock_data.csv")

df = pd.read_csv("stock_data.csv",skiprows=1)  #we can skip rows from here 

df = pd.read_csv('stock_data.csv', header=1, names = ["symbol","eps","price","people"]) # we can change the name of coloum

# this is for specific value 
# here we provide a dictionary for specific value 
df = pd.read_csv('stock_data.csv', header=1, nrows=4 , na_values = {
    'eps':['not available'],
    'revenue':[-1],
    'people':['n.a.']
})# nrows => it shows only goals ]m 


# we can use this for every one 
df = pd.read_csv('stock_data.csv', header=1, na_values = ['not available',-1,'n.a.'])  # isme jha jha yeh aise rhengi wo NAN hojaygi

# now we are changing in file and export it as csv
# let say manager said to you that , can you calculate pe ratio coloum
df['pe'] = df['price']/df['eps']

# now we want to export this change into real csv file 
df.to_csv('pe.csv') # in your python.main folder your new file is saved 

# df.to_csv('pe.csv', index= False , header=False) # by index=0 (your serial no is removed) and by header=false (header is removed)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 15 ( reading excel files)
# for reading exel file , we need to run this command " pip install openpyxl" in your bash terminal

'''
Writing Data to Excel (to_excel)
A. Writing a Single DataFrame

# Save DataFrame to a single sheet without writing row numbers
df.to_excel('clean_movies.xlsx', sheet_name='Top_Movies', index=False)

B. Writing Multiple DataFrames to Multiple Sheets (pd.ExcelWriter)
To write multiple DataFrames into a single Excel workbook with multiple tabs, use the pd.ExcelWriter() context manager

 Handling Sheets
Unlike CSVs (which only store 1 flat table per file), Excel workbooks contain multiple tabbed sheets.

# Create an ExcelWriter object
with pd.ExcelWriter('company_report.xlsx', engine='openpyxl') as writer:
    df_bollywood.to_excel(writer, sheet_name='Bollywood', index=False)
    df_hollywood.to_excel(writer, sheet_name='Hollywood', index=False)
    df_summary.to_excel(writer, sheet_name='Summary_Stats')

'''

df_movies = pd.read_excel("movies-db.xlsx", "movies")  #excel file is movies-db , and in that files we are opening movies
df_movies.head(5)

df_financials = pd.read_excel("movies-db.xlsx", "financials")  #excel file is movies-db , and in that files we are opening financials
df_financials .head(6)


'''
# after below i am updating my functions 
def currencychanger (curr):
    if curr == "INR":
        return "USD"
    else
       curr


df_actors = pd.read_excel("movies-db.xlsx", "financials", convertors = {
'currency': currencychanger
}) 

'''
# read about pandas excel read documentation 

df_actors = pd.read_excel("movies-db.xlsx", "actors")  #excel file is movies-db , and in that files we are opening actors
df_actors .head(4)

df_merged = pd.merge(df_movies ,df_financials, on="movie_id" )

with pd.ExcelWriter("movie_final.xlsx") as writer:
    df_financials.to_excel(writer , sheet_name='financials')
    df_movies.to_excel(writer , sheet_name='movies')


