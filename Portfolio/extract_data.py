#!/usr/bin/env python3.6

import re
import sys
import time
import datetime
import requests
import click 
from tqdm import tqdm
from urllib.parse import urlparse


def split_crumb_store(v):
    return v.split(':')[2].strip('"')


def find_crumb_store(lines):
    # Looking for
    # ,"CrumbStore":{"crumb":"9q.A4D1c.b9
    for l in lines:
        if re.findall(r'CrumbStore', l):
            return l
    print("Did not find CrumbStore")


def get_cookie_value(r):
    return {'B': r.cookies['B']}


def get_page_data(symbol):
    url = "https://finance.yahoo.com/quote/%s/?p=%s" % (symbol, symbol)
    r = requests.get(url)
    cookie = get_cookie_value(r)

   
    lines = r.content.decode('unicode-escape').strip(). replace('}', '\n')
    return cookie, lines.split('\n')


def get_cookie_crumb(symbol):
    cookie, lines = get_page_data(symbol)
    crumb = split_crumb_store(find_crumb_store(lines))
    return cookie, crumb


def get_data(symbol, start_date, end_date, cookie, crumb):
    filename = '%s.csv' % (symbol)
    url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&crumb=%s" % (symbol, start_date, end_date, crumb)
    response = requests.get(url, cookies=cookie)
    with open (filename, 'wb') as handle:
        for block in tqdm(response.iter_content(1024)):
            handle.write(block)



@click.group()
def main(): 
	pass 

#extract parameters
@main.command('extract')
@click.option('--symbol','symbol')
@click.option('--time.since','start_date')
@click.option('--time.until','end_date')



def download_quotes(symbol, start_date, end_date):
    #start_date = 0
    #end_date = get_now_epoch()
    if start_date is not None : 
    	start_date = time.strptime(start_date,"%d-%m-%Y");
    	start_date = int(time.mktime(start_date));

    else :
    	start_date = 0 

    if end_date is not None : 
        end_date = time.strptime(end_date,"%d-%m-%Y")
        end_date = int(time.mktime(end_date))
    else:
        end_date = int(time.time())

    cookie, crumb = get_cookie_crumb(symbol)
    get_data(symbol,start_date,end_date,cookie,crumb)
    

if __name__ == '__main__':
   main()
