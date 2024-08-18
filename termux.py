import os
import subprocess

def clone_repo(repo_url, destination_folder):
    # Check if Git is installed
    if subprocess.run(["git", "--version"], capture_output=True).returncode != 0:
        print("Git is not installed. Please install Git and try again.")
        return
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Navigate to the destination folder
    os.chdir(destination_folder)
    
    # Clone the repository
    clone_command = f"git clone {repo_url}"
    result = subprocess.run(clone_command, shell=True)
    
    if result.returncode == 0:
        print(f"Repository cloned successfully into {destination_folder}")
    else:
        print(f"Failed to clone the repository. Error code: {result.returncode}")

if __name__ == "__main__":
    repo_url = input("Enter the repository URL: ")
    destination_folder = input("Enter the destination folder: ")
    clone_repo(repo_url, destination_folder)
