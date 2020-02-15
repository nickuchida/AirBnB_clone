#!/usr/bin/python3
'''console for airbnb'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''class for command prompt module'''
    prompt = '(hbnb) '

    def empty(self):
        '''empy line'''
        pass

    def help(self):
        '''default help displays command options'''
        print('help commands')

    def do_EOF(self, line):
        '''EOF to exit program'''
        return True

    def do_quit(self, line):
        '''quit to exit program'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
