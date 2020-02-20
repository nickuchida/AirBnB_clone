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
        mydict = storage.all()
        vclasses = ['BaseModel', 'Place', 'User', 'State',
                    'City', 'Amenity', 'Review']

        tokens = line.split(" ")

        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in vclasses:
            print("** class doesn't exist **")
            return
        if tokens[0] in vclasses and len(tokens) < 2:
            print("** instance id missing **")
            return
        if "{}.{}".format(tokens[0], tokens[1]) not in mydict.keys():
            print("** no instance found **")
            return
        if len(tokens) == 2:
            print("** attribute name missing **")
            return
        if len(tokens) == 3:
            print("** value missing **")
            return
        if tokens[2] not in ["id", "updated_at", "created_at"]:
            obj = mydict[name]
            obj.__dict__[tokens[2]] = token[3]
            obj.updated_at = datetime.now()
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
