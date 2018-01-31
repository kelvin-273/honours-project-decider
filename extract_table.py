import bs4
import re

def get_soup(arg):
    return bs4.BeautifulSoup(open(arg), "lxml")

def unpad(s):
    return re.sub(r"^[ \r\n\t]*", "",
                  re.sub(r"[ \r\n\t]*$", "", s))

def unwhitespace(s):
    return re.sub(r"[ \r\n\t]", "", s)

if __name__ == '__main__':
    soup = bs4.BeautifulSoup(open("table.html"), "lxml")
    [thead, tbody] = soup.find("table").children
    header = [unpad(i.text) for i in thead.find_all("th")]
    rows = [[unpad(j.text) for j in i.find_all("td")] for i in tbody.find_all("tr")]
    lod = [{i:j for (i,j) in zip(header, row)} for row in rows]
    del(soup, thead, tbody, header, rows)
