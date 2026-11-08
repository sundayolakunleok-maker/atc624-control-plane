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


if __name__ == "__main__":
    unittest.main()
