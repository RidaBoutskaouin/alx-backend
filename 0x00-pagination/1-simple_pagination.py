#!/usr/bin/env python3
"""Simple helper function"""

from typing import Tuple, List
import csv


class Server:
    """Server class to paginate a database of popular baby names"""
    
        DATA_FILE = "Popular_Baby_Names.csv"
    
        def __init__(self):
            """Initialize the class"""
            self.__dataset = None
    
        def dataset(self) -> List[List]:
            """Read the dataset and return it"""
            if self.__dataset is None:
                with open(self.DATA_FILE, "r") as f:
                    reader = csv.reader(f)
                    self.__dataset = [row for row in reader]
            return self.__dataset
        
        @staticmethod
        def index_range(page: int, page_size: int) -> Tuple[int, int]:
            """Return a tuple of size two containing a start index and an end index"""
            return ((page - 1) * page_size, page * page_size)
    
        def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """Get the requested page"""
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0
            start, end = self.index_range(page, page_size)
            return self.dataset()[start:end]
