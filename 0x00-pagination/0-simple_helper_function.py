#!/usr/bin/env python3
""" 0-simple_helper_function.py """


def index_range(page: int, page_size: int) -> tuple:
    """ Set up indexPage & endPage """
    indexPage = (page - 1) * page_size
    endPage = page * page_size
    return (indexPage, endPage)
