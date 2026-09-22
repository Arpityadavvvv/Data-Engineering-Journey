from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
  return {"message": "PyCharm + FastAPI setup complete! or baki chize bhi "}


@app.get("/test")
def test():
  return {"status": "Success"}


@app.get("/")  # Yahan '/' ki jagah '/hello' likhna hai
def hello():
  return {"hello": "world"}

food_items = {
  'indian':['samosa','dosa','idli'],
  'american':['crsoo','latte','bun'],
  'italian':['pasta','bread']
}
from enum import Enum
class avialblCuisine (str,Enum):
  indian = "indian"
  american = "american"
  italian = "italian"

'''

01 FastApi decorator ke thik neeche likhe function 
ko automatically pakad leta hai.

02 Doubt 02: Kya get_items function API call ke sath juda hua hai?
Haan, 100% juda hua hai!

03 Doubt 03: food_items ko kaise pata chala ki cuisine ka matlab khana hai?
food_items (ya computer) ko English ka "cuisine" matlab nahi pata! Uske liye 
cuisine bas ek variable (box) hai.

04  {} Kyu Lagate Hain url me ?
{} ka matlab hota hai ki URL ka yeh hissa fixed (hardcoded) nahi hai,
 balki change hota rahega.
 
05 FastAPI ko pehle se bata rahe ho ki roll_number ki value hamesha ek Integer 
(Number) honi chahiye.

'''
@app.get("/get_items/{cuisine}")
def get_items(cuisine:avialblCuisine):
  return food_items.get(cuisine)

# http://127.0.0.1:8000/get_items/american

coupen = {

  1 : '10% dscount',
  2 : '20% discount',
  3 : '30% discount'
}

@app.get("/get_coupen/{code}")
def get_coupen (code : int):
      return coupen.get(code)

#http://127.0.0.1:8000/docs will give you inbult documentation


'''

formatted_list = [
    # ------------------ PART 1: FORMAT ------------------
    {
        'name': d['name'],
        'email': d['email'],
        'address': f"{d['address']['street']}, {d['address']['city']}",
    }
    # ------------------ PART 2: LOOP --------------------
    for d in data
]

Rule Remember karne ka Easy RuleJab bhi aap List Comprehension 
likhein, hamesha is structure ko yaad rakhein Pura Output Format for{ item } 
in  list text

'''

# these are importan resources 

01 https://jsonplaceholder  # this is placeholder  on which we can test API's 

02 if we use  http://127.0.0.1:8000/docs  # this is place fastapi provides api docs and testing 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class - 02 
# src/customers_db.py

class CustomersDB:
    def __init__(self):
        """Initialize an in-memory list to simulate a database."""
        self.customers = []
        self.next_id = 1
        self.connection = None

    def connect(self):
        """Simulate connecting to a database."""
        self.connection = "DummyConnectionObject"
        print("Connected to the database.")

    def insert_customer(self, name, email):
        """Insert a new customer into the list."""
        customer = {
            "id": self.next_id,
            "name": name,
            "email": email
        }
        self.customers.append(customer)
        self.next_id += 1

    def get_all_customers(self):
        """Retrieve all customers from the list."""
        return self.customers

    def get_customer_by_name(self, name):
        """Retrieve a customer by name."""
        for customer in self.customers:
            if customer["name"] == name:
                return customer
        return None

    def clear_customers(self):
        """Clear all customers (reset the database)."""
        self.customers = []
        self.next_id = 1

    def close(self):
        """Simulate closing the database connection."""
        self.connection = None
        print("Database connection closed.")

# test file 

import pytest
from customer_db import CustomersDB


def test_insert_customer():
    db = CustomersDB() # creating db object
    db.connect()  # connecctig db

    db.insert_customer("Virat Kohli", "virat@xyz.com")
    customer = db.get_customer_by_name("Virat Kohli")
    assert customer is not None
    assert customer['name'] == "Virat Kohli"
    assert customer['email'] == "virat@xyz.com"

    db.close()

def test_get_all_customers():
    db = CustomersDB()
    db.connect()

    db.insert_customer("Virat Kohli", "virat@xyz.com")
    db.insert_customer("Taylor Swift", "taylor@xyz.com")

    customers = db.get_all_customers()
    assert len(customers) == 2

    db.close()

# test file 2 
import pytest
from customer_db import CustomersDB

@pytest.fixture
def db():
    db_instance = CustomersDB()
    db_instance.connect()
    yield db_instance
    db_instance.close()


def test_insert_customer(db):
    db.insert_customer("Virat Kohli", "virat@xyz.com")
    customer = db.get_customer_by_name("Virat Kohli")
    assert customer is not None
    assert customer['name'] == "Virat Kohli"
    assert customer['email'] == "virat@xyz.com"
    db.clear_customers()


def test_get_all_customers(db):
    db.insert_customer("Virat Kohli", "virat@xyz.com")
    db.insert_customer("Taylor Swift", "taylor@xyz.com")

    customers = db.get_all_customers()
    assert len(customers) == 2

    db.clear_customers()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# pydantic 

from fstapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int

''' 
#### Create a model for User
@app.post("/add_user/")
def create_user(user: User):
    return f"User created successfully: User {user}"

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


from pydantic import ValidationError

user = User(id=3, name="Dhaval Patel")

### It will throw an error when a field is missing

from pydantic import ValidationError
user = User(id=3, name="Dhaval Patel")
from pydantic import ValidationError

user = User(id=3, name="Dhaval Patel")


02 #### It will throw error when invalid data type is passed

User(id=3, name="Dhaval Patel", age="30 years", email="dhaval@xyz.com")
'''

'''
# after automation it will not throw an error 

User(id=3, name="Dhaval Patel", age="30", email="dhaval@xyz.com")

from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    address: Optional[str] = None

user = User(id=3, name="Dhaval Patel", age=30, email="dhaval@xyz.com")
print(user)
'''


# final quiz learning 
#=------------------------------------------------------------------------------------------------#
# Final Quiz question

01 What is the purpose of PEP 20, also known as the Zen of Python?
Ans :To provide a set of 19 guiding principles for writing clean, readable, and idiomatic Python code.

02 To throw an exception you need to use the following in Python ?
Ans: The raise keyword.

03 The purpose of OCR (Optical Character Recognition) is to ?
Ans :Convert images of text (scanned documents, photos, PDF images) into machine-editable and searchable text data

04 The database and surrounding system that is used for analytical needs is called ?
Ans :Data Warehouse (or an OLAP system - Online Analytical Processing).

05 Write a regular expression to represent an Indian phone number. For example: (91)8899776655. Here first 4 characters must be (91)
   and then there should be exactly 10 digits
Ans:

06 You have a string s="IBM|US|100|5.4", you want to separate individual components by
   | so that you get "IBM", "US", "100" and "5.4" as a separate element. For this you can use,
Ans: s.split('|')

07 How to access the last letter of a string?
Ans :Using negative indexing: s[-1]

08 Python is popular because
Ans Simple and highly readable syntax, vast library ecosystem, and versatility across different
    domains (Data Engineering, AI, Web, Automation).

09 Which of the following code snippets will raise a ValueError in Python?
Ans

Q12.
Let’s say you have a pandas dataframe that has three columns (1) match_id (2) player_name (3) score. Each row represents a score by a player in a given match. What is the correct code that will display the player's name and their total score?

df.player.groupby().score.sum()
df.player.groupby().score.total()
df.groupby(”player”)[”score”].sum()
df.groupby(”score”)[”player”].sum()

Q19.
Which of the following code snippets will raise a ValueError in Python?
int("twenty")
"data" * "3"
print(len([1, 2, 3]))
result = 10 / 0

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# testing using pytest assignment 

# iventory.py
class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity
        else:
            self.stock[item] = quantity

    def remove_stock(self, item, quantity):
        if item not in self.stock or self.stock[item] < quantity:
            raise ValueError("Insufficient stock")
        self.stock[item] -= quantity

    def check_availability(self, item, quantity):
        return self.stock.get(item, 0) >= quantity

# test_inventory.py
import pytest
from iventory import Inventory

def test_add_stock():
    inv = Inventory()

    # 2. ACT: Ussi warehouse me 100 Apples add kiye
    inv.add_stock('Apple', 100)

    # 3. ASSERT: Ussi warehouse se check kiya ki 100 Apples hain ya nahi
    assert inv.check_availability('Apple',100) is True

def test_remove_stock():
    inv = Inventory()
    inv.add_stock('Apple', 100)

    inv.remove_stock('Apple',50)

    assert inv.check_availability('Apple',50) is True

def test_check_availability():
    inv = Inventory()

    # 01 Add the apple in stock
    inv.add_stock('Apple', 100)

    # 02 Remove 50 apples from stock
    inv.remove_stock('Apple', 50)

    # 03 now i am checking 50 apples are avilable in stock or not
    inv.check_availability('Apple', 50) is True

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------




