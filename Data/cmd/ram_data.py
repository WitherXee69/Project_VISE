import psutil


ram0 = psutil.virtual_memory()[0]
ram1 = psutil.virtual_memory()[1]
rampersent = psutil.virtual_memory()[2]
ram3 = psutil.virtual_memory()[3]
ram4 = psutil.virtual_memory()[4]

gb = 1024 * 1024 * 1024
mb = 1024 * 1024

ramtotal = ram0/(1024 * 1024 * 1024)
ramavalx = ram1/(1024 * 1024 * 1024)
ramuse = ram3/(1024 * 1024 * 1024)
ramfree = ram4/(1024 * 1024)
