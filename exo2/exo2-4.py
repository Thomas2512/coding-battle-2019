hhmm = str(input())
M = int(input())
H = int(input())

hh =int(hhmm.split(":")[0])
mm =int(hhmm.split(":")[1])

inter = (hh*H + mm)/M
HH =int((inter//60)%24)
#HH = int(np.mod(inter//60, 24))
MM =int(inter %60)
if MM<10&MM>0: MM='0'+str(MM)

print(str(HH)+":"+str(MM))