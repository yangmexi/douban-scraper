import sys

import pandas as pd

from scraper import DoubanParser

if __name__ == "__main__":
    # TODO: change to sys argv
    uid = "35086050"
    section = "movie"
    status = ["do", "wish", "collect"]
    douban_parser = DoubanParser(uid)
    for s in status:
        resp = douban_parser.parse_page(section, s)
        if resp is None:
            print(f"{s}_{section} page is empty!")
            continue
        catalog = pd.DataFrame(resp)
        catalog.to_csv(f"{section}_{s}.csv", index=False)