import socket  # module used for network communication


def scan_ports():
    """
    This function performs port scanning on a target system.

    It:
    - Takes target IP/domain from user
    - Takes port range
    - Checks which ports are open
    """

    # -------------------------------
    # Step 1: Take user input
    # -------------------------------
    
    # ask user for target (IP or domain)
    target = input("Target: ")

    # ask user for starting port and convert to integer
    start_port = int(input("Start port: "))

    # ask user for ending port and convert to integer
    end_port = int(input("End port: "))

    # -------------------------------
    # Step 2: Start scanning
    # -------------------------------
    
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

            # if result is 0 → port is OPEN
            if result == 0:
                print(f"[OPEN] Port {port}")

            # close the socket after checking
            s.close()

        except:
            # if any error happens (invalid input, network issue)
            print(f"[ERROR] Port {port}")

    # -------------------------------
    # Step 3: Scan complete
    # -------------------------------
    
    print("\nScan Complete.\n")
