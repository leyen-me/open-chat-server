import os
import shutil
import zipfile


class FileUtil:

    @classmethod
    def delete_file(cls, file_path):
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 删除文件
            os.remove(file_path)
        else:
            pass

    @classmethod
    def delete_dir(cls, directory_path):
        # 检查文件夹是否存在
        if os.path.exists(directory_path):
            # 删除文件
            shutil.rmtree(directory_path)
        else:
            pass

    @classmethod
    def zip(cls, filepath, zippath):
        # 创建一个zip对象
        with zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 写入文件
            zipf.write(filepath)