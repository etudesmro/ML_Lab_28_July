import pandas as pd
import numpy as np
import os
import glob

def is_file_exist(filename):
    """
        if the file filename exists in current firectory return True, else False
    """
    fullname = os.path.join(os.getcwd(),filename)
    
    return os.path.isfile(fullname)
   
    
def read_dataset(filename, is_header_present=False):
    """
        The function reads the dataset from the provided path 
       
        Parameters:
            filename (str): filename to read
            is_header_present(boolean) : True for file having headers
                                         False if the file have no headers
                                         Default value is False

        Returns:
            dataFrame(panda.dataFrame):Returning value, can be None if the filename is not present
        
    """
    # if the file exists return the dataset inside, return an error message if not
    if is_file_exist(filename):
        if is_header_present:
            df = pd.read_csv(filename, sep=',')
        else:    
            df = pd.read_csv(filename, header=None, sep=',')
        
    else:
        df = None
    
    return df

def list_files():
    """
        Funtion to return a list of files in current directory
    """
    
    #get my pwd
    my_dir_is=os.getcwd()
    
    return os.listdir(my_dir_is)

def clean_extension(extension):
    
    """
        this function clean parameter extension of trailing spaces or .
        returns a clean extention
    """
    clean_extension = extension.strip()
    if clean_extension.startswith('.'): # Check if there is a . at the begining of the extension
        clean_extension = clean_extension[1:] # if yes, select only the extension fomr the 2nd character
    return clean_extension

def list_file_with_extension_cur_glob(extension):
    
    """
        The function filter the files presents in local directory filtered by extension,
        there is a list of allowed extensions : ['pdf','csv','data','txt']
       
        Parameters:
            extension (str): extension to filter on

        Returns:
            list of files having this extension
        
    """
    
    cleaned_extension = clean_extension(extension)
        
    allowed = ['pdf','csv','data','txt']
    
    try:
        if cleaned_extension not in allowed:
            raise ValueError
        else:
            current_directory = os.getcwd()
            full_path = os.path.join(current_directory, '*.' + cleaned_extension)
            return glob.glob(f"*.{cleaned_extension}")
        
    except ValueError:
        print('Extension used is not allowed, please used one of these : ')
        print(str(allowed))
    except Exception as e:
        print("Unexpected error:", e)

