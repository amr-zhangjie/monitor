import excelOp
excel_op = excelOp.ExcelOperate()
excel_op.write_excel()
# ssh_moniter = moniter.Moniter('10.8.7.60',22,'root','dfcw88!')
# ssh_moniter.disk_stat()
# ssh_moniter.mem_info()
# ssh_moniter.cpu_info()
# ssh_moniter.jps_server()

"""
shi_jian=datetime.date.today().__format__('%Y%m%d')
print(shi_jian)
#time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
pwd=os.getcwd();
path=pwd+'\\data\\cgrzzl_server.xlsx'
is_sign=os.path.exists(path)
if(is_sign):
    print('当前目录：'+path)
    shutil.copy(path,pwd+'\\data\\cgrzzl_server_'+shi_jian+'.xlsx')
    #shutil.move(path,pwd+'\\data\\cgrzzl_server_111.xlsx')
else:
    print('目录错误')
"""
