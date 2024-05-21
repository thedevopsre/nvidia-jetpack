import os
import sys
import subprocess

MODULE_NAME_TABLE = {
    'p3767-0005': 'NVIDIA Jetson Orin Nano (Developer kit)',
    'p3767-0004': 'NVIDIA Jetson Orin Nano (4GB ram)',
    'p3767-0003': 'NVIDIA Jetson Orin Nano (8GB ram)',
    'p3767-0001': 'NVIDIA Jetson Orin NX (8GB ram)',
    'p3767-0000': 'NVIDIA Jetson Orin NX (16GB ram)',
    'p3701-0005': 'NVIDIA Jetson AGX Orin (64GB ram)',
    'p3701-0004': 'NVIDIA Jetson AGX Orin (32GB ram)',
    'p3701-0002': 'NVIDIA Jetson IGX Orin (Developer kit)',
    'p3701-0000': 'NVIDIA Jetson AGX Orin',
    'p3668-0003': 'NVIDIA Jetson Xavier NX (16GB ram)',
    'p3668-0001': 'NVIDIA Jetson Xavier NX',
    'p3668-0000': 'NVIDIA Jetson Xavier NX (Developer kit)',
    'p2888-0008': 'NVIDIA Jetson AGX Xavier Industrial (32 GB ram)',
    'p2888-0006': 'NVIDIA Jetson AGX Xavier (8 GB ram)',
    'p2888-0005': 'NVIDIA Jetson AGX Xavier (64 GB ram)',
    'p2888-0004': 'NVIDIA Jetson AGX Xavier (32 GB ram)',
    'p2888-0003': 'NVIDIA Jetson AGX Xavier (32 GB ram)',
    'p2888-0001': 'NVIDIA Jetson AGX Xavier (16 GB ram)',
    'p3448-0003': 'NVIDIA Jetson Nano (2 GB ram)',
    'p3448-0002': 'NVIDIA Jetson Nano module (16Gb eMMC)',
    'p3448-0000': 'NVIDIA Jetson Nano (4 GB ram)',
    'p3636-0001': 'NVIDIA Jetson TX2 NX',
    'p3509-0000': 'NVIDIA Jetson TX2 NX',
    'p3489-0888': 'NVIDIA Jetson TX2 (4 GB ram)',
    'p3489-0000': 'NVIDIA Jetson TX2i',
    'p3310-1000': 'NVIDIA Jetson TX2',
    'p2180-1000': 'NVIDIA Jetson TX1',
    'r375-0001': 'NVIDIA Jetson TK1',
    'p3904-0000': 'NVIDIA Clara AGX',
    # Other modules
    'p2595-0000-A0': 'Nintendo Switch'
}

NVIDIA_JETPACK = {
    # -------- JP6 --------
    "36.2.0": "6.0 DP",
    "36.0.0": "6.0 EA",
    # -------- JP5 --------
    "35.5.0": "5.1.3",
    "35.4.1": "5.1.2",
    "35.3.1": "5.1.1",
    "35.3.0": "5.1.1 PRE",
    "35.2.1": "5.1",
    "35.1.0": "5.0.2 GA",
    "34.1.1": "5.0.1 DP",
    "34.1.0": "5.0 DP",
    "34.0.1": "5.0 PRE-DP",
    # -------- JP4 --------
    "32.7.4": "4.6.4",
    "32.7.3": "4.6.3",
    "32.7.2": "4.6.2",
    "32.7.1": "4.6.1",
    "32.6.1": "4.6",
    "32.5.2": "4.5.1",
    "32.5.1": "4.5.1",
    "32.5.0": "4.5",
    "32.5": "4.5",
    "32.4.4": "4.4.1",
    "32.4.3": "4.4",
    "32.4.2": "4.4 DP",
    "32.3.1": "4.3",
    "32.2.3": "4.2.3",
    "32.2.1": "4.2.2",
    "32.2.0": "4.2.1",
    "32.2": "4.2.1",
    "32.1.0": "4.2",
    "32.1": "4.2",
    "31.1.0": "4.1.1",
    "31.1": "4.1.1",
    "31.0.2": "4.1",
    "31.0.1": "4.0",
    # -------- Old JP --------
    "28.4.0": "3.3.3",
    "28.2.1": "3.3 | 3.2.1",
    "28.2.0": "3.2",
    "28.2": "3.2",
    "28.1.0": "3.1",
    "28.1": "3.1",
    "27.1.0": "3.0",
    "27.1": "3.0",
    "24.2.1": "3.0 | 2.3.1",
    "24.2.0": "2.3",
    "24.2": "2.3",
    "24.1.0": "2.2.1 | 2.2",
    "24.1": "2.2.1 | 2.2",
    "23.2.0": "2.1",
    "23.2": "2.1",
    "23.1.0": "2.0",
    "23.1": "2.0",
    "21.5.0": "2.3.1 | 2.3",
    "21.5": "2.3.1 | 2.3",
    "21.4.0": "2.2 | 2.1 | 2.0 | 1.2 DP",
    "21.4": "2.2 | 2.1 | 2.0 | 1.2 DP",
    "21.3.0": "1.1 DP",
    "21.3": "1.1 DP",
    "21.2.0": "1.0 DP",
    "21.2": "1.0 DP",
}

# Run dpkg-query to get the version of nvidia-l4t-core
def get_nvidia_l4t():
    if sys.version_info >= (3, 7):  # Check if capture_output is supported
        output = subprocess.run(['dpkg-query', '--showformat=\'${Version}\'', '--show', 'nvidia-l4t-core'], capture_output=True, text=True)
        version = output.stdout.strip().split('-')[0].lstrip('\'')
    else:
        process = subprocess.Popen(['dpkg-query', '--showformat=\'${Version}\'', '--show', 'nvidia-l4t-core'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = process.communicate()  # Get the stdout and ignore stderr
        version = stdout.decode().strip().split('-')[0].lstrip('\'')
    return version

nvidia_l4t_version = get_nvidia_l4t()

if nvidia_l4t_version in NVIDIA_JETPACK:
    result = NVIDIA_JETPACK[nvidia_l4t_version]
else:
    print("No corresponding NVIDIA JetPack version found.")

# Read the output of /proc/device-tree/compatible
with open("/proc/device-tree/compatible", "r") as file:
    compatible_data = file.read().strip()

# Check if the compatible_data matches any entry in the MODULE_NAME_TABLE
matched_module = None
for module_code, module_name in MODULE_NAME_TABLE.items():
    if module_code in compatible_data:
        matched_module = module_name
        break

if matched_module:
    print(f"Device: {matched_module} Model: {result}")
else:
    print("No matching device found in the MODULE_NAME_TABLE.")
