#Call of the libraries necessary for the program
import os


#Function to show the actual directory
def show_path():
    #Get the actual path
    path = os.getcwd() 

    #Print the path
    print(path)   