import paramiko


class Moniter:
    """linux服务器监控"""
    def __init__(self, ip, port, name, pwd):
        """初始化"""
        self.ip = ip
        self.port = port
        self.name = name
        self.pwd = pwd
        # 建立ssh连接
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client.connect(self.ip, self.port, self.name, self.pwd)

    def disk_stat(self):
        """磁盘空间监控"""
        stdin, stdout, stderr = self.client.exec_command('df -h ')
        content = stdout.readlines()
        print('************************磁盘空间监控****************************')
        for i in content[1:]:
            i = i.replace('\n', '').split()
            print("\t文件系统：", i[0], )
            print("\t容量：", i[1], )
            print("\t已用：", i[2], )
            print("\t可用：", i[3], )
            print("\t已用%挂载点：", i[4])

    def mem_info(self):
        """内存监控"""
        stdout = self.client.exec_command("cat /proc/meminfo")[1]
        content = stdout.readlines()
        # print(content)
        mems = {}
        for line in content:
            fields = line.split()
            mems[fields[0]] = int(fields[1]) * 1024
        MemTotal = mems['MemTotal:']
        MemFree = mems['MemFree:']
        Buffers = mems['Buffers:']
        Cached = mems['Cached:']
        SwapCached = mems['SwapCached:']
        SwapTotal = mems['SwapTotal:']
        SwapFree = mems['SwapFree:']
        print('******************************内存监控*********************************')
        print("总内存：", MemTotal)
        print("空闲内存：", MemFree)
        print("给文件的缓冲大小:", Buffers)
        print("高速缓冲存储器使用的大小:", Cached)
        print("被高速缓冲存储用的交换空间大小:", SwapCached)
        print("给文件的缓冲大小:", Buffers)
        if int(SwapTotal) == 0:
            print(u"交换内存总共为：0")
        else:
            Rate_Swap = 100 - 100 * int(SwapFree) / float(SwapTotal)
            print(u"交换内存利用率：", Rate_Swap)
        Free_Mem = int(MemFree) + int(Buffers) + int(Cached)
        Used_Mem = int(MemTotal) - Free_Mem
        Rate_Mem = 100 * Used_Mem / float(MemTotal)
        print(u"内存利用率：", str("%.2f" % Rate_Mem), "%")

    def cpu_info(self):
        """CPU使用率监控"""
        stdin, stdout, stderr = self.client.exec_command("top -b -n1 | sed -n '3p'|awk '{print $2}'")
        content = stdout.read().decode()
        # print(content)
        print('当前CPU使用率'+content.strip().replace(',', '').replace('us', ''))

    def jps_server1(self):
        stdin, stdout, stderr = self.client.exec_command("jps")
        """
        print(stdin)
        print(stdout)
        print(stderr)
        """
        # content1 = stdin.read()
        content2 = stdout.read()
        # content3 = stderr.read().decode()
        # print(content1)
        print(content2)
        # print(content3)

    def jps_server(self):
        """JPS微服务监控"""
        stdin, stdout, stderr = self.client.exec_command("jps")
        content = stdout.readlines()
        return content
        """
        for i in content:
            i = i.replace('\n', '').split()
            print("\t服务ID：", i[0] )
            print("\t服务名称：", i[1])
        """
