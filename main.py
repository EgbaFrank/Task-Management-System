#!/usr/bin/env python3
"""Driver code for the models.base_module script"""
from models.base_model import BaseModel


base1 = BaseModel()

base1.name = "John Doe"

print(base1.__dict__)

print(base1)
