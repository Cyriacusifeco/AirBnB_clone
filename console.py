#!/usr/bin/python3
"""
Commandline interpreter that would allow for
easy manipulation of data for this project.
"""

import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Entry point of command interpreter.
    """

    prompt = '(hbnb) '

    allowed_classes = ["BaseModel",
                        "User",
                        "State",
                        "City",
                        "Amenity",
                        "Place",
                        "Review",
                      ]

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""

        return True

    def help_quit(self):

        print("Quit command to exit the program")

    def help_EOF(self):

        print("EOF command to exit the program")

    def emptyline(self):
        pass

    def do_create(self, args):
        """
         Creates a new instance of BaseModel, saves it (to the JSON file)
         and prints the id. Usage: $ create BaseModel
        """
        if not args:

            print("** class name missing **")

            return

        class_name = args.split()[0]

        if class_name not in HBNBCommand.allowed_classes:

            print("** class doesn't exist **")

            return

        new_instance = eval(class_name + "()")

        new_instance.save()

        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""

        arg_list = args.split()

        if not arg_list:

            print("** class name missing **")

        elif arg_list[0] not in HBNBCommand.allowed_classes:

            print("** class doesn't exist **")

        elif len(arg_list) == 1:

            print("** instance id missing **")

        else:

            all_instances = models.storage.all()

            instance = arg_list[0] + '.' + arg_list[1]

            if instance in all_instances.keys():

                print(all_instances[instance])

            else:
                print("** no instance found **")

    def do_destroy(self, args):

        """Deletes an instance based on the class name and id
           (save the change into the JSON file)
        """

        arg_list = args.split()

        if not arg_list:

            print("** class name missing **")

        elif arg_list[0] not in HBNBCommand.allowed_classes:

            print("** class doesn't exist **")

        elif len(arg_list) == 1:

            print("** instance id missing **")

        else:

            all_instances = models.storage.all()

            instance_key = arg_list[0] + '.' + arg_list[1]

            if instance_key in all_instances.keys():

                del(all_instances[instance_key])
                models.storage.save()

            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""

        arg_list = args.split()

        if not args or arg_list[0] in HBNBCommand.allowed_classes:

            obj_list = []

            all_instances = models.storage.all()

            for instance in all_instances.values():

                obj_list.append(instance.__str__())

            print(obj_list)

        else:

            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (the changes are saved in a JSON file).
        Usage: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        arg_list = arg.split()

        if not arg_list:

            print("** class name missing **")

        elif arg_list[0] not in HBNBCommand.allowed_classes:

            print("** class doesn't exist **")

        elif len(arg_list) == 1:

            print("** instance id missing **")

        elif len(arg_list) == 2:

            print("** attribute name missing **")

        elif len(arg_list) == 3:

            print("** value missing **")

        else:
            all_obj = models.storage.all()

            instance = "{}.{}".format(arg_list[0], arg_list[1])

            if instance in all_obj.keys():

                for value in all_obj.values():

                    try:
                        attr_type = type(getattr(value, arg_list[2]))

                        arg_list[3] = attr_type(arg_list[3])

                    except AttributeError:
                        pass

                setattr(value, arg_list[2], arg_list[3])
                models.storage.save()

            else:
                print("** no instance found **")



if __name__ == '__main__':

    HBNBCommand().cmdloop()
