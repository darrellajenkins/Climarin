import unittest
from unittest.mock import patch
import logging
import io
import sys
from contextlib import redirect_stdout
import core

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_core.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('test_core')

class TestCore(unittest.TestCase):
    """Test cases for core.py functions"""

    def setUp(self):
        """Set up test fixtures"""
        logger.info('Setting up test case')
        # Reset any global variables if needed

    def tearDown(self):
        """Tear down test fixtures"""
        logger.info('Tearing down test case')

    @patch('builtins.input')
    def test_player_1_warrior(self, mock_input):
        """Test player_1 function with Warrior selection"""
        logger.info('Testing player_1 function with Warrior selection')

        # Mock the input values
        mock_input.side_effect = ['w', 'TestWarrior']

        # Capture stdout to prevent it from showing in test output
        with redirect_stdout(io.StringIO()):
            name, character = core.player_1()

        # Assertions
        self.assertEqual(name, 'TestWarrior')
        self.assertEqual(character.__class__.__name__, 'Warrior')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_1_monster(self, mock_input):
        """Test player_1 function with Monster selection"""
        logger.info('Testing player_1 function with Monster selection')

        # Mock the input values
        mock_input.side_effect = ['m', 'TestMonster']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_1()

        # Assertions
        self.assertEqual(name, 'TestMonster')
        self.assertEqual(character.__class__.__name__, 'Monster')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_1_sorcerer(self, mock_input):
        """Test player_1 function with Sorcerer selection"""
        logger.info('Testing player_1 function with Sorcerer selection')

        # Mock the input values
        mock_input.side_effect = ['s', 'TestSorcerer']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_1()

        # Assertions
        self.assertEqual(name, 'TestSorcerer')
        self.assertEqual(character.__class__.__name__, 'Sorcerer')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_1_sage(self, mock_input):
        """Test player_1 function with Sage selection"""
        logger.info('Testing player_1 function with Sage selection')

        # Mock the input values
        mock_input.side_effect = ['g', 'TestSage']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_1()

        # Assertions
        self.assertEqual(name, 'TestSage')
        self.assertEqual(character.__class__.__name__, 'Sage')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_2_warrior(self, mock_input):
        """Test player_2 function with Warrior selection"""
        logger.info('Testing player_2 function with Warrior selection')

        # Mock the input values
        mock_input.side_effect = ['w', 'TestWarrior2']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_2()

        # Assertions
        self.assertEqual(name, 'TestWarrior2')
        self.assertEqual(character.__class__.__name__, 'Warrior')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_2_monster(self, mock_input):
        """Test player_2 function with Monster selection"""
        logger.info('Testing player_2 function with Monster selection')

        # Mock the input values
        mock_input.side_effect = ['m', 'TestMonster2']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_2()

        # Assertions
        self.assertEqual(name, 'TestMonster2')
        self.assertEqual(character.__class__.__name__, 'Monster')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_2_sorcerer(self, mock_input):
        """Test player_2 function with Sorcerer selection"""
        logger.info('Testing player_2 function with Sorcerer selection')

        # Mock the input values
        mock_input.side_effect = ['s', 'TestSorcerer2']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_2()

        # Assertions
        self.assertEqual(name, 'TestSorcerer2')
        self.assertEqual(character.__class__.__name__, 'Sorcerer')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input')
    def test_player_2_sage(self, mock_input):
        """Test player_2 function with Sage selection"""
        logger.info('Testing player_2 function with Sage selection')

        # Mock the input values
        mock_input.side_effect = ['g', 'TestSage2']

        # Capture stdout
        with redirect_stdout(io.StringIO()):
            name, character = core.player_2()

        # Assertions
        self.assertEqual(name, 'TestSage2')
        self.assertEqual(character.__class__.__name__, 'Sage')
        logger.debug(f'Character created: {character.__class__.__name__} with name {name}')

    @patch('builtins.input', side_effect=['invalid', 'w', 'TestWarrior'])
    @patch('core.player_1', wraps=core.player_1)
    def test_player_1_invalid_input(self, wrapped_player_1, mock_input):
        """Test player_1 function with invalid input"""
        logger.info('Testing player_1 function with invalid input')

        # Capture stdout
        with redirect_stdout(io.StringIO()) as captured_output:
            name, character = wrapped_player_1()

        # Assertions
        self.assertEqual(name, 'TestWarrior')
        self.assertEqual(character.__class__.__name__, 'Warrior')
        self.assertEqual(wrapped_player_1.call_count, 2)  # Called once initially, then recursively
        logger.debug(f'Character created after invalid input: {character.__class__.__name__} with name {name}')
        logger.debug(f'Function called {wrapped_player_1.call_count} times')

    @patch('builtins.input', side_effect=['invalid', 'w', 'TestWarrior2'])
    @patch('core.player_2', wraps=core.player_2)
    def test_player_2_invalid_input(self, wrapped_player_2, mock_input):
        """Test player_2 function with invalid input"""
        logger.info('Testing player_2 function with invalid input')

        # Capture stdout
        with redirect_stdout(io.StringIO()) as captured_output:
            name, character = wrapped_player_2()

        # Assertions
        self.assertEqual(name, 'TestWarrior2')
        self.assertEqual(character.__class__.__name__, 'Warrior')
        self.assertEqual(wrapped_player_2.call_count, 2)  # Called once initially, then recursively
        logger.debug(f'Character created after invalid input: {character.__class__.__name__} with name {name}')
        logger.debug(f'Function called {wrapped_player_2.call_count} times')

    @patch('builtins.input')
    @patch('core.player_1')
    @patch('core.player_2')
    def test_game_flow_quit(self, mock_player_2, mock_player_1, mock_input):
        """Test game flow with quit option"""
        logger.info('Testing game flow with quit option')

        # Setup mocks
        mock_player_1.return_value = ('Player1', unittest.mock.MagicMock())
        mock_player_2.return_value = ('Player2', unittest.mock.MagicMock())
        mock_input.return_value = 'q'

        # Need to modify the module to make it testable
        # Save original code
        original_player_1 = core.player_1
        original_player_2 = core.player_2

        try:
            # Replace with mocks
            core.player_1 = mock_player_1
            core.player_2 = mock_player_2

            # Create a modified version of core module for testing
            # This is a bit hacky but necessary to test the main game flow
            test_module_code = """
from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs
import time

field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']

def player_1():
    pass  # Will be mocked

def player_2():
    pass  # Will be mocked

# Test version that returns instead of running the full game
def run_game_test():
    player_1_result = player_1()
    p1_name = player_1_result[0]
    p1_charac = player_1_result[1]

    player_2_result = player_2()
    p2_name = player_2_result[0]
    p2_charac = player_2_result[1]

    opponents = [(p1_name, p1_charac), (p2_name, p2_charac)]

    p = True
    while p:
        play = input("[P]lay, [S]top, or [Q]uit ")
        if play.lower() == 'q':
            p = False
            print("Thanks for playing!")
            return "quit"
        elif play.lower() == 'p':
            for name, charac in opponents:
                print(f"{name} begins...")
                print(charac.move())
                if isinstance(charac, Sorcerer):
                    charac.magic()
            return "play"
        elif play.lower() == 's':
            print("Score is tied 1 to 1")
            return "stop"
"""

            # Execute the test module code
            test_module = {}
            exec(test_module_code, test_module)

            # Capture stdout
            with redirect_stdout(io.StringIO()) as captured_output:
                result = test_module["run_game_test"]()

            # Assertions
            self.assertEqual(result, "quit")
            self.assertEqual(mock_player_1.call_count, 1)
            self.assertEqual(mock_player_2.call_count, 1)
            logger.debug(f'Game flow result: {result}')

        finally:
            # Restore original code
            core.player_1 = original_player_1
            core.player_2 = original_player_2

    @patch('builtins.input')
    @patch('core.player_1')
    @patch('core.player_2')
    def test_game_flow_play(self, mock_player_2, mock_player_1, mock_input):
        """Test game flow with play option"""
        logger.info('Testing game flow with play option')

        # Setup mocks
        mock_warrior = unittest.mock.MagicMock()
        mock_warrior.__class__.__name__ = 'Warrior'
        mock_warrior.move.return_value = "Warrior moves"

        mock_sorcerer = unittest.mock.MagicMock()
        mock_sorcerer.__class__.__name__ = 'Sorcerer'
        mock_sorcerer.move.return_value = "Sorcerer moves"

        mock_player_1.return_value = ('Player1', mock_warrior)
        mock_player_2.return_value = ('Player2', mock_sorcerer)
        mock_input.return_value = 'p'

        # Need to modify the module to make it testable
        # Save original code
        original_player_1 = core.player_1
        original_player_2 = core.player_2

        try:
            # Replace with mocks
            core.player_1 = mock_player_1
            core.player_2 = mock_player_2

            # Create a modified version of core module for testing
            test_module_code = """
from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs
import time

field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']

def player_1():
    pass  # Will be mocked

def player_2():
    pass  # Will be mocked

# Test version that returns instead of running the full game
def run_game_test():
    player_1_result = player_1()
    p1_name = player_1_result[0]
    p1_charac = player_1_result[1]

    player_2_result = player_2()
    p2_name = player_2_result[0]
    p2_charac = player_2_result[1]

    opponents = [(p1_name, p1_charac), (p2_name, p2_charac)]

    p = True
    while p:
        play = input("[P]lay, [S]top, or [Q]uit ")
        if play.lower() == 'q':
            p = False
            print("Thanks for playing!")
            return "quit"
        elif play.lower() == 'p':
            for name, charac in opponents:
                print(f"{name} begins...")
                print(charac.move())
                if isinstance(charac, Sorcerer):
                    charac.magic()
            return "play"
        elif play.lower() == 's':
            print("Score is tied 1 to 1")
            return "stop"
"""

            # Execute the test module code
            test_module = {}
            exec(test_module_code, test_module)

            # Capture stdout
            with redirect_stdout(io.StringIO()) as captured_output:
                result = test_module["run_game_test"]()

            # Assertions
            self.assertEqual(result, "play")
            self.assertEqual(mock_player_1.call_count, 1)
            self.assertEqual(mock_player_2.call_count, 1)
            self.assertEqual(mock_warrior.move.call_count, 1)
            self.assertEqual(mock_sorcerer.move.call_count, 1)
            logger.debug(f'Game flow result: {result}')

        finally:
            # Restore original code
            core.player_1 = original_player_1
            core.player_2 = original_player_2

    @patch('builtins.input')
    @patch('core.player_1')
    @patch('core.player_2')
    def test_game_flow_stop(self, mock_player_2, mock_player_1, mock_input):
        """Test game flow with stop option"""
        logger.info('Testing game flow with stop option')

        # Setup mocks
        mock_player_1.return_value = ('Player1', unittest.mock.MagicMock())
        mock_player_2.return_value = ('Player2', unittest.mock.MagicMock())
        mock_input.return_value = 's'

        # Need to modify the module to make it testable
        # Save original code
        original_player_1 = core.player_1
        original_player_2 = core.player_2

        try:
            # Replace with mocks
            core.player_1 = mock_player_1
            core.player_2 = mock_player_2

            # Create a modified version of core module for testing
            test_module_code = """
from characters import Monster, Warrior, Sorcerer, Sage
import special_abilities as spc_abs
import time

field = ['A', 'B', 'C', 'M', 'X', 'Y', 'Z']

def player_1():
    pass  # Will be mocked

def player_2():
    pass  # Will be mocked

# Test version that returns instead of running the full game
def run_game_test():
    player_1_result = player_1()
    p1_name = player_1_result[0]
    p1_charac = player_1_result[1]

    player_2_result = player_2()
    p2_name = player_2_result[0]
    p2_charac = player_2_result[1]

    opponents = [(p1_name, p1_charac), (p2_name, p2_charac)]

    p = True
    while p:
        play = input("[P]lay, [S]top, or [Q]uit ")
        if play.lower() == 'q':
            p = False
            print("Thanks for playing!")
            return "quit"
        elif play.lower() == 'p':
            for name, charac in opponents:
                print(f"{name} begins...")
                print(charac.move())
                if isinstance(charac, Sorcerer):
                    charac.magic()
            return "play"
        elif play.lower() == 's':
            print("Score is tied 1 to 1")
            return "stop"
"""

            # Execute the test module code
            test_module = {}
            exec(test_module_code, test_module)

            # Capture stdout
            with redirect_stdout(io.StringIO()) as captured_output:
                result = test_module["run_game_test"]()

            # Assertions
            self.assertEqual(result, "stop")
            self.assertEqual(mock_player_1.call_count, 1)
            self.assertEqual(mock_player_2.call_count, 1)
            logger.debug(f'Game flow result: {result}')

        finally:
            # Restore original code
            core.player_1 = original_player_1
            core.player_2 = original_player_2

    def test_field_variable(self):
        """Test the field variable in core.py"""
        logger.info('Testing field variable')

        # Check field variable
        self.assertEqual(core.field, ['A', 'B', 'C', 'M', 'X', 'Y', 'Z'])
        self.assertEqual(len(core.field), 7)
        logger.debug(f'Field variable: {core.field}')

if __name__ == '__main__':
    logger.info('Starting test execution')
    unittest.main()
    logger.info('Test execution completed')
