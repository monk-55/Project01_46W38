
"""
This function calculates the power output of a wind turbine based on a given wind speed and the following default parameters:

rated power, with a default value: 15,
cut-in wind speed, with a default value: 3,
rated wind speed, with a default value: 11,
cut-out wind speed, with a default value: 25

Also an interpolation option is required in the inputs, a string to define the interpolation method, This can only be "linear" or "cubic"and has
a default value: "linear".

You should also write the main script to run your function for at least one example. These can be done in one script that looks like the following:
"""

#Function definition including default values for everything except wind_speed. Note int_option is a string

def power_output(wind_speed, rated_power = 15, cut_in = 3, rated_wind_speed = 11, cut_out = 25, int_option = 'linear'):
    """
    The following code will first check if the wind speed is below cut in or above cut out, in which case power will be zero.
    Secondly it will check if wind speed is at rated and also below cut out, in which case power will be equal to rated
    If neither of those conditions are satisfied it will calculate the power based on the interpolation option specified
    """
    # checking if below cut in or above cut out.
    if wind_speed < cut_in or wind_speed > cut_out:
        power = 0
        return power
        #checking if rated or above and below cut in
    elif wind_speed >= rated_wind_speed and wind_speed <= cut_out:
        power = rated_power
        return power
        #if neither of the above the power to be calculated, different methods dependent on int_option specified, try except is included to catch
        #inputs that are neither linear or cubic
    else:

        if int_option == 'linear':
            power = rated_power*((wind_speed - cut_in) / (rated_wind_speed - cut_in))
            return power
        elif int_option == 'cubic':
            power = rated_power*((wind_speed**3)/(rated_wind_speed**3))
            return power
        else: 
            raise ValueError(f"{int_option} is not a valid option, please specify linear or cubic")



if __name__ == '__main__':
    # Example using the function above with a wind speed of 8.4 m/s and all other inputs left as default
    power = power_output(wind_speed = 8.4)
    print(f'First example: power = {power}') 

    # Example uses the same wind speed but cubic interpolation
    power = power_output(wind_speed = 8.4, int_option='cubic')
    print(f'Second example: power = {power}')  # Add comment when needed
    
    # Example uses a wind speed of 23
    power = power_output(wind_speed = 23)
    print(f'Third example: power = {power}')  # Add comment when needed






