#!/usr/bin/python3
"""
Entry point of the command interpreter.
"""
import cmd
from models import storage
from datetime import datetime

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
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        new_instance = storage.CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
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
        if class_name not in storage.CLASSES:
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
            print([str(obj) for obj in all_objs.values()])
        else:
            class_name = args[0]
            if class_name not in storage.CLASSES:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in all_objs.values() if isinstance(obj, storage.CLASSES[class_name])])

    def do_count(self, arg):
        """ Retrieves the number of instances of a class """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        count = sum(1 for obj in all_objs.values() if isinstance(obj, storage.CLASSES[class_name]))
        print(count)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id with a dictionary representation """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
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
            print("** dictionary missing **")
            return
        try:
            update_dict = eval(args[2])
            if not isinstance(update_dict, dict):
                raise ValueError("Not a dictionary")
        except (NameError, ValueError, SyntaxError):
            print("** invalid dictionary **")
            return
        for k, v in update_dict.items():
            setattr(all_objs[key], k, v)
        setattr(all_objs[key], 'updated_at', datetime.now())
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
