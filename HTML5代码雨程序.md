上次我们制作了`cmd`的数字雨程序（[点击这里查看](https://blog.csdn.net/PanDaoxi2020/article/details/108146578)），这一次我们使用HTML来制作。
先简单介绍一下HTML：

> HTML又叫`超文本标记语言`，标准通用标记语言下的一个应用。 “超文本”就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。 超文本标记语言的结构包括“头”部分（`<head>`）、和“主体”部分（英语：`<body>`），其中“头”部提供关于网页的信息，“主体”部分提供网页的具体内容。

我们开始写代码：
1.新建一个文本文档，输入以下内容（有开发工具的可以用开发工具）：

```html
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <title>NumberRain</title>
  <style type="text/css">
   canvas{
    display: block;
    }
  </style>
 </head>
 <body>
  <canvas id="canvas"></canvas>
  <script>
    function $(id){
      return document.getElementById(id);
    }
   var mywindow=window.screen;
   var canvas=$("canvas");
   canvas.width=mywindow.width;
   canvas.height=mywindow.height;
   var str="0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()-+{}|:<>?,.";
   str=str.split("");
   var fontSize=16;
   var cols=canvas.width/fontSize;
   var drops=[];
   for(var i=0;i<cols;i++){
     drops[i]=1;
   }
   var ctx=canvas.getContext("2d");
   function draw(){
    ctx.fillStyle="rgba(0,0,0,0.05)";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.fillStyle="green";
    ctx.font=fontSize+"px arial";
    for(var i=0;i<cols;i++){
      var text=str[ Math.floor( Math.random() * (str.length) ) ];
      ctx.fillText(text,i*fontSize,drops[i]*fontSize);
      if(drops[i]*fontSize > canvas.height || Math.random() > 0.95)
          drops[i] = 0;
      drops[i]++;
    }
  }
  setInterval(draw,33);
 </script>
</body>
</html>
```
代码写完后保存退出，改拓展名为`.html`或`.htm`，效果大家自己尝试，非常好看。

注：在CSDN博客里也可以直接调用HTML标签！

<u>这是使用u标签（下划线）</u>
<b>这是使用b标签（加粗）</b>
<i>这是使用i标签（倾斜）</i>
<del>这是使用del标签（删除线）</del>
<a href="https://www.baidu.com" target="_blank">这是使用a标签（超链接，代码是`<a href="https://www.baidu.com" target="_blank">`）</a>

这是编辑区：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200821145153334.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
这是效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200821145219899.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)

