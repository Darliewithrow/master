# Actor Data Parser

This repository contains a Python script to parse actor data from a formatted string.

## Problem Statement

Parse actor information from the following format:
```
actor:Daractor:Darliewithrowliewithrowactor:Darliewithrowactor:Darliewithrow
```

## Solution

The `actor_parser.py` script parses the input string by splitting on the `actor:` delimiter, then intelligently filters out corrupted and fragmented actor names to extract only valid actor names.

### Usage

Run with default data:
```bash
python3 actor_parser.py
```

Run with data from a file:
```bash
python3 actor_parser.py actor_data.txt
```

### Output

```
Parsed Actors:
1. Darliewithrow

Total unique actors: 1
```

## Testing

Run the test suite:

```bash
python3 test_actor_parser.py
```

## Implementation Details

- The parser splits the input string by `actor:` delimiter
- Identifies and filters out corrupted names with internal repetitions
- Removes fragment names that are prefixes of longer valid names
- Maintains unique actors in order of first appearance
- Returns a list of valid actor names

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
# Actor Data Parser

This repository contains a Python script to parse actor data from a formatted string.

## Problem Statement

Parse actor information from the following format:
```
actor:Daractor:Darliewithrowliewithrowactor:Darliewithrowactor:Darliewithrow
```

## Solution

The `actor_parser.py` script parses the input string by splitting on the `actor:` delimiter, then intelligently filters out corrupted and fragmented actor names to extract only valid actor names.

### Usage

Run with default data:
```bash
python3 actor_parser.py
```

Run with data from a file:
```bash
python3 actor_parser.py actor_data.txt
```

### Output

```
Parsed Actors:
1. Darliewithrow

Total unique actors: 1
```

## Testing

Run the test suite:

```bash
python3 test_actor_parser.py
```

## Implementation Details

- The parser splits the input string by `actor:` delimiter
- Identifies and filters out corrupted names with internal repetitions
- Removes fragment names that are prefixes of longer valid names
- Maintains unique actors in order of first appearance
- Returns a list of valid actor names

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
