from netmiko import ConnectHandler
from getpass import getpass

my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}
net_connect = ConnectHandler(**my_device)
print(net_connect.find_prompt())
net_connect.disconnect()
