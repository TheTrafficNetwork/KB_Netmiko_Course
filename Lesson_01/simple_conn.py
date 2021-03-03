from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="cisco.lasthop.io",
    username="pytclass",
    password=getpass(),
)
print(net_connect.find_prompt())