#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#    Life is short , you need Python !!!
#    Kelvin® kelvin.su@qq.com , Version 1.0 for Python 3.7.2 2019-05-21
"""
    此程序在Windows10、python3.7.2上测试成功
    paramiko模块登陆，并获取信息，程序运行需要两个文件，分别为Device_List.db和Command_list.conf
    Device_List.db 格式： 序号，IP地址，主机名，ssh端口号，用户名，密码    分隔用英文逗号(,)
    Command_List.conf 格式：每一行一个命令集，文件结尾不能有空行
"""
import paramiko
import time

NowDate=time.strftime("%Y%m%d", time.localtime())
NowTime=time.strftime("%H:%M:%S", time.localtime())
Separate_start="**************************** ["
Separate_end="] ****************************"

#设备返回信息保存目录
file_path='D:/test/'

def ssh_login(HostIPadd, HostName, HostPort, HostUser, HostPass):
    try:
        print("开始登陆主机【%s】，IP地址【%s】，并获取信息"%(HostName, HostIPadd))
        transport = paramiko.Transport(HostIPadd, HostPort)
        transport.connect(username=HostUser, password=HostPass)

        file_name = open(file_path+HostIPadd+"_"+HostName+"_"+NowDate+".txt", \
                         mode='a+' ,encoding="utf-8")
        file_name.write("主机名称：【"+HostName+"】"+"        "+ \
                        "主机地址：【"+HostIPadd+"】"+"        "+ \
                        "信息获取时间：【"+NowDate+" "+NowTime+"】"+"\n")
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        
        #设备命令列表
        command_name = open("D:/config/Command_List.conf",mode='r',encoding="utf-8")
        command_list = command_name.readlines()
        command_lens = len(command_list)
        for i in range(len(command_list)):
            file_name.write(Separate_start+command_list[i].strip('\n')+Separate_end+"\n")
            print(Separate_start+command_list[i].strip('\n')+Separate_end)
            stdin,stdout,stderr=ssh.exec_command(command_list[i].strip('\n'))
            print("    获取主机信息命令：[ %s ]"% command_list[i].strip('\n'))
            command_out = stdout.read().decode(encoding='utf-8')
            print(command_out)
            file_name.write(command_out)
        command_name.close()
        
        file_name.close()
        transport.close()
        print("IP地址【%s】，主机名【%s】，这是第【%s】台主机命令执行完毕" % (HostIPadd, HostName, HostNo))
    except ValueError:
        print("Error !!!")

if __name__ == "__main__":
    #设备地址、帐号等信息
    file_db = open("D:/config/Device_List.db",mode='r',encoding="utf-8")
    while 1:
        line = file_db.readline()
        if not line:
            break
        line = line.split(',')
        HostNo = line[0]
        HostIPadd = line[1]
        HostName = line[2]
        HostPort = int(line[3])
        HostUser = line[4]
        HostPass = line[5].replace("\r\n","").replace("\n", "")
        #print(HostNo, HostIPadd, HostName, HostPort, HostUser, HostPass)
        ssh_login(HostIPadd, HostName, HostPort, HostUser, HostPass)
    pass
