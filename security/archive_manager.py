import shutil
import os

def archive_session(folder_path, archive_name="session_backup.zip"):
    shutil.make_archive(archive_name.replace(".zip", ""), 'zip', folder_path)
