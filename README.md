# Spider-of-owhat-and-taoba

#### 1. Files in ./Taoba

> get_title.py

Try to get the title of every money collection project. You can input the links of project line by line, and the program can read it and craw the total deposit of every project. Finally, save the title and the account of money in the excel file.

> read_from_text.py 

A package to read links of taoba in the data.txt

> tao_ba.py

Use BeautifulSoup4, Selenium,webdriver to craw the data from taoba. then save and output in a excel file.

Here are some points of my code.

##### 1. About dynamic data on the page

```python
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("var q=document.documentElement.scrollTop=0")
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
```

Because a part of  data in this website is loaded by javascript, I use selenium to control the browser scrolling up and down for loading and getting all the data from the page. I hope someone can find better idea to finish this job. If you have a better idea please contact me. I'd like to improve the efficiency of this code 

##### 2.About save data

```python
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
```

Write all my code to an excel.

##### 3.About ranking

```python
result = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
```

To rank the id by money every id contribute.

##### 4.How to use

In main function, input your links to url_list[]. There are two available ways. One is 

```python
url_list.append(link1)
url_list.append(link2)
```

The other is 

```python
id_list = read_from_text.get_data_from_file()
```

#### 2. Files in ./owhat

Basically same as files in ./taoba

#### 3. merge.py

To merge data from owhat(excel) and taoba(excel). 



If you have any problem about my code, you can contact me: csrjlu@outlook.com.

