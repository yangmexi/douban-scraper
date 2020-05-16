import pandas as pd

from scraper import DoubanPaser

if __name__ == "__main__":
    # TODO: change to sys argv
    uid = "35086050"
    status = "collect"
    douban_parser = DoubanPaser(uid)
    resp = douban_parser.parse_movies(status)
    movies = pd.DataFrame(resp)
    movies.to_csv(f"movies_{status}.csv", index=False)