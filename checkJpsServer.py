import moniter


class CheckJpsServer:
    def check_server(self):
        dict_list = {'10.8.6.10': [], '10.8.6.11': [], '10.8.6.12': [], '10.8.6.13': [],
                     '10.8.5.35': [], '10.8.5.36': [], '10.8.5.37': [], '10.8.5.39': [],
                     '10.8.5.40': [], '10.8.5.41': [], '10.8.5.42': [], '10.8.5.57 ': [],
                     '10.8.5.83': [], '10.8.5.34': []}

        dict_list['10.8.6.10'] = self.check_10_8_6_10_server()
        dict_list['10.8.6.11'] = self.check_10_8_6_11_server()
        dict_list['10.8.6.12'] = self.check_10_8_6_12_server()
        dict_list['10.8.6.13'] = self.check_10_8_6_13_server()

        dict_list['10.8.5.35'] = self.check_10_8_5_35_server()
        dict_list['10.8.5.36'] = self.check_10_8_5_36_server()
        dict_list['10.8.5.37'] = self.check_10_8_5_37_server()
        dict_list['10.8.5.39'] = self.check_10_8_5_39_server()

        dict_list['10.8.5.40'] = self.check_10_8_5_40_server()
        dict_list['10.8.5.41'] = self.check_10_8_5_41_server()
        dict_list['10.8.5.42'] = self.check_10_8_5_42_server()
        dict_list['10.8.5.57'] = self.check_10_8_5_57_server()

        dict_list['10.8.5.83'] = self.check_10_8_5_83_server()

        # dict_list['10.8.5.34'] = self.check_10_8_5_34_server()
        return dict_list
        # print(dict_list)

    def check_10_8_6_10_server(self):
        list_10_8_6_10 = ['QuorumPeerMain:0', 'Jps:0', 'Bootstrap:0']
        ssh_moniter1 = moniter.Moniter('10.8.6.10', '22', 'root', '123456')
        jps_content1 = ssh_moniter1.jps_server()
        return self.compare_data(list_10_8_6_10, jps_content1)

    def check_10_8_6_11_server(self):
        list_10_8_6_11 = ['LogConsumer:0', 'LogProvider:0', 'AuthConsumer:0', 'AuthProvider:0', 'FrameworkConsumer:0',
                          'FrameworkProvider:0', 'Jps:0', 'WrapperSimpleApp:0']
        ssh_moniter2 = moniter.Moniter('10.8.6.11', '22', 'root', '123456')
        jps_content2 = ssh_moniter2.jps_server()
        return self.compare_data(list_10_8_6_11, jps_content2)

    def check_10_8_6_12_server(self):
        list_10_8_6_12 = ['ExcelExportConsumer:0', 'FinanceprdProvider:0', 'OrganizationProvider:0', 'Jps:0', 'WrapperSimpleApp:0',
                          'BasicdataConsumer:0', 'BasicdataProvider:0', 'BusinessConsumer:0', 'BusinessProvider:0', 'OrganizationConsumer:0',
                          'FinanceprdConsumer:0']
        ssh_moniter3 = moniter.Moniter('10.8.6.12', '22', 'root', '123456')
        jps_content3 = ssh_moniter3.jps_server()
        return self.compare_data(list_10_8_6_12, jps_content3)

    def check_10_8_6_13_server(self):
        list_10_8_6_13 = ['Jps:0', 'CrontabConsumer:0', 'CommercialConsumer:0', 'ChannelmngConsumer:0', 'lanyou.rzzl.api.jar:0',
                          'CommercialProvider:0', 'ThirdInterfaceConsumer:0', 'ChannelmngProvider:0', 'CfconfigProvider:0', 'CommonConsumer:0',
                          'CfconfigConsumer:0', 'CommonProvider:0']
        ssh_moniter4 = moniter.Moniter('10.8.6.13', '22', 'root', '123456')
        jps_content4 = ssh_moniter4.jps_server()
        return self.compare_data(list_10_8_6_13, jps_content4)

    def check_10_8_5_35_server(self):
        list_10_8_5_35 = ['Bootstrap:0', 'ExternalworkProvider:0', 'TransferProvider:0', 'Jps:0', 'CgrzWeixinBoot:0',
                          'ExternalworkConsumer:0', 'TransferConsumer:0', 'RzzlPayBoot:0']
        ssh_moniter5 = moniter.Moniter('10.8.5.35', '22', 'root', '123456')
        jps_content5 = ssh_moniter5.jps_server()
        return self.compare_data(list_10_8_5_35, jps_content5)

    def check_10_8_5_36_server(self):
        list_10_8_5_36 = ['Jps:0', 'WrapperSimpleApp:0']
        ssh_moniter6 = moniter.Moniter('10.8.5.36', '22', 'root', '123456')
        jps_content6 = ssh_moniter6.jps_server()
        return self.compare_data(list_10_8_5_36, jps_content6)

    def check_10_8_5_37_server(self):
        list_10_8_5_37 = ['QuorumPeerMain:0', 'activemq.jar:0', 'Jps:0']
        ssh_moniter7 = moniter.Moniter('10.8.5.37', '22', 'root', '123456')
        jps_content7 = ssh_moniter7.jps_server()
        return self.compare_data(list_10_8_5_37, jps_content7)

    def check_10_8_5_39_server(self):
        list_10_8_5_39 = ['WorkflowConsumer:0', 'WorkflowProvider:0', 'Jps:0', 'PlatConsumer:0', 'PlatProvider:0',
                          'FileUploadConsumer:0']
        ssh_moniter8 = moniter.Moniter('10.8.5.39', '22', 'root', '123456')
        jps_content8 = ssh_moniter8.jps_server()
        return self.compare_data(list_10_8_5_39, jps_content8)

    def check_10_8_5_40_server(self):
        list_10_8_5_40 = ['WorkflowProvider:0', 'PlatProvider:0', 'Jps:0', 'PlatConsumer:0', 'FileUploadConsumer:0',
                          'WorkflowConsumer:0']
        ssh_moniter9 = moniter.Moniter('10.8.5.40', '22', 'root', '123456')
        jps_content9 = ssh_moniter9.jps_server()
        return self.compare_data(list_10_8_5_40, jps_content9)

    def check_10_8_5_41_server(self):
        list_10_8_5_41 = ['WebServiceConsumer:0', 'CarmanagerProvider:0', 'CustomermanagerConsumer:0', 'BasicDataConsumer:0', 'CarmanagerConsumer:0',
                          'Jps:0', 'CustomermanagerProvider:0', 'BasicDataProvider:0']
        ssh_moniter10 = moniter.Moniter('10.8.5.41', '22', 'root', '123456')
        jps_content10 = ssh_moniter10.jps_server()
        return self.compare_data(list_10_8_5_41, jps_content10)

    def check_10_8_5_42_server(self):
        list_10_8_5_42 = ['CarmanagerProvider:0', 'CustomermanagerConsumer:0', 'CustomermanagerProvider:0', 'CarmanagerConsumer:0',
                          'BasicDataProvider:0', 'BasicDataConsumer:0', 'Jps:0', 'WebServiceConsumer:0']
        ssh_moniter11 = moniter.Moniter('10.8.5.42', '22', 'root', '123456')
        jps_content11 = ssh_moniter11.jps_server()
        return self.compare_data(list_10_8_5_42, jps_content11)

    def check_10_8_5_57_server(self):
        list_10_8_5_57 = ['Bootstrap:0', 'WeixinConsumer:0', 'WeiXinProvider:0', 'lanyou.rzzl.api.jar:0', 'Jps:0']
        ssh_moniter12 = moniter.Moniter('10.8.5.57', '22', 'root', '123456')
        jps_content12 = ssh_moniter12.jps_server()
        return self.compare_data(list_10_8_5_57, jps_content12)

    def check_10_8_5_83_server(self):
        list_10_8_5_83 = ['Jps:0', 'CgrzWeixinBoot:0', 'WeiXinExportConsumer:0']
        ssh_moniter13 = moniter.Moniter('10.8.5.83', '22', 'root', '123456')
        jps_content13 = ssh_moniter13.jps_server()
        return self.compare_data(list_10_8_5_83, jps_content13)

    def check_10_8_5_34_server(self):
        list_10_8_5_34 = ['WrapperSimpleApp:0', 'cook-dynamic-dataSource.jar:0', 'WrapperSimpleApp:0',
                          'Jps:0', 'WrapperSimpleApp:0', 'WrapperSimpleApp:0', 'WrapperSimpleApp:0']
        ssh_moniter14 = moniter.Moniter('10.8.5.34', '22', 'root', '123456')
        jps_content14 = ssh_moniter14.jps_server()
        return self.compare_data(list_10_8_5_34, jps_content14)

    def compare_data(self, list1: list, list2: list):
        for i in list2:
            i = i.replace('\n', '').split()
            j = 0
            while j < len(list1):
                item2 = list1[j].split(':')
                if (item2[1] != '1' and item2[0] == i[1]):
                    list1[j] = i[1]+':1'
                j = j+1
        return list1
