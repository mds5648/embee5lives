from selenium import webdriver
import time
if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=r"C:\Users\Matthew Stoffolano\Desktop\chromedriver.exe")
    driver.get('https://python.org')