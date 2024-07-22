
[video(video-t2YWVOmZ-1640501970587)(type-bilibili)(url-https://player.bilibili.com/player.html?aid=507605863)(image-https://img-blog.csdnimg.cn/img_convert/650fb176724a15c696dbe55c03dadf5d.png)(title-程序运行视频)]

```python
# 2021 12 25 - Pandaoxi
# 快乐的电脑 程序
import pygame
from pygame.locals import *
from easygui import msgbox
from random import randint

pygame.init()
pygame.mixer.init()
canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption('快乐的电脑')
canvas.fill((255,255,255))
sound = pygame.mixer.Sound('./music.mp3')
sound.play()

def getEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            msgbox('电脑：你礼貌吗？不让我快乐？\n你想关掉这个窗口？\n不存在的。当然，电脑也不同意呢。','快乐的电脑','继续 HAPPY')
    
while True:
    canvas.fill((randint(0,255),randint(0,255),randint(0,255)))
    getEvent()
    pygame.display.update()
```
这一段程序，请谨慎运行。其中的`music.mp3`，请到[这里](https://pandaoxi2020.lanzouy.com/i9jvQxzboud)下载。
程序可以不断变更窗口颜色，让人眼花缭乱，而且关不掉，如果想要关掉请用任务管理器关，从窗口关的事件我在程序里改了。

