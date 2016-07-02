#!/usr/bin/env python

import unittest
import importlib

REQUIRE_DAY1 = ["numpy",
                'scipy',
                "pandas",
                "plotly",
                "sklearn",
                "jupyter"
               ]

REQUIRE_DAY2 = ["matplotlib",
                "theano",
                "keras",
                "cv2"
               ]

def generate_test(module, package=None):
    """ Generate a TestCase to be added to a testsuite
    @return Test function
    """
    def test_import(self):
        """ Try and import the named module, capture any failure
        @return True if the model is installed
        """
        try:
            if package is None:
                importlib.import_module(module)
            else:
                importlib.import_module(module, package)
        except ImportError as e:
            self.fail("%s is not installed" % module)

    return test_import

class RequirementCheck(unittest.TestCase):
    """ Check the requirements are installed
    """
    @classmethod
    def register(cls, name, module):
        """ Register a TestCase
        """
        setattr(cls, name, module)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    def add_tests(require, comment):
        """ Add a test
        """
        for requirement in require:
            RequirementCheck.register("test_%s" % requirement, generate_test(requirement))
        return None

    add_tests(REQUIRE_DAY1, "Day 1")
    add_tests(REQUIRE_DAY2, "Day 2")
    suite.addTest(unittest.makeSuite(RequirementCheck))
    def _error(error):
        """ Parse error
        """

        return [item[1].splitlines()[-1].split(':', 1)[-1].strip()  for item in error]
#item
    suite.run(result)
    if result.failures:
        failures = _error(result.failures)
        print "Failures: %s" % ", ".join(failures)
    if result.errors:
        errors = _error(result.errors)
        print "Error: %s" % ", ".join(errors)
    if len(result.errors)+len(result.failures) > 0: 
        "Errors"
        
