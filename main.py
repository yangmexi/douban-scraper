#!/usr/bin/env python3

import argparse

import pandas as pd

from scraper import DoubanParser

parse = argparse.ArgumentParser(description="This is a script for scraping douban user's collections")
parse.add_argument("uid", help="UID of the target user")
parse.add_argument("-c", "--sec", dest="section", help="The section of collections, can be movie, book or game.",
                   default="movie")
parse.add_argument("-s", "--status", help="The status of collections, can be do, wish or collect.")
parse.add_argument("-n", "--name", help="The .csv file prefix", default="poi")
args = parse.parse_args()


def parse_and_save(uid, section, status, name):
    douban_parser = DoubanParser(uid)
    resp = douban_parser.parse_page(section, status)
    if resp is None:
        print(f"{section}/{status} page is empty!")
    else:
        catalog = pd.DataFrame(resp)
        catalog.to_csv(f"{name}_{section}_{status}.csv", index=False)


if __name__ == "__main__":
    uid = args.uid
    section = args.section
    if args.name is not None:
        name = args.name
    else:
        name = uid

    if args.status is not None:
        status = args.status
        print(f"Start to read user_{uid}'s {section} in {status} ...")
        parse_and_save(uid, section, status, name)
    else:
        status = ["collect", "wish", "do"]
        for s in status:
            print(f"Start to read user_{uid}'s {section} in {s} ...")
            parse_and_save(uid, section, s, name)