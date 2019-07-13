

def caltime(h,a):
    return str((((h/360)*a%24)))

def calangle(h,a):
    x = caltime(h,a)
    #print(x)
    h,m = x.split(".")
    h = int(h)
    m = int(m)

    if h == 12:
        h = 0
    if m == 60:
        m = 0

    min = int((str(int(m) * 6))[:2])
    #print(h,min)

    angle_hour = 0.5 * (60 * int(h)+ int(min))
    angle_min = 6 * int(min)
    angle = abs(angle_hour - angle_min)
    angle2 = abs( 360 - angle)
    if (angle<=180):
        print('{:.2f}'.format(angle),end="")
    else:
        print('{:.2f}'.format(angle2),end="")

hrs = int(input())
degree = float(input())
calangle(hrs,degree)