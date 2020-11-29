import time
import pickle
from selenium import webdriver

"""
Get cookies from site.
How To - Instructions:
1. Run script "get_cookies.py"
2. You have 90 seconds to enter login and password, on the opened page.
   After the script has finished running - you should see the file "cookies". 
   If file "cookies" exist, change "a_test_google_search_using_using_selenium" to "test_google_search_using_using_selenium"
   run "tests.py". 
"""


######################################### get cookie ##############################
SITE_WITH_COOKIES = "https://www.google.com"

browser = webdriver.Firefox()
browser.get("site for cookie")
time.sleep(90) # time to login

pickle.dump(browser.get_cookies(), open('cookie', 'wb'))
print("Cookies saved")
