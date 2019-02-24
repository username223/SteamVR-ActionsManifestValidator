#!/usr/bin/env python
r"""Command-line tool to validate the OpenVR actions manifest files
Usage::
    $ cat actions_manifest.json | python manifest_verifier.py
OR
    $ python manifest_verifier.py actions_manifest.json
"""
import argparse
import json
import sys
from enum import Enum

def main():
    options = initialize_args()
    json_str = get_file_contents(options)
    verify_correct_json(json_str)

    exit_successfully()

def call_error(error_code: int, error_message: str):
    print(f"ERROR {error_code}: " + str(error_message))
    sys.exit(error_code)

def verify_correct_json(json_string: str):
    try:
        json.loads(json_string)
    except ValueError as e:
        exit_code = ErrorCodes.INVALID_JSON.value 
        call_error(exit_code, e)

def initialize_args():
    prog = 'python manifest_verifier.py'
    description = ('A simple command line tool to verify OpenVR actions manifests.')
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('infile', nargs='?', type=argparse.FileType(),
                        help='a JSON file to be validated')   
    return parser.parse_args()

def get_file_contents(options) -> str:
    if options.infile:
        print("Verifying " + options.infile.name + ".")
        return options.infile.read()
    else:
        print("Verifying file from STDIN.")
        return sys.stdin.read()

def exit_successfully():
    print("File verified.")
    sys.exit(ErrorCodes.CORRECT_EXIT.value)

class ErrorCodes(Enum):
    CORRECT_EXIT = 0
    INVALID_JSON = 1

if __name__ == '__main__':
    main()
