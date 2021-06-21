#IMPORTS
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import random

#DEFINE
global browser
browser_profile = webdriver.FirefoxProfile()
browser_profile.set_preference("dom.webnotifications.enabled", False)
browser = webdriver.Firefox(firefox_profile=browser_profile)


#ÚčTY, KTORé SA BUDú FOLLOWOVAT
channels = []                        #ADD ALL CHANNELS FROM WHERE YOU WANT A FOLLOWERS
#POOL KOMENTáROV
comments = []                        #CREATE A POOL OF COMMENTS YOU WANT TO UPLOAD                   
#HASHTAGY NA VYHLADANIE FOTIEK
hashtags = []                        #HASHTAGS FOR FINDING SPECIFIC CONTENT

#METHODS
def start_log():

        __define_password = "zadajte svoje heslo"                                                    #HESLO UCTU
        __define_username = "zadajte svoje meno"                                                     #USERNAME UCTU
        #TRY TO LOG
        try:
            browser.get('https://www.instagram.com/')                                                #OPEN INSTAGRAM
            browser.implicitly_wait(10)
            sleep(2)

            accept_cookies = browser.find_element_by_xpath('//*[@class="aOOlW  bIiDR  "]')           #ACCEPT COOKIES
            accept_cookies.click();
            sleep(5)

            name = browser.find_element_by_xpath('//*[@name="username"]')                            #USERNAME TEXT
            name.send_keys(__define_username)

            password = browser.find_element_by_xpath('//*[@name="password"]')                        #PASSWORD TEXT
            password.send_keys(__define_password)

            login = browser.find_element_by_xpath('//*[@type="submit"]')                             #LOGIN BUTTON
            login.click();
            sleep(1)
        except:
            print("Some problem with logging in")

        #TRY TO DISMISS SAVING CREDENTIALS
        try:
            decline_save_credentials = browser.find_element_by_xpath('//*[@class="cmbtv"]')                   #DECLINE SAVING CREDENTIALS
            decline_save_credentials.click();
            sleep(1)
        except:
            print("No popup window: CREDENTIALS")

        try:
            turn_off_notification = browser.find_element_by_xpath('//*[@class="aOOlW  bIiDR  "]')             #TURNOFF NOTITIFICATION
            turn_off_notification.click();
        except:
            print("No popup window: NOTITIFICATION")

def follow(pocetFollowov):
        i = 1
        while i <= pocetFollowov:
            sleep(0.5)
            try:
                find_follower = browser.find_element_by_xpath('//*[@class="sqdOP  L3NKy   y3zKF     "]')       #FIND FOLLOWER IN LIST OF FOLLOWERS
                find_follower.click()                                                                          #FOLLOW
                i += 1
            except:
                element_inside_popup = browser.find_element_by_xpath('//div[@class="isgrP"]//a')
                element_inside_popup.send_keys(Keys.END)                                                       #IF ERROR OCCURS SLIDE DOWN

        sleep(1)
        homepage()


def find():                                                                                                   #METHOD FOR FINDING CHANNELS AND ALL ITS FOLLOWERS
    try:
        rand = random.randint(1,len(channels))                                                                #RANDOM NUMBER BETWEEN 1 AND NUMBER OF CHANNELS
        channel_name = channels[rand]
        find = browser.find_element_by_xpath('//*[@placeholder="Hľadať"]')                                    #CLICK ON FIND TEXT
        sleep(0.5)
        find.send_keys(channel_name)

        find_specific = browser.find_element_by_xpath('//*[@href="/{}/"]'.format(channel_name))               #CLICK ON SPECIFIC CHANNEL
        sleep(0.5)
        find_specific.click()

        followers = browser.find_element_by_xpath('//*[@href="/{}/followers/"]'.format(channel_name))         #CLICK ON FOLLOWERS
        sleep(0.5)
        followers.click()

        sleep(1)
    except:
        print("Error occured in find method")

def unfollow(pocetUnfollow):
    browser.get('https://www.instagram.com/beesophisticated/')                                              #GET TO MY PAGE
    followers = browser.find_element_by_xpath('//*[@href="/beesophisticated/following/"]')                  #CLICK ON MY FOLLOWERS
    followers.click()
    sleep(0.2)

    for x in range(40):                                                                                     #FOR NON UNFOLLOWING NEW-FOLLOWERS
        element_inside_popup = browser.find_element_by_xpath('//div[@class="isgrP"]//a')
        element_inside_popup.send_keys(Keys.END)
        sleep(1)

    sleep(0.5)
    find_followers = browser.find_elements_by_xpath('//*[@class="sqdOP  L3NKy    _8A5w5    "]')
    sleep(0.5)

    i = 1
    while i <= pocetUnfollow:
        sleep(0.2)
        try:
            find_followers[250+i].click()                                                                  #FIND PRECISE NUMBER OF FOLLOWERS
            find_delete_button = browser.find_element_by_xpath('//*[@class="aOOlW -Cab_   "]')             #FIND DELETE BUTTON
            find_delete_button.click()
            i += 1
        except:
            #KED DOJDEME NAKONIEC DOSAHU OKNA POSUNIE SA DOLU
            if(browser.find_element_by_xpath('//*[@class="aOOlW   HoLwm "]')):
                error = browser.find_element_by_xpath('//*[@class="aOOlW   HoLwm "]')
                error.click()
                homepage()
                sleep(500)
            else:
                element_inside_popup = browser.find_element_by_xpath('//div[@class="isgrP"]//a')
                element_inside_popup.send_keys(Keys.END)

    sleep(1)
    homepage()

def homepage():
        browser.get('https://www.instagram.com/')

def comment(number_of_comments):                                                                             #COMMENT ON PHOTO

    try:
        rand = random.randint(1,len(hashtags))
        go = 0
        while(go):
            if(rand in already_used_hashtags):
                rand = random.randint(0,13)
            else:
                already_used_hashtags.append(rand)
                go = 1

        choosen_hashtag = hashtags[rand]

        #FIND HASHTAG
        find = browser.find_element_by_xpath('//*[@placeholder="Hľadať"]')                                    #CLICK ON FIND TEXT
        find.send_keys("#{}".format(choosen_hashtag))

        #CLICK ON HASHTAG
        find_specific = browser.find_element_by_xpath('//*[@href="/explore/tags/{}/"]'.format(choosen_hashtag))                 #KLIKNUT NA VSETKYCH FOLLOWEROV KTORYCH KANAL MA
        find_specific.click()

        #FIND AND CLICK ON IMAGE BLOCK
        image_block = browser.find_element_by_xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]')
        image_block.click()


        for x in range(number_of_comments):
            #FIND AND WRITE COMMENT IN COMMENT SECTION
            rand = random.randint(0,7)
            comment = browser.find_element_by_class_name('Ypffh')        #CLICK ON COMMENT SECTION
            comment.click()
            sleep(2)
            comment = browser.find_element_by_class_name('Ypffh')
            comment.click()
            comment.send_keys("{}".format(comments[rand]))
            comment.send_keys(Keys.ENTER)
            #WAIT A SECOND
            sleep(3)
            #FLIP THE PAGE
            flip_page = browser.find_element_by_xpath('//*[@class=" _65Bje  coreSpriteRightPaginationArrow"]')
            flip_page.click()
            sleep(0.5)
    except:
        print("Došlo k chybe pri uploadovaní komentu")

    homepage()

def solving_errors():
    try:
        if(browser.find_element_by_xpath('//*[@class="mt3GC"]')):
            error = browser.find_element_by_xpath('//*[@class="aOOlW  bIiDR  "]')
            error.click()
        else:
            alert = browser.switch_to_alert()
            alert.accept()

    except:
        print("Another error.. Need an update")



start_log()
sleep(2)

error_counter = 0
while 1:
        try:
            unfollow(5)                               #UNFOLLOW
            find()                                    #FIND CHANNEL
            follow(10)                                #FOLLOW N ACCOUNTS
            comment(5)                                #COMMENT N PHOTOS
            for x in range(500):                      #SLEEP FOR N SECONDS
                sleep(1)
            homepage()                                #RETURN TO HOMEPAGE
            sleep(2)
        except:
                print("Error occured")
                homepage()
