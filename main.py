#!/usr/bin/env python3

import argparse

import pandas as pd

from scraper import DoubanParser

parse = argparse.ArgumentParser(description="This is a script for scraping douban user's collections")
parse.add_argument("uid", help="UID of the target user")
parse.add_argument("-c", "--sec", dest="section", help="The section of collections, can be movie, book or game.",
                   default="movie")
parse.add_argument("-s", "--status", help="The status of collections, can be do, wish or collect.",
                   default=["do", "wish", "collect"])
args = parse.parse_args()

if __name__ == "__main__":
    # TODO: change to sys argv
    uid = args.uid
    section = args.section
    status = args.status
    print(f"Start to read user_{uid}'s {section} in {status} ...")
    douban_parser = DoubanParser(uid)
    for s in status:
        resp = douban_parser.parse_page(section, s)
        if resp is None:
            print(f"{section}/{s} page is empty!")
            continue
        catalog = pd.DataFrame(resp)
        catalog.to_csv(f"{section}_{s}.csv", index=False)
