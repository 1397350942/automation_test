import xlrd


class Read_Ex():
    def read_excel(self):
        # 打开Excel表
        book = xlrd.open_workbook(r"C:\Users\wengw\Documents\automation_test\接口测试\Data\data2.xlsx")
        # 找到sheet页
        table = book.sheet_by_name("Sheet1")
        # 获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols
        s = []
        key = table.row_values(0)  # 这是第一行数据,作为字典的key值
        if row_Num <= 1:
            print("没有数据")
        else:
            j = 1
            for i in range(row_Num - 1):
                d = {}
                values = table.row_values(j)
                for x in range(col_Num):
                    d[key[x]] = values[x]
                j += 1
                s.append(d)
        return s


if __name__ == '__main__':
    r = Read_Ex()
    s = r.read_excel()
    print(s)
