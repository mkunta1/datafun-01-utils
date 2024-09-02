''' ITERATION 4

Module: Mahitha Analytics - Reusable Module for My Data Analytics Projects


This module provides a simple, reusable foundation for my analytics projects.

Process:
In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offers methods to calculate mean and standard deviation.

'''
#####################################
# Import modules at the top.
#####################################

# In Python, we can import modules to add extra tools and functions.
# Below, we're importing:
# - `statistics`:  This gives us tools to calculate things like averages.
# Use CTRL F and type statistics to see where it is used in the code.
# Did you find statistics.mean()?
# Did you find statistics.stdev()?

import statistics


#####################################
# Declare global variables
#####################################

# Boolean variables to indicate if the company has international clients and is privately owned.

has_international_clients: bool = True
is_provately_held: bool = True

#Interger variable for the number of years in operation 
years_in_operation: int = 10
number_of_months:   int = 12


#Float variable for the average client satisfaction score 
average_client_satisfaction: float = 4.7 

#List of strings representing the skills pffered by the company 
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
courses_offered: list = ["math", "science", "english"]

#List of floats representing individual client satisfaction scores 
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
temperature_values: list = [40.8, 37.6, 44.9, 25.0, 44.7]


#####################################
# Calculate Statistics
#####################################

# Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev().
min_score:  float = min(client_satisfaction_scores)
max_score:  float = max(client_satisfaction_scores)
mean_score:  float = statistics.mean(client_satisfaction_scores)
stdev_score:  float = statistics.stdev(client_satisfaction_scores)
min_temp:  float = min(temperature_values)
max_temp:  float = max(temperature_values)
mean_temp:  float = statistics.mean(temperature_values)
stdev_temp:  float = statistics.stdev(temperature_values)

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
-------------------------------------------------------------
Mahitha Analytics : Delivering Professional Insights
-------------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Privately held:  {is_provately_held}
Years in Operation:  {years_in_operation}
Number of Months:  {number_of_months}
Skills Offered:  {skills_offered}
Courses Offered:  {courses_offered}
Temperature values (F):  {temperature_values}
Client Satisfaction Scores:  {client_satisfaction_scores}
Minimum Client Satisfacton Score:  {min_score}
Maximum Client Satisfaction Score:  {max_score}
Average Client Satisfaction Score:  {mean_score}
Standard Deviation of Client Satisfaction Scores:  {stdev_score}
Minimum Temperature (F):  {min_temp}
Maximum Temperature (F):  {max_temp}
Mean Temperature (F):  {mean_temp}
Standard Deviation of Temperature (F):  {stdev_temp}
"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main() function now calls the get_byline function to retrieve the byline.

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
