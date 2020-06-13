from bs4 import BeautifulSoup


def page_number(html):
    soup = BeautifulSoup(html, "lxml")
    paginator = soup.find("div", class_="paginator")
    if paginator is None:
        return 0
    return int(paginator.find_all("a")[-2].text)


def parse_text(bs4_tag, option=None):
    if option == "title":
        return bs4_tag.text.strip().split("\n")[0]
    return bs4_tag.text.strip()


def parse_rating(rating_tag):
    tags = rating_tag.find_all("span")
    star, record_time, movie_tag = None, None, None
    for t in tags:
        val = t.attrs["class"][0]
        if val.startswith("rating"):
            star = int(val[6])
        if val == "date":
            record_time = t.text
        if val == "tags":
            movie_tag = t.text[4:].split(" ")
    return star, record_time, movie_tag


def parse_movie_page(html):
    """
    :param html:
    :return: list of items if the page is not empty, otherwise return None value.
    """
    soup = BeautifulSoup(html, 'lxml')
    content = []
    listing = soup.find("div", class_="grid-view")
    items = listing.find_all("div", class_="item")
    if len(items) == 0:
        return None
    for m in items:
        comp = [res for res in m.find_all("li")]
        if len(comp) == 4:
            title, cast, ratings, comment = comp
        elif len(comp) == 3:
            title, cast, ratings = comp
            comment = None
        else:
            print("one entry seems to be weird ...")
            continue
        link = title.find("a")["href"]
        title = parse_text(title, option="title")
        # TODO: parse more specific cast info
        cast = parse_text(cast)
        star, rec, tag = parse_rating(ratings)
        if comment is not None:
            comment = parse_text(comment)
        item = {
            "link": link,
            "title": title,
            "cast": cast,
            "tag": tag,
            "date": rec,
            "star": star,
            "comment": comment
        }
        content.append(item)
    return content


def parse_book_page(html):
    """
    parse douban book page
    :param html: html text format page
    :return: a list of items, each item is a key-value map
    """
    content = []
    return content


def parse_game_page(html):
    """
    parse douban game page
    :param html: html text format page
    :return: a list of items, each item is a key-value map
    """
    # TODO: implement parse_game_page
    content = []
    return content