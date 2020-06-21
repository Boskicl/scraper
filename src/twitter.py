from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os
import getpass

class Twitter:
    def __init__(self,username,passwrd,dirname,tweets):
        self.username   = username
        self.password   = passwrd
        self.dirname    = dirname
        self.tweetnum   = tweets
        self.url        = 'https://twitter.com'
        self.driver     = webdriver.Chrome(executable_path="/home/local/DEVNET/boskicl/scripts/data_scrapper/src/chromedriver") # path to chromedriver 
    
    def create_dir(self):
        if not os.path.exists("data"):
            try:
                os.mkdir("data")
                print("Created data directory.")
            except:
                print("Unable to create data directory: Directory already exists.")
        else:
            print("Unable to create data directory: Directory already exists.")
        
        if not os.path.exists("data/data_" + self.dirname):
            try:
                os.mkdir("data/data_" + dirname)
                print("Created data/data_{0} directory".format(self.dirname))
            except:
                print("Unable to create data/data_{0} directory: Directory already exists.".format(self.dirname))
        else:
            print("Unable to create data/data_{0} directory: Directory already exists.".format(self.dirname))
            
        if not os.path.exists("data/data_" + self.dirname + '/img'):
            try:
                os.mkdir("data/data_" + dirname + '/img')
                print("Created data/data_{0}/img directory.".format(self.dirname))
            except:
                print("Unable to create data/data_{0}/img directory: Directory already exists.".format(self.dirname))
        else:
            print("Unable to create data/data_{0}/img directory: Directory already exists.".format(self.dirname))
        
        
    def login(self):
        driver      = self.driver
        print("Checking for Directories...")
        directory   = self.create_dir()
        driver.get(self.url)
        
        
        #driver.get('{}/accounts/login/'.format(self.url))
        #sleep(2)
        #driver.find_element_by_name('username').send_keys(self.username)
        #driver.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        #sleep(3)
        #driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        #sleep(2)
        
#tweetnum = str(input('How many Tweets do you want to scrap? (int): '))
#dirname = 'tweets'
#print("Starting Social Media Scrapper...")
#twitter = Twitter('hi','bye',dirname,tweetnum)
#print("Logging into Twitter")
#twitter.login()
