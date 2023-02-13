import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test for class state
    """
    def test_state_name_is_string(self):
        """
	Check that state name is string
	"""
        state = State()
        state.name = "Test state name"
        self.assertIsInstance(state.name, str)

if __name__ == '__main__':
    unittest.main()

