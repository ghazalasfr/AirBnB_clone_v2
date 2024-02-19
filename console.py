#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""the main console 
the console module

"""


from datetime import datetime
import re
import shlex
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City



class HBNBCommand(cmd.Cmd):
    """the class HBNBCommand definition"""
    prompt = '(hbnb) '
    myclasses = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        """
        pass

    def do_EOF(self, line):
        """
         terminate and quit
        """
        return True

    def do_Quit(self, line):
        """
        terminate and quit
        """
        return True

    def do_create(self, line):
        """ the create function
        it will Creates a new instance of BaseModel.
        """
        try:
            if not line:
                raise SyntaxError()

            split_line = line.split(" ")
            instance = eval("{}()".format(split_line[0]))

            for args in split_line[1:]:
                p = args.split("=")
                k = p[0]
                v = p[1].replace("_", " ")

                if hasattr(instance, k):
                    try:
                        setattr(instance, k, eval(v))
                    except Exception:
                        pass

            instance.save()

            print("{}".format(instance.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            pass

    def do_show(self, line):
        """ show function
        its Prints the string representation of an instance
        """
        cmd_args = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if cmd_args is None:
            print('** class name missing **')
        elif cmd_args not in self.myclasses:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            donnees = models.storage.all().get(cmd_args + '.' + arg)
            if donnees is None:
                print('** no instance found **')
            else:
                print(donnees)

    def do_destroy(self, line):
        """the destroy function
        that Deletes an instance based on the class name and id.
        """
        cmd_args = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if cmd_args is None:
            print('** class name missing **')
        elif cmd_args not in self.myclasses:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            key = cmd_args + '.' + arg
            donnees = models.storage.all().get(key)
            if donnees is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def all(self, line):
        """this function Prints all string representation of all instances
        """
        cmd_args = self.parseline(line)[0]
        objects_all = models.storage.all()
        if cmd_args is None:
            print([str(objects_all[obj]) for obj in objects_all])
        elif cmd_args in self.myclasses:
            keys = objects_all.keys()
            print([str(objects_all[key]) for key in keys if key.startswith(cmd_args)])
        else:
            print("** class doesn't exist **")

    def update(self, line):
        """this function 
        Updates an instance based on the class name and id
        """
        variables = shlex.split(line)
        args_size = len(variables)
        if args_size == 0:
            print('** class name missing **')
        elif variables[0] not in self.myclasses:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = variables[0] + '.' + variables[1]
            donnees = models.storage.all().get(key)
            if donnees is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                variables[3] = self.TestValue(variables[3])
                setattr(donnees, variables[2], variables[3])
                setattr(donnees, 'updated_at', datetime.now())
                models.storage.save()

    def TestValue(self, value):
        """ this function 
        Checks a parameter value for an update
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value

if __name__ == '__main__':
    HBNBCommand().cmdloop()
