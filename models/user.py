#!/usr/bin/python3
"""
A module for Users.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A Class, User that inherits from
    BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
