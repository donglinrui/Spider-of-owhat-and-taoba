import xlrd
import xlwt
global data_dict
data_dict = {}#“ID-集资金额”的字典 全局变量
def update_dict(name,money):#将数据存储到字典里，id-集资数
    if data_dict.get(name) != None:
        money = data_dict.get(name) + money
        data_dict.update({name: money})
    else:
        data_dict.update({name: money})
def get_data(name):
    data = xlrd.open_workbook(name)
    table = data.sheet_by_index(0)
    for i in range(table.nrows-2):
        id = table.cell(i+1,0).value
        money = table.cell(i+1,1).value
        update_dict(id,money)
def write_in_excel(name):#合并
    print("正在合并excel中...")
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
    get_data('owhat总榜.xls')
    get_data('taoba总榜.xls')
    write_in_excel("taoba+owhat合并.xls")