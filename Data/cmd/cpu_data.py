import psutil
from Data.Speak_All.speak_print_only import speak

cpu0 = psutil.cpu_count()
cpu1 = psutil.cpu_percent()
cpu2 = psutil.cpu_times()

print(cpu0)
print(cpu1)
print(cpu2)
