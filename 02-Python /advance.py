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


