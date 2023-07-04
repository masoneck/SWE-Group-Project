import subprocess



if __name__ == '__main__':
    subprocess.run(r'pylint .\tests\ .\src\ --disable=missing-module-docstring', check=True)