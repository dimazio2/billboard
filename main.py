from selenium import webdriver
from bs4 import BeautifulSoup

BASE_URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")
url = BASE_URL + date

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument("window-size=1920x1080")
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

song_names_spans = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.get_text() for song in song_names_spans]

print(song_names)