import subprocess

PYTHON_BIN = "./.env/bin/python"
SCRIPT_FILE = "grobbed.py"


def main() -> None:
    subprocess.Popen([PYTHON_BIN, SCRIPT_FILE])


if __name__ == "__main__":
    main()
