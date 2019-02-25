#!/usr/bin/env python
r"""Command-line tool to validate the OpenVR actions manifest files
Usage::
    $ cat actions_manifest.json | python manifest_verifier.py
OR
    $ python manifest_verifier.py actions_manifest.json
"""
__version__ = "0.1.0"

import argparse
import json
import sys
from common import *
from checks import *

errors_detected = False

def main(options):
    json_str = get_file_contents(options)
    verify_correct_json(json_str)

    json_obj = json.loads(json_str)

    check_missing_default_bindings(options, json_obj)
    check_missing_actions(options, json_obj)
    check_missing_action_sets(options, json_obj)
    check_missing_localization(options, json_obj)

    check_localization_missing_en_us_language(options, json_obj)
    check_localization_duplicate_values(options, json_obj)

    exit_successfully()

def initialize_args(args):
    prog = "python manifest_verifier.py"
    description = ("A simple command line tool to verify OpenVR actions manifests.")
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('--version', action='version',
                    version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument("infile", nargs="?", type=argparse.FileType(),
                        help="a JSON file to be validated")
    parser.add_argument(W_NO_MISSING_DEFAULT_BINDINGS,
                        dest="missing_bindings",
                        action="store_false",
                        help=W_NO_MISSING_DEFAULT_BINDINGS_EXPLANATION)
    parser.add_argument(W_NO_MISSING_ACTIONS,
                        dest="missing_actions",
                        action="store_false",
                        help=W_NO_MISSING_ACTIONS_EXPLANATION)
    parser.add_argument(W_NO_MISSING_ACTION_SETS,
                        dest="missing_action_sets",
                        action="store_false",
                        help=W_NO_MISSING_ACTION_SETS_EXPLANATION)
    parser.add_argument(W_NO_MISSING_LOCALIZATION,
                        dest="missing_localization",
                        action="store_false",
                        help=W_NO_MISSING_LOCALIZATION_EXPLANATION)
    parser.add_argument(W_NO_EN_US_LANGUAGE,
                        dest="missing_en_us_language",
                        action="store_false",
                        help=W_NO_EN_US_LANGUAGE_EXPLANATION)
    parser.add_argument(W_NO_LOCALIZATION_DUPLICATES,
                        dest="missing_localization_duplicates",
                        action="store_false",
                        help=W_NO_LOCALIZATION_DUPLICATES_EXPLANATION)
    return parser.parse_args(args)

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


if __name__ == "__main__":
    options = initialize_args(sys.argv[1:])
    main(options)
