import pytest
import personnel_functions

def test_office_workers():
	test = personnel_functions.office_workers()
	assert type(test) == list
	assert min(test) == test[0]
	assert max(test) == test[-1]

def test_managers():
	test = personnel_functions.managers()
	assert type(test) == list
	assert min(test) == test[0]
	assert max(test) == test[-1]

def test_executives():
	test = personnel_functions.executives()
	assert type(test) == list
	assert min(test) == test[0]
	assert max(test) == test[-1]

def test_CEO():
	test = personnel_functions.CEO()
	assert type(test) == list
	assert min(test) == test[0]
	assert max(test) == test[-1]


