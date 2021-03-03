from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()
time.sleep(4)

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    session_log="Lesson_01/cisco3.out",
)
print(net_connect.find_prompt())
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect
