import subprocess

def install_pygame():
    try:
        subprocess.run(["pip", "install", "pygame"], check=True)
        print("pygame installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_pygame()
