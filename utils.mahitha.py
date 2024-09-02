''' ITERATION 2

Module: Mahitha Analytics - First Tutorial

'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Mahitha Analytics: First Tutorial'

####################################
# Define the get_byline() Function
###################################

def get_byline() -> str:
    """ Return the byline for my analytics project. """
    return byline 
    
####################################
# Define a main fucntion for this module.
###################################    

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    #print(byline)
    print(get_byline())

#####################################
# Conditional Execution 
#####################################

if __name__ == '__main__':
    main()
