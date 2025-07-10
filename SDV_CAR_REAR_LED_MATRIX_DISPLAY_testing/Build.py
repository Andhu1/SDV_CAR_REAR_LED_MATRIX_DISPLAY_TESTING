import subprocess
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
# 🔧 Configurable Paths (Update these)
UV4_PATH = r"C:\Keil_v5\UV4\UV4.exe"
FROMELF_PATH = r"C:\Keil_v5\ARM\ARMCC\bin\fromelf.exe"
PROJECT_PATH = r"C:\Users\DELL\.jenkins\workspace\SDV_demo1\SDV_CAR_REAR_LED_MATRIX_DISPLAY_testing\Uart_project.uvprojx"
TARGET_NAME = "Target 1"  # Use exact target name from Keil
AXF_FILE = r"C:\Users\DELL\.jenkins\workspace\SDV_demo1\SDV_CAR_REAR_LED_MATRIX_DISPLAY_testing\Uart_project.axf"
HEX_FILE = r"C:\Users\DELL\.jenkins\workspace\SDV_demo1\SDV_CAR_REAR_LED_MATRIX_DISPLAY_testing\Uart_project.hex"

def build_project():
    print("🚧 Building Keil project...")
    build_cmd = [UV4_PATH, "-b", PROJECT_PATH, "-t", TARGET_NAME]
    result = subprocess.run(build_cmd, capture_output=True, text=True)

    print(result.stdout)
    if result.returncode == 0:
        print("✅ Build completed successfully.")
        return True
    else:
        print("❌ Build failed.")
        print(result.stderr)
        return False

def generate_hex():
    print("📦 Generating HEX file from AXF...")
    if not os.path.exists(AXF_FILE):
        print(f"❌ AXF file not found: {AXF_FILE}")
        return False

    hex_cmd = [FROMELF_PATH, "--i32", AXF_FILE, "--output", HEX_FILE]
    result = subprocess.run(hex_cmd, capture_output=True, text=True)

    if result.returncode == 0 and os.path.exists(HEX_FILE):
        print(f"✅ HEX file created: {HEX_FILE}")
        return True
    else:
        print("❌ Failed to generate HEX file.")
        print(result.stderr)
        return False

if __name__ == "__main__":
    if build_project():
        generate_hex()
