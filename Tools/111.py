import os
import zipfile

def extract_all_zip_files():
    current_dir = os.getcwd()
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.zip'):
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall(current_dir)

if __name__ == "__main__":
    extract_all_zip_files()
