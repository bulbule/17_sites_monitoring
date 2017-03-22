import whois
import os
import requests
import argparse
import datetime
from termcolor import colored


MIN_PREPAYED_DAYS = 30


def get_min_expiration_date(days_interval):
    today = datetime.datetime.today()
    min_exp_date = today + datetime.timedelta(days=days_interval)
    return min_exp_date


def load_urls4check(path):
    if not os.path.exists(path):
        raise ValueError('Incorrect path')
    with open(path, "r") as urls_file:
        return urls_file.read()


def split_urls(urls_file):
    return urls_file.splitlines()


def parse_urls():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_urls_file')
    args = parser.parse_args()
    return args.path_to_urls_file


def is_server_respond_with_200(url):
    return get_status_code(url) == 200


def get_status_code(url):
    response = requests.get(url)
    return response.status_code


def get_domain_expiration_date(url):
    response = whois.whois(url)
    if isinstance(response.expiration_date, list):
        return response.expiration_date[0]
    else:
        return response.expiration_date


def check_expiration_date(exp_date):
    if exp_date is not None:
        return exp_date >= get_min_expiration_date(MIN_PREPAYED_DAYS)
    else:
        return False


def output(urls):
    for url in urls:
        exp_date = get_domain_expiration_date(url)
        if is_server_respond_with_200(url) and check_expiration_date(exp_date):
            print(colored(url, 'green'), 'OK')
        elif is_server_respond_with_200(url) and not check_expiration_date(exp_date):
            print(colored(url, 'red'), 'expired')
        elif not is_server_respond_with_200(url) and check_expiration_date(exp_date):
            print(colored(url, 'red'),
                  'status code - {}'.format(get_status_code(url)))
        else:
            print(colored(url, 'red'),
                  'expired with status code - {}'.format(get_status_code(url)))


if __name__ == '__main__':
    path_to_urls = parse_urls()
    urls = split_urls(load_urls4check(path_to_urls))
    output(urls)
