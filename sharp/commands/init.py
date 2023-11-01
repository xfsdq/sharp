import os
from utils import console, config

def init(args):
    if len(args) != 2: console.error("Invalid arguments")
    project_type = args[0]
    project_name = args[1]
    if project_type == "docker-php": init_docker_php(project_name)
    else: console.error("Invalid project type")

def init_docker_php(name):
    try:
        cwd = os.getcwd()
        data_dir = config.config["Sharp"]["DataDirectory"] + "/data/init/docker-php"

        os.makedirs(cwd + "/src/www", exist_ok=True)
        os.makedirs(cwd + "/src/db", exist_ok=True)

        with open(data_dir + "/docker-compose.yml") as f:
            docker_compose = f.read()
        with open(data_dir + "/Dockerfile") as f:
            dockerfile = f.read()


        with open(cwd + "/docker-compose.yml", "w") as f:
            f.write(docker_compose)
        with open(cwd + "/src/Dockerfile", "w") as f:
            f.write(dockerfile)

        console.success("Project created.")
    except:
        console.error("An error occurred.")