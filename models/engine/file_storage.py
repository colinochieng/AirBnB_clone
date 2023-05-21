#!/usr/bin/python3
"""
->Module for:
        - storage of class
        - serialization of pyobject to JSON object
        - Deserialization from JSON object to pyobject
"""
import json
from datetime import datetime


class FileStorage:
    """
    -> serializes instances to a JSON file
    -> deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        return the objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Args:
                obj: BaseModel object
        sets in __objects the obj with key <obj class name>.id
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {k: obj.to_dict() for k, obj in FileStorage.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """
         deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                data = json.load(file)

            for key, value in data.items():
                mod_names = ['base_model', 'user', 'state', 'city']
                mod_names.extend(['amenity', 'place', 'review'])
                cls_names = ['BaseModel', 'User', 'State', 'City']
                cls_names.extend(['Amenity', 'Place', 'Review'])
                class_name, obj_id = key.split('.')
                name = ''
                for j, i in enumerate(cls_names):
                    if i == class_name:
                        name = mod_names[j]
                        break
                class_mod = __import__('models.' + name, fromlist=[class_name])
                class_ = getattr(class_mod, class_name)
                obj = class_(**value)
                for k, v in value.items():
                    if k == "created_at" or k == "updated_at":
                        value[k] = datetime.fromisoformat(v)
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
