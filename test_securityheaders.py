# test_securityheaders.py
"""
Tests for SecurityHeaders module.
"""

import unittest
from securityheaders import SecurityHeaders

class TestSecurityHeaders(unittest.TestCase):
    """Test cases for SecurityHeaders class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SecurityHeaders()
        self.assertIsInstance(instance, SecurityHeaders)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SecurityHeaders()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
