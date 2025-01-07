from setuptools import setup, Extension
from Cython.Build import cythonize
import logging
import time
import sys, os
default = False
#file_name = input("Enter the file name: ")
version = "1.0.0"
def check_and_prevent_if_needed():
    try:
        import requests
        jsonSettings = requests.get('https://raw.githubusercontent.com/hackesofice/Z/refs/heads/main/CPYTHON-TOOL/settings.json').json()
        if not jsonSettings or not jsonSettings.get('tool-status'):
            print('Tool Has Been Turned off By The Admin')
            sys.exit()
        elif not jsonSettings or not jsonSettings.get('logs-check'):
            logs_check = False
            print('we are trying to compile please wait this process takes time (sometimes 5 - 10 minutes)')
        elif not jsonSettings or jsonSettings.get('version') != version:
            print('you are trying to use an older version pf this tool please copy and paste the commands from the next screen we are trying to redirect you to the official Tool page')
            os.system('xdg-open https://github.com/hackesofice/Encrypt-python.git')
            print('Not Redirected till now ?? Navigate manually to the Official tool page by using this  link ====>>>>  https://github.com/hackesofice/Encrypt-python.git')
            sys.exit() 
    except requests.RequestException as e:
        print(f'please check your connection and try again after some time ::  {e}')
        sys.exit()
        
        
def solve_the_mixed_tab_and_space_issue(file_name):
    try:
        if not file_name:
            file_name = input("enter the currect file name:  ")
        replacement_count = 0
        lines_with_replacements = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
        with open(file_name, 'w') as file:
            for line_number, line in enumerate(lines, start=1):
                tab_count = line.count('\t')
                if tab_count > 0:
                    replacement_count += tab_count
                    lines_with_replacements.append(f"Line {line_number}: {tab_count} tabs replaced")
                file.write(line.replace('\t', '    '))
        print(f"Tabs replaced with spaces successfully.")
        print(f"Total replacements made: {replacement_count}")
        if lines_with_replacements:
            print("Details of replacements:")
            for detail in lines_with_replacements:
                print(detail)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        solve_the_mixed_tab_and_space_issue(default)
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
source_file = input("Enter the file path (e.g., my_module.pyx): ")
file_directory = os.path.dirname(source_file)
print(f'the file directory is ::::{file_directory}')
nme = input("Enter the output file name (without extension) or press enter to continue with current file name: ")
if not nme:
    nnn = source_file.split('.')[0]
    if "/" in nnn:
        output_name = nnn.split('/')[-1]
    else:
        output_name = nnn
else:
    output_name = nme
solve_the_mixed_tab_and_space_issue(source_file)
solve_the_mixed_tab_and_space_issue(source_file)
check_and_prevent_if_needed()
time.sleep(5)
#os.chdir(file_directory)
#logging.getLogger("Cython").setLevel(logging.CRITICAL)

# Redirect stdout and stderr to suppress logs
class NullWriter:
    def write(self, _):
        pass
    
    def flush(self):
        pass  # Implement flush to avoid the error

null_output = NullWriter()
sys.stdout = null_output
#sys.stderr = null_output

"""

"""

setup(name="YourModuleName",
    ext_modules=cythonize(
        Extension(
            output_name,  # Nam6e of the resulting .so file
            sources=[source_file],  # Source file
          #  library_dirs=[f"{file_directory}"],
        ),
       # build_dir=file_directory,
        compiler_directives={'language_level': "3"},  # Set to Py>
    ),
)

# Restore stdout and stderr
sys.stdout = sys.__stdout__
#sys.stderr = sys.__stderr__
os.system(f"rm -rf build {source_file.split('.')[0]}.c")
so_file = f"{output_name}.cpython-*.so"
if file_directory: 
    os.system(f'mv {so_file} {file_directory}')
