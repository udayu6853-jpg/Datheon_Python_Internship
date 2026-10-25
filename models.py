
from datetime import datetime
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, item_id, title, price):
        self.__item_id = item_id
        self.__title = title
        self.__price = price
        self.__is_checked_out = False
        self.__borrow_date = None

    @property
    def item_id(self):
        return self.__item_id

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @property
    def is_checked_out(self):
        return self.__is_checked_out

    @property
    def borrow_date(self):
        return self.__borrow_date

    def checkout(self):
        if self.__is_checked_out:
            raise ValueError(
                f"'{self.title}' is already checked out."
            )

        self.__is_checked_out = True
        self.__borrow_date = datetime.now()

    def return_item(self):
        if not self.__is_checked_out:
            raise ValueError(
                f"'{self.title}' is not checked out."
            )

        self.__is_checked_out = False
        self.__borrow_date = None

    @abstractmethod
    def calculate_fee(self, days=1):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    def __str__(self):
        status = (
            "Checked Out"
            if self.is_checked_out
            else "Available"
        )
        return f"{self.title} (ID: {self.item_id}) - {status}"

    def __len__(self):
        return len(self.title)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"item_id={self.item_id!r}, "
            f"title={self.title!r}, "
            f"price={self.price!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.item_id == other.item_id


class Book(LibraryItem):
    def __init__(self, item_id, title, price, author, pages):
        super().__init__(item_id, title, price)
        self.author = author
        self.pages = pages

    def calculate_fee(self, days=1):
        return max(days, 0) * 2.0

    def display_metadata(self):
        return (
            f"Book | Author: {self.author} | "
            f"Pages: {self.pages}"
        )


class Magazine(LibraryItem):
    def __init__(self, item_id, title, price, issue_number):
        super().__init__(item_id, title, price)
        self.issue_number = issue_number

    def calculate_fee(self, days=1):
        return max(days, 0) * 1.0

    def display_metadata(self):
        return f"Magazine | Issue: {self.issue_number}"


class DigitalMedia(LibraryItem):
    def __init__(
        self, item_id, title, price, file_format, file_size_mb
    ):
        super().__init__(item_id, title, price)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def calculate_fee(self, days=1):
        return max(days, 0) * 0.5

    def display_metadata(self):
        return (
            f"Digital Media | Format: {self.file_format} | "
            f"Size: {self.file_size_mb} MB"
        )
