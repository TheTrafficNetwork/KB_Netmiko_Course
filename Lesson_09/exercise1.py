from getpass import getpass
import yaml
from netmiko import ConnectHandler, file_transfer, progress_bar


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
    cmd = f"copy {file_system}/{dest_file} system:running-config"

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
            # progress4=progress_bar,
        )

        file_exists = transfer_dict["file_exists"]
        md5_verify = transfer_dict["file_verified"]

        if file_exists and md5_verify:
            output = ssh_conn.send_command_timing(
                cmd,
                strip_prompt=False,
                strip_command=False,
            )
            if "Destination filename" in output:
                output += ssh_conn.send_command(
                    "\n",
                    strip_prompt=False,
                    strip_command=False,
                )
        print(transfer_dict)
        print("\n")
        print(output)
        name_check = ssh_conn.send_command("show run | i name-server").strip()
        ns_len = len(name_check.split()) == 4
        ns_88 = "8.8.8.8" in name_check
        ns_84 = "8.8.4.4" in name_check
        if ns_len and ns_88 and ns_84:
            print("\nThe name servers are configured properly.\n")
        else:
            print(f"\nThe name servers are misconfigured.\n{name_check}\n")
        domain_check = ssh_conn.send_command("show run | i ip domain name")
        if "lasthop.io" in domain_check:
            print("\nDomain name is configured properly\n")
        else:
            print(f"\nDomain is misconfigured.\n{domain_check}")

        ssh_conn.disconnect()
