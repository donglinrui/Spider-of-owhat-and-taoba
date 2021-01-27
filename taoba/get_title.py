from bs4 import BeautifulSoup
import time
from selenium import webdriver
import xlwt
import read_from_text
import requests
import re
global driver
def get_title_money(url):
    driver.get(url)
    time.sleep(1)
    title = driver.title
    html = driver.page_source
    money = re.match(r'.*class="f-gold"><span>￥(.*?)<.*',html,re.DOTALL)
    money =money.group(1)
    return title,money
if __name__ == '__main__':
    driver = webdriver.Chrome()
    id_list = read_from_text.get_data_from_file()
    money_sum = 0
    workbook = xlwt.Workbook(encoding='uft-8')
    worksheet = workbook.add_sheet("项目总结")
    worksheet.write(0, 0, "项目名称")
    worksheet.write(0, 1, "集资额")
    worksheet.col(0).width = 10000
    worksheet.col(1).width = 3500
    for i in range(len(id_list)):
        id = id_list[i]
        url = 'https://www.taoba.club/#/pages/idols/detail?id=' + id
        title,money = get_title_money(url)
        print(title,money)
        worksheet.write(i + 1, 0, title)
        worksheet.write(i + 1, 1, money)
        worksheet.write(i + 1, 2, url)
        money_sum += float(money)
    workbook.save("项目总结.xls")
    print("taoba总额：",money_sum)