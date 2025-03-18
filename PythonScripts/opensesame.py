import subprocess

def open_windows():
    while True:
        subprocess.run(["google-chrome"])

if __name__ == "__main__":
    open_windows()