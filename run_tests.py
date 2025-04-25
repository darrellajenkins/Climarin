"""
Script to run the tests for core.py
"""
import unittest
import logging
import sys

# Configure logging for the test runner
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_runner.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('test_runner')

if __name__ == '__main__':
    logger.info('Starting test runner')
    
    # Import the test module
    import test_core
    
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromModule(test_core)
    
    # Run the tests
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Log the results
    logger.info(f'Tests run: {result.testsRun}')
    logger.info(f'Errors: {len(result.errors)}')
    logger.info(f'Failures: {len(result.failures)}')
    logger.info(f'Skipped: {len(result.skipped)}')
    
    # Print any errors or failures
    if result.errors:
        logger.error('Errors:')
        for test, error in result.errors:
            logger.error(f'{test}: {error}')
    
    if result.failures:
        logger.error('Failures:')
        for test, failure in result.failures:
            logger.error(f'{test}: {failure}')
    
    logger.info('Test runner completed')
    
    # Exit with appropriate status code
    sys.exit(not result.wasSuccessful())