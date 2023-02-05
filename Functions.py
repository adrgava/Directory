#Call of the libraries necessary for the program
import os

#Function to show the actual path directory
def show_path():
    #Get the actual path
    path = os.getcwd() 

    #Return the path
    return(path)   

#Function to show all elements from this path
def show_elements():
    #Get the actual path 
    actual_path = show_path()

    #Get the content from the actual directory path
    content = os.listdir(path = actual_path)

    #Recupera información del directorio
    information = os.scandir(actual_path)

    #Show all content and differentiates directories from files
    for element in information:
        #Show the directories
        if element.is_dir():
            print("Dir: ", element.name)
        #Show the files
        elif element.is_file():
            print(f"File: {element.name}")
    
#Function to create a new folder 
def create_folder(foldername):
    #Get the actual path 
    actual_path = show_path()

    #Generate the full path of the file, path + name 
    folder_path = os.path.join(actual_path, foldername)

    #Detect if the folder exist in the path, if not create the new folder
    if os.path.exists(folder_path):
        print("A folder with that name already exists")
    else:
        #Create the new folder
        os.mkdir(folder_path)
        print("Carpeta {} created".format(foldername))
