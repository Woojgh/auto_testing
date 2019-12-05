import os
import io
import json
import requests
import shutil


os.system('pip3 install pytest')
os.system('pip3 install requests')

repo_url = input('Please enter repo url to test.')

user, repo = repo_url.split('/')[3:]
git_url = repo_url + '.git'


def gps():
    return os.getcwd()


def clone():
    os.system(f'git clone {git_url}')


# def mem_god(path):
#     output = io.StringIO()
#     print(path)
#     file_name = path.split('/')[-1]
#     with open(os.getcwd() + '/' + file_name, 'rb') as input:
#         data = input.read(100000)
#         output.write(data)
#     return output

def refresh_dirs_and_files():
    for root, dirs, files in os.walk(os.getcwd()):
        return {'root': root, 'dirs': dirs, 'files': files}


def auto_test():
    _ = refresh_dirs_and_files()
    if 'test_copy.py' in _['files']:
        os.remove('test_copy.py')
        _ = refresh_dirs_and_files()
    if '__pycache__' in _['dirs']:
        shutil.rmtree('__pycache__')
        _ = refresh_dirs_and_files()
    for file in _['files']:
        if file.startswith("test_"):
            if file != 'test_copy.py':
                with open('test_copy.py', 'a+') as output, \
                        open(os.getcwd() + '/' + file, 'rb') as input:
                    data = input.read(100000)
                    output.write(data.decode())
                    output.close()
                    _ = refresh_dirs_and_files()
    for file in _['files']:
        if file.startswith("test_"):
            print('Testing: ' + file)
            os.system('pytest ' + file)
    if 'test_copy.py' in _['files']:
        os.remove('test_copy.py')



if __name__ == '__main__':
    auto_test()
