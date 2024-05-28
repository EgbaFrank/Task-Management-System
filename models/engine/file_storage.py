#!/usr/bin/env python3
"""
Contains file storage functionality
"""
import json


class FileStorage:
    """Enable objects persistence via file storage"""
    __file_path = "instances.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all stored objects"""
        return __objects

    def new(self, obj):
        """Adds a new object"""
        __objects[f"{obj.__class__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """Serializes and save the __objects dictionary to file"""
        with open(__file_path, 'w', encoding="utf-8") as file:
            json.dump(__objects, file)

    def reload(self):
        """Deserializes the JSON string from file"""
        try:
            with open(__file_path, encoding="utf-8") as file:
                __objects = json.load(file)
        except FileNotFoundError:
            pass
