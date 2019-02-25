HEADER_DEFAULT_BINDINGS = "default_bindings"
HEADER_ACTIONS = "actions"
HEADER_ACTION_SETS = "action_sets"
HEADER_LOCALIZATION = "localization"

LOCALIZATION_LANGUAGE_TAG = "language_tag"
LOCALIZATION_EN_US_LANGUAGE = "en_US"


W_NO_MISSING_DEFAULT_BINDINGS = "--Wno-missing-default-bindings"
W_NO_MISSING_DEFAULT_BINDINGS_EXPLANATION = f"The manifest does not contain a '{HEADER_DEFAULT_BINDINGS}' section."

W_NO_MISSING_ACTIONS = "--Wno-missing-actions"
W_NO_MISSING_ACTIONS_EXPLANATION = f"The manifest does not contain an '{HEADER_ACTIONS}' section."

W_NO_MISSING_ACTION_SETS = "--Wno-missing-action-sets"
W_NO_MISSING_ACTION_SETS_EXPLANATION = f"The manifest does not contain an '{HEADER_ACTION_SETS}' section."

W_NO_MISSING_LOCALIZATION = "--Wno-missing-localization"
W_NO_MISSING_LOCALIZATION_EXPLANATION = f"The manifest does not contain a '{HEADER_LOCALIZATION}' section."

W_NO_EN_US_LANGUAGE = "--Wno-missing-en-us-language"
W_NO_EN_US_LANGUAGE_EXPLANATION = f"The manifest '{HEADER_LOCALIZATION}' section '{LOCALIZATION_LANGUAGE_TAG}' object does not contain '{LOCALIZATION_EN_US_LANGUAGE}'."

W_NO_LOCALIZATION_DUPLICATES = "--Wno-localization-duplicate-values"
W_NO_LOCALIZATION_DUPLICATES_EXPLANATION = f"The '{HEADER_LOCALIZATION}' header contains objects with the same value."

