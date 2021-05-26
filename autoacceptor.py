import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# linkedin post liker
#
# Add your post url (if any) to your posts here for others to like them : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
#
#
#
# To like other people's post:
# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb

# step 1 change this from : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
links = [
    "https://www.linkedin.com/mynetwork/"
]
# step 2 : run code , check if you are logged in (if not, then login) then press 1 in console
# step 3 : the code shoud take care of the rest add your posts that you would want to get liked


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")
# delete this after every month

while "1" != input("press 1 when signed in: "):
    pass
for link in links:
    try:
        print("accessing link ", link)
        driver.get(link)
        sleep(2)
        all_buttons = driver.find_elements_by_tag_name("button")
        accept_buttons = [btn for btn in all_buttons if btn.text == "Accept"]

        for btn in accept_buttons:
            driver.execute_script("arguments[0].click()", btn)
            break

    except Exception as e:
        print("error processing link\nlink: ", link, "\nerror", e)

driver.close()
