"""
This program allows the user to view and manage a roster of various employees.

This program is an employee manager. It will load in, from text files, lists of all the employees in four
different positions: office worker, manager, executive, and CEO. Each position is made into its own class,
which is a subclass of a base employee class. The user will have the ability to print info about each employee,
promote them, demote them, and fire them. They will also be able to hire new employees. For simplicity, there is
a lack of instance methods. This is so the user can view and edit, or 'manage' employee info by directly calling
each method instead of having to create class instances each time they wanted to perform an action on a certain
employee. This program also contains recursion for randomly generating an employee name for promotion, and the
use of the prettytable module to create a table in a text file of all the current employees.

CS 162 Final

Samuel Somatis
"""


import random
from prettytable import PrettyTable
import personnel_functions

# Initialization
off = personnel_functions.office_workers()
man = personnel_functions.managers()
exe = personnel_functions.executives()
ceo = personnel_functions.CEO()


class Employee:
    """Base class containing methods that pertain to all employee types. Parent to all other employee classes."""

    def __init__(self, name):
        """Initialize the class. Each instance should have a name."""
        self.name = name

    @classmethod
    def suggested_promotion(cls, n):
        """
        Suggest an employee to promote.

        This function will check if a list has only one element, if not, it will pop an element out
        and call itself to again check if the length is now one. It will continue until the length is
        one, and it will print that element as the suggested employee.

        Parameters
        ----------
        n : list
            A list of employee names.

        Prints
        ------
        str
            A string containing the randomly chosen element.

        """
        try:
            copy = n.copy()
            if len(copy) == 0:
                print("Error: No employee names given")

            elif len(copy) == 1:
                print(f'Suggested Employee: {copy[0]}')

            else:
                x = random.randint(0, len(copy)-1)
                copy.pop(x)
                cls.suggested_promotion(copy)

        except AttributeError:
            print("Call with list only")

    def table_maker():
        """
        Create a table of all current employees.

        Make a copy of each of the four lists being used. After checking that all elements in each are
        strings, this function will find the length of the largest list, and append empty strings to
        every other list until they are the same length as the largest. Each list is then iterated over
        and appended as rows into a table. This table is written to a text file.
        """
        try:
            off_copy = off.copy()
            man_copy = man.copy()
            exe_copy = exe.copy()
            ceo_copy = ceo.copy()
            list_of_lists = [off_copy, man_copy, exe_copy, ceo_copy]

            for i in list_of_lists:
                for j in i:
                    if type(j) == str:
                        continue
                    else:
                        raise ValueError('All elements must be strings')

            row_num = max(len(off_copy), len(man_copy),
                          len(exe_copy), len(ceo_copy))
            for i in list_of_lists:
                if len(i) != row_num:
                    diff = row_num - len(i)
                    for j in range(diff):
                        i.append('')

            t = PrettyTable(
                ['Office Workers', 'Managers', 'Executives', 'CEO'])
            for i in range(row_num):
                t.add_row([off_copy[i], man_copy[i], exe_copy[i], ceo_copy[i]])

            with open('Employee Table.txt', 'w') as f:
                f.write(str(t))

        except FileNotFoundError:
            print("Error: No file entered")


class OfficeWorker(Employee):
    """Class containg all methods related to managing office workers."""
    
    def get_personnel():
        """Iterate through office workers list, prints each element as a string."""
        if len(off) == 0:
            print("There are no office workers")
        else:
            for i in off:
                print(str(i))

    def pay(hours):
        """
        Given the hours, calculates the amount this employee type will earn.

        Parameters
        ----------
        hours: int or float

        Prints
        ------
        str
            A string containg the calculated income.

        """
        try:
            hourly = 15.37
            if hours == 0:
                print("With 0 hours they will earn nothing")
            elif hours == 1:
                print(f"The hourly rate for an office worker is ${hourly}")
            else:
                print(f"With {hours} hours, an office worker will earn ${hourly*hours:.2f}")

        except TypeError:
            print("Error: Call with integers only")

    def promote(name):
        """Move name from office workers list to managers list, provided name is in the office workers list."""
        try:
            if name in off:
                off.remove(name)
                man.append(name)
                man.sort()
            else:
                print(f"{name} cannot be promoted from an office worker, as they are not in the personnel list")

        except TypeError:
            print("Error: Call with strings only")

    def demote(name):
        """Print a message that an office worker cannot be demoted."""
        print('Office Worker is the lowest position')

    def hire(name):
        """Append a name into the office workers list."""
        try:
            off.append(name)
            off.sort()

        except TypeError:
            print("Call with strings only")

    def fire(name):
        """Remove a name from the office workers lists, provided the name is in the office workers list."""
        try:
            if name in off:
                off.remove(name)
            else:
                print(f"Error: {name} not found in personnel list")

        except TypeError:
            print("Error: Call with strings only")


class Manager(Employee):
    """Class containing all methods related to managing managers."""
    
    def get_personnel():
        """Iterate through managers list, prints each element as a string."""
        if len(man) == 0:
            print("There are no managers")
        else:
            for i in man:
                print(str(i))

    def pay(hours):
        """
        Given the hours, calculates the amount this employee type will earn.

        Parameters
        ----------
        hours: int or float

        Prints
        ------
        str
            A string containg the calculated income.

        """
        try:
            hourly = 17.47
            if hours == 0:
                print("With 0 hours, they will earn nothing")
            elif hours == 1:
                print(f"The hourly rate for a manager is ${hourly}")
            else:
                print(f"With {hours} hours, a manager will earn ${hourly*hours:.2f}")

        except TypeError:
            print("Error: Call with integers only")

    def promote(name):
        """Move name from managers list to executives list, provided name is in the managers list."""
        try:
            if name in man:
                man.remove(name)
                exe.append(name)
                exe.sort()
            else:
                print(f"{name} cannot be promoted from a manager, as they are not in the personnel list")

        except TypeError:
            print("Error: Call with strings only")

    def demote(name):
        """Move name from managers list to office workers list, provided name is in the managers list."""
        try:
            if name in man:
                man.remove(name)
                off.append(name)
                off.sort()
            else:
                print(f"{name} cannot be demoted from a manager as they are not in the personnel list")

        except TypeError:
            print("Error: Call with strings only")

    def hire(name):
        """Append a name to the managers list."""
        try:
            man.append(name)
            man.sort()

        except TypeError:
            print("Error: Call with strings only")

    def fire(name):
        """Remove a name from the managers list, provided the name is in the managers list."""
        try:
            if name in man:
                man.remove(name)
            else:
                print(f"Error: {name} not found in personnel list")

        except TypeError:
            print("Error: Call with strings only")


class Executive(Employee):
    """Class containing all methods related to managing executives."""
    
    def get_personnel():
        """Iterate through executives list, prints each element as a string."""
        if len(exe) == 0:
            print("There are no executives")
        else:
            for i in exe:
                print(str(i))

    def pay(years):
        """
        Given the years, calculates the amount this employee type will earn.

        Parameters
        ----------
        hours: int or float

        Prints
        ------
        str
            A string containg the calculated income.

        """
        try:
            salary = 131537
            if years == 0:
                print("In 0 years, they will earn nothing")
            elif years == 1:
                print(f"The annual salary for an executive is ${salary}")
            else:
                print(f"With {years} years, an executive will earn ${salary*years}")

        except TypeError:
            print("Call with integers only")

    def promote(name):
        """Move name from executive list to ceo list, provided name is in the executives list."""
        try:
            if name in exe:
                exe.remove(name)
                ceo.append(name)
                ceo.sort()
            else:
                print(f"{name} cannot be promoted from an executive, as they are not in the personnel list")

        except TypeError:
            print("Error: Call with strings only")

    def demote(name):
        """Move name from executives list to managers list, provided name is in the executives list."""
        try:
            if name in exe:
                exe.remove(name)
                man.append(name)
                man.sort()
            else:
                print(f"{name} cannot be demoted from an executive, as they are not in the personnel list")

        except TypeError:
            print("Error: Call with strings only")

    def hire(name):
        """Append a name to the executives list."""
        try:
            exe.append(name)
            exe.sort()

        except TypeError:
            print("Error: Call with strings only")

    def fire(name):
        """Remove a name from the executives list, provided the name is in the executives list."""
        try:
            if name in exe:
                exe.remove(name)
            else:
                print(f"Error: {name} not  found in personnel list")

        except TypeError:
            print("Error: Call with strings only")


class CEO(Employee):
    """Class containing all methods related to managing CEO(s)."""
    
    def get_personnel():
        """Iterate through ceo list, prints each element as a string."""
        if len(ceo) == 0:
            print("There are no CEO\'s")
        else:
            for i in ceo:
                print(str(i))

    def pay(years):
        """
        Given the years, calculates the amount this employee type will earn.

        Parameters
        ----------
        hours: int or float

        Prints
        ------
        str
            A string containg the calculated income.

        """
        try:
            salary = 173633
            if years == 0:
                print('In 0 years, they will earn nothing')
            elif years == 1:
                print(f"The annual salary for a CEO is ${salary}")
            else:
                print(f"With {years} years, a CEO will earn ${salary*years}")

        except TypeError:
            print("Call with integers only")

    def promote(name):
        """Print a message that the CEO cannot be promoted."""
        print('A CEO cannot be promoted')

    def demote(name):
        """Print a message that a CEO cannot be demoted."""
        print("A CEO cannot be demoted")

    def hire(name):
        """Print a message that a CEO cannot be hired."""
        print("A CEO cannot be hired outright")

    def fire(name):
        """Print a message that a CEO cannot be fired."""
        print('A CEO cannot be fired')
