#!/usr/bin/python3
'''console for airbnb'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    '''class for command prompt module'''
    HClasses = {"BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review}
    prompt = '(hbnb) '

    def empty(self):
        '''empy line'''
        pass

    def help(self):
        '''default help displays command options'''
        print('help commands')

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''EOF to exit program'''
        return True

    def do_quit(self, line):
        '''quit to exit program'''
        return True

    def do_create(self, line):
        if line and line in self.HClasses.keys():
            k = self.HClasses[line]()
            k.save()
            print(k.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            if tokens[0] not in self.HClasses.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(tokens) == 2:
            if tokens[0] in self.HClasses.keys():
                string = "{}.{}".format(tokens[0], tokens[1])
                if string in storage.all().keys():
                    print(storage.all()[string])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            if tokens[0] not in self.HClasses.keys():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(tokens) == 2:
            if tokens[0] in self.HClasses.keys():
                string = "{}.{}".format(tokens[0], tokens[1])
                if string in storage.all().keys():
                    del storage.all()[string]
                    print("deleted")
                else:
                    print("** no instance found **")

    def do_all(self, line=""):
        if len(line) == 0:
            for key, value in storage.all().items():
                print(value)
        if line in self.HClasses.keys():
                for key, value in storage.all().items():
                    if line in key:
                        print(value)
        elif len(line) != 0 and line not in self.HClasses.keys():
            print("** class doesn't exist **")

    def do_update(self, line):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
