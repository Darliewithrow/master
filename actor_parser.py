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
        data: Input string in format "actor:<name>" where name may be corrupted
        
    Returns:
        List of valid actor names, filtering out corrupted partial names
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
    
    # First pass: identify corrupted names (those with internal repetition)
    corrupted_actors = set()
    for actor in unique_actors:
        # Check if this is a corrupted name with internal repetition
        # For example, "Darliewithrowliewithrow" has "liewithrow" repeated
        for other_actor in unique_actors:
            if actor != other_actor and actor.startswith(other_actor):
                # Check if removing the prefix leaves a suffix that overlaps
                suffix = actor[len(other_actor):]
                # If the suffix is part of the prefix actor, this is likely corruption
                if suffix and suffix in other_actor:
                    corrupted_actors.add(actor)
                    break
    
    # Second pass: filter based on validity
    filtered_actors = []
    for actor in unique_actors:
        # Skip already identified corrupted names
        if actor in corrupted_actors:
            continue
        
        # Check if this is a prefix of another NON-corrupted actor (likely a fragment)
        is_prefix_of_valid = False
        for other_actor in unique_actors:
            if (actor != other_actor and 
                other_actor.startswith(actor) and 
                other_actor not in corrupted_actors and
                len(actor) <= len(other_actor) / 2):  # Only if significantly shorter
                # This actor is a prefix of another valid one, likely incomplete
                is_prefix_of_valid = True
                break
        
        if not is_prefix_of_valid:
            filtered_actors.append(actor)
    
    return filtered_actors


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
