# Linux下的查找方法

* slug: Linux下的查找方法
* published: 2014-08-03 23:41
* tags: Linux, 查找
* category: linux

----------------------------------------------------------

* find /etc -type d –print 在/etc目录下查找所有的目录
* find . ! -type d –print 在当前目录下查找除目录以外的所有类型的文件
* find . -name "*.conf"  -mtime +5 -ok rm {  } \;
在当前目录中查找所有文件名以.conf结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示
