#!/usr/bin/python3
"""
A program for the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


cls_var = ['BaseModel', 'User', 'State', 'City', 'Amenity']
cls_var.extend(['Place', 'Review'])


def parse(line, name, st=False):
    """
    Parses command line argument
    """
    if st:
        import shlex
        line = line.replace("update(", "").replace(")", "")
        line = line.replace("{", "").replace("}", "")
        line = line.replace(",", "").replace(":", "")
        li_st = shlex.split(line)
        new = {}
        i = 1
        while i < len(li_st) - 1:
            new[li_st[i]] = li_st[i + 1]
            i += 2
        li_st[0] = li_st[0].split('.')
        new_l = []
        new_l = [li_st[0], new]

        return new_l
    else:
        str_li = line.split('.')
        str_li[1] = str_li[1].replace(name, "").replace(")", "")
        str_li[1] = str_li[1].replace('"', "")
        str_li[1] = str_li[1].replace("'", "").replace(",", "")
    return ' '.join(str_li)


class HBNBCommand(cmd.Cmd):
    """A class for command line control"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """
        EOF command (control: ctrl+D)
         to exit the program
        """
        return True

    def emptyline(self):
        pass

    def default(self, line):
        if line.endswith('.all()'):
            class_name = line[:-6]
            self.do_all(class_name)
        elif line.endswith('.count()'):
            class_name = line[:-8]
            self.do_count(class_name)
        elif 'show' in line:
            self.do_show(parse(line, 'show('))
        elif 'destroy' in line:
            self.do_destroy(parse(line, 'destroy('))
        elif 'update' in line:
            if '{' in line and '}' in line:
                new = parse(line, 'update(', st=True)
                for k, v in new[1].items():
                    joined = ' '.join(new[0])
                    joined += f' {k} {v}'
                    self.do_update(joined)
            else:
                self.do_update(parse(line, 'update('))
        else:
            return super().default(line)

    def do_create(self, line):
        """
        -> Creates a new instance of BaseModel,
        -> saves it (to the JSON file) and prints the id
        -> Ex: $ create BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line in cls_var:
            new_instance = globals()[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        -> Prints the string representation of an instance based on:
         ~the class name and id.
        ->Ex: $ show BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in cls_var:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        new_dict = storage.all()
        search_key = f"{args[0]}.{args[1]}"
        if search_key in storage.all():
            print(storage.all()[search_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        -> Deletes an instance based on :
            `the class name and id`
            `(save the change into the JSON file).`
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in cls_var:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        search_key = f"{args[0]}.{args[1]}"
        if search_key in storage.all():
            del storage._FileStorage__objects[search_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        if arg and arg not in cls_var:
            print("** class doesn't exist **")
            return
        if not arg:
            for v in storage.all().values():
                print(v)
        else:
            for k, v in storage.all().items():
                name, id = k.split('.')
                if name == arg:
                    print(v)

    def do_update(sel, arg):
        """
        -> Updates an instance based on:
            `the class name` and `id`
            ->by adding or updating attribute
            ->(save the change into the JSON file).
        -> Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in cls_var:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        search_key = f"{args[0]}.{args[1]}"

        if search_key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        new_instance = storage.all()[search_key]
        setattr(new_instance, args[2], args[3].strip('\"'))
        new_instance.save()

    def do_count(self, arg):
        """
        Prints the total of all instances
        based or not on the class name
        """
        if not arg:
            if len(arg) == 0:
                print("** class name missing **")
                return
        if arg and arg not in cls_var:
            print("** class doesn't exist **")
            return
        count = 0

        for k, v in storage.all().items():
            name, id = k.split('.')
            if name == arg:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
