import os
import subprocess
import sys
import platform

is_windows = platform.system() == "Windows"


def main():
    try:
        # Locate the qmlformat binary
        from PySide6 import __file__ as pyside_path

        qt_tools_dir = os.path.dirname(pyside_path)
        qmlformat_path = os.path.join(
            qt_tools_dir, "qmlformat.exe" if is_windows else "qmlformat"
        )

        if not os.path.isfile(qmlformat_path):
            print(f"qmlformat binary not found in '{qmlformat_path}'")
            sys.exit(1)

        # Extract additional arguments passed via pre-commit
        extra_args = sys.argv[1:-1]
        files = [f for f in sys.argv[-1:] if f.endswith(".qml")]
        if not files:
            print("No .qml files to process.")
            return 0

        print(f"Processing .qml files with qmlformat: {files}")
        for file in files:
            subprocess.run([qmlformat_path, *extra_args, "--inplace", file], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(e.returncode)

    return 0


if __name__ == "__main__":
    sys.exit(main())
