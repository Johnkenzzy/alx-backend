#!/usr/bin/env python3
"""Defines index_range function"""


def index_range(page, page_size):
    """Return a tuple of size two containing start and end indexes"""
    pages = page_size * page
    return (pages - page_size), pages
