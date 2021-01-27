from bs4 import BeautifulSoup
import time
from selenium import webdriver
import xlwt
global data_dict
import read_from_text
from pynput.keyboard import Key,Controller
data_dict = {}#“ID-集资金额”的字典 全局变量
def get_from_internet(url_list):#从网页上获取html数据
    driver = webdriver.Chrome()
    html_list = []
    #keyboard = Controller()
    for url in url_list:
        print("正在采集url为："+url+"的数据...")
        driver.get(url)
        i = ''
        while (i != 'ok'):
            i = input('if ok please input:')
        html = driver.execute_script("return document.documentElement.outerHTML")
        html_list.append(html)  # 将采集到html数据加入列表中
    return html_list
    # for url in url_list:
    #     print("正在采集url为："+url+"的数据...")
    #     driver.get(url)
    #     html = ''
    #     while(1):#上下滑动网页，加载出所有页面，如果获取到的数据不全，请延长延时时间
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         driver.execute_script("var q=document.documentElement.scrollTop=0")
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         keyboard.press(Key.space)
    #         keyboard.release(Key.space)
    #         keyboard.press(Key.space)
    #         keyboard.release(Key.space)
    #         keyboard.press(Key.space)
    #         keyboard.release(Key.space)
    #         time.sleep(0.5)#延时时间，为了能够让页面加载完全
    #         #如果页面获取到的数据不再更新，即页面全部加载完，就停止采集
    #         if html == driver.execute_script("return document.documentElement.outerHTML"):
    #             break
    #         else:
    #             html = driver.execute_script("return document.documentElement.outerHTML")
    #     html_list.append(html)#将采集到html数据加入列表中
    # return html_list

def update_dict(name,money):#将数据存储到字典里，id-集资数
    if data_dict.get(name) != None:
        money = data_dict.get(name) + money
        data_dict.update({name: money})
    else:
        data_dict.update({name: money})

def get_data(url_list):#获取数据
    print("开始采集数据...")
    html_list = get_from_internet(url_list)
    for html in html_list:#遍历html列表(每个集资链接一个html)
        soup = BeautifulSoup(html, 'lxml')
        html = soup.prettify()
        soup = BeautifulSoup(html, 'lxml')
        list = soup.find_all("div",{"class":"one_mess"})#获取list
        for i in range(len(list)):
            name = list[i].contents[1].text.strip()
            name = name.split()
            name = name[0]
            money = list[i].contents[1].contents[1].contents[2].strip()
            money = float(money)
            update_dict(name,money)

def output_result():#输出结果到控制台
    print("集资排行榜")
    result = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)  # 排序data_dict.并存到二维数组中，二维数组第一个元素是id，第二个元素是集资额
    for i in result:
        print(i)

def write_in_excel(name):#写入excel
    print("正在写入excel中...")
    result = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)  # 排序data_dict.并存到二维数组中，二维数组第一个元素是id，第二个元素是集资额
    workbook = xlwt.Workbook(encoding='uft-8')
    worksheet = workbook.add_sheet("集资排行榜")
    worksheet.write(0, 0, "ID")
    worksheet.write(0, 1, "集资额")
    worksheet.col(0).width = 8000
    worksheet.col(1).width = 3000
    for i in range(0, len(result)):
        worksheet.write(i + 1, 0, result[i][0])
        worksheet.write(i + 1, 1, result[i][1])
    workbook.save(name)
    print("写入成功！写入同目录下" + name)

if __name__ == '__main__':
    url_list = []
    #要选择包含“toplist”的页面url（排行榜的url），可写入多条url
    #url_list.append('https://m.owhat.cn/shop/toplist.html?id=134185')
    #url_list.append('https://m.owhat.cn/shop/toplist.html?id=91697')
    #url_list.append('https://m.owhat.cn/shop/toplist.html?id=92385')
    id_list = read_from_text.get_data_from_file()
    for id in id_list:
        url = 'https://m.owhat.cn/shop/toplist.html?id=' + id
        url_list.append(url)
    get_data(url_list)#获取数据
    #output_result()#输出结果到控制台
    write_in_excel('owhat.xls')