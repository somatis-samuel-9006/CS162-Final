import pytest
from Employee_Manager import *
import personnel_functions
off = personnel_functions.office_workers()
man = personnel_functions.managers()
exe = personnel_functions.executives()
ceo = personnel_functions.CEO()


def test_get_office_personnel(capsys):
	OfficeWorker.get_personnel()
	captured = capsys.readouterr()
	assert captured.out == "Elisabeth Eliseus\nHerta Mathilda\nMeliton Hartwig\nStraton Herminia\nTalya Algirdas\nTekoa Margarita\n"

def test_get_manager_personnel(capsys):
	Manager.get_personnel()
	captured = capsys.readouterr()
	assert captured.out == "Neelima Eva\nPatrick Renza\nUliana Herman\nVeronika Timur\n"

def test_get_executive_personnel(capsys):
	Executive.get_personnel()
	captured = capsys.readouterr()
	assert captured.out == "Ivan Ami\nMichaela Arne\nVasia Nirmala\n"

def test_get_CEO_personnel(capsys):
	CEO.get_personnel()
	captured = capsys.readouterr()
	assert captured.out == "Govannon Simon\n"

def test_no_pay(capsys):
	OfficeWorker.pay(0)
	captured = capsys.readouterr()
	assert captured.out == "With 0 hours they will earn nothing\n"

def test_office_pay(capsys):
	OfficeWorker.pay(5)
	captured = capsys.readouterr()
	assert captured.out == "With 5 hours, an office worker will earn $76.85\n"

def test_manager_pay(capsys):
	Manager.pay(5)
	captured = capsys.readouterr()
	assert captured.out == "With 5 hours, a manager will earn $87.35\n"

def test_executive_pay(capsys):
	Executive.pay(5)
	captured = capsys.readouterr()
	assert captured.out == "With 5 years, an executive will earn $657685\n"

def test_CEO_pay(capsys):
	CEO.pay(5)
	captured = capsys.readouterr()
	assert captured.out == "With 5 years, a CEO will earn $868165\n"

def test_office_worker_promote(capsys):
	OfficeWorker.promote("Elisabeth Eliseus")
	Manager.get_personnel()
	captured = capsys.readouterr()
	assert captured.out == "Elisabeth Eliseus\nNeelima Eva\nPatrick Renza\nUliana Herman\nVeronika Timur\n"

def test_alphabetical_swap(capsys):
	OfficeWorker.hire("zz")
	OfficeWorker.get_personnel()
	captured = capsys.readouterr()
	assert captured.out == "Herta Mathilda\nMeliton Hartwig\nStraton Herminia\nTalya Algirdas\nTekoa Margarita\nzz\n" 
