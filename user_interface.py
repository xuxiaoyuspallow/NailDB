import cmd

from sqlcommandprocessor.parse import SqlParser


class Interface(cmd.Cmd):
    def __init__(self):
        super(Interface, self).__init__()
        self.prompt = '>>>'

    def parseline(self, line):
        """
        将语句传给sql解析器
        """
        print(SqlParser.execute(line))


if __name__ == '__main__':
    cli = Interface()
    cli.cmdloop('NailDB version 1.0, Enjoy yourself:)')
