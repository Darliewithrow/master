"""Utilities for working with Ethereum transaction IDs (hashes)."""

import re

_TX_RE = re.compile(r'\b0x[0-9a-fA-F]{64}\b')


def is_valid_transaction_id(tx: str) -> bool:
    """Return True if *tx* is a well-formed Ethereum transaction hash.

    A valid transaction ID is a 66-character string that starts with ``0x``
    followed by exactly 64 hexadecimal characters (case-insensitive).

    Examples::

        >>> is_valid_transaction_id(
        ...     "0xDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF"
        ... )
        True
        >>> is_valid_transaction_id("0xabc")
        False
    """
    if not isinstance(tx, str):
        return False
    return bool(re.fullmatch(r'0x[0-9a-fA-F]{64}', tx))


def format_transaction_id(tx: str, short: bool = False) -> str:
    """Return a normalised (lowercase) representation of *tx*.

    When *short* is ``True`` the hash is truncated to the form
    ``0x<first-6-chars>...<last-6-chars>``, e.g. ``0xdeadbe...adbeef``.

    Raises ``ValueError`` if *tx* is not a valid transaction ID.

    Examples::

        >>> fmt = format_transaction_id(
        ...     "0xDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF",
        ...     short=True,
        ... )
        >>> fmt
        '0xdeadbe...adbeef'
    """
    if not is_valid_transaction_id(tx):
        raise ValueError(f"Invalid transaction ID: {tx!r}")
    normalised = tx.lower()
    if short:
        hex_part = normalised[2:]  # strip leading '0x'
        return f"0x{hex_part[:6]}...{hex_part[-6:]}"
    return normalised


def parse_transaction_ids(text: str) -> list:
    """Return a sorted list of unique, normalised transaction IDs found in *text*.

    The function scans *text* for substrings that look like Ethereum transaction
    hashes (``0x`` followed by 64 hex characters) and returns them lowercased and
    deduplicated.

    Examples::

        >> ids = parse_transaction_ids(
        ...     "sent via 0xabc123def456abc123def456abc123def456abc123def456abc123def456ab01"
        ...     " and 0xfeed00cafe11feed00cafe11feed00cafe11feed00cafe11feed00cafe11feed00"
        ... )
        >> len(ids)
        2
    """
    matches = _TX_RE.findall(text)
    unique = {m.lower() for m in matches}
    return sorted(unique)
