#tire_volume.py
from datetime import datetime
import math
print('This program calculte the tire volume')
print()
form_1 = 0
volume_1 = None

w=float(input('Please Enter the width of the tire in mm: '))
a =float(input('Please Enter the aspect ratio of the tire: '))
d =float(input('Enter the diameter of the wheel in inches : '))
w1 =int(w)
a1 =int(a)
d1 =int(d)



volume_1 = math.pi*(w**2)*a*(w*a+2540*d)/10000000000

print('the volume is: {:,.2f}'.format(volume_1))
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")
with open("tire_volume.txt",'a')as volume_file:
    print(file = volume_file)
    print(f"{current_date_and_time:%Y-%m-%d}, {w1}, {a1}, {d1}, {volume_1:,.2f}", file = volume_file)
