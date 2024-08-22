import os
import re
import argparse
from jtop.core.common import get_var
from jtop.core.nvpmodel import nvpmodel_query
from jtop.core.hardware import get_platform_variables
from jtop.core.jetson_variables import get_jetson_variables
from jtop.core.jetson_libraries import get_libraries, get_cuda, get_opencv
from jtop.core.exceptions import JtopException
from jtop.service import status_service
from jtop.terminal_colors import bcolors

# Version match
VERSION_RE = re.compile(r""".*__version__ = ["'](.*?)['"]""", re.S)
COPYRIGHT_RE = re.compile(r""".*__copyright__ = ["'](.*?)['"]""", re.S)


def main():
    parser = argparse.ArgumentParser(
        description='Show detailed information about this board. Machine, Jetpack, libraries and other',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', dest="verbose", help='Show all variables', action="store_true",
                        default=False)
    parser.add_argument('-s', '--serial', dest="serial", help='Show serial number', action="store_true", default=False)

    # Copyrights
    print("Software part of jetson-stats {version} - {copyright}".format(
        version=get_var(VERSION_RE), copyright=get_var(COPYRIGHT_RE)))

    # Parse arguments
    args = parser.parse_args()

    # Read all Jetson Variables
    jetson = get_jetson_variables()

    # Extract and remove Serial Number
    serial_number = jetson['Serial Number']
    del jetson['Serial Number']

    # Prepare the model info string
    if jetson['Jetpack']:
        model_info = "Model: {model} for DSBOARD-NX2 - Jetpack {jetpack} [L4T {L4T}]".format(
            model=jetson['Model'],
            jetpack=jetson['Jetpack'],
            L4T=jetson['L4T']
        )
    else:
        model_info = "Jetpack missing!\n - Model: {model}\n - L4T: {L4T}".format(
            model=jetson['Model'],
            L4T=jetson['L4T']
        )

    # Print the model info
    print(model_info)

    # Write the model info to a file
    with open("version.txt", "w") as file:
        file.write(model_info)

    # Continue with the rest of the script (truncated for brevity)
    # Print NVP model status
    try:
        nvpmodel_now = nvpmodel_query()
        print("{service}[{number}]: {name}".format(
            service=bcolors.ok(bcolors.bold("NV Power Mode")),
            name=bcolors.bold(nvpmodel_now['name']),
            number=bcolors.bold(nvpmodel_now['id'])))
    except JtopException:
        pass

    # Print serial number
    if serial_number:
        if not args.serial:
            serial_number = "[XXX Show with: jetson_release -s XXX]"
        print("{sn_string} {serial_number}".format(sn_string=bcolors.ok(bcolors.bold("Serial Number:")),
                                                   serial_number=serial_number))

    # (Rest of your script...)


if __name__ == "__main__":
    main()
