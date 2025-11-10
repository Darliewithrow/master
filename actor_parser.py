#!/usr/bin/env python3
"""
Actor Data Parser

This script parses actor data from a formatted string.
The input format is: actor:<name>actor:<name>...
"""

import re
import sys
from typing import List, Set


def parse_actors(data: str) -> List[str]:
    """
    Parse actor names from the input string.
    
    Args:
        data: Input string in format "actor:<name>actor:<name>..."
        
    Returns:
        List of unique actor names in order of appearance
    """
    if not data:
        return []
    
    # Split by 'actor:' and filter out empty strings
    parts = data.split('actor:')
    actors = [part.strip() for part in parts if part.strip()]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_actors = []
    for actor in actors:
        if actor not in seen:
            seen.add(actor)
            unique_actors.append(actor)
    
    return unique_actors


def main():
    # Check if a file path is provided as argument
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
        # The problem statement data
        input_data = "actor:Daractor:Darliewithrowliewithrowactor:Darliewithrowactor:Darliewithrow"
    
    print(f"Input data: {input_data}\n")
    
    actors = parse_actors(input_data)
    
    print("Parsed Actors:")
    for i, actor in enumerate(actors, 1):
        print(f"{i}. {actor}")
    
    print(f"\nTotal unique actors: {len(actors)}")


if __name__ == "__main__":
    main()
