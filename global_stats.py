import shutil


def show_global_stats(disks):
    total_system_data = {"total_space":0, "used_space":0, "free_space":0}
    for disk in disks :
        total, used, free = shutil.disk_usage(disk)
        total_system_data["total_space"] += total
        total_system_data["used_space"] += used
        total_system_data["free_space"] += free

    for spec in total_system_data :
        print(f"{spec} : {((total_system_data[spec])/ 1024**3)} GB")