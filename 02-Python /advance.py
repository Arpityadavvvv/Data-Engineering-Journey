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


