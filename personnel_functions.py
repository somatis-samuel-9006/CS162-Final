"""
This program contains functions for accessing the employee roster.

Each of these four functions will take all names from a corresponding text file and return a sorted
list of the names to be used in the main program file. The use of the sort function and the with open
file I/O structure will be useful here.

CS162 Final

Samuel Somatis
"""


def office_workers():
    """Read from a txt file, return a list where each element is one line."""
    try:
        off_list = []
        with open('office_workers.txt', 'r') as f:
            fr = f.readlines()
            for line in fr:
                off_list.append(line.strip('\n'))
        off_list.sort()

        return off_list

    except FileNotFoundError:
        print(f"Error: No such file or directory. Default file is 'office_workers.txt'")


def managers():
    """Read from a txt file, return a list where each element is one line."""
    try:
        man_list = []
        with open('managers.txt', 'r') as f:
            fr = f.readlines()
            for line in fr:
                man_list.append(line.strip('\n'))
        man_list.sort()

        return man_list

    except FileNotFoundError:
        print(f"Error: No such file or directory. Default file is 'managers.txt'")


def executives():
    """Read from a txt file, return a list where each element is one line."""
    try:
        exe_list = []
        with open('executives.txt', 'r') as f:
            fr = f.readlines()
            for line in fr:
                exe_list.append(line.strip('\n'))
        exe_list.sort()

        return exe_list

    except FileNotFoundError:
        print(f"Error: No such file or directory. Default file is 'executives.txt'")


def CEO():
    """Read from a txt file, return a list where each element is one line."""
    try:
        ceo_list = []
        with open('ceo.txt', 'r') as f:
            fr = f.readlines()
            for line in fr:
                ceo_list.append(line.strip('\n'))
        ceo_list.sort()

        return ceo_list

    except FileNotFoundError:
        print(f"Error: No such file or directory. Default file is 'ceo.txt'")
