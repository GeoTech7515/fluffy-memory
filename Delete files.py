import os

directory = 'D:\\' # specify the directory you want to look in
file_type = '.sno' # specify the file type you want to delete

for filename in os.listdir(directory):
    if filename.endswith(file_type):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
