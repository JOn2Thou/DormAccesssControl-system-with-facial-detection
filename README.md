1、运行MySQL和Redis，并在setting.py文件中配置数据库链接信息。
```
MySQL数据库使用5.7.27开发，建议使用相同版本(应该mysqlclient有向上兼容
项目自带Windows系统调试用Redis-x64-3.2.100，默认监听127.0.0.1，6379端口，requirepass为Qq111111
```
2、修改setting.py文件，进行下一步配置。
```
SMTP(邮箱SMTP功能，用于账户登录提示、邮箱发送验证码等功能)
ALiCloud_AFS(阿里云AFS人机验证，用于前端登录滑动验证)
```
3、生成数据表(像运行正常的Django项目一样使用指令)
```
python manage.py makemigrations
python manage.py migrate
```
4、导入初始系统设置数据
```
数据文件位置：/数据库/system_setting_systemsetting.sql

5.启动redis（cd到redis目录输入redis-server.exe redis.windows.conf）
```
6、启动项目(像运行正常的Django项目一样使用指令)
```
python manage.py runserver 127.0.0.1:8080
```
7.运行前端（cd到前端目录，输入python -m http.server）

