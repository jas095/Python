import os

def rename_files():
    #step one
    file_list = os.listdir(r"/home/jas/workspace-python/Curso/prank")#path to the files.
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"/home/jas/workspace-python/Curso/prank")
    
    #step two
    for file_name in file_list:
	print("Old name - "+file_name)
	print("New name - "+file_name.translate(None,'0123456789'))
        os.rename(file_name,file_name.translate(None,'0123456789'))
	
    os.chdir(saved_path)


rename_files()
