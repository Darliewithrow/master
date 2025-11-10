#!/usr/bin/env python3
"""
Test suite for Actor Data Parser
"""

import unittest
from actor_parser import parse_actors


class TestActorParser(unittest.TestCase):
    """Test cases for the actor parser"""
    
    def test_simple_actors(self):
        """Test parsing simple actor list"""
        data = "actor:John actor:Jane actor:Bob"
        expected = ["John", "Jane", "Bob"]
        self.assertEqual(parse_actors(data), expected)
    
    def test_duplicate_actors(self):
        """Test that duplicate actors are removed"""
        data = "actor:Alice actor:Bob actor:Alice"
        expected = ["Alice", "Bob"]
        self.assertEqual(parse_actors(data), expected)
    
    def test_empty_string(self):
        """Test parsing empty string"""
        self.assertEqual(parse_actors(""), [])
    
    def test_single_actor(self):
        """Test parsing single actor"""
        data = "actor:SingleActor"
        expected = ["SingleActor"]
        self.assertEqual(parse_actors(data), expected)
    
    def test_problem_statement_data(self):
        """Test the actual problem statement data"""
        data = "actor:Daractor:Darliewithrowliewithrowactor:Darliewithrowactor:Darliewithrow"
        result = parse_actors(data)
        # Should parse into distinct actors
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        # Check that Darliewithrow is in the results
        self.assertIn("Darliewithrow", result)
    
    def test_actors_with_whitespace(self):
        """Test parsing actors with whitespace"""
        data = "actor: SpaceActor  actor:NoSpace  "
        result = parse_actors(data)
        self.assertIn("SpaceActor", result)
        self.assertIn("NoSpace", result)
    
    def test_no_actor_prefix(self):
        """Test string without actor prefix"""
        data = "JustAName"
        expected = ["JustAName"]
        self.assertEqual(parse_actors(data), expected)


if __name__ == "__main__":
    unittest.main()
