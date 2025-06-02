# This script is used to create a project structure so that manual creation of folders and files is not required saving time.

import os
import logging
from pathlib import Path

# Logging string
# This Logging string is required because whenever we execute this python script it will create the files and folders so instead of printing the execution of the operation we will log it which is a good practice when we are implementing any project so instead of using print statement use log statement which requires a loging string
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name= 'cnnClassifier'

list_of_files=[
    #create a folder called  github inside it create a folder called workflows and inside it create a file .gitkeep because whenever we commit our code in github if our folder is empty so it wont upload the folder to github unless it has some files present in it
    # this file will be removed when we are creating our cicd pipeline and will create our cicd component over there and for cicd deployment we need one file called main.yaml inside which we mention all our commands
    "github/workflows/.gitkeep",
    #creatiing a source folder src
    f"src/{project_name}/__init__.py",
    #create a component folder inside the src folder
    f"src/{project_name}/componenets/__init__.py",
     #create a utils folder inside the src folder
    f"src/{project_name}/utils/__init__.py",
    #create a config folder inside the src folder
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    #create a pipeline folder inside the src folder
    f"src/{project_name}/pipeline/__init__.py",
    #create a entity folder inside the src folder
    f"src/{project_name}/entity/__init__.py",
    #create a constant folder inside the src folder    
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")