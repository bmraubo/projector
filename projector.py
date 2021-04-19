import os, argparse
from random import randint

#generate project name

def generate_project_name():
    confirm = ''
    #picks one adjective and one noun and joins them as 'adjective-noun'
    with open('english-adjectives.txt') as a:
        adjs = a.read().splitlines()
        adj = adjs[randint(0, len(adjs))]
    with open('english-nouns.txt') as n:
        nouns = n.read().splitlines()
        noun = nouns[randint(0, len(nouns))]
    project_name = str(adj + '-' + noun)
    #asks for confirmation before proceeding, in case name is stupid
    while confirm.lower() != 'y':
        print(f'Project will be called: {project_name}')
        confirm = input('Confirm? (y/n) ')
        if confirm.lower() == 'y':
            print(f'Project name {project_name} accepted!')
            return project_name
        elif confirm.lower() == 'n':
            project_name = generate_project_name()
        else:
            print(f'{confirm} is not valid input. Please try again.')
    
def custom_name():
    #allows input of custom name and checks
    confirm = ''
    while confirm != 'y':
        project_name = input('Enter Custom Name: ')
        confirm = input(f'Project will be called: {project_name}\nHappy? (y/n) ')
        if confirm.lower() == 'y':
            print(f'Project name {project_name} accepted!')
            return project_name
        elif confirm.lower() == 'n':
            continue
        else:
            print(f'{confirm} is not valid input. Please try again.')

def name_generator():
    #asks if user wants to custom name and runs appropriate func.
    confirm = ''
    while confirm.lower() != 'y' or confirm.lower() != 'n':
        confirm = input('Would you like to enter a custom project name? (y/n) ')
        if confirm.lower() == 'y':
            return custom_name()
        elif confirm.lower() == 'n':
            return generate_project_name()
        else:
            print(f'{confirm} is not valid input. Please try again.')

#create project directory

def create_top_folder(project_name):
    #creates the top folder and returns the path for use in other funcs
    folder_input = argparse.ArgumentParser()
    folder_input.add_argument('--dir', help='create project in directory')
    parent_folder = folder_input.parse_args().dir
    path = os.path.join(parent_folder, project_name)
    os.mkdir(path)
    return path

#set up venv

def create_venv(path):
    #creates venv and requirements.txt file
    os.system(f'python3 -m venv {os.path.join(path, "venv")}')
    with open(os.path.join(path, 'requirements.txt'), 'w+') as f:
        f.close()
    print(f'Virtual environment created at {path}')

#process

if __name__ == '__main__':
    project_name = name_generator()
    path = create_top_folder(project_name)
    create_venv(path)