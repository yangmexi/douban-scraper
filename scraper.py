import time
import logging

from helper import loader, parser

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)


class DoubanParser:
    def __init__(self, uid: str):
        """
        :param uid:
        """
        self.poi = uid

    def parse_page(self, section: str, status: str):
        if status not in ["collect", "wish", "do"]:
            raise ValueError("[Error] Wrong status!")
        s_values = []
        p = loader.content(self.poi, section, status, 0)
        num_page = parser.page_number(p)
        if num_page == 0:
            num_page += 1
        for n in range(0, num_page):
            logging.info(f"Loading page {n}")
            page_html = loader.content(self.poi, section, status, n)
            if section == "movie":
                items = parser.parse_movie_page(page_html)
            elif section == "book":
                items = parser.parse_book_page(page_html)
            elif section == "game":
                items = parser.parse_game_page(page_html)
            else:
                raise ValueError("invalid douban section! should be 'movie', 'book' or 'game'")
            if items is None:
                return None
            s_values += items
        return s_values
