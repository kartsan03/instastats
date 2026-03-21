import psutil, sys
from global_stats import show_global_stats 

def printer_banner():
    banner = r"""    
   (_)___  _____/ /_____ ______/ /_____ _/ /______
  / / __ \/ ___/ __/ __ `/ ___/ __/ __ `/ __/ ___/
 / / / / (__  ) /_/ /_/ (__  ) /_/ /_/ / /_(__  ) 
/_/_/ /_/____/\__/\__,_/____/\__/\__,_/\__/____/                                                   
"""
    print(banner)

printer_banner()
print("Welcome to instastats")
print("You can easily monitor your system with this tool")

all_disks = psutil.disk_partitions()
list_of_system_disks = []
for disk in all_disks:
    list_of_system_disks.append(disk.device)

print("Please choose the disk you want to see information about:")
print("|| 0  General information about your system")

for i, device in enumerate(list_of_system_disks, start=1):
    print(f"|| {i}  {device}")

try:
    user_choice = int(input("Enter your choice: "))
    
except ValueError:
    print("Invalid input. Please enter a number. Exiting program.")
    sys.exit()

if 0 <= user_choice <= (len(list_of_system_disks)) :
        if user_choice == 0:
            show_global_stats(list_of_system_disks)
        if user_choice > 0:
            disk_index = user_choice - 1
            show_global_stats(list_of_system_disks[disk_index])
else:
        print("Please enter number from list above. Exiting program.")