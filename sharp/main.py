#!/usr/bin/python3
import sys

from utils import console
import commands

def main(args):
    if args == []: console.error("Please enter a command")
    command = args[0]
    arguments = args[1:]
    if command == "make":
        commands.make.make(arguments)
    elif command == "init":
        commands.init.init(arguments)
    elif command == "deploy":
        commands.deploy.deploy(arguments)
    else:
        console.error("Invalid command")

if __name__ == "__main__":
    console.console.print("\n💻 [bold white]Sharp v1.0.0[/bold white]\n")
    main(sys.argv[1:])
