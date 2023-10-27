from bs4 import BeautifulSoup
import requests
import numpy as np
from datetime import datetime
import csv


LINK = "https://jiji.com.gh/search?query=iphone%2011%20"


def main():
    prices = get_prices_by_link(LINK)
    prices_without_outliers = remove_outliers(prices)
    print(get_average(prices_without_outliers))
    print(prices)
    print(prices_without_outliers)
    save_to_file(prices_without_outliers)


def get_prices_by_link(link):
    # get source
    r = requests.get(link)

    # parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')
    # find all list item from search result
    search_results = page_parse.find("div", {"class":"b-advert-listing"}).find_all("div", {"class":"b-list-advert__item-wrapper"})

    item_prices = []

    for result in search_results:
        price_as_text = result.find("div", {"class":"b-list-advert-base__data__price"}).text
        price = actual_price(price_as_text)
        item_prices.append(price)

    return item_prices


def actual_price(price_as_text):
        _, new_price = price_as_text.strip().split(" ")
        price = float(new_price.replace(",",""))
        return price


def remove_outliers(prices, m=2):
    data = np.array(prices)
    new_list = [x for x in prices if (x > np.mean(data) - m * np.std(data))]
    final_list = [x for x in new_list if (x < np.mean(data) + m * np.std(data))]
    return final_list


def get_average(prices):
    return round(np.mean(prices), 2)


def save_to_file(prices):
    fields=[datetime.today().strftime("%B-%D-%Y"), np.round(get_average(prices),2)]
    with open("prices.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(fields)


if __name__ == "__main__":
    main()