from enum import Enum
from http.client import HTTPException
from tkinter.tix import Form
from typing import List, Literal, Optional
from urllib import response

import time

from click import File
from fastapi import FastAPI, Query, Path, Body,Cookie,Header,UploadFile,Form, File, status,Depends,Request
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime, timedelta
from fastapi.encoders import jsonable_encoder
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt,JWTError
from fastapi.middleware.cors import CORS
app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/")
# async def post():
#     return {"message": "Hello fromt he post route.....!"}

# @app.put("/")
# async def put():
#     return {"message": "Hello fromt he put route.....!"}

# @app.get("/users")
# async def get_users():
#     return {"message": "list of users.....!"}


# @app.get("/users/{user_id}")
# async def get_user_id(user_id: int):
#     return {"user_id": user_id}



# class FoodEnum(str,Enum):
#     fruits = "fruits"
#     vegitable = "vegetable"
#     dairy = "dairy"
    
    
    
# @app.get("/foods/{food_name}")
# async def get_food_name(food_name: FoodEnum):
#     if food_name == FoodEnum.vegitable:
#         return {"food_name": food_name, "message": "vegitable food"}
    
    
#     if food_name == FoodEnum.dairy:
#         return {"food_name": food_name, "message": "dairy food"}
    
#     if food_name == FoodEnum.fruits:
#         return {"food_name": food_name, "message": "fruits food"}
    
#     return {"message": "food not found"}


# # fake_item_db = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"}]

# # @app.get("/items")
# # async def list_items(skip: int = 0, limit : int = 10):
# #     return fake_item_db[skip : skip + limit]    

 
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, sample_query_param:str, q: Optional[str] = None, short: bool = False):
#     item= {"item_id": item_id, "sample_query_param": sample_query_param}
    
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#         return item
#         # return ({"item_id": item_id, "q": q})   
#     # return ({"item_id": item_id})
    
    
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q:Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#         return item
#         # return ({"item_id": item_id, "q": q})   
#     # return ({"item_id": item_id})
    



# # Reques Body

# class Item(BaseModel):
#     name :str
#     desceription: Optional[str] = None
#     price:float
#     tax:float 
    
# @app.post("/items")
# async def create_item(item:Item ):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         return {"item": item, "price_with_tax": price_with_tax}
#     return item_dict


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}



# @app.get("/items")
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items_hidden")
# async def hidden_query_route(hidden_query: str = Query(..., include_in_schema=False)):
#     if hidden_query :
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}

# #  Path parametere and Numeric Validation
# @app.get("/item_validation/{item_id}")
# async def read_item_validation(*,item_id: int = Path(..., title = "ID of the item to get") , q: str = Query(None, alias="item-query")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results 


# # Body - Multiple parameters


# class Item(BaseModel):
#     name :str
#     description: Optional[str] = None
#     price:float
#     tax:Optional[float] = None
    
# class User(BaseModel):
#     username :str
#     full_name: Optional[str] = None
    
# @app.put("/items/{item_id}")
# async def update_item(*, 
#                       item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150), 
#                       q: Optional[str] = None, 
#                       item: Optional[Item] = None,
#                       importance: int = Body(...),
#                       user: User):
    
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results


# #Body Field

# class Item(BaseModel):
#     name : str
#     description: Optional[str] = Field (..., title="Description of the item")
#     price: float = Field (gt=0, description="The price must be greater than zero")
    
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item : Item = Body(...,embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results 


# #Body-  Nested Model

# class Item(BaseModel):
#     name : str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: list = []
    
    
# @app.put("/items/{item_id}")
# def updated_item(item_id : int, item:Item):
#     results = {"item_id":item_id, "item":item}
#     return results

#  Declare Request Example data 

# class Item(BaseModel):
#     name : str=Field(...,example="Foo")
#     description: Optional[str] =  Field(...,example="A very nice Item")
#     price: float = Field (...,example=35.4)
#     tax: Optional[float] =Field(...,example=3.2)
    
#     class Config:
#         schema_extra={
#             "example":{
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2
#             }
#         }
        
        
        
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id,"item": item}
#     return results


# # Extra Data Type
# @app.put("/items/{item_id}")
# async def read_items(item_id: UUID,
#                      start_datetime: Optional[datetime] = Body(None),
#                      end_datetime: Optional[datetime] = Body(None),
#                      repeat_at: Optional[datetime] = Body(None),
#                      process_after: Optional[timedelta] = Body(None)):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {"item_id":item_id,
#             "start_datetime":start_datetime,
#             "end_datetime":end_datetime,
#             "repeat_at":repeat_at,
#             "process_after":process_after,
#             "start_process":start_process,
#             "duration":duration ,
#             "repeat_at":repeat_at
#              }


## Cookie and Header Parameters

# @app.get("/items")
# async def read_items(cookies_id: str = Cookie(None),
#                      accept_encoding: Optional[List[str]] = Header(None, convert_underscores=False),
#                      sec_ch_ua: Optional[str] = Header(None),
#                      user_agent: Optional[str] = Header(None),
#                      x_token: List[str] = Header(None)):
#     return {"cookies_id": cookies_id,
#             "Accept-Encoding": accept_encoding,
#             "sec-ch-ua": sec_ch_ua,
#             "user-agent": user_agent,
#             "x-token": x_token
#             }


## Response Model

# class Item(BaseModel):
#     name : str=Field(...,example="Foo")
#     description: Optional[str] =  Field(...,example="A very nice Item")
#     price: float = Field (...,example=35.4)
#     tax: Optional[float] =Field(...,example=3.2)
    
    
# @app.post("/items", response_model=Item)
# async def create(item: Item):
#     return item

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserIn(UserBase):
#     password: str  

# class UserOut(UserBase):
#     pass

 
# @app.post("/users/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user

### Response Model with List

# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags : List[str] = []
    
    
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": ["tag1", "tag2"]},
# }


# @app.get("/items/{item_id}", response_model=Item,response_model_exclude_unset=True)
# async def read_item(item_id: Literal["foo", "bar", "baz"]):
#     return Item[item_id]

## Request form and file 
# @app.post("/files/")
# async def create_file(file: bytes=File(...), fileb : UploadFile=File(...),token : str = Form(...)):
#     return {'file': file, 'token': token, 'fileb': fileb.content_type}

##Path operation configuration

# class Item(BaseModel):
#     name:str
#     description:Optional[str] = None
#     price:float
#     tax:Optional[float] = None
#     tags: List[str] = None
    
    
# class Tags(Enum):
#     items ="items"
#     users = "users"
    
# @app.post("/items", 
#           response_model=Item,
#           status_code=status.HTTP_201_CREATED,
#           tags=['items'],
#           summary="Create an item",
#           description="Create an item with all the information, name, description, price, tax and a set of unique tags",)
# async def create_item(item: Item):
#     """
#     create an item with al informations
#     -**name**: The name of the item
#     -**description**: The description of the item
#     -**price**: The price of the item
#     -**tax**: The tax of the item
#     -**tags**: The tags of the item
#     """
#     return item

# @app.get("/items/",tags=[Tags.items,Tags.users])
# async def read_item():
#     return [{"name":"foo", "price":40}]

# @app.get("/users/",tags=[Tags.users])
# async def get_user():
#     return [{"name":"narayan"}]


# @app.get("/elements/",tags=[Tags.items], deprecated=True)
# async def read_element():
#     return [{"name":"foo", "price":40}]

## JSON compatibility Encode and body updates

# class Item(BaseModel):
#    name : str
#    description : Optional[str] = None
#    price : float
#    tax : Optional[float] = None
#    tags : List[str] = []
   

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar":{"name":"bar","description":"The bartenders","price":62,"tax":20.2},
#     "baz":{"name":"baz","description":None,"price":50.2,"tax":10.5,"tags":["tag1","tag2"]}   
# }
  
  
# @app.get("/items/{item_id}",response_model=Item)
# async def read_item(item_id: str):
#     return items.get(item_id)
  
# @app.put("/items/{item_id}")
# async def update_item(item_id: str, item: Item):
#     updated_item_encode = jsonable_encoder(item)
#     items[item_id] = updated_item_encode
    
#     return updated_item_encode 

# @app.patch("/items/{item_id}")
# async def patch_item(item_id: str, item: Item):
#     stored_item_data = items.get(item_id)
#     if stored_item_data is not None:
#         stored_item_data = Item(**stored_item_data)
        
#     else:
#         stored_item_data = Item()
        
#     update_data = item.dict()
#     update_item = stored_item_data.copy(update=update_data)
#     items[item_id]=     jsonable_encoder(update_item)
#     print(items)
#     return update_item
    
    
## Dependencies Intro


# async def common_parameters(q:Optional[str] = None, skip:int = 0, limit:int = 100):
#     return {"q":q,"skip":skip,"limit":limit}


# @app.get('/items/')
# async def get_item(commons: dict = Depends(common_parameters)):
#     return commons

# @app.get('/users/')
# async def get_user(commons: dict = Depends(common_parameters)):
#     return commons
         
         
# ##classes as dependencies
# fake_items_db = [{"item_name":"foo"}, {"item_name":"bar"}, {"item_name":"baz"}]

# class commonQueryParams:
#     def __init__ (self, q:Optional[str] = None, skip:int = 0, limit:int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit
        
        
# @app.get('/items/')
# async def read_item(commons: dict = Depends(commonQueryParams)):
#     response = {}
#     if commons.q:
#         response.update({"q":commons.q})
        
#     items = fake_items_db[commons.skip:commons.skip+commons.limit]
#     response.update({"items":items})
#     return response


## Sub Dependencies
## Security

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# fake_user_db = {
#     "johndoe": dict(
#         username="johndoe",
#         full_name="John Doe",
#         email="johndoe@example.com",
#         hashed_password="fakehashedhello123",
#         disable=False
#     ),
#     "alice": dict(
#         username="alice",
#         full_name="Alice",
#         email="alice@example.com",
#         hashed_password="fakehashedhello123",
#         disable=False
#     )
# }

# def fake_hash_password(password: str):
#     return f"fakehashed{password}"

# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disable: Optional[bool] = None

# class UserInDB(User):
#     hashed_password: str

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#     return None

# def fake_decode_token(token):
#     return get_user(fake_user_db, token)

# async def get_current_user(token: str = Depends(oauth2_schema)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(status_code=404, detail="Not found", headers={"www-authenticate": "Bearer"})
#     return user

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disable:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# app = FastAPI()

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_user_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect password")
#     return {"access_token": user.username, "token_type": "bearer"}

# @app.get("/users/me")
# async def get_me(current_user: User = Depends(get_current_active_user)):
#     return current_user

# @app.get("/items/")
# async def read_item(token: str = Depends(oauth2_schema)):
#     return {'token': token}



##Security with JWT

# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# fake_user_db = dict(
#     johndoe= dict(
#         username= "johndoe",
#         full_name= "John Doe",
#         email= "johndoe@example.com",
#         hashed_password= "$2b$12$qjasbFJL5Mty9Z/n7ZofC.QD2XINjR3uBtWRB7f6pyT9qi4Iyfitm",
#         disabled= False
#     )
# )

# class Token(BaseModel):
#     access_token: str
#     token_type: str
    
# class TokenData(BaseModel):
#     username: Optional[str] = None
    
# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None
    
# class UserInDB(User):
#     hashed_password: str
    
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
#     return None

# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt 

# @app.post("/token/", response_model=Token)
# async def login_for_access_token(form_data : OAuth2PasswordRequestForm =Depends()):
#     user = authenticate_user(fake_user_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    
#     access_token_expire = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub":user.username}, 
#      expires_delta=access_token_expire
#      )
#     return {"access_token": access_token, "token_type": "bearer"}
    

# async def get_current_user(token:str =Depends(oauth2_schema)):
#     credentials_exception = HTTPException(
#         # status_code=status.HTTP_401_UNAUTHORIZED,
#         # detail="Could not validate credentials",
#         # headers={"WWW-Authenticate": "Bearer"}
#     )
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         username : str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_user_db,username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
    
# async def get_current_active_user(current_user:User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# @app.get("/users/me", response_model=User)
# async def get_me(current_user:User=Depends(get_current_active_user)):
#     return current_user

# @app.get("/users/me/items")
# async def read_own_items(current_user:User=Depends(get_current_active_user)):
#     return [{"item_id":"foo"},{ "owner":current_user.username}]

## Middleware and CORS

# class MyMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request:Request, call_next):
#         start_time = time.time()
#         response = await call_next(request)
#         process_time = time.time()-start_time
#         response.headers["X-process-time"] = str(process_time)
#         return response

# origin = ["http://localhost:3000", "http://localhost:8000"]
   
# app.add_middleware(MyMiddleware)
# app.add_middleware(CORSMiddleware, allow_origin=origin)
# @app.get("/blah")
# async def read_blah():
#     return {"message": "Hello World"}


## SQL(Relation) Database 
