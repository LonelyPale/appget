# 设计 design

# 版本 0.1.0

# 权限
需要root用户

# 目录
所有软件都按照这个规则
/usr/local/bin 创建可执行文件的快捷方式
/usr/local/app 安装软件的目录
/usr/local/app/app123 已安装app
/usr/local/app/app123/.appget 已安装app的安装脚本目录，用于卸载、查询、显示基本信息
/usr/local/app/appget 自身的目录(特殊：无version和.appget子目录)
/usr/local/app/appget/bin 可执行文件的目录
/usr/local/app/appget/lib 库文件的目录，appget、applib(public)的python包和其他要用到的库安装到这个目录
/usr/local/app/appget/plugins 插件目录
/usr/local/app/appget/plugins/myapp 自定义私有的软件安装脚本目录myapp(private)
/usr/local/app/appget/config/appget.toml 配置文件

# app脚本文件
* 一个app的name和filename必须是唯一的（推荐二者相同），否则出现同名app时会互相覆盖
* 一个app只允许存在一个版本
* app脚本必须是一个独立的文件，不允许拆分为多个文件放到子目录下，这样不方便管理

## 全局的app脚本文件
* 必须位于applib或myapp包内，可以有多级子目录（推荐以功能来划分）
* 必须通过`__init__.py`把子模块导入到根模块内（加载器只从根模块读取app脚本类）

## 已安装的app脚本文件
* 由`全局的app脚本文件`拷贝而来
* 必须位于app安装目录内的`.appget`子目录内

# 配置文件
```toml

```


