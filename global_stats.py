import shutil

def show_global_stats(disks):
    if type(disks) == list :
        total_system_data = {"Total space":0, "Used space":0, "Free space":0}
        for disk in disks :
            total, used, free = shutil.disk_usage(disk)
            total_system_data["Total space"] += total
            total_system_data["Used space"] += used
            total_system_data["Free space"] += free

        for spec in total_system_data :
            print(f"{spec} : {((total_system_data[spec])/ 1024**3)} GB")
    else:
        total, used, free = shutil.disk_usage(disks)
        total_disk_data = {"Total space":total, "Used space": used, "Free space": free}
        for spec in total_disk_data :
            print(f"{spec} : {((total_disk_data[spec])/ 1024**3)} GB")