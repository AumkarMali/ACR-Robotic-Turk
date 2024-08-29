import subprocess

def clear_moves(file_path):
    try:
        with open(file_path, 'r+') as file:
            file.truncate(0)  # Truncate the file to zero length
    except IOError as e:
        print(f"File I/O error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

clear_moves('save_move.txt')


# Paths to the Python scripts
venv_python = '.venv\\Scripts\\python.exe'
script1 = 'gameProcessing.py'
script2 = 'GUI.py'

process1 = subprocess.Popen([venv_python, script1])
process2 = subprocess.Popen([venv_python, script2])

process1.wait()
process2.wait()
