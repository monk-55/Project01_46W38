
"""
This function calculates the power output of a wind turbine based on a given wind speed (wind_speed) and the following default parameters:

rated power (rated_power), with a default value: 15,
cut-in wind speed (cut_in), with a default value: 3,
rated wind speed (rated_wind_speed), with a default value: 11,
cut-out wind speed (cut_out), with a default value: 25
Also an interpolation option is required in the inputs(int_option), a string to define the interpolation method, This can only be "linear" or "cubic"and has
a default value: "linear".

If the user wants to leave all defaults as they are then only the wind_speed needs to be specified, otherwise please specify the values required for
any of the other inputs. As above when specifying int_option only enter 'linear' or 'cubic'.

The code below includes use of the function for 3 examples.
"""

#Function definition including default values for everything except wind_speed. Note int_option is a string

def calculate_power_output(wind_speed, rated_power = 15, cut_in = 3, rated_wind_speed = 11, cut_out = 25, int_option = 'linear'):
    """
    The following code will first check if the wind speed is below cut in or above cut out, in which case power will be zero.
    Secondly it will check if wind speed is at rated and also below cut out, in which case power will be equal to rated
    If neither of those conditions are satisfied it will calculate the power based on the interpolation option specified
    """
    # checking if below cut in or above cut out.
    if wind_speed < cut_in or wind_speed >= cut_out:
        power = 0
        #checking if rated or above and below cut in
    elif wind_speed >= rated_wind_speed and wind_speed < cut_out:
        power = rated_power
        #if neither of the above the power to be calculated, different methods dependent on int_option specified, try except is included to catch
        #inputs that are neither linear or cubic
    else:

        if int_option == 'linear':
            power = rated_power*((wind_speed - cut_in) / (rated_wind_speed - cut_in))
        elif int_option == 'cubic':
            power = rated_power*((wind_speed**3)/(rated_wind_speed**3))
        else: 
            raise ValueError(f"{int_option} is not a valid option, please specify linear or cubic")
        
    return power



if __name__ == '__main__':
    # Example using the function above with a wind speed of 8.4 m/s and all other inputs left as default
    power = calculate_power_output(wind_speed = 8.4)
    print(f'First example: power = {power}') 

    # Example uses the same wind speed but cubic interpolation
    power = calculate_power_output(wind_speed = 8.4, int_option='cubic')
    print(f'Second example: power = {power}')  

    # Example uses a wind speed of 23
    power = calculate_power_output(wind_speed = 23)
    print(f'Third example: power = {power}')  






