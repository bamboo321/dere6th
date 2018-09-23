from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import datetime


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

    #全席指定取得
    day1zenseki = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[1]').text

    #立ち見取得
    day1tatimi = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[2]').text

    #芝生指定取得
    day1shibahu = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[3]').text

    #見切れ取得
    day1mikire = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[3]').text

    #現在時刻取得
    day1t = datetime.datetime.today()

    #前のページに戻る
    day1backbutton = driver.find_element_by_xpath('//*[@id="bw1002"]/div[6]/a')

    #ボタンをクリック
    day1backbutton.click()

    #2日目次へボタンを探す
    day2nextbutton = driver.find_element_by_xpath('//*[@id="performancesArea"]/div[3]/div[1]/table/tbody/tr[2]/td[5]/div/a')

    #ボタンをクリック
    day2nextbutton.click()

    #全席指定取得
    day2zenseki = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[1]').text

    #立ち見取得
    day2tatimi = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[2]').text

    #芝生指定取得
    day2shibahu = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[3]').text

    #見切れ取得
    day2mikire = driver.find_element_by_xpath('//*[@id="bw1002"]/div[2]/table/tbody/tr[2]/td[4]').text

    #現在時刻取得
    day2t = datetime.datetime.today()

    #リストの作成
    day1r = [day1t.strftime("%Y/%m/%d %H:%M:%S"),day1zenseki, day1tatimi, day1shibahu, day1mikire]
    day2r = [day2t.strftime("%Y/%m/%d %H:%M:%S"),day2zenseki, day2tatimi, day2shibahu, day2mikire]


    #結果の出力
    outputResults(day1r, day2r)


    #終了
    driver.quit()


def outputResults(day1r, day2r):
    with open('day1result', 'a') as f:
        writer1 = csv.writer(f, lineterminator='\n')
        writer1.writerow(day1r)

    with open('day2result', 'a') as f:
        writer2 = csv.writer(f, lineterminator='\n')
        writer2.writerow(day2r)

    


if __name__ == '__main__':
    main()
