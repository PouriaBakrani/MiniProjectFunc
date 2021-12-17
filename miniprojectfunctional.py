from funcs import *
user_data = {'user car': None, 'Hour in': None, 'Hour out': None, 'Minute in': None, 'Minute out': None}
user_car = input("what is the type of your car: (car/bus/truck) or 0 to Exit ")
while user_car != "0":
    #  Getting car module from user
    car_getter(user_data, user_car)

    # Getting the entrance and exit time
    in_hour = in_hour_checker(user_data)
    in_minute = in_minute_checker(user_data)
    out_hour = out_hour_checker(user_data)
    out_minute = out_minute_checker(user_data)

    while out_hour == in_hour and in_minute > out_minute:
        out_minute = out_minute_checker(user_data)

    # Calculating the whole hours , if the user stay even 1 more minute then it will add an hour
    out_hour = hour_checker(out_hour, in_hour)
    total_min = minute_checker(out_minute, in_minute)
    total_hours_mins = (out_hour - in_hour, total_min)
    parking_hour = less_than_1hour_checker(in_minute, out_minute, out_hour, in_hour)
    total_hours = hours_mins_seperator(out_hour, in_hour, total_hours_mins)
    rounded_hours = hours_rounder(total_hours_mins, out_minute, in_minute, total_hours)

    # Calculating the pay fee for each car, truck, bus
    payment = payment_calculator(user_car, total_hours)

    # Printing receipt
    receipt_printer(user_data, parking_hour, total_min, rounded_hours, payment)

    user_car = input("what is the type of your car: (car/bus/truck) or 0 to Exit ")