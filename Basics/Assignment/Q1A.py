# Validate a given public IP address to check if it follows the correct format (IPv4).
    # We also need to make sure that the ip we get is a public IP (should be of the correct range (public ip range) and it should also be a valid address (not 257))
    # Do with and without regex without using modules

# Soltution:
import re
def ip_check(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(regex, ip):
        print("IP address is valid")
    else:
        print("IP address is not valid")

ip = "10.0.1.0"
ip_check(ip)