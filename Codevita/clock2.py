import datetime

def caltime(h,a):
    time = ((h/360)*a) % 24
    result = str(datetime.timedelta(hours=time))
    hours = result.split(":")[0]
    minutes = result.split(":")[1]
    return hours, minutes

def calangle(h,a):

    h,m = caltime(h, a)
    h = int(h)
    m = int(m)

    min = m

    angle_hour = 0.5 * (60 * int(h)+ int(min))
    angle_min = 6 * int(min)
    angle = abs(angle_hour - angle_min)
    angle2 = abs( 360 - angle)
    if (angle<=180):
        print('{:.2f}'.format(angle), end='')
    else:
        print('{:.2f}'.format(angle2), end='')

hrs = int(input())
degree = float(input())

calangle(hrs,degree)