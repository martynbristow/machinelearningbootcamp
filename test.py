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

def check_requirements(requirement, comment=""):
    """ x
    """
    if comment:
        print "Checking requirements: %s" % comment
    for require in requirement:
        print "Registering test for: %s" % require
        RequirementCheck.register("test_%s" % require, generate_test(require))
    #unittest.main()
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(RequirementCheck))
    #fooRunner = unittest.TextTestRunner()
    #fooRunner.run(suite)
    def _error(error):
        for issue in error:
            print issue[1]
    suite.run(result)
    if result.failures:
        _error(result.failures)
    if result.errors:
        _error(result.errors)
    if len(result.errors)+len(result.failures) > 0:
        print "Sorry "


if __name__ == "__main__":
    check_requirements(REQUIRE_DAY1, "Day 1")
    check_requirements(REQUIRE_DAY2, "Day 2")
