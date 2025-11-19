import unittest
import tkinter as tk
from clicker import ClickerApp


class TestClickerApp(unittest.TestCase):
    """Test cases for the ClickerApp class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.root = tk.Tk()
        self.app = ClickerApp(self.root)

    def tearDown(self):
        """Clean up after each test method."""
        self.root.destroy()

    def test_initial_count(self):
        """Test that the counter starts at 0."""
        self.assertEqual(self.app.count.get(), 0)

    def test_increment(self):
        """Test that increment increases the count by 1."""
        initial_count = self.app.count.get()
        self.app.increment()
        self.assertEqual(self.app.count.get(), initial_count + 1)

    def test_multiple_increments(self):
        """Test multiple increments."""
        self.app.increment()
        self.app.increment()
        self.app.increment()
        self.assertEqual(self.app.count.get(), 3)

    def test_decrement(self):
        """Test that decrement decreases the count by 1."""
        self.app.count.set(5)
        self.app.decrement()
        self.assertEqual(self.app.count.get(), 4)

    def test_decrement_negative(self):
        """Test that decrement can go negative."""
        self.app.decrement()
        self.assertEqual(self.app.count.get(), -1)

    def test_reset(self):
        """Test that reset sets the count to 0."""
        self.app.count.set(10)
        self.app.reset()
        self.assertEqual(self.app.count.get(), 0)

    def test_reset_from_negative(self):
        """Test that reset works from negative values."""
        self.app.count.set(-5)
        self.app.reset()
        self.assertEqual(self.app.count.get(), 0)

    def test_increment_decrement_sequence(self):
        """Test a sequence of increment and decrement operations."""
        self.app.increment()  # 1
        self.app.increment()  # 2
        self.app.decrement()  # 1
        self.app.increment()  # 2
        self.assertEqual(self.app.count.get(), 2)


if __name__ == '__main__':
    unittest.main()
