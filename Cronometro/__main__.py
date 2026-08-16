from time import sleep

h = int(input('Cronometrar quanto tempo(h): ')) 
m = int(input('Cronometrar quanto tempo(m): ')) 
s = int(input('Cronometrar quanto tempo(s): '))

temp = (h * 3600) + (m * 60) + s

print(f'CRONOMETRAR: {h}:{m}:{s}')

while temp != -1:
    print(f'{h}:{m}:{s}')
    temp -= 1
    s -= 1
    sleep(0.1)
    if s <= 0:
        if m > 0:
            m -= 1
            s = 60
    if m <= 0:
        if h > 0:
            h -= 1
            m = 60