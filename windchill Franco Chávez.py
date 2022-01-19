#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#Where,T= Air Temperature (ºF) V= Wind Speed (mph)


def wind_chill(t,v) :
    return 35.74 + 0.6215*float(t) - 35.75*(float(v)**0.16) + 0.4275*float(t)*(float(v)**0.16)

def farenheit_to_celsius(t,v):
    return 35.74 + 0.6215*(float(t)*9/5+32) - 35.75*(float(v)**0.16) + 0.4275*(float(t)*9/5+32)*(float(v)**0.16)
    
    
v = None
t = input('Please enter temperature value: ')
print()
choose = input('Farenheit or Celsius?  (f/c): ')
print()
print('-------------------------------------------------------------------------')

if choose == 'f':

    for v in range (5,65,5) :
        chill = wind_chill(t,v)   
        print(f'At temperature {t:3} °F, and wind speed {v:3} mph, the windchill is:{chill:6.2f} °F')
    t == None
elif choose == 'c':
    for v in range (5,65,5) :
        celsius_chill =  farenheit_to_celsius(t,v) 
        print(f'At temperature {t:3} °F, and wind speed {v:3} mph, the windchill is:{celsius_chill:6.2f} °F')
else:
    print('Choose a valid option')
print('-------------------------------------------------------------------------')


