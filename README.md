## 0. 接口自动化测试

1. 什么情况要用接口自动化测试 ( pytest + requests + allure )

2. 什么时候要用 ui 自动化测试 （pytest + seleniume ）

3. jmeter 压力测试

前后端分离
前端： vue
后端： 接口 

postman 接口调试工具

json : 序列化格式

## 1. 添加依赖
按 requirements.txt 说明添加依赖

```
pip install pytest
pip install pytest-rerunfailures #失败后重试
pip install requests 
pip install json # json 处理
pip install xlrd # excel 处理
pip install yaml # yaml 文件处理
```

## 2. 框架文件说明

1. config ---> 配置文件
2. data   ---> 测试
3. report ---> 测试报告
4. tests  ---> 测试用例
5. utils  ---> 工具类

## 3. 登陆方式说明

食安系统使用 oauth2 +jwt 接口验证说明， 模拟登陆的方式
1. 模拟登陆 /login.do ,并返回 jwt 的token 
2. 在每次请求中 添加请求头 header "Authorization":"Bears {jwt}"

## 4. http 请求参数说明
https://www.cnblogs.com/jpfss/p/10979583.html

1、HTTP请求方式

如下表：

GET 向Web服务器请求一个文件

POST 向Web服务器发送数据让Web服务器进行处理

PUT 向Web服务器发送数据并存储在Web服务器内部

HEAD 检查一个对象是否存在

DELETE 从Web服务器上删除一个文件

CONNECT 对通道提供支持

TRACE 跟踪到服务器的路径

OPTIONS  查询Web服务器的性能

 2. User-Agent

说明：

HTTP客户端运行的浏览器类型的详细信息。通过该头部信息，web服务器可以判断到当前HTTP请求的客户端浏览器类别。

实例： User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11

3. Content-Type

说明：

显示此HTTP请求提交的内容类型。一般只有post提交时才需要设置该属性。

实例：

Content-type: application/x-www-form-urlencoded;charset:UTF-8

有关Content-Type属性值可以如下两种编码类型：

（1）“application/x-www-form-urlencoded”： 表单数据向服务器提交时所采用的编码类型，默认的缺省值就是“application/x-www-form-urlencoded”。 然而，在向服务器发送大量的文本、包含非ASCII字符的文本或二进制数据时这种编码方式效率很低。

（2）“multipart/form-data”： 在文件上载时，所使用的编码类型应当是“multipart/form-data”，它既可以发送文本数据，也支持二进制数据上载。

当提交为单单数据时，可以使用“application/x-www-form-urlencoded”；当提交的是文件时，就需要使用“multipart/form-data”编码类型。

在Content-Type属性当中还是指定提交内容的charset字符编码。一般不进行设置，它只是告诉web服务器post提交的数据采用的何种字符编码。

一般在开发过程，是由前端工程与后端UI工程师商量好使用什么字符编码格式来post提交的，然后后端ui工程师按照固定的字符编码来解析提交的数据。所以这里设置的charset没有多大作用。

4. cookie

说明： HTTP请求发送时，会把保存在该请求域名下的所有cookie值一起发送给web服务器。


5.  接口验证

oauth 
JWT 接口签名验证


6. pytest 

1. fixture : https://www.cnblogs.com/superhin/p/11455376.html
2. @pytest.mark.parametrize  https://www.cnblogs.com/superhin/p/11477620.html

7. test  

    setup() 前置条件
    test_function1
    test_function2
    teardown () 后置条件