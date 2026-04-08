#!/usr/bin/env python3
"""
Transaction ID Handler

This module provides functions to validate, normalize, and handle
Ethereum transaction IDs (transaction hashes).

Ethereum transaction IDs are 32-byte values represented as 66-character
hex strings (including the '0x' prefix).
"""

import re
import sys
from typing import List, Optional


# Ethereum transaction ID pattern: '0x' followed by exactly 64 hex characters
TX_ID_PATTERN = re.compile(r'^0x[0-9a-fA-F]{64}$')
TX_ID_LENGTH = 64  # hex characters after '0x'


def is_valid_transaction_id(tx_id: str) -> bool:
    """
    Check whether a string is a valid Ethereum transaction ID.

    A valid transaction ID starts with '0x' and is followed by
    exactly 64 hexadecimal characters (case-insensitive).

    Args:
        tx_id: The string to validate.

    Returns:
        True if tx_id is a valid Ethereum transaction ID, False otherwise.
    """
    if not isinstance(tx_id, str):
        return False
    return bool(TX_ID_PATTERN.match(tx_id))


def normalize_transaction_id(tx_id: str) -> Optional[str]:
    """
    Normalize a transaction ID to lowercase hex with '0x' prefix.

    Args:
        tx_id: A raw transaction ID string. May include or omit the '0x'
               prefix and may use upper- or lower-case hex digits.

    Returns:
        The normalized transaction ID (lowercase, with '0x' prefix), or
        None if the input cannot be normalized to a valid ID.
    """
    if not isinstance(tx_id, str):
        return None

    stripped = tx_id.strip()

    # Add '0x' prefix if missing
    if not stripped.startswith('0x') and not stripped.startswith('0X'):
        stripped = '0x' + stripped

    normalized = '0x' + stripped[2:].lower()

    if not is_valid_transaction_id(normalized):
        return None

    return normalized


def format_transaction_id(tx_id: str, short: bool = False) -> Optional[str]:
    """
    Return a human-readable representation of a transaction ID.

    Args:
        tx_id: A transaction ID string (with or without '0x' prefix).
        short: If True, return a shortened form showing the first and last
               six hex characters separated by '...'.

    Returns:
        The formatted string, or None if tx_id is not valid.
    """
    normalized = normalize_transaction_id(tx_id)
    if normalized is None:
        return None

    if short:
        # e.g. 0xabcdef...123456
        hex_part = normalized[2:]
        return f"0x{hex_part[:6]}...{hex_part[-6:]}"

    return normalized


def parse_transaction_ids(data: str) -> List[str]:
    """
    Extract all valid Ethereum transaction IDs from a block of text.

    Args:
        data: A string that may contain one or more transaction IDs.

    Returns:
        A list of unique, normalized transaction IDs found in the text,
        in the order they first appear.
    """
    if not data:
        return []

    # Find all candidate '0x...' tokens
    candidates = re.findall(r'0x[0-9a-fA-F]+', data)

    seen: set = set()
    result: List[str] = []
    for candidate in candidates:
        normalized = normalize_transaction_id(candidate)
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(normalized)

    return result


def main() -> None:
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as f:
                input_data = f.read().strip()
            print(f"Reading from file: {file_path}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
            sys.exit(1)
    else:
        # Example Ethereum transaction IDs for demonstration
        input_data = (
            "0xabc123def456abc123def456abc123def456abc123def456abc123def456abc1 "
            "0xDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF "
            "invalid_tx "
            "0xabc123def456abc123def456abc123def456abc123def456abc123def456abc1"
        )

    print(f"Input data:\n{input_data}\n")

    tx_ids = parse_transaction_ids(input_data)

    print("Found transaction IDs:")
    for i, tx_id in enumerate(tx_ids, 1):
        short = format_transaction_id(tx_id, short=True)
        print(f"  {i}. {tx_id}  (short: {short})")

    print(f"\nTotal unique transaction IDs: {len(tx_ids)}")


if __name__ == "__main__":
    main()
