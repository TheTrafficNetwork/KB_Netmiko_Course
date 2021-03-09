import os
from netmiko import ConnectHandler
from getpass import getpass

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = (
    os.getenv("NETMIKO_PASSWORD")
    if os.getenv("NETMIKO_PASSWORD")
    else getpass()
)

devices = {
    "cisco3": {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
    "nxos1": {
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
    "arista1": {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": password,
    },
}

for key in devices.keys():
    net_connect = ConnectHandler(**devices[key])
    print(net_connect.find_prompt())
    net_connect.disconnect()
