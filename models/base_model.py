#!/usr/bin/python3
"""
A base module that defines all common attributes/methods for
for other classes.

"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for
    other classes.
    """

    def __init__(self):
        """
        constructor method for BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        returns the string representation of
        the class.
        """
        return "[{}] ({}) <{}>"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):

        """
        updates the public instance attribute updated_at
        with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):

        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
