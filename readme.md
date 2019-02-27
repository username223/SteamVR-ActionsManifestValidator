# SteamVR Actions Manifest Validator

An application for validating SteamVR action manifest files. Intended to be run on CI servers.

SteamVR does not adequately give out errors for incorrect action manifests. This severely hinders development when there is no documentation or the documentation is plain wrong.

To use specify the action manifest as an argument:

```sh
$ python manifest_verifier.py action_manifest.json
Verifying action_manifest.json.
File verified.

```

Or pipe into the script:

```sh
$ cat action_manifest.json | python manifest_verifier.py
Verifying file from STDIN.
File verified.
```

On errors:

```sh
$ cat action_manifest.json | python manifest_verifier.py test/no_language_en_us.json
Verifying test/no_language_en_us.json.
ERROR:
        The manifest 'localization' section 'language_tag' object does not contain 'en_US'.
        To disable this check run with: '--Wno-missing-en-us-language'
```

If the manifest is not correctly formed JSON (duplicate keys not allowed) the program will exit with error code 1. If the manifest contains any of the below errors it will exit with error code 2. If no errors were detected, the program will exit with code 0.

[This](action_manifest.json) is a working action manifest and what I'm assuming a correctly formatted manifest looks like. It is in use by [OpenVR Advanced Settings](https://github.com/OpenVR-Advanced-Settings/OpenVR-AdvancedSettings).

## Checks

### Missing `default_bindings`
Disabled with `--Wno-missing-default-bindings`.

Checks if the JSON contains a `"default_bindings"` object. Is here to make sure `default_bindings` is spelled correctly.

### Missing `actions`
Disabled with `--Wno-missing-actions`.

Checks if the JSON contains an `"actions"` object. Is here to make sure `actions` is spelled correctly.

### Missing `action_sets`
Disabled with `--Wno-missing-action-sets`.

Checks if the JSON contains an `"action_sets"` object. Is here to make sure `action_sets` is spelled correctly.

### Missing `localization`
Disabled with `--Wno-missing-localization`.

Checks if the JSON contains an `"localization"` object. Is here to make sure `localization` is spelled correctly. If this is disabled other checks that expect the `localization` to be there must also be disabled.

### Missing `en_US` language in `localization`
Disabled with `--Wno-missing-en-us-language `.

Checks if the `localization` object contains an entry for `en_US`. This is the fallback locale and it should be present. This is also here to make sure people don't mistype `en_US` as only `en`, as is done in the official documentation.

### Duplicate values in `localization`
Disabled with `--Wno-localization-duplicate-values`.

Checks if the `localization` object contains several objects with the same value, since it is highly likely to be a copy paste error. Duplicate keys are already checked when the JSON is tested for validity. It is not possible to disable that check.
