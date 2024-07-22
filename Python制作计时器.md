今天我们来制作一个计时器，需要使用`pygame`，自行安装。话不多说，直接看代码：

```python
import pygame
from pygame.locals import *
from time import sleep

pygame.init()
count = 0

def fillText(content,cn):
    global canvas
    canvas = pygame.display.set_mode((1200,35))
    pygame.display.set_caption('计时器')
    canvas.fill((225,225,225))

    fonts = pygame.font.SysFont('Courier New',25,bold = 1)
    renderFont = fonts.render(str(content),1,(0,0,0))
    canvas.blit(renderFont,(0,0))

def exitEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

while True:
    exitEvent()
    fillText('the number of seconds remaining:%d' % (count),(0,12))
    count += 1
    sleep(1)
    pygame.display.update()
```

