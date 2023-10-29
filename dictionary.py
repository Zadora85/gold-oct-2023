# Import the 'os' module to work with the file system.
import os

# Change the current working directory (CWD), but the 'os.chdir' function call is missing the directory path.
os.chdir('gold-oct-2023')

# Get the current working directory (CWD).
cwd = os.getcwd()

files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

for file in files:
    file_path = os.path.join(cwd, file)
    file_size = os.path.getsize(file_path)
    print(f"File Name: {file}, File Size: {file_size} bytes")
    

        
    
    
    
    
    
        
    
    










    
    
    













