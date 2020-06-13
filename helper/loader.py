import time
import logging
import requests
from requests.exceptions import RequestException

import conf

logging.basicConfig(level=logging.DEBUG,
                   datefmt='%Y/%m/%d %H:%M:%S',
                   format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)


def gen_url(uid, category, status, page):
    # TODO: change para to ENUM?
    if category not in ["movie", "book", "game"]:
        raise ValueError("[Error] Wrong category!")
    if status not in ["collect", "wish", "do"]:
        raise ValueError("[Error] Wrong status!")

    postfix = ""
    if page != 0:
        postfix = f"?start={(page)*conf.ITEM_PER_PAGE}"

    if category == "movie":
        return f"https://movie.douban.com/people/{uid}/{status}" + postfix
    if category == "book":
        return f"https://book.douban.com/people/{uid}/{status}" + postfix
    if category == "game":
        return f"https://www.douban.com/people/{uid}/games?action={status}" + postfix


def page(url, s=None):
    time.sleep(conf.SLEEP_TIME)
    try:
        resp = requests.get(url, headers=conf.HEADER)
        if resp.status_code == 200:
            return resp
        return None
    except RequestException:
        print(f"Failed to load page: {url}")
        return None


def content(uid, category, status, num_page):
    p = gen_url(uid, category, status, num_page)
    html = page(p).text
    logging.info(f"Loading page {p}")
    return html
