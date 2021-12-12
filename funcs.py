def in_hour_checker(in_hour=-1):
    while in_hour not in range(24):
        in_hour = int(input("Hour vehicle entered lot (0 – 24)? "))
    return in_hour


def in_minute_checker(in_minute=-1):
    while in_minute not in range(60):
        in_minute = int(input("Minute vehicle entered lot (0 – 60)? "))
    return in_minute


def out_hour_checker(out_hour=-1):
    while out_hour not in range(24):
        out_hour = int(input("Hour vehicle left lot (0 – 24)? "))
    return out_hour


def out_minute_checker(out_minute=-1):
    while out_minute not in range(60):
        out_minute = int(input("Minute vehicle left lot (0 – 60)? "))
    return out_minute