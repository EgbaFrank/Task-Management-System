#!/usr/bin/env python3
"""
Contains base model implementation
"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents a Base Model with basic attributes and methods"""
    def __init__(self):
        """Initializes a BaseModel instance, with an ID and timestamp"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns class string format when print called"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates update_at timestamp"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of a BaseModel object"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
