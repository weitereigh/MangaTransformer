# test_mangatransformer.py
"""
Tests for MangaTransformer module.
"""

import unittest
from mangatransformer import MangaTransformer

class TestMangaTransformer(unittest.TestCase):
    """Test cases for MangaTransformer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaTransformer()
        self.assertIsInstance(instance, MangaTransformer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaTransformer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
