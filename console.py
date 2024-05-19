#!/usr/bin/python3
"""
Command interpreter for AirBnB clone project.
"""

import cmd
from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # Fetch instance here (to be implemented)
            pass

    # Additional command methods to be implemented...


if __name__ == '__main__':
    HBNBCommand().cmdloop()

