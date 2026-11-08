"""Tests for welcome.welcome_message."""

import unittest

from welcome import welcome_message


class WelcomeMessageTests(unittest.TestCase):
    def test_returns_personalized_message_for_a_name(self):
        self.assertEqual(welcome_message("Sunday"), "Welcome, Sunday!")

    def test_returns_guest_for_empty_name(self):
        self.assertEqual(welcome_message(""), "Welcome, Guest!")

    def test_returns_guest_for_whitespace_only_name(self):
        self.assertEqual(welcome_message("   "), "Welcome, Guest!")

    def test_trims_surrounding_spaces(self):
        self.assertEqual(welcome_message("  Sunday  "), "Welcome, Sunday!")

    def test_returns_guest_for_none(self):
        self.assertEqual(welcome_message(None), "Welcome, Guest!")

    def test_uses_custom_greeting(self):
        self.assertEqual(welcome_message("Sunday", "Hello"), "Hello, Sunday!")

    def test_custom_greeting_ignored_for_empty_name(self):
        self.assertEqual(welcome_message("", "Hello"), "Welcome, Guest!")

    def test_custom_greeting_ignored_for_whitespace_only_name(self):
        self.assertEqual(welcome_message("   ", "Hello"), "Welcome, Guest!")

    def test_custom_greeting_ignored_for_none(self):
        self.assertEqual(welcome_message(None, "Hello"), "Welcome, Guest!")


if __name__ == "__main__":
    unittest.main()
