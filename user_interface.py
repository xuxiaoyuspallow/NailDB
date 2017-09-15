import cmd


class Interface(cmd.Cmd):
    def __init__(self):
        super(Interface, self).__init__()
        self.prompt = '>>>'

    # def



if __name__ == '__main__':
    cli = Interface()
    cli.cmdloop('NailDB version 1.0, Enjoy yourself:)')