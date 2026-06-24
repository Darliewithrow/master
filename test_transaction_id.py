#!/usr/bin/env python3
"""
Test suite for Transaction ID Handler
"""

import unittest
from transaction_id import (
    is_valid_transaction_id,
    normalize_transaction_id,
    format_transaction_id,
    parse_transaction_ids,
)


class TestIsValidTransactionId(unittest.TestCase):
    """Tests for is_valid_transaction_id."""

    def test_valid_lowercase(self):
        tx = "0x" + "a" * 64
        self.assertTrue(is_valid_transaction_id(tx))

    def test_valid_uppercase(self):
        tx = "0x" + "A" * 64
        self.assertTrue(is_valid_transaction_id(tx))

    def test_valid_mixed_case(self):
        tx = "0xaAbBcCdDeEfF" + "0" * 52
        self.assertTrue(is_valid_transaction_id(tx))

    def test_too_short(self):
        tx = "0x" + "a" * 63
        self.assertFalse(is_valid_transaction_id(tx))

    def test_too_long(self):
        tx = "0x" + "a" * 65
        self.assertFalse(is_valid_transaction_id(tx))

    def test_missing_prefix(self):
        tx = "a" * 64
        self.assertFalse(is_valid_transaction_id(tx))

    def test_invalid_hex_chars(self):
        tx = "0x" + "g" * 64
        self.assertFalse(is_valid_transaction_id(tx))

    def test_empty_string(self):
        self.assertFalse(is_valid_transaction_id(""))

    def test_non_string_input(self):
        self.assertFalse(is_valid_transaction_id(12345))  # type: ignore[arg-type]


class TestNormalizeTransactionId(unittest.TestCase):
    """Tests for normalize_transaction_id."""

    def test_uppercase_normalized_to_lowercase(self):
        tx = "0x" + "A" * 64
        self.assertEqual(normalize_transaction_id(tx), "0x" + "a" * 64)

    def test_prefix_added_when_missing(self):
        tx = "a" * 64
        self.assertEqual(normalize_transaction_id(tx), "0x" + "a" * 64)

    def test_leading_whitespace_stripped(self):
        tx = "  0x" + "b" * 64
        self.assertEqual(normalize_transaction_id(tx), "0x" + "b" * 64)

    def test_invalid_returns_none(self):
        self.assertIsNone(normalize_transaction_id("not_a_tx_id"))

    def test_non_string_returns_none(self):
        self.assertIsNone(normalize_transaction_id(None))  # type: ignore[arg-type]

    def test_already_normalized(self):
        tx = "0x" + "1234567890abcdef" * 4
        self.assertEqual(normalize_transaction_id(tx), tx)


class TestFormatTransactionId(unittest.TestCase):
    """Tests for format_transaction_id."""

    def test_full_format(self):
        tx = "0x" + "a" * 64
        self.assertEqual(format_transaction_id(tx), "0x" + "a" * 64)

    def test_short_format(self):
        tx = "0x" + "abcdef" + "0" * 52 + "123456"
        result = format_transaction_id(tx, short=True)
        self.assertEqual(result, "0xabcdef...123456")

    def test_invalid_returns_none(self):
        self.assertIsNone(format_transaction_id("invalid"))

    def test_normalizes_case(self):
        tx = "0x" + "A" * 64
        self.assertEqual(format_transaction_id(tx), "0x" + "a" * 64)


class TestParseTransactionIds(unittest.TestCase):
    """Tests for parse_transaction_ids."""

    def test_single_tx_id(self):
        tx = "0x" + "1" * 64
        result = parse_transaction_ids(f"tx={tx}")
        self.assertEqual(result, [tx])

    def test_multiple_tx_ids(self):
        tx1 = "0x" + "1" * 64
        tx2 = "0x" + "2" * 64
        result = parse_transaction_ids(f"{tx1} {tx2}")
        self.assertEqual(result, [tx1, tx2])

    def test_duplicates_removed(self):
        tx = "0x" + "a" * 64
        result = parse_transaction_ids(f"{tx} {tx}")
        self.assertEqual(result, [tx])

    def test_invalid_entries_skipped(self):
        tx = "0x" + "c" * 64
        result = parse_transaction_ids(f"garbage {tx} more_garbage")
        self.assertEqual(result, [tx])

    def test_empty_string(self):
        self.assertEqual(parse_transaction_ids(""), [])

    def test_no_tx_ids(self):
        self.assertEqual(parse_transaction_ids("no transaction ids here"), [])

    def test_case_normalization(self):
        tx_upper = "0x" + "A" * 64
        tx_lower = "0x" + "a" * 64
        # Both forms refer to the same ID; only one should appear
        result = parse_transaction_ids(f"{tx_upper} {tx_lower}")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], tx_lower)


if __name__ == "__main__":
    unittest.main()
