# SteamVR Actions Manifest Verifier

An application for verifying SteamVR action manifest files. Intended to be run on CI servers.

## Command Line Arguments

All warnings are enabled by default. Use command line arguments to selectively disable unneeded warnings.

| Command | Explanation |
|---------|--------------|
| --Wno-missing-default-bindings | Disables warning on missing "default_bindings" header. |
| --Wno-missing-actions | Disables warnings on missing "actions" header. |
| --Wno-missing-action-sets | Disables warnings on missing "action_sets" header. |
| --Wno-missing-localization | Disables warnings on missing "localization" header. If this is disabled other switches that use the `localization` object must also be disabled. |
| --Wno-missing-en-us-language | Disables warnings on missing "en_US" in "language_tag" under the "localization" header. |
| --Wno-localization-duplicate-values | Disables warnings on objects having the same values in the localization object. |
|  |  |