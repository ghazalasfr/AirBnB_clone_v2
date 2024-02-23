
nsole for AirBnB"""
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """the main class
    """
    prompt = "(hbnb) "
    all_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def emptyline(self):
        """empty lines"""
        pass

    def do_quit(self, line):
        """quit function"""
        return True

    def do_EOF(self, line):
        """eof funstion"""
        return True

    def do_create(self, args):
        """create function
            SyntaxError: ...
            NameError: ...

        """

        try:
            if not args:
                raise SyntaxError()

            varsplite = args.split(" ")
            inst = eval("{}()".format(varsplite[0]))

            for i in varsplite[1:]:
                x = i.split("=")
                key = x[0]
                value = x[1].replace("_", " ")

                if hasattr(inst, key):
                    try:
                        setattr(inst, key, eval(value))
                    except Exception:
                        pass

            inst.save()

            print("{}".format(inst.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            pass

    def do_show(self, line):
        """show function
            SyntaxError: ...
            NameError: ...
            IndexError: ...
            KeyError: ...
        """
        try:
            if not line:
                raise SyntaxError()
            listes = line.split(" ")
            if listes[0] not in self.all_classes:
                raise NameError()
            if len(listes) < 2:
                raise IndexError()
            objects = storage.all()
            key = listes[0] + '.' + listes[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy function
            SyntaxError: ...
            NameError: ...
            IndexError: ...
            KeyError: ...
        """
        try:
            if not line:
                raise SyntaxError()
            listes = line.split(" ")
            if listes[0] not in self.all_classes:
                raise NameError()
            if len(listes) < 2:
                raise IndexError()
            objects = storage.all()
            key = listes[0] + '.' + listes[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all function
        Exceptions:
            NameError: ...
        """
        objects = storage.all()
        listes = []
        if not line:
            for key in objects:
                listes.append(objects[key])
            print(listes)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.all_classes:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    listes.append(objects[key])
            print(listes)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates function
        """
        try:
            if not line:
                raise SyntaxError()
            listes = split(line, " ")
            if listes[0] not in self.all_classes:
                raise NameError()
            if len(listes) < 2:
                raise IndexError()
            objects = storage.all()
            key = listes[0] + '.' + listes[1]
            if key not in objects:
                raise KeyError()
            if len(listes) < 3:
                raise AttributeError()
            if len(listes) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[listes[2]] = eval(listes[3])
            except Exception:
                v.__dict__[listes[2]] = listes[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """count function
        """
        counter = 0
        try:
            listes = split(line, " ")
            if listes[0] not in self.all_classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == listes[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """strips function
        Args:
            args: ...
        Return:
            returns string of argumetns
        """
        nouveau = []
        nouveau.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            nouveau.append(((new_str.split(", "))[0]).strip('"'))
            nouveau.append(my_dict)
            return nouveau
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        nouveau.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in nouveau)

    def default(self, line):
        """default function
        """
        listes = line.split('.')
        if len(listes) >= 2:
            if listes[1] == "all()":
                self.do_all(listes[0])
            elif listes[1] == "count()":
                self.count(listes[0])
            elif listes[1][:4] == "show":
                self.do_show(self.strip_clean(listes))
            elif listes[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(listes))
            elif listes[1][:6] == "update":
                args = self.strip_clean(listes)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
