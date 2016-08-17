import urllib.request
from bs4 import BeautifulSoup, NavigableString

"""Simple web scraper to test out beautiful soup. Scrapes from the NASDAQ website and runs on command line."""

company_list = []
company_acronym = input("Input a company acronym, or input \"n\" to quit.")
while(company_acronym.strip().replace("\"\"","").lower() != "n"):
    company_list.append(company_acronym)
    company_acronym = input("Input a company acronym, or input \"n\" to quit.")
if len(company_list) == 0:
    print("You have inputted no companies.")
invalid_list = []
final_company_list = company_list[:]
for company in company_list:
    site = urllib.request.urlopen("http://www.nasdaq.com/symbol/" + company).read()
    soup = BeautifulSoup(site, "html.parser")
    check_exists = soup.find_all("div", class_="notTradingIPO")
    if check_exists == []:
        continue
    else:
        invalid_list.append(company)
        final_company_list.remove(company)
for invalid in invalid_list:
    print(invalid + " does not exist. Make sure you inputted it correctly.")
stock_data = {}
data_list = []
company_stock_info = {}
counter = 0
for company in final_company_list:
    site = urllib.request.urlopen("http://www.nasdaq.com/symbol/" + company).read()
    soup = BeautifulSoup(site, "html.parser")
    link_identifiers = soup.find_all("a", class_="tt show-link")
    for link_identifier in link_identifiers:
        link_children = link_identifier.children
        for child in link_children:
            if isinstance(child, NavigableString) and child != "\n":
                formattedString = child.string.replace("\r\n", "").strip()
                stock_data[formattedString] = []
                data_list.append(formattedString)
        table_data = link_identifier.parent
        table_sibling = table_data.next_sibling.next_sibling.text
        table_sibling = table_sibling.replace("\xa0","").strip()
        stock_data[data_list[counter]].append(table_sibling)
        counter += 1
    company_stock_info[company] = stock_data
    stock_data = {}
    data_list = []
    counter = 0
if company_stock_info:
    print(company_stock_info)