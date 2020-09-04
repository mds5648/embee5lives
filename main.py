"""
Description:  This is meant to solve Hack "The Box Emdee five for life" challenge.  To run this you must have a
chrome.exe
Language: python 3.8
Author: Matthew Stoffolano
"""
from selenium import webdriver
import hashlib

exe_path = r"C:\Users\Matthew Stoffolano\Desktop\chromedriver.exe"
link = "docker.hackthebox.eu:32348"


"""
Description:This find the code that needs to be encrypted
html_file(String):This is the source code from the site
return(String): The code that needs to be encrypted
"""
def code_finder(html_file):
    first = html_file.split('<h3 align="center">')
    second = first[1].split('</h3>')
    return second[0]


"""
Descripton: Encrypts a string with md6 encryption
string(String): This is the string before encryption
return(String):  The encryption of the string
"""
def md5_encryption(string):
    encrypt = hashlib.md5(string.encode())
    return encrypt.hexdigest()


"""
Description:This will access the webpage and completed the desired process
"""
def main():
    driver = webdriver.Chrome(executable_path=exe_path)
    driver.get(link)
    source = driver.page_source
    md5_encryption(code_finder(source))
    text_box = driver.find_element_by_name("hash")
    text_box.send_keys(md5_encryption(code_finder(source)))
    submit = driver.find_element_by_xpath("html/body/center/form[input/@value='Submit']")
    submit.submit()


if __name__ == '__main__':
    main()
