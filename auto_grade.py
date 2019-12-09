import os
import shutil

try:
    import requests
except:
    os.system('pip3 install requests')
    uninstall_requests = True
    import requests


try:
    import pytest
except:
    os.system('pip3 install pytest')
    uninstall_pytest = True
    import pytest


def gps():
    return os.getcwd()

# test_url = input('Please input test url, local or web')


# repo_url = input('Please enter repo url to test.')

# user, repo = repo_url.split('/')[3:]
# test_user, test_repo = test_url.split('/')[3:]

# git_url = repo_url + '.git'
def get_test_file(file_name):
    file_pile = requests.get('https://api.github.com/repos/Woojgh/data-structure/contents/src/tests')
    return [i for i in file_pile.json() if i['name'] == file_name][0]['download_url']


# def clone():
#     os.system(f'git clone {git_url}')


# def mem_god(path):
#     import io
#     output = io.StringIO()
#     print(path)
#     file_name = path.split('/')[-1]
#     with open(os.getcwd() + '/' + file_name, 'rb') as input:
#         data = input.read(100000)
#         output.write(data)
#     return output

def refresh_dirs_and_files():
    for root, dirs, files in os.walk(gps()):
        return {'root': root, 'dirs': dirs, 'files': files}


def auto_test():
    _ = refresh_dirs_and_files()
    if 'test_copy.py' in _['files']:
        os.remove('test_copy.py')
    if 'results.log' in _['files']:
        os.remove('results.log')
        _ = refresh_dirs_and_files()
    if 'teacher_test_copy.py' in _['files']:
        os.remove('teacher_test_copy.py')
        _ = refresh_dirs_and_files()
    if '__pycache__' in _['dirs']:
        shutil.rmtree('__pycache__')
        _ = refresh_dirs_and_files()
    test_file_name = [i for i in _['files'] if '.py' in i and 'test_' in i][0]
    test_copy = requests.get(get_test_file(test_file_name))._content
    name_list = []
    with open('teacher_test_copy.py', 'a+') as get_output:
        get_output.write(test_copy.decode())
        get_output.close()
    test_list = [i for i in test_copy.decode().split('def')]

    for line in test_list[1:]:
        assert_line = line.split('(')[0]
        name_list.append(assert_line)
    for file in _['files']:
        if file.startswith("test_"):
            if file != 'test_copy.py':
                with open('test_copy.py', 'a+') as output, \
                        open(gps() + '/' + file, 'rb') as input:
                    data = input.read(100000)
                    output.write(data.decode())
                    output.close()
                    _ = refresh_dirs_and_files()
    for file in _['files']:
        if file.startswith("teacher"):
            print('Testing teacher file: ' + file)
            for name in name_list:
                tested_file = os.system('pytest -v -k ' + name + ' ' + file + ' | tee -a results.log')
        elif file.startswith("test_"):
            print('Testing: ' + file)
            tested_file = os.system('pytest ' + file)
    with open('results.log', 'rb') as thing: data = thing.read(10000)
    total = len([i for i in data.decode().split('teacher_test_copy')])
    passed = len([i for i in data.decode().split('teacher_test_copy') if 'PASSED' in i])
    if passed > total / 2:
        print("Tests Unlocked")
    else:
        print("Tests are still locked")
    if 'test_copy.py' in _['files']:
        os.remove('test_copy.py')
    if 'teacher_test_copy.py' in _['files']:
        os.remove('teacher_test_copy.py')


if __name__ == '__main__':
    auto_test()
    os.system('pip3 uninstall -n requests')
    os.system('pip3 uninstall -n pytest')
    # os.system('pip3 uninstall -y requests')
    # os.system('pip3 uninstall -y pytest')
