import subprocess
import sys


if __name__ == '__main__':
    # If packages are renamed, then update these strings
    packages = ['model', 'view', 'controller'] if len(sys.argv) < 1 else sys.argv[1:]
    for package in packages:
        subprocess.run(f'python3 -m unittest discover tests.{package} "*_test.py" -v', check=True)
