import datetime
import os
import shutil
import xlwt
import checkJpsServer


class ExcelOperate:
    def create_excel(self):
        shi_jian = datetime.date.today().__format__('%Y%m%d')
        print(shi_jian)
        pwd = os.getcwd()
        path = pwd + '\\data\\cgrzzl_server.xlsx'
        is_sign = os.path.exists(path)
        if (is_sign):
            print('当前目录：' + path)
            shutil.copy(path, pwd + '\\data\\cgrzzl_server_' + shi_jian + '.xlsx')
        else:
            print('目录错误')

    def write_excel(self):
        shi_jian = datetime.date.today().__format__('%Y%m%d')
        pwd = os.getcwd()

        wb = xlwt.Workbook()
        ws = wb.add_sheet('代码生成sheet')  # 增加sheet
        ws.col(0).width = 200 * 30  # 设置第一列列宽
        ws.col(1).width = 230 * 30

        ws.write(0, 0, '服务器', self.set_style('Times New Roman', 220, bold=True))
        ws.write(0, 1, "服务名称", self.set_style('Times New Roman', 220, bold=True))
        ws.write(0, 2, "是否存在", self.set_style('Times New Roman', 220, bold=True))

        check_Jps_Server = checkJpsServer.CheckJpsServer()
        dict_list = check_Jps_Server.check_server()

        i = 0
        j = 1
        item1 = dict_list['10.8.6.10']
        item2 = dict_list['10.8.6.11']
        item3 = dict_list['10.8.6.12']
        item4 = dict_list['10.8.6.13']
        item5 = dict_list['10.8.5.35']
        item6 = dict_list['10.8.5.36']
        item7 = dict_list['10.8.5.37']
        item8 = dict_list['10.8.5.39']
        item9 = dict_list['10.8.5.40']
        item10 = dict_list['10.8.5.41']
        item11 = dict_list['10.8.5.42']
        item12 = dict_list['10.8.5.57']
        item13 = dict_list['10.8.5.83']
        """
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        print(item5)
        print(item6)
        print(item7)
        print(item8)
        print(item9)
        print(item10)
        print(item11)
        print(item12)
        print(item13)
        """
        while i < len(item1):
            tpList = item1[i].split(':')
            ws.write(j, 0, '10.8.6.10', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j+1
            i = i+1

        i = 0
        while i < len(item2):
            tpList = item2[i].split(':')
            ws.write(j, 0, '10.8.6.11', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j+1
            i = i+1

        i = 0
        while i < len(item3):
            tpList = item3[i].split(':')
            ws.write(j, 0, '10.8.6.12', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item4):
            tpList = item4[i].split(':')
            ws.write(j, 0, '10.8.6.13', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item5):
            tpList = item5[i].split(':')
            ws.write(j, 0, '10.8.5.35', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item6):
            tpList = item6[i].split(':')
            ws.write(j, 0, '10.8.5.36', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item7):
            tpList = item7[i].split(':')
            ws.write(j, 0, '10.8.5.37', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item8):
            tpList = item8[i].split(':')
            ws.write(j, 0, '10.8.5.39', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item9):
            tpList = item9[i].split(':')
            ws.write(j, 0, '10.8.5.40', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item10):
            tpList = item10[i].split(':')
            ws.write(j, 0, '10.8.5.41', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item11):
            tpList = item11[i].split(':')
            ws.write(j, 0, '10.8.5.42', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item12):
            tpList = item12[i].split(':')
            ws.write(j, 0, '10.8.5.57', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        i = 0
        while i < len(item13):
            tpList = item13[i].split(':')
            ws.write(j, 0, '10.8.5.83', self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 1, tpList[0], self.set_style('Times New Roman', 220, bold=False))
            ws.write(j, 2, tpList[1], self.set_style('Times New Roman', 220, bold=False))
            j = j + 1
            i = i + 1

        wb.save(pwd + '\\data\\cgrzzl_server_' + shi_jian + '.xls')  # 保存xls

    def set_style(self, name, height, bold=False, format_str=''):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.height = height

        borders = xlwt.Borders()  # 为样式创建边框
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1

        style.font = font
        style.borders = borders
        style.num_format_str = format_str

        return style
