import time
import logging

from helper import loader, parser

logging.basicConfig(level=logging.DEBUG,
                   datefmt='%Y/%m/%d %H:%M:%S',
                   format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)


class DoubanPaser:
    def __init__(self, uid: str):
        """
        :param uid:
        :param categories:
        """
        self.poi = uid

    def parse_movies(self, status: str):
        if status not in ["collect", "wish", "do"]:
            raise ValueError("[Error] Wrong status!")

        # TODO: deal wth empty page
        s_values = []
        p = loader.content(self.poi, "movie", status, 0)
        num_page = parser.page_number(p)
        for n in range(0, num_page):
            logging.info(f"Loading page {n}")
            page_html = loader.content(self.poi, "movie", status, n)
            items = parser.parse_movie_page(page_html)
            s_values += items
        return s_values



