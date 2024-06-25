#An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3 , 4 or 5. In case of invalid job level, 
#consider hike percentage to be 0. Given the current salary and job level, write a Python program to find and display the new salary of an employee. 
#Hike percentage based on job levels are given below

Job level     Hike Percentage (applicable on current salary)

3                        15

4                         7

5                         5


def calculate_new_salary(current_salary, job_level):
    # Define the hike percentages for each job level
    hike_percentages = {
        3: 15,
        4: 7,
        5: 5
    }
    
    # Get the hike percentage based on the job level, default to 0 if invalid
    hike_percentage = hike_percentages.get(job_level, 0)
    
    # Calculate the new salary
    new_salary = current_salary + (current_salary * hike_percentage / 100)
    
    return new_salary

# Take inputs from the user
current_salary = float(input("Enter the current salary: "))
job_level = int(input("Enter the job level: "))

# Calculate the new salary
new_salary = calculate_new_salary(current_salary, job_level)

# Display the new salary
print(f"The new salary after applying the hike is: {new_salary:.2f}")
