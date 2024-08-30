#!/usr/bin/env python3
""" 1-simple_pagination.py """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ set up and manipulate csv data"""
    startPage = (page - 1) * page_size
    endPage = page * page_size
    return (startPage, endPage)


class Server:
    """ class server """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached data """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get Page """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
