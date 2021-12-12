from funcs import *
user_car = input("what is the type of your car: (car/bus/truck) or 0 to Exit ")
while user_car != "0":
    #  Getting car module from user
    while user_car.lower() not in ("bus", "truck", "car"):
        user_car = input("what is the type of your car: (car/bus/truck) ")

    # Getting the entrance and exit time
    in_hour = in_hour_checker()
    in_minute = in_minute_checker()
    out_hour = out_hour_checker()
    out_minute = out_minute_checker()

    # Calculating the whole hours , if the user stay even 1 more minute then it will add an hour
    while True:
        if out_hour < in_hour:
            print("left hour cannot be less than entered hour")
            out_hour = out_hour_checker()
        else:
            break
    while True:
        if out_minute < in_minute:
            total_mins = (60 - in_minute) + out_minute
            break
        else:
            total_mins = out_minute - in_minute
            break

    total_hours_mins = (out_hour - in_hour, total_mins)
    if in_minute > out_minute:
        parking_hour = out_hour - in_hour - 1
    else:
        parking_hour = out_hour - in_hour
    if out_minute - in_minute > 0:
        total_hours = total_hours_mins[0] + 1
    else:
        total_hours = total_hours_mins[0]
    if total_hours_mins[0] == 1 and out_minute < in_minute:
        total_hours = 0

    if total_hours_mins[0] == 1 and out_minute < in_minute:
        rounded_hours = total_hours + 1
    else:
        rounded_hours = total_hours
    # Calculating the pay fee for each car, truck, bus
    if user_car == "car":
        if total_hours > 3:
            payment = (total_hours - 3) * 1.5
        else:
            payment = 0

    elif user_car == "bus":
        if total_hours > 1:
            payment = (total_hours - 1) * 3.70 + 2
        elif total_hours == 1:
            payment = 2
        else:
            payment = total_hours * 2

    elif user_car == "truck":
        if total_hours > 2:
            payment = (total_hours - 2) * 2.30 + 2
        elif total_hours == 2:
            payment = 2
        else:
            payment = total_hours

    print("Parking lot charges")
    print(f"type of the car : {user_car}")
    print(f"time in: {in_hour}:{in_minute}")
    print(f"time out: {out_hour}:{out_minute}")
    print(f"parking time: {parking_hour}:{total_mins}")
    print(f"rounded total : {rounded_hours} hours")
    print(f"total charges: ")
    if user_car == "car":
        print(f"${payment:.2f}")
    elif user_car == "bus":
        print(f"${payment:.2f}")
    elif user_car == "truck":
        print(f"${payment:.2f}")

    user_car = input("what is the type of your car: (car/bus/truck) or 0 to Exit ")