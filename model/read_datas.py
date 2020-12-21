import xlrd
def readexcel(sheet,filename=None):
    if not filename:
        filename="../data/login_datas.xlsx"
        data=xlrd.open_workbook(filename)
        table=data.sheet_by_name('login')
        e_list=[]
        for row in range(1,table.nrows):
            e_list.append(table.row_values(row))
        print(e_list)
        return e_list

if __name__ == "__main__":
    username,password=readexcel("")[0]
    print(username)



