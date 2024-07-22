今天我们来实现一下VBS循环说数字的效果。
新建一个文本文档，改拓展名为`.vbs`或`.vbe`，输入以下内容：

```vbnet
set sapi = createObject("Sapi.SpVoice")
for i = 1 to 100
sapi.Speak i
Next
```
保存，退出，运行，就能听见标准“讲述人”的声音了！
