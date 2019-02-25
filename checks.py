import json
from enum import Enum
from common import *
import sys

class ErrorCodes(Enum):
    CORRECT_EXIT = 0
    INVALID_JSON = 1
    ERRORS_DETECTED = 2

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys. Python does not do this by default."""
    dictionary = {}
    for key, value in ordered_pairs:
        if key in dictionary:
           raise ValueError("Duplicate key: %r" % (key,))
        else:
           dictionary[key] = value
    return dictionary

def verify_correct_json(json_string: str):
    try:
        json.loads(json_string, object_pairs_hook=dict_raise_on_duplicates)
    except ValueError as e:
        exit_code = ErrorCodes.INVALID_JSON.value
        print(f"ERROR:")
        print("\t" + str(e))
        print("\tUnable to continue.")
        sys.exit(exit_code)

def check_missing_default_bindings(options, json_obj):
    if not options.missing_bindings:
        return

    if HEADER_DEFAULT_BINDINGS in json_obj:
        return

    log_error_and_exit(W_NO_MISSING_DEFAULT_BINDINGS,
                        W_NO_MISSING_DEFAULT_BINDINGS_EXPLANATION)

def check_missing_actions(options, json_obj):
    if not options.missing_actions:
        return

    if HEADER_ACTIONS in json_obj:
        return

    log_error_and_exit(W_NO_MISSING_ACTIONS,
                        W_NO_MISSING_ACTIONS_EXPLANATION)

def check_missing_action_sets(options, json_obj):
    if not options.missing_action_sets:
        return

    if HEADER_ACTION_SETS in json_obj:
        return

    log_error_and_exit(W_NO_MISSING_ACTION_SETS,
                        W_NO_MISSING_ACTION_SETS_EXPLANATION)

def check_missing_localization(options, json_obj):
    if not options.missing_localization:
        return

    if HEADER_LOCALIZATION in json_obj:
        return

    log_error_and_exit(W_NO_MISSING_LOCALIZATION,
                        W_NO_MISSING_LOCALIZATION_EXPLANATION)

def check_localization_missing_en_us_language(options, json_obj):
    if not options.missing_en_us_language:
        return

    localization_header = json_obj[HEADER_LOCALIZATION]

    en_us_exists = False
    for language in localization_header:
        if language[LOCALIZATION_LANGUAGE_TAG] == LOCALIZATION_EN_US_LANGUAGE:
            en_us_exists = True

    if en_us_exists:
        return

    log_error_and_exit(W_NO_EN_US_LANGUAGE,
                        W_NO_EN_US_LANGUAGE_EXPLANATION)

def check_localization_duplicate_values(options, json_obj):
    if not options.missing_localization_duplicates:
        return

    localization_header = json_obj[HEADER_LOCALIZATION]

    for language in localization_header:
        values = {}
        for key, value in language.items():
            if value in values:
                log_error_and_exit(W_NO_LOCALIZATION_DUPLICATES,
                        W_NO_LOCALIZATION_DUPLICATES_EXPLANATION
                            + " '"
                            + key
                            + "' contains the value '"
                            + value
                            +"', the same as '"
                            + values[value]
                            + "'.")
            values[value] = key


def log_error_and_exit(error_command: str, error_explanation: str):
    print("ERROR:")
    print("\t" + error_explanation)
    print("\tTo disable this check run with: '" + error_command + "'")
    sys.exit(ErrorCodes.ERRORS_DETECTED.value)