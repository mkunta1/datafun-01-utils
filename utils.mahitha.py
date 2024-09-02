''' ITERATION 3

Module: Mahitha Analytics - First Tutorial

'''

#####################################
# Declare a global variable named byline.
#####################################

# Boolean variables to indicate if the company has international clients and is privately owned.

has_international_clients: bool = True
is_provately_held: bool = True

#Interger variable for the number of years in operation 
years_in_operation: int = 10
number_of_months:   int = 12

#List of strings representing the skills pffered by the company 
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
courses_offered: list = ["math", "science", "english"]

#List of floats representing individual client satisfaction scores 
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
temperature_values: list = [40.8, 37.6, 44.9, 25.0, 44.7]

##################################
#Declare a global variable named byline. 
#make it a multiline f-string to show our infotmation. 
##################################

byline: str = f"""
-------------------------------------------------------------
Mahitha Analytics: Delivering Professional Insights
-------------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Provately Held:  {is_provately_held}
Years in Operation:  {years_in_operation}
Number of Months:  {number_of_months}
Skills Offered:  {skills_offered}
Courses Offered:  {courses_offered}
Client Satisfaction Scores:  {client_satisfaction_scores}
Temperature Values:  {temperature_values}
"""
###################################
#Define the get_byline() fucntion
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
