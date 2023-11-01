import os
from utils import console

def make(args):
    if args == []: console.error("Please enter a command")
    if args[0] == "rewrite":
        if len(args) == 1: console.error("Please enter a file extension")
        path = args[2] if len(args) == 3 else ""
        make_htaccess(args[1], path)

def make_htaccess(extension, path):
    try:
        if not path: path = os.getcwd()
        htaccess = """RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^\.]+)$ $1."""+extension+""" [NC,L]\n"""
        with open(path + "/.htaccess", "a") as f:
            f.write(htaccess)
        console.success("Rewriting successfully created")
    except:
        console.error("[red][bold]✗[/bold] An error occurred while creating .htaccess[/red]")