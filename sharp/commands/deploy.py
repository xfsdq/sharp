import configparser
import paramiko
import json

from utils import config as cfg, console

def deploy(args):
    remote = True
    if "--local" in args:
        remote = False
        args.remove("--local")

    if args[0] == "db":
        deploy_database(remote)

def deploy_database(remote):
    config = cfg.config
    host = config["SSH"]["host"]
    username = config["SSH"]["username"]
    password = config["SSH"]["password"]
    known_hosts = config["SSH"]["knownHosts"]
    if remote:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys(known_hosts)
        ssh.connect(host, username=username, password=password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("python3 /data/scripts/init_db.py")
        credentials = json.loads(ssh_stdout.read().decode())
        console.success("Database created.", pad=False)
        console.info("Host: " + credentials[0] + ":" + credentials[1], pad=False)
        console.info("Username: " + credentials[2], pad=False)
        console.info("Password: " + credentials[3], pad=False)
        console.info("Admin: http://" + credentials[0] + ":" + str(int(credentials[1])+1))
