@[TOC]

<hr>

# 一、前言


我最近在参加世青赛，参加了`Python`组，需要通过`CodeCombat`闯关。为了方便他人学习，特此编写。

`CodeCombat`共20关，还有一个竞技场。以下为详细通关攻略及代码。

<hr>

# 二、通关过程及代码
## 第一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b62d371926114376aec9fbb7eeab719d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 向宝石进发。
# 小心尖刺！
# 在下面输入你的代码，完成后点击运行。

hero.moveRight()
hero.moveDown()
hero.moveRight()


```

<hr>

## 第二关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/703442de32c94f67a8b83fe42bc0ac95.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 利用你的移动命令收集所有宝石。

hero.moveRight()
hero.moveDown()
hero.moveUp(2)
hero.moveRight()


```

<hr>

## 第三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b16725890feb41e8833a0f2ce229c9cb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)


```python
# 避开食人魔的视线，收集宝石。
hero.moveRight()
hero.moveUp()
hero.moveRight()
hero.moveDown()
hero.moveRight()


```

<hr>

## 第四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9e25fb9dd4f045c1aac53b235a4a69a5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 使用带参数的移动命令，移动到更远。
hero.moveRight(3)
hero.moveUp()
hero.moveRight()
hero.moveDown(3)
hero.moveRight(2)


```

<hr>

## 第五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/125bd017c3c04b449fd840ea70901d39.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 抵御 "Brak" 和"Treg"！
# 小食人魔攻击两次才会被击败。

hero.moveRight()
hero.attack("Brak")
hero.attack("Brak")
hero.moveRight()
hero.attack("Treg")
hero.attack("Treg")
hero.moveRight(2)


```

<hr>

## 第六关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ea5a5a9eb3ba4cf08e489fda88e2ef3d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python


hero.say("密码是什么？")
# 使用 “say()” 函数说出密码。
# 密码是: "Achoo"

hero.say("Achoo")
hero.moveUp(2)

```

<hr>

## 第七关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e72be72ed8054d4c9f03754546c9b2d0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你需要图书馆大门的开门密码！
# 密码就在 提示 中！
# 请点击代码窗口上的蓝色 “提示” 按钮。
# 如果你在关卡中遇到了困难，请点击 “提示” 按钮！

hero.moveRight()
hero.say("我还不知道密码呢！")  # ∆
hero.say("Hush")
hero.moveRight()


```

<hr>

## 第八关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/586588a409c7416681fff9c952e88c20.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 释放囚犯，击败守卫并夺取宝石。
hero.moveRight()
# 从"Weak Door"后解救Patrick。
hero.attack("Weak Door")
# 击败名为"Two"的守卫。
hero.moveRight(3)
hero.moveDown()
for i in range(5):
    hero.attack("Two")
# 获得宝石。
hero.moveDown(2)


```

<hr>

## 第九关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e223f11b27b41e99ab17064f764b408.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 代码通常按编写顺序执行。
# 循环会多次重复一个代码块。
# 按Tab或4个空格，把移动指令缩进到循环内部。

while True:
    hero.moveRight()
    # 在这里给循环里加 moveLeft 命令。
    hero.moveLeft()
    

```

<hr>

## 第十关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a206a944953f4e1fb2078b0651beac50.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 循环是处理重复事情的最好方法。

while True:
    # 在这里添加需要重复运行的命令。
    hero.moveRight(2)
    hero.moveUp(2)
    

```

<hr>

## 第十一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c8277f2828e04850a357807115ee75bd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 使用少于5条语句穿越迷宫
while True:
    hero.moveRight(2)
    hero.moveDown()
    

```

<hr>

## 第十二关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b8cf8acdb9904c29a5bbfa8ef43a539a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 攻击大门(“Door”)
# 需要攻击很多次,请使用"while-true"循环

while True:
    hero.attack("Door")

```

<hr>

## 第十三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a2e8503968094156ae2537a50a308554.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你可以在循环前写代码
hero.moveRight()
# 在使用循环逃离迷宫之前，打开"Chest"！
hero.moveUp()
hero.attack("Chest")
# 回到主走廊
hero.moveDown()
while True:
    # 移动3次
    hero.moveRight(3)
    # 再走动三次
    hero.moveDown(3)
    
    
```

<hr>

## 第十四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2f337f7eb6fa4895b557ea2ccec739f2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 周围可能有东西能帮到你。
hero.moveUp()
hero.moveRight(2)
# 首先，移动到橱柜。
hero.moveDown(2)
# 然后，使用while-true循环攻击"Cupboard"（橱柜）。
while True:
    hero.attack("Cupboard")

```

<hr>

## 第十五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c03de5fcb81846e293ac24e563110dcf.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你可以像名牌那样使用变量

enemy1 = "Kratt"
enemy2 = "Gert"
enemy3 = "Ursa"

def attackEnemy(name):
    for i in range(2):
        hero.attack(name)
        
attackEnemy(enemy1)
attackEnemy(enemy2)
attackEnemy(enemy3)

```

<hr>

## 第十六关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c8122ba1f5e646bdb911b2ddca2f3cec.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你的英雄不知道这些敌人的名字！
# 这眼镜给了你 “findNearestEnemy” 寻找最近敌人的能力。

# 将hero.findNearestEnemy()的结果赋值给变量enemy1：
enemy1 = hero.findNearestEnemy()
# enemy1现在指向最近的敌人。使用变量进行攻击！
hero.attack(enemy1)
hero.attack(enemy1)

# enemy1已被打败，再次调用hero.findNearestEnemy()将会找到附近的新敌人。
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.attack(enemy2)

# 将hero.findNearestEnemy()的结果赋值给变量enemy3：
enemy3 = hero.findNearestEnemy()
# 现在使用enemy3变量进行攻击。
hero.attack(enemy3)
hero.attack(enemy3)

```

```python
# 或者使用这种冒险的行为（可能会被要求重载源码）
def attackEnemy():
    enemy = hero.findNearestEnemy()
    for i in range(2):
        hero.attack(enemy)

for i in range(3):
    attackEnemy()

```

<hr>

## 第十七关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c69bc0b77333442b9e70a41613c90216.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 创建第二个变量并进行攻击.

enemy1 = hero.findNearestEnemy()
hero.attack(enemy1)
hero.attack(enemy1)

enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.attack(enemy2)

hero.moveDown()
hero.moveRight(2)


```

<hr>

## 第十八关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a586af5098534bb1a06554db14f3851c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 使用while-true循环移动并攻击目标。

while True:
    hero.moveRight()
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    for i in range(2):
        hero.attack(enemy)
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()
    

```

<hr>

## 第十九关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/78389a9fc57243f882bfbbcebff9dcdc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 建造三个围栏来阻挡食人魔！

hero.moveDown()
hero.buildXY("fence", 36, 34)
hero.buildXY("fence", 36, 30)
hero.buildXY("fence", 36, 26)
hero.moveRight(3)

```

<hr>

## 第二十关（竞技场）
规则：

```python
# 欢迎来到Wakka Maul竞技场！准备战斗！
# 通过迷宫，获得宝石来增强战力。
# 毁掉门来释放盟友（或是敌人）。
# 例如，攻击标有"g"的门，使用:
#hero.attack("g")
# 有了足够金币，你就能够招募你想要的战士！
#hero.say("soldier") 招募1名士兵，花费20金币！
#hero.say("archer") 招募1名弓箭手，花费25金币！
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3e5e5e617df945d5981e41fdd6f1c668.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 欢迎来到Wakka Maul竞技场！准备战斗！
# 通过迷宫，获得宝石来增强战力。
# 毁掉门来释放盟友（或是敌人）。
# 例如，攻击标有"g"的门，使用:
#hero.attack("g")
# 有了足够金币，你就能够招募你想要的战士！
#hero.say("soldier") 招募1名士兵，花费20金币！
#hero.say("archer") 招募1名弓箭手，花费25金币！

hero.moveUp(2)
hero.moveRight(2)
hero.moveUp(0.5)
hero.moveDown(1)

while True:
    hero.say("archer")
    hero.say("soldier")

```
超级简单，说白了就是去拿宝箱，有了金币就可以拿到很多小兵。

<hr>

# 三、竞技场
## 蓝方竞技场
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8b4bb17195d14c0b81c30a590d0af560.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/cfcdf01f5c4c4fd7b4284d7f95233cd9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
目前蓝方取得第12名的成绩。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c4ef51a5dbb14622bccf92b70b6902a0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 欢迎来到Wakka Maul竞技场！准备战斗！
# 通过迷宫，获得宝石来增强战力。
# 毁掉门来释放盟友（或是敌人）。
# 例如，攻击标有"d"的门，使用:
#this.attack("d")
# 有了足够金币，你就能够招募你想要的战士！
#hero.say("thrower") 招募2名投矛手，每个9金币！
#hero.say("scout") 花费18金币招募侦察兵。

hero.moveDown(3)
hero.moveLeft(2)
hero.moveUp(4)
hero.moveRight()
hero.attack("d")
hero.moveLeft(4)
hero.moveDown()
hero.attack("b")
hero.attack("c")
hero.moveDown(1.3)
while True:
    hero.say("scout")
    hero.say("thrower")

```
另一种解法是：

```python
# 欢迎来到Wakka Maul竞技场！准备战斗！
# 通过迷宫，获得宝石来增强战力。
# 毁掉门来释放盟友（或是敌人）。
# 例如，攻击标有"d"的门，使用:
#this.attack("d")
# 有了足够金币，你就能够招募你想要的战士！
#hero.say("thrower") 招募2名投矛手，每个9金币！
#hero.say("scout") 花费18金币招募侦察兵。

hero.moveUp()
hero.moveLeft()
hero.attack("d")
hero.moveLeft()
hero.moveDown(3.5)
hero.moveUp(0.5)
hero.moveRight(1.5)
hero.moveLeft(0.5)
hero.moveUp()
hero.moveLeft(0.5)
while True:
    hero.say("thrower")
    hero.say("scout")

```
经过我几次改进，最终代码为：

```python
# 欢迎来到Wakka Maul竞技场！准备战斗！
# 通过迷宫，获得宝石来增强战力。
# 毁掉门来释放盟友（或是敌人）。
# 例如，攻击标有"d"的门，使用:
#this.attack("d")
# 有了足够金币，你就能够招募你想要的战士！
#hero.say("thrower") 招募2名投矛手，每个9金币！
#hero.say("scout") 花费18金币招募侦察兵。

hero.moveUp()
hero.moveLeft()
hero.attack("d")
hero.say("scout")
hero.moveLeft()
hero.moveDown(3.5)
hero.moveUp(0.5)
hero.moveRight(1.5)
hero.moveLeft(0.5)
hero.moveUp()
hero.moveLeft(0.5)
while True:
    hero.say("thrower")
    hero.say("scout")

```


<hr>

## 红方竞技场
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/57586bf2eacc4f7d8bbc76da26825403.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
别看代码少，拿的分可不少，才7行我就第三名了。蓝方得有十几行，才拿十几名，这些代码可谓短小精炼了。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f695a8a872a24f1dafe5329eb94dbcfb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
我作死挑战了对面第一名，结果胜了！
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7861cd12785f4e57bd4e269c04807798.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
第二名我也赢了。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/801a8ef46a9141a0a09f97f3a8fb0ea9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
第三名也是。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6676bd441d574d01a9ba2cd63db0aa5c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 欢迎来到Wakka Maul竞技场！准备战斗！
# 通过迷宫，获得宝石来增强战力。
# 毁掉门来释放盟友（或是敌人）。
# 例如，攻击标有"g"的门，使用:
#hero.attack("g")
# 有了足够金币，你就能够招募你想要的战士！
#hero.say("soldier") 招募1名士兵，花费20金币！
#hero.say("archer") 招募1名弓箭手，花费25金币！

hero.moveUp(2)
hero.moveRight(2)
hero.moveUp(0.3)
hero.moveDown(0.6)

while True:
    hero.say("archer")
    hero.say("soldier")

```
<hr>

截至2021年8月30日15时05分，我的石家庄市排名为：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1f6450cfdb2f4078a5a0a2cc8b1c985a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

