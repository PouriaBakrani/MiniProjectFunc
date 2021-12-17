def in_hour_checker(data, in_hour: int = -1) -> int:
    """
    This function get the entered `hour` to the gate from user
    and will check it if its between 0 to 24
    :param in_hour, data: entered `hour` to the gate
    :return: `hour` if its between 0 to 24
    """
    while in_hour not in range(24):
        in_hour = int(input("Hour vehicle entered lot (0 – 24)? "))
    data['Hour in'] = in_hour
    return in_hour


def in_minute_checker(data, in_minute: int = -1) -> int:
    """
    This function get the entered `minute` to the gate from user
    and will check it if its between 0 to 60
    :param in_minute, data: entered `minute` to the gate
    :return: `minute` if its between 0 to 60
    """
    while in_minute not in range(60):
        in_minute = int(input("Minute vehicle entered lot (0 – 60)? "))
    data['Minute in'] = in_minute
    return in_minute

def out_hour_checker(data, out_hour: int = -1) -> int:
    """
    This function get the left `hour` to the gate from user
    and will check it if its between 0 to 24
    :param out_hour: left `hour` to the gate
    :return: `hour` if its between 0 to 24
    """
    while out_hour not in range(24):
        out_hour = int(input("Hour vehicle left lot (0 – 24)? "))
    data['Hour out'] = out_hour
    return out_hour


def out_minute_checker(data, out_minute: int = -1) -> int:
    """
    This function get the left `minute` to the gate from user
    and will check it if its between 0 to 60
    :param out_minute, data: left `minute` to the gate
    :return: `minute` if its between 0 to 60
    """
    while out_minute not in range(60):
        out_minute = int(input("Minute vehicle left lot (0 – 60)? "))
    data['Minute out'] = out_minute
    return out_minute


def hour_checker(out_hour, in_hour):
    while True:
        if out_hour < in_hour:
            print("left hour cannot be less than entered hour")
            out_hour = out_hour_checker()
        else:
            break
    return out_hour


def minute_checker(out_minute, in_minute):
    while True:
        if out_minute < in_minute:
            total_min = (60 - in_minute) + out_minute
            break
        else:
            total_min = out_minute - in_minute
    return total_min


def less_than_1hour_checker(in_minute, out_minute, out_hour, in_hour):
    if in_minute > out_minute:
        parking_hour = out_hour - in_hour - 1
    else:
        parking_hour = out_hour - in_hour
    return parking_hour


def hours_mins_seperator(out_minute, in_minute, total_hours_mins):
    if out_minute - in_minute > 0:
        total_hours = total_hours_mins[0] + 1
    else:
        total_hours = total_hours_mins[0]
    if total_hours_mins[0] == 1 and out_minute < in_minute:
        total_hours = 0
    return total_hours


def hours_rounder(total_hours_mins, out_minute, in_minute, total_hours):
    if total_hours_mins[0] == 0 and out_minute > in_minute:
        rounded_hours = total_hours + 1
    elif total_hours_mins[0] == 1 and out_minute > in_minute:
        rounded_hours = total_hours + 1
    else:
        rounded_hours = total_hours
    return rounded_hours


def car_getter(data, user_car):
    while user_car.lower() not in ("bus", "truck", "car"):
        user_car = input("what is the type of your car: (car/bus/truck) ")
    data['user car'] = user_car


def payment_calculator(user_car, total_hours):
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
    return payment


def receipt_printer(data, parking_hour, total_min, rounded_hours,
                    payment):
    print("Parking lot charges")
    print(f"type of the car : {data.get('user car')}")
    print(f"time in: {str(data.get('Hour in')).zfill(2)}:{str(data.get('Minute in')).zfill(2)}")
    print(f"time out: {str(data.get('Hour out')).zfill(2)}:{str(data.get('Minute out')).zfill(2)}")
    print(f"parking time: {parking_hour}:{str(total_min).zfill(2)}")
    print(f"rounded total : {str(rounded_hours).zfill(2)} hours")
    print(f"total charges: ${payment:.2f}")