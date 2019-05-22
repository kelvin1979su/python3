# python3 部分运维脚本

## gat_info.py
本程序使用paramiko模块用ssh方式登录设备，并执行Command_List.conf内的命令，并将返回值保存在file_path变量的文件夹下。保存的文件命名为[IP地址_主机名_当天日期.txt]

程序运行需要两个文件，分别为Device_List.db和Command_list.conf
通过读取Device_List.db内的主机信息，使用paramiko模块登陆，执行Command_List内的命令，

**Device_List.db**
格式： 序号，IP地址，主机名，ssh端口号，用户名，密码
分隔用英文逗号(,)

**Command_List.conf**
格式：每一行一个命令集，文件结尾不能有空行
