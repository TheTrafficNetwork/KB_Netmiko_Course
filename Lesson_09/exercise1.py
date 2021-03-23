from getpass import getpass
from os import putenv

import yaml
from netmiko import ConnectHandler, file_transfer


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


source_file = "exercise1.txt"
dest_file = "exercise1.txt"
direction = "put"
file_system = "flash:"

if __name__ == "__main__":
    password = getpass()

    my_devices = load_devices()
    device_list = my_devices["cisco"]
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        ssh_conn = ConnectHandler(**device_dict)
        transfer_dict = file_transfer(
            ssh_conn,
            source_file=source_file,
            dest_file=dest_file,
            file_system=file_system,
            direction=direction,
            overwrite_file=True,
            inline_transfer=True,
        )
        output = ssh_conn.send_command_timing(
            "copy flash:/exercise1.txt system:running-config",
            strip_prompt=False,
            strip_command=False,
        )
        ssh_conn.disconnect()
        print(transfer_dict)
        print(output)
