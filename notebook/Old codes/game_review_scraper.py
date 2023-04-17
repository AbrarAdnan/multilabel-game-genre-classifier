from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

links = {
    'https://www.metacritic.com/browse/games/genre/metascore/action/all?view=detailed' : 'action',
    'https://www.metacritic.com/browse/games/genre/metascore/adventure/all?view=detailed' : 'adventure',
    'https://www.metacritic.com/browse/games/genre/metascore/fighting/all?view=detailed' : 'fighting',
    'https://www.metacritic.com/browse/games/genre/metascore/first-person/all?view=detailed' : 'first-person',
    'https://www.metacritic.com/browse/games/genre/metascore/flight/all?view=detailed' : 'flight',
    'https://www.metacritic.com/browse/games/genre/metascore/party/all?view=detailed' : 'party',
    'https://www.metacritic.com/browse/games/genre/metascore/platformer/all?view=detailed' : 'platformer',
    'https://www.metacritic.com/browse/games/genre/metascore/puzzle/all?view=detailed' : 'puzzle',
    'https://www.metacritic.com/browse/games/genre/metascore/racing/all?view=detailed' : 'racing',
    'https://www.metacritic.com/browse/games/genre/metascore/real-time/all?view=detailed' : 'real-time',
    'https://www.metacritic.com/browse/games/genre/metascore/role-playing/all?view=detailed' : 'role-playing',
    'https://www.metacritic.com/browse/games/genre/metascore/simulation/all?view=detailed' : 'simulation',
    'https://www.metacritic.com/browse/games/genre/metascore/sports/all?view=detailed' : 'sports',
    'https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed' : 'strategy',
    'https://www.metacritic.com/browse/games/genre/metascore/third-person/all?view=detailed' : 'third-person',
    'https://www.metacritic.com/browse/games/genre/metascore/turn-based/all?view=detailed' : 'turn-based',
    'https://www.metacritic.com/browse/games/genre/metascore/wargame/all?view=detailed' : 'wargame',
    'https://www.metacritic.com/browse/games/genre/metascore/wrestling/all?view=detailed' : 'wrestling',
        }
css_selectors = ['div.browse_list_wrapper:nth-child(3)',
                 'div.browse_list_wrapper:nth-child(5)',
                 'div.browse_list_wrapper:nth-child(7)',
                 'div.browse_list_wrapper:nth-child(9)'
                ]

def get_data(driver,genre):
    review_data = []
    while True:
        print('At Page = ', driver.current_url)
        for css in css_selectors:
            review_table = driver.find_element(By.CSS_SELECTOR,css)
            summaries = review_table.find_elements(By.CLASS_NAME,'clamp-summary-wrap')
            for i in summaries:
                summary = i.find_element(By.CLASS_NAME,'summary')
                title = i.find_elements(By.CLASS_NAME,'title')
                link = i.find_elements(By.TAG_NAME,'a')
                review_data.append({
                    'title' : title[1].text,
                    'genre' : genre,
                    'url' : link[1].get_attribute('href'),
                    'summary' : summary.text,
                })
            df = pd.DataFrame(data=review_data, columns=review_data[0].keys())
            df.to_csv("datasets/" + f"{genre}_game_reviews.csv", index=False)
            
        try:
            next_button = driver.find_element(By.CSS_SELECTOR,'span.flipper:nth-child(2)')
            link_container = next_button.find_element(By.TAG_NAME,'a')
            next_page_link = link_container.get_attribute('href')
            driver.get(next_page_link)
        except:
            return
        
start = time.time()
# driver = webdriver.Firefox()
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
for link,genre in links.items():
    driver.get(link)
    get_data(driver,genre)
end = time.time()
print(end - start)
driver.close()
# took 3978 seconds