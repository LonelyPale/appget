# 设计 design

# 权限
需要root用户

# 目录
所有软件都按照这个规则
/usr/local/bin 创建可执行文件的快捷方式
/usr/local/app 安装软件的目录
/usr/local/app/appget 自身的目录
/usr/local/app/appget/bin 可执行文件的目录
/usr/local/app/appget/lib 库文件的目录，appget、applib(public)的python包和其他要用到的库安装到这个目录
/usr/local/app/appget/plugins 插件目录
/usr/local/app/appget/plugins/myapp 自定义私有的软件安装脚本目录myapp(private)
/usr/local/app/appget/config/appget.toml 配置文件

# 配置文件
```toml

```
