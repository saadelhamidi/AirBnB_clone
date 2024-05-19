#!/usr/bin/python3
"""
Command interpreter module
"""
import cmd
import os
import re
import sys
import ast
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from uuid import uuid4

storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class to manage AirBnB objects
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if arg:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                storage.new(new_instance)
                storage.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Show an instance of a class based on its id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance based on its id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances or all instances of a class"""
        if arg:
            print([str(obj) for obj in storage.all().values()
                   if obj.__class__.__name__ == arg])
        else:
            print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Update an instance based on its id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
