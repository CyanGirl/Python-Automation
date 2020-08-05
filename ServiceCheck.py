import paramiko
import re


def commandExec(hostname, port, username, password, command):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=hostname, port=port,
                       username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode()
        # print(output)

        pattern = r"running"
        match = re.search(pattern, output)

        if match:
            print("\nThe service is running!")
        else:
            print("\nWhoops! The service is not running.")

    except:
        print("Could not connect to the Server!")
        
