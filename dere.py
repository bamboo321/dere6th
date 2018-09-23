from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def isDebugMode(bl):
    global driver

    if bl == True:
        driver = webdriver.Chrome()
    else:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options = options)


def main():
    isDebugMode(True)

    driver.get('http://eplus.jp/cinderella6th/')

    #チェックボックスを探す
    cbox = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[3]/div/div/form/center/input')

    #クリック
    cbox.click()

    #同意してお申込みへボタンを探す
    agrbutton = driver.find_element_by_xpath('/html/body/div/main/div/div/div/section[3]/div/div/form/center/a')

    #ボタンクリック
    agrbutton.click()

    #1日目次へボタンを探す
    day1nextbutton = driver.find_element_by_xpath('//*[@id="performancesArea"]/div[2]/div[1]/table/tbody/tr[2]/td[5]/div/a')

    #ボタンをクリック
    day1nextbutton.click()

    #前のページに戻る
    


if __name__ == '__main__':
    main()
