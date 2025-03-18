import logging
from datetime import datetime

# Set up logging at the beginning of your script
logging.basicConfig(
    filename='package_updates.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_error(error_message):
    """Log error messages to both console and file"""
    print(f"ERROR: {error_message}")
    logging.error(error_message)

def alert_console(message):
    """Make error messages stand out in console"""
    border = "!" * (len(message) + 8)
    print(f"\n{border}")
    print(f"!!! {message} !!!")
    print(f"{border}\n")


# Use Case
# if output.returncode != 0:
#     error_message = "Error updating all packages"
#     log_error(error_message)
#     alert_console(error_message)
#     log_error(output.stderr)
#     print(output.stderr.decode())