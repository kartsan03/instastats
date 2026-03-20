import shutil
import psutil

def printer_banner():
    banner = r"""    
   (_)___  _____/ /_____ ______/ /_____ _/ /______
  / / __ \/ ___/ __/ __ `/ ___/ __/ __ `/ __/ ___/
 / / / / (__  ) /_/ /_/ (__  ) /_/ /_/ / /_(__  ) 
/_/_/ /_/____/\__/\__,_/____/\__/\__,_/\__/____/                                                   
"""
    print(banner)

printer_banner()
print("Welcome in instastats")
print("You can easily monitor your system with this tool")


all_disks = psutil.disk_partitions()
total, used, free = shutil.disk_usage('/')
list_of_system_disks = []

for disk in all_disks:
    list_of_system_disks.append(disk.device)

print("Please choose the disk you want to see information about:")
print("|| 0 General Information about your system")

for i, device in enumerate(list_of_system_disks, start=1):
    print(f"|| {i}  {device}")

# total, used, free = shutil.disk_usage('/')
# print(f'Total: {total / (2**30)} GiB')
# print(f'Used: {used / (2**30)} GiB')
# print(f'Free: {free / (2**30)} GiB')