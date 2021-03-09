import os
from netmiko import ConnectHandler
from getpass import getpass
import logging


logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = (
    os.getenv("NETMIKO_PASSWORD")
    if os.getenv("NETMIKO_PASSWORD")
    else getpass()
)

devices = {
    "arista1": {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
    "arista2": {
        "device_type": "arista_eos",
        "host": "arista2.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
    "arista3": {
        "device_type": "arista_eos",
        "host": "arista3.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
    "arista4": {
        "device_type": "arista_eos",
        "host": "arista4.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
}

for key in devices.keys():
    net_connect = ConnectHandler(**devices[key])
    output = net_connect.send_command("show ip arp")
    print(output)
    net_connect.disconnect()
