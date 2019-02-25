from manifest_verifier import main, initialize_args
from common import *
import unittest
import argparse

def run_file_with_args_and_assert_code(self, args, error_code):
    with self.assertRaises(SystemExit) as cm:
        options = initialize_args(args)
        main(options)
    self.assertEqual(cm.exception.code, error_code)

class TestFeatures(unittest.TestCase):
    def test_should_fail_missing_default_bindings(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_default_bindings.json"],
                                         2)

    def test_should_work_missing_default_bindings(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_default_bindings.json",
                                        W_NO_MISSING_DEFAULT_BINDINGS],
                                        0)

    def test_should_fail_missing_actions(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_actions_bindings.json"],
                                        2)

    def test_should_work_missing_actions(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_actions_bindings.json",
                                        W_NO_MISSING_ACTIONS],
                                        0)

    def test_should_fail_missing_action_sets(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_action_sets_bindings.json"],
                                        2)
    
    def test_should_work_missing_action_sets(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_action_sets_bindings.json",
                                        W_NO_MISSING_ACTION_SETS],
                                        0)

    def test_should_fail_missing_localization(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_localization_bindings.json"],
                                        2)

    def test_should_fail_missing_en_us_language(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_language_en_us.json"],
                                        2)

    def test_should_work_missing_en_us_language(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_language_en_us.json",
                                        W_NO_EN_US_LANGUAGE],
                                        0)

    def test_should_fail_duplicate_keys(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_localization_duplicates_bindings.json"],
                                        1)

    def test_should_fail_duplicate_values(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_localization_duplicate_values.json"],
                                        2)

    def test_should_work_duplicate_values(self):
        run_file_with_args_and_assert_code(self,
                                        ["test/no_localization_duplicate_values.json",
                                        W_NO_LOCALIZATION_DUPLICATES],
                                        0)
