# DB-Project
数据库诗词查询Web项目。

# 相关配置介绍

本地测试环境：Windows系统

后端：Django

前端：Layui

数据库：MySQL5.6

服务器：Centos7.6+Apache2.4.46+Pure-Ftpd 1.0.49+Python3.7




# 本地测试过程

编写完代码后，采用以下步骤，可在本地电脑访问页面：

1. 在电脑中配置好python环境，并安装MySQL；

2. 使用以下指令，在python中下载django包和pymysql包：

   python环境：`pip install django`  和 `pip install pymysql`

   anaconda环境：`conda install django` 和 `conda install pymysql`

3. 在数据库中，运行db.sql文件，生成数据库中所需要的表；

4. 启动windows命令行，进入mysql目录，输入  `net start mysql`  启动数据库；

5. 进入该项目目录，输入 `python manage.py runserver 0.0.0.0:80`  启动服务器；

6. 打开任意浏览器，通过链接 http://localhost/login/index.html 进入登录注册界面；

7. 成功注册且登录后，即可测试相关功能。



# 客户端测试过程

1. 打开浏览器
2. 访问http://101.34.34.103:8088/login/index.html
