import functools
import os

import schedule
from seleniumwire.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def url_parser():
    """
    Parsers the URLs to check inventory on from a file specified by the environment.
    :return: A list of URLs parsed from the file
    """
    file = os.getenv('URL_FILE')
    with open(file, 'r') as fp:
        urls = fp.readlines()
    urls = [i.strip() for i in urls if not i.startswith('#')]
    print(f'Checking inventory of {len(urls)} items...')
    return urls


def inventory_lookup(driver, url):
    driver.get(url)
    add_to_cart_btn = driver.find_element_by_css_selector('#addtocart-target')
    if add_to_cart_btn.text == 'ADD TO CART':
        status = 'IN STOCK!'
    else:
        status = 'Out of Stock'
    print(f'{driver.title}: {status}')


def job():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    with Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options) as driver:
        driver.header_overrides = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.61 Safari/537.36'
        }
        urls = url_parser()
        for url in urls:
            inventory_lookup(driver, url)
        driver.quit()


def main():
    interval = os.getenv('INTERVAL')
    schedule.every(int(interval)).minutes.do(job)
    print(f'Jobs will be scheduled every {interval} minutes')

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
