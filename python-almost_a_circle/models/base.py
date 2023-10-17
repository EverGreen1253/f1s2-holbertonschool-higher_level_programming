#!/usr/bin/python3
""" Nameless module for Base class """
import json


class Base:
    """A Base class.

    Args:
        None

    Returns:
        Nothing

    """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def __str__(self):
        return self.id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to JSON string

        Args:
            list_dictionaries (any): the data to convert to JSON

        Returns:
            String representation of the converted data

        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return str(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Convert to JSON string then write to file

        Args:
            list_objs (any): the data to convert to JSON

        Returns:
            Nothing

        """

        class_name = cls.__name__
        file_name = class_name + ".json"

        to_save = []
        if list_objs is not None and len(list_objs) > 0:
            list_dictionaries = []
            for i in range(len(list_objs)):
                list_dictionaries.append(list_objs[i].to_dictionary())

            to_save = cls.to_json_string(list_dictionaries)

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(str(to_save))

    @staticmethod
    def from_json_string(json_string):
        """Convert string to json

        Args:
            json_string (str) : string representation of list of dicts

        Returns:
            list

        """

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a class instance with everything already set

        Args:
            key-value pairs (dictionary)

        Returns:
            the class instance

        """

        class_name = cls.__name__

        class_instance = None
        if class_name == "Rectangle":
            class_instance = cls(1, 1)
        elif class_name == "Square":
            class_instance = cls(1)

        class_instance.update(**dictionary)

        return class_instance

    @classmethod
    def load_from_file(cls):
        """Reads a file and creates mulitple class instances

        Args:
            nothing

        Returns:
            list of instances

        """

        filename = cls.__name__ + ".json"

        data = ""
        list_data = []

        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    data += line
        except IOError:
            return []

        list_data = cls.from_json_string(data)

        if len(list_data) == 0:
            return []

        list_instances = []
        for i in range(len(list_data)):
            new_instance = cls.create(**dict(list_data[i]))
            list_instances.append(new_instance)

        return list_instances
