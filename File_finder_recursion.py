#Implement a file recursion finder without using Python's os.walk()

import os 
path = r'example_directory_path_goes_here'

def find_files(suffix, path):
    '''
    Find all files beneath path with file name suffix.
    
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories
    
    There is no limit to the depth of the subdirectories.
    
    Args:
        suffix(str): suffix of the file name to be found
        path(str): path of the file directory
        
    Returns:
        a list of paths
    '''
    
    #Base case
    if len(os.listdir(path)) == 0:
        print("Empty path")
        
    if suffix == "":
        print("I don't want to return every type of file; give specific suffix")
        
    name_of_entries = os.listdir(path)
    
    file_paths = [entry for entry in name_of_entries if ('.' + suffix) in entry]
    
    folder_paths = [folder for folder in  name_of_entries if '.' not in folder]
    
    for folder in folder_paths:
        file_paths.extend(find_files(suffix=suffix, path=path + '/' + folder))
        #Recursive call done here
        
    return file_paths
    
    #Might be done
    
    
''' Edge test cases. Commented test cases are ones that fail'''

find_files(".c", path)
#We expect to return all files under a directory that end with ".c"
#['t1.c', 'a.c', 'b.c', 'a.c']
print(find_files("c", path))


#find_files(c, path)
#Wwe expect a NameError, since c is not the correct datatype


#find_files(_, path)
#We expect a NameError, since underscore _ is not the correct datatype

#find_files( ,path)
#We expect a SyntaxError, since we have a missing parameter    
    
    
    
    