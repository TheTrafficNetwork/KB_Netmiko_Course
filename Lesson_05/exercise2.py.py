import os
from getpass import getpass
import yaml
from netmiko import ConnectHandler
import time


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


if __name__ == "__main__":

    # Code so automated tests will run properly
    # Check for environment variable, if that fails, use getpass().
    password = (
        os.getenv("NETMIKO_PASSWORD")
        if os.getenv("NETMIKO_PASSWORD")
        else getpass()
    )

    device_dict = load_devices()

    nxos1 = device_dict["nxos1"]
    nxos2 = device_dict["nxos2"]

    for device in (
        nxos1,
        nxos2,
    ):
        device["password"] = password
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_from_file("exercise2.txt")
        output += net_connect.save_config()
        time.sleep(10)
        print(f"\n{output}\n\n")
        net_connect.disconnect()
