from netmiko import ConnectHandler
from getpass import getpass

my_device = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "session_log": "Lesson_01/nxos1.out",
}
with ConnectHandler(**my_device) as net_connect:
    print(net_connect.find_prompt())
