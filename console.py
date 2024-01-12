#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it, and prints the id """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.CLASSES:
            print("** class doesn't exist **")
            return
        new_instance = FileStorage.CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """ Prints all string representations of all instances """
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(all_objs[obj]) for obj in all_objs])
        else:
            if args[0] not in FileStorage.CLASSES:
                print("** class doesn't exist **")
                return
            print([str(all_objs[obj]) for obj in all_objs if args[0] in obj])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in FileStorage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        storage.save()

    def do_quit(self, arg):
        """ Exits the program """
        return True

    def do_EOF(self, arg):
        """ Exits the program """
        print("")
        return True

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
