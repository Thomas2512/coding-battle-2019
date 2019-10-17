
local = string(input())
M = int(input())
H = int(input())

hh = int(local[:2])
mm = int(local[3:])

terr_min = (hh * H + mm) // M

hour = (terr_min//60) % 24
min = terr_min-(terr_min//60 * 60)
result = "{:.0f}:{:.0f}".format(hour, min)

print (result)