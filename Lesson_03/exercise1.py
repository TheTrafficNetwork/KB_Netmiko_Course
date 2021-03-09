import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Code so automated tests will run properly
# Check for environment variable, if that fails, use getpass().
password = (
    os.getenv("NETMIKO_PASSWORD")
    if os.getenv("NETMIKO_PASSWORD")
    else getpass()
)

my_device = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**my_device)
output = net_connect.send_command("show vlan", use_textfsm=True)
pprint(output)
net_connect.disconnect()

for vlan in output:
    if vlan["vlan_id"] == "7":
        print(f"Vlan 7's name is {vlan['name']}.")
