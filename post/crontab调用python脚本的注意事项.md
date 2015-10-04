
# crontab调用python脚本的注意事项

* slug: crontab调用python脚本的注意事项
* published: 2014-08-09 17:41
* tags: crontab, python
* category: linux

----------------------------------------------------------

### 1、基本命令

* 查看： `crontab -l`
* 编辑： `crontab -e `
* 重启服务： `service crond restart`

### 2、语法格式

格式如下:

`f1 f2 f3 f4 f5 program`

其中 f1 是表示分钟，f2 表示小时，f3 表示一个月份中的第几日，f4 表示月份，f5 表示一个星期中的第几天。值的范围分别对应0－59，0－23，1－31，1－12，0－7（0和7都代表星期天）。program 表示要执行的程式。

* 当 f1 为 a-b 时表示从第 a 分钟到第 b 分钟这段时间内要执行，f2 为 a-b 时表示从第 a 到第 b 小时都要执行，其余类推
* 当 f1 为 \*/n 时表示每 n 分钟执行一次，f2 为 \*/n 表示每 n 小时执行一次，其余类推
* 当 f1 为 a, b, c,… 时表示第 a, b, c,… 分钟要执行，f2 为 a, b, c,… 时表示第 a, b, c…个小时要执行，其余类推
* 任何一个字段中的一个星号都是一个通配符。如果第一个字段含有一个星号，那个作业每分钟运行一次，以此类推，第二个字段含有通配符那就是每小时执行一次

#### 下面是两个例子：
* 每周六早上10点重启应用。
> 0 10 * * 6 sh /home/alexzhou/bin/restart_tuli.sh

* 每周二和每月的初一，十五的早上2点钟，更新solr索引。
> 0 2 1,15 * 2 python /home/alexzhou/update_index.py

### 3、调用 python 脚本时注意实现

如果程序是从 `if __name__ == "__main__":` 开始执行的话，在shell中可以运行执行，但在 crontab 中不能执行，所以脚本要调用的函数不能在 `if __name__ == "__main__": ` 中

代码示例:

``` python
def run():
       print "run"

if __name__ == "__main__":
     run（）
```

上面的脚本不会在crontab中运行， 需要改成如下方式：

``` python
def run():
    print "run"
run()
```

### 四、当前目录的问题，配置文件等要使用绝对路径

例如：

``` python
logging.config.fileConfig("log.conf")
```

由于 crontab 执行时，脚本的当前目录已经改变，此时 log.conf 会找不到，会造成程序错误退出。
要修改为如下方式：  

``` python
logging.config.fileConfig("/home/terry/python/web/log.conf")
```
