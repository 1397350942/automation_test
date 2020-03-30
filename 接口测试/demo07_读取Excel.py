import xlrd

# 打开Excel表
book = xlrd.open_workbook("./Data/data1.xlsx")
# 定位sheet表
table = book.sheet_by_name("Sheet1")

print(table.nrows) # 统计有多少行
print(table.ncols) # 统计列数
print(table.row_values(0)) # 获取第1行的数据
