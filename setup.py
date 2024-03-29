import os
import zipfile

def unzip_tool_zip():
    # 获取当前文件的路径
    current_path = os.path.dirname(os.path.abspath(__file__))
    
    # Tool.zip文件路径
    tool_zip_path = os.path.join(current_path, 'Tools.zip')

    # 判断Tool.zip文件是否存在
    if os.path.exists(tool_zip_path):
        # 解压Tool.zip文件到当前文件夹
        with zipfile.ZipFile(tool_zip_path, 'r') as zip_ref:
            zip_ref.extractall(current_path)
        print("setup finished")
    else:
        print("ERROR")

if __name__ == "__main__":
    unzip_tool_zip()
