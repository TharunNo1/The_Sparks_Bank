from django.db import models
from datetime import datetime

class Customer:
    id: int 
    name: str 
    balance: int 

class Trans:
    sender: str 
    receiver: str 
    amount: int
    status: str
    datetime: datetime