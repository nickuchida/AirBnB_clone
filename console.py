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
    '''Class for command prompt module'''
    HClasses = {"BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review}
    prompt = '(hbnb) '

    def empty(self):
        '''Empy line'''
        pass

    def help(self):
        '''Default help displays command options'''
        print('help commands')

    def emptyline(self):
        '''Prevents previous line from being reprinted'''
        pass

    def do_EOF(self, line):
        '''EOF to exit program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_create(self, line):
        '''Creates a new BaseModel Instance'''
        if line and line in self.HClasses.keys():
            k = self.HClasses[line]()
            k.save()
            print(k.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''
        Prints the string representation
        of an instance based on the class name and id
        '''
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
        '''Deletes an instance based on the class name and id'''
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
                else:
                    print("** no instance found **")

    def do_all(self, line=""):
        '''
        Prints all string representation of all instances
        based or not on the class name
        '''
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
        '''
        Updates an instance based on the class name and
        id by adding or updating attribute
        '''
        tokens = line.split(" ")
        if len(tokens) < 4:
            if len(tokens) == 0:
                print("** class name missing **")
            if len(tokens) == 1:
                print("** instance id missing **")
            if len(tokens) == 2:
                print("** value missing **")
            if len(tokens) == 3:
                print("** value missing **")
        else:
            c_name = tokens[0]
            if c_name not in HBNBCommand.HClasses.keys():
                print("** class doesn't exist **")
            _inst = tokens[1]
            val = self.obj[_inst].__class__.__name__
            if _inst not in self.obj or val != c_name:
                print("** no instance found **")
            att = tokens[2]
            att_val = tokens[3]
            (self.obj[_inst]).__dict__[att] = att_val
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
