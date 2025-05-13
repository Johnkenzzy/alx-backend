#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Preserve pagination on dataset change
        """
        assert isinstance(page_size, int) and page_size > 0
        assert index is None or (isinstance(index, int) and index >= 0)
        dataset = self.indexed_dataset()
        total_items = len(dataset)

        if index is None:
            index = 0
        if index >= total_items:
            return {
                "index": index,
                "next_index": None,
                "page_size": 0,
                "data": []
                }

        start_index = index
        end_index = min(start_index + page_size, total_items)
        data = []
        for i in range(start_index, end_index):
            if i in dataset:
                data.append(dataset[i])
        next_index = end_index if end_index < total_items else None

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
