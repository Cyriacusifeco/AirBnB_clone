#!/usr/bin/python3
"""
Commandline interpreter that would allow for
easy manipulation of data for this project.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Entry point of command interpreter.
    """

    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
