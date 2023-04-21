#!/usr/bin/python3
"""
The almost a circle module
"""
import json
import csv


class Base:
    """
    Represents the Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns the JSON string
        representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes the JSON string
        representation of list_objs to a file."""
        with open("{}.json".format(cls.__name__), 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Function  that returns the list of the JSON string
        representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with all attributes
        already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            if cls.__name__ == "Square":
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances from a JSON strings file."""
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                f_contents = f.read()
                list_objs_dicts = cls.from_json_string(f_contents)
                list_objs = []
                for obj_dict in list_objs_dicts:
                    obj = cls.create(**obj_dict)
                    list_objs += [obj]
                return list_objs
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that writes the CSV string representation of
        a list of objects."""
        with open("{}.csv".format(cls.__name__), 'w+') as f:
            if list_objs is None or list_objs == []:
                f.write("")
            list_objs_dicts = [obj.to_dictionary() for obj in list_objs]
            write = csv.DictWriter(f, list_objs_dicts[0].keys())
            writer.writeheader()
            writer.writerows(list_objs_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """Function that returns a list of instances from a CSV file."""
        try:
            with open("{}.csv".format(cls.__name__), 'r') as f:
                reader = csv.DictReader(f)
                list_objs = []
                for row in reader:
                    obj_dict = {}
                    for k, v in row.items():
                        obj_dict[k] = int(v)
                    obj = cls.create(**obj_dict)
                    list_objs += [obj]
                return list_objs
        except IOError:
            return []
