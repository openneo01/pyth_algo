
input_cust = 5
input_time = "18:23:00"
input_range_time = ("12:23:00 21:28:00;18:13:00 22:48:00;23:41:00 23:52:00;11:46:00 20:58:00;14:57:00 17:57:00")

def itime(stime):
    (h,m,s) = stime.split(':') 
    return int(h) * 3600 + int(m) * 60 + int(s)
    
otime = itime(input_time)

cust = 0
for rng_time in input_range_time.split(';'):
    if itime(rng_time.split(' ')[0]) < otime < itime(rng_time.split(' ')[1]):
        cust +=1
    
print(cust)
