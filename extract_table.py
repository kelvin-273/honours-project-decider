import bs4
import re
from functools import reduce

def get_soup(arg):
    return bs4.BeautifulSoup(open(arg), "lxml")

def unpad(s):
    return re.sub(r"^[ \r\n\t]*", "",
                  re.sub(r"[ \r\n\t]*$", "", s))

def unwhitespace(s):
    return re.sub(r"[ \r\n\t]", "", s)

def clean_supervisors(s):
    s = re.sub(r",? *& *(, )?", ", ", s)
    s = re.sub(r",? +and *(, )?", ", ", s)
    s = re.sub(r"\xa0", "", s)
    name = re.compile(r"([A-Za-z]+[-\. ]*)+(\(([A-Za-z]+[-\., ]*)+\))")
    s = re.findall(name, s)
    return s

def extract_table(filename):
    soup = bs4.BeautifulSoup(open(filename), "lxml")
    [thead, tbody] = soup.find("table").children
    header = [unpad(i.text) for i in thead.find_all("th")]
    rows = [[unpad(j.text) for j in i.find_all("td")] for i in tbody.find_all("tr")]
    lod = [{i:j for (i,j) in zip(header, row)} for row in rows]
    return lod

if __name__ == '__main__':
    from decisions import lmap
    lod = extract_table("table.html")
    for item in lod:
        item["Supervisors"] = clean_supervisors(item["Supervisors"])
    sups = reduce(lambda a, b: a + b, lmap(lambda d: d["Supervisors"], lod))
    sups.sort()
