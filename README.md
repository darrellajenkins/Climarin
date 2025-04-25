# Climarin Tests

This repository contains tests for the Climarin game, focusing on the core functionality in `core.py`.

## Test Structure

The tests are organized as follows:

- `test_core.py`: Contains unit tests for the functions and game flow in `core.py`
- `run_tests.py`: A script to run the tests and log the results

## Logging

The tests use the Python logging module to record test execution and results. Logs are written to:

- `test_core.log`: Contains detailed logs from the test execution
- `test_runner.log`: Contains logs from the test runner

The logging is configured to:
- Write logs to both files and the console
- Include timestamps, logger names, and log levels
- Use DEBUG level for detailed information and INFO level for general execution flow

## Running the Tests

To run the tests, execute the `run_tests.py` script:

```
python run_tests.py
```

This will:
1. Run all the tests in `test_core.py`
2. Display the results in the console
3. Write detailed logs to the log files
4. Exit with status code 0 if all tests pass, or 1 if any tests fail

## Test Coverage

The tests cover the following aspects of `core.py`:

1. Character selection functions:
   - `player_1()`: Tests for all character types (Warrior, Monster, Sorcerer, Sage)
   - `player_2()`: Tests for all character types (Warrior, Monster, Sorcerer, Sage)
   - Invalid input handling for both functions

2. Game flow:
   - Play option: Tests character moves and special abilities
   - Stop option: Tests score display
   - Quit option: Tests game termination

3. Variables:
   - `field` variable: Tests the content and length

## Mocking

The tests use `unittest.mock` to:
- Mock user input to simulate different user choices
- Mock character objects to avoid dependencies on the actual character classes
- Wrap functions to test recursive calls
- Capture stdout to test printed output

## Adding More Tests

To add more tests:
1. Add new test methods to the `TestCore` class in `test_core.py`
2. Follow the existing pattern of using appropriate logging and mocking
3. Run the tests to verify they pass