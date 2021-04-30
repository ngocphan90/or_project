def main():
    """some scripts to run."""


class LibraryItem:
    """
      Class that initializes the id and title of a library item. Holds the check out date and requested date
      if they is any. Also holds the location of the item and the ability to get it.
     """

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = 'ON_SHELF'
        self._date_checked_out = None
        self._requested_by = None
        self._checked_out_by = None

    def get_library_item_id(self):
        return self._library_item_id

    def get_title(self):
        return self._title

    def get_location(self):
        return self._location

    def set_location(self, new_location):
        self._location = new_location

    def get_date_checked_out(self):
        return self._date_checked_out

    def get_requested_by(self):
        return self._requested_by

    def get_checked_out_by(self):
        return self._checked_out_by

    def set_checked_out_by(self, new_check_out):
        self._checked_out_by = new_check_out

    def set_date_checked_out(self, current_library_date):
        self._date_checked_out = current_library_date

    def set_requested_by(self, patron):
        self._requested_by = patron


class Book(LibraryItem):
    """
    This is a book library item class that includes the author of the book and the number of
     days it can be checked out.
     """

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_author(self):
        return self._author

    def get_check_out_length(self):
        return self._check_out_length


class Patron:
    """
    This class is for the patrons of the library. It takes an id and name. Includes any fines the patron may owe
     or items they have checked out.
    """

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self, ):
        return self._patron_id

    def get_name(self):
        return self._name

    def get_fine_amount(self):
        return self._fine_amount

    def get_checked_out_items(self):
        return self._checked_out_items

    def add_library_item(self, item_id):
        """Adds library item to the patrons checked out items"""
        self._checked_out_items.append(item_id)

    def remove_library_item(self, item_id):
        """Removes library item from checked out items."""
        self._checked_out_items.remove(item_id)

    def amend_fine(self, dollar_amount):
        """Adds to patrons fine amount or subtracts from it."""
        self._fine_amount += dollar_amount


class Library:
    """
    This class functions as the library. It has a collection of the library items and a list of patron members.
    The library is able to search items or members. It functions to check out and return items for patrons and also to
    pay any fines the patron owes. Patrons are also able to put in requests for items through the library.
    """

    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
