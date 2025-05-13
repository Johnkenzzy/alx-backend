#!/usr/bin/env python3
"""Define Server class"""
import csv
import math
from typing import List, Tuple, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get items list of page range
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        list_range: Tuple[int] = index_range(page, page_size)
        self.dataset()
        if list_range[0] >= len(self.__dataset):
            return []

        return self.__dataset[list_range[0]:list_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get a dictionary containing pagination details
        """
        pages_list: List[List] = self.get_page(page, page_size)
        total_items: int = len(self.dataset())
        total_pages: int = math.ceil(total_items / page_size)
        next_page: int = page + 1 if page < total_pages else None
        prev_page: int = page - 1 if page > 1 else None

        return {
            "page_size": len(pages_list),
            "page": page,
            "data": pages_list,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
