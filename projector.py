import os, argparse
from random import randint

#generate project name

def generate_project_name():
    #picks one adjective and one noun and joins them as 'adjective-noun'
    with open('english-adjectives.txt') as a:
        adjs = a.read().splitlines()
        adj = adjs[randint(0, len(adjs))]
    with open('english-nouns.txt') as n:
        nouns = n.read().splitlines()
        noun = nouns[randint(0, len(nouns))]
    return str(adj + '-' + noun)

def check_project_name(project_name):
    #checks project name with user (in case it is really stupid)
    confirm = ''
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

#create project directory

def create_top_folder(project_name):
    #creates the top folder and returns the path for use in other funcs
    folder_input = argparse.ArgumentParser()
    folder_input.add_argument('--dir', help='create project in directory')
    parent_folder = folder_input.parse_args().dir
    path = os.join(parent_folder, project_name)
    os.mkdir(path)
    return path

#set up venv

def create_venv(path):
    #creates venv and requirements.txt file
    os.system('python3 -m venv ' + path)
    with open(path + 'requirements.txt') as f:
        f.close()

#create repo folder

#set up github

def create_repo(project_name):
    os.system(f"curl -u 'qxcross' https://api.github.com/user/repos -d '{'name':'{project_name}', 'private': 'true'}'")



if __name__ == '__main__':
    project_name = generate_project_name()
    check_project_name(project_name)
    path = create_top_folder()
    create_venv(path)