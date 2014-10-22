#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import sys
from math import ceil

BASE_URL_CATEGORY = 'http://www.alexa.com/topsites/category;%d/Top/%s'
BASE_URL_COUNTRY = 'http://www.alexa.com/topsites/countries;%d/%s'

if __name__ == '__main__':
    
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: (country|category) CODE TOP-N\n');
        sys.exit(1);
    
    if sys.argv[1] == "country":
    	code = sys.argv[2].upper();
    	base_url = BASE_URL_COUNTRY;
    else:
    	code = sys.argv[2];
    	base_url = BASE_URL_CATEGORY;
    	
    number = int(sys.argv[3]);
    delimiter = ' ';

    page_numbers = int(ceil(number/25.0));

    for page_num in range(0, page_numbers): 
    
    	response = requests.get(base_url % (page_num, code))
    
        soup = BeautifulSoup(response.text)
        bullets = soup.find_all('li', {'class':'site-listing'})
    
        for bullet in bullets:
            rank = bullet.div.contents[0]
            site = bullet.div.findNextSibling().a.contents[0]
            print('%s%s%s' % (rank, delimiter, site))
