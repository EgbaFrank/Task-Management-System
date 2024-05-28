#!/usr/bin/env python3
"""Driver code for the models.base_model script"""
from models.base_model import BaseModel


base1 = BaseModel()
base1.name = "John Doe"

json_model = base1.to_dict()

base2 = BaseModel(**json_model)

print(base1.__dict__)
print(base2.__dict__)
print(type(base1.created_at))
print(type(base2.created_at))
print(base1)
base2.save()
print(base2)
