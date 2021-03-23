import yaml
from concurrent.futures import ProcessPoolExecutor, wait
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler


def load_devices(device_file="lab_devices.yml"):
    device_dict = {}
    with open(device_file) as f:
        device_dict = yaml.safe_load(f)
    return device_dict


def ssh_conn(device_name, device_dict, cmd=None):
    with ConnectHandler(**device_dict) as net_connect:
        if cmd is None:
            return net_connect.find_prompt()
        else:
            output = net_connect.send_command(cmd)
            return (device_name, output)


if __name__ == "__main__":
    password = getpass()

    my_devices = load_devices()
    arista_list = my_devices["arista"]
    cisco_list = my_devices["cisco"]
    nxos_list = my_devices["nxos"]
    juniper_list = my_devices["juniper"]
    device_list = juniper_list + arista_list + cisco_list + nxos_list

    # Kirk's command list as a dict
    # cmd_dict = {"cisco_nxos": "show ip arp vrf management", "juniper_junos": "show arp"}

    max_threads = 20

    pool = ProcessPoolExecutor(max_threads)

    future_list = []
    for device_name in device_list:
        device_dict = my_devices[device_name]
        device_dict["password"] = password
        # Kirk's application of the command
        # platform = device_dict["device_type"]
        # Get command from dict, default to show ip arp if not in dict
        # cmd = cmd_dict.get(platform, "show ip arp")
        if device_name in arista_list:
            arp_cmd = "show ip arp"
        if device_name in cisco_list:
            arp_cmd = "show ip arp"
        if device_name in nxos_list:
            arp_cmd = "show ip arp vrf management"
        if device_name in juniper_list:
            arp_cmd = "show arp"
        future = pool.submit(
            ssh_conn,
            device_name=device_name,
            device_dict=device_dict,
            cmd=arp_cmd,
        )
        future_list.append(future)

    wait(future_list)

    for future in future_list:
        result = future.result()
        device_name, output = result
        print("-" * 20)
        print(f"{device_name}:\n\n{output}")
        print("-" * 20)
        print()