local = string(input())
M = int(input())
H = int(input())

hh = int(local[:2])
mm = int(local[3:])

terr_min = (hh * H + mm) // M

hour = (terr_min//60) % 24
minutes = terr_min - (60 * terr_min//60)
result = "{:.0f}:{:.0f}".format(hour, minutes)

print (result)