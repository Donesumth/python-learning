import pytest
from crawler import fetch_book_info
import csv

def test_fetch_book_info_valid_url():
    url = "https://book.douban.com/tag/小说"
    books = fetch_book_info(url)
    assert isinstance(books, list), "返回结果应为列表"
    assert len(books) > 0, "应抓取到图书数据"
    assert all("title" in book and "author" in book and "rating" in book for book in books), "每本书应包含必要字段"

def test_fetch_book_info_invalid_url():
    url = "https://book.douban.com/404"
    books = fetch_book_info(url)
    assert books == [], "无效 URL 应返回空列表"

def test_fetch_book_info_empty_url():
    url = ""
    books = fetch_book_info(url)
    assert books == [], "空 URL 应返回空列表"
