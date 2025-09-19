
"""
task details:
In this project, you need to write a function to calculate the power output by implementing the model defined in the last section. Your function need to fullfil the following requirements:

Have a meaningful and proper name.
Takes the following inputs (each with proper variable name):
wind speed (we assume it will be a float number),
rated power, with a default value: 15,
cut-in wind speed, with a default value: 3,
rated wind speed, with a default value: 11,
cut-out wind speed, with a default value: 25,
interpolation option, a string to define the interpolation method, can only be "linear" or "cubic", with a default value: "linear".
Returns the computed power output using the model and the inputs.
Have proper docstring and several (at least 3) comments to explain the function.
Include error handling by raising proper error when the user gives an invalid input for the string defining the interpolation option.
You should also write the main script to run your function for at least one example. These can be done in one script that looks like the following:
"""
#Creating the function

def power_output(wind_speed, rated_power, cut_in, rated_wind_speed, cut_out, int_option):
    """
    Docstring here.
    """
    # Add comment if needed.
    if wind_speed < cut_in or wind_speed > cut_out:
        power = 0
    elif wind_speed >= rated_wind_speed and wind_speed <= cut_out:
        power = rated_power
    else:
        if int_option == 'linear':
            power = rated_power*((wind_speed - cut_in) / (rated_wind_speed - cut_in))
        
     
 # Add comment if needed.

    return power

if __name__ == '__main__':
    # Write the main script to use the function here:
    wind_speed =float(input('what is the wind speed?'))
    rated_power = 15
    cut_in = 3
    rated_wind_speed = 11
    cut_out = 25
    int_option = 'linear'




    # Add comments to explain if needed.
    power = power_output(wind_speed,rated_power, cut_in, rated_wind_speed, cut_out, int_option)
    print(f'power = {power}')  # Add comment when needed






