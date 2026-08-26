# test_zenweaver.py
"""
Tests for ZenWeaver module.
"""

import unittest
from zenweaver import ZenWeaver

class TestZenWeaver(unittest.TestCase):
    """Test cases for ZenWeaver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZenWeaver()
        self.assertIsInstance(instance, ZenWeaver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZenWeaver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
