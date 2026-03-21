"""
Port Scanner (Learning Version)

This program checks which ports are OPEN on a target system.
It tries to connect to each port in a given range.

If connection works → OPEN
If not → CLOSED
"""

import socket  # import module used for network communication


def scan_ports(target, start_port, end_port):
    # print what we are scanning
    print(f"\nScanning {target}...\n")

    # loop through ports from start to end
    for port in range(start_port, end_port + 1):
        try:
            # create a socket object (used to connect to another system)
            s = socket.socket()

            # set timeout so program doesn't wait too long
            s.settimeout(0.5)

            # try connecting to the target at this port
            # returns 0 if connection is successful
            result = s.connect_ex((target, port))

            # if result is 0 → connection successful → port is OPEN
            if result == 0:
                print(f"[OPEN] Port {port}")

            # close the socket after checking
            s.close()

        except:
            # if any error happens (invalid input, network issue)
            print(f"[ERROR] Port {port}")


def main():
    # ask user for target (IP or domain)
    target = input("Target: ")

    # ask user for starting port and convert to integer
    start_port = int(input("Start port: "))

    # ask user for ending port and convert to integer
    end_port = int(input("End port: "))

    # call the scanning function with user inputs
    scan_ports(target, start_port, end_port)


# this ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()