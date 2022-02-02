from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys


def test_scores_service():
    driver = webdriver.Chrome(executable_path="C:\\Users\dgotl\Desktop\chromedriver.exe")
    driver.get("localhost:8000")
    selenume_score = driver.find_element_by_id("score")
    return 1 < selenume_score < 1000

def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)

