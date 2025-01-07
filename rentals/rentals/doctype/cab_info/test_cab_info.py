# Copyright (c) 2025, praveen and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestCabInfo(UnitTestCase):
	"""
	Unit tests for CabInfo.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestCabInfo(IntegrationTestCase):
	"""
	Integration tests for CabInfo.
	Use this class for testing interactions between multiple components.
	"""

	pass
