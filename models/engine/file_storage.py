#!/usr/bin/python3
"""
Este módulo define la clase FileStorage.
"""
import json
from os import path
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    La clase FileStorage se encargará se serializar y
    deserealizar archivos para recuperar instancias de BaseModel.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retorna el contenido de .__objects.
        Returns:
            dict
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Este método almacena la instancias de clase,
        recibidas en .__objects.
        Args:
            obj (object): Instacias a almacenar.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Este método guarda un diccionario retornado de las
        instancias almacenadas en .__objects.
        Return:
            None
        """
        new_dict = {}

        for k, obj in FileStorage.__objects.items():
            new_dict[k] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Este método lee un archivo en formato .json, que se guardo
        previamente con el método .save(), el diccionario recuperado
        se convertirá a objetos de python (dict) que seran utilizados
        para recuperar las instancias de clase BaseModel creadas
        anteriormente, estan istancias serán almacendas en .__objects.
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as json_file:
                objs = json.load(json_file)
            for k, v in objs.items():
                from models.base_model import BaseModel
                bs = BaseModel(**v)
                FileStorage.__objects[k] = bs

    def attributes(self):

        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str
                 },
        }

        return attributes
