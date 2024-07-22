@[TOC](目录)

# 一、前言
前面一直在努力学习，学习了`codecombat`新一期的计算机科学课程，涉及到了许多其他的东西。以前的移动函数有5个，但是复赛就1个；以前的攻击函数只有1个，但是复赛有2个。
关卡也比原来多了，学习的东西自然不同。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/cc148637385f45e8a1373106896f9cf4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
下面是具体的闯关过程及源代码。
# 二、具体闯关流程（1~23）
## 第一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/88011dcf745e4bad934fe1e8ce658f6e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 在标记上建造两段围栏来保护村民。
# 把鼠标悬停在地图上，以得到X,Y坐标。

hero.buildXY("fence", 40, 52)
hero.buildXY("fence", 40, 20)

```
## 第二关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1ca17b99678d439b996cf405b25a128c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 到小路的尽头去，并在那儿修一个栅栏。
# 利用你的 moveXY(x, y)坐标移动功能。
hero.moveXY(36, 60)
hero.moveXY(37, 13)
hero.buildXY("fence", 72, 25)

```

## 第三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2003b42205de4a36b3a741a6d405d650.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 英雄完全糊涂了！
# 纠正路径，别让其踩到地雷。

hero.moveXY(11,37)
hero.moveXY(35, 25)
hero.moveXY(40, 56)
hero.moveXY(77, 58)

```

## 第四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/66fa37749dc94e6c926e64441bb1ac36.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 区域内有一名猎头者！
# 在森林附近跑动，以躲避他的视线

while True:

    # 用 moveXY 在森林中保持移动，以确保存活。
    # 不要忘记缩进。
    hero.moveXY(56, 44)
    hero.moveXY(40, 56)
    hero.moveXY(24, 44)
    hero.moveXY(24, 24)
    hero.moveXY(40, 12)
    hero.moveXY(56, 24)

```

## 第五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/fd2d9ecb89d74d01a400ea5408002c32.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 通过林地，务必留意危险！
# 这些森林小屋中可能有食人魔！

hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# if语句会检查某变量有没有食人魔。
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(49, 51)
enemy = hero.findNearestEnemy()
if enemy:
    # 在这里攻击敌人：
    hero.attack(enemy)
    hero.attack(enemy)
    # `pass`语句是占位符，不做任何事情，它只帮助结束if语句。
    pass

hero.moveXY(58, 14)
enemy = hero.findNearestEnemy()
# 使用if语句检查敌人是否存在：
if enemy:
    # 如果敌人存在，就攻击它：
    hero.attack(enemy)
    hero.attack(enemy)

    
```

## 第六关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/81d8ee1a8bf84100b172ec2c0223d96e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 记得敌人可能还不存在。
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # 如果有敌人，攻击它！
        hero.attack(enemy)
        hero.attack(enemy)
        pass

```

## 第七关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4d93f48b259c4280abb68da725ff9007.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 记得敌人可能还不存在。
while True:
    enemy = hero.findNearestEnemy()
    # 如果有敌人，攻击它！
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)

    

```

## 第八关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6a02b1ef98fb44a6828c4da609ebbfab.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 在食人魔的营地中打败它们！

while True:
    enemy = hero.findNearestEnemy()
    # 使用一个 “if” 语句去检查是否有敌人存在:
    if enemy:
        # 攻击敌人，如果存在的话：
        hero.attack(enemy)
        hero.attack(enemy)

```

## 第九关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ecda67b9a44646929e24892f526a5cb5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 在村口巡逻。
# 如果发现敌人，就攻击它。
while True:
    hero.moveXY(35, 34)
    leftEnemy = hero.findNearestEnemy()
    if leftEnemy:
        hero.attack(leftEnemy)
        hero.attack(leftEnemy)
    # 现在移动到右侧入口。
    hero.moveXY(60, 31)
    # 再次使用findNearestEnemy，来找到右侧的敌人。
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    # 如果有右侧的敌人，使用"if"来攻击。
    hero.moveXY(35, 34)

```

## 第十关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/af5e6881c9654b62b738ef1c94e3b9a7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 在村口巡逻。
# 当你见到食人魔时，建造一个火焰陷阱"fire-trap"。
# 不要让任何农民受到误伤。

while True:
    hero.moveXY(43, 50)
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 43, 50)

    hero.moveXY(25, 34)
    left = hero.findNearestEnemy()
    # 检查`left`是否存在。
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 25, 35)
    top = hero.findNearestEnemy()
    if top:
        hero.buildXY("fire-trap", 43,20 )

    hero.moveXY(25, 34)
    left = hero.findNearestEnemy()
    if left:
        # 在25,34处建造一个陷阱，如果敌人存在的话。
        hero.buildXY("fire-trap", 25, 34)
    hero.moveXY(43, 20)
    # 为下面的敌人设置一个变量。
    enemy = hero.findNearestEnemy()
    # 检查下面是否有敌人存在。
    if enemy:
        # 在43,20处建造一个陷阱，如果敌人存在的话。
        hero.buildXY("fire-trap", 43, 20)

```

## 第十一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9f99a1d8994c44ffb757b99672240e12.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 待在中间防守！

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # 亦或主动出击…
        hero.attack(enemy)
        hero.attack(enemy)
        pass
    else:
        # …亦或回到你的阵地防守。
        hero.moveXY(40, 35)
        pass

```

## 第十二关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/abe6d399fb9841c7a781459ea319d988.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 如果有敌人，那么就攻击它。
# 否则，攻击宝箱！

while True:
    # 使用if/else语句。
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        hero.attack(enemy)
    else:
        hero.attack("Chest")
    
    
```

## 第十三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ba5f3c22d6e84961b66ca540cf7a83f9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 尽可能多地使用你的新技能"cleave"。

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        # 用“Cleave”干掉敌人！
        hero.cleave(enemy)
        pass
    else:
        # 否则（如果“cleave”还没准备好），就用普通攻击。
        hero.attack(enemy)
        pass

```

## 第十四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/34f9fb38bd1946548f3ba0dd1272e212.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 劈斩正在10秒冷却中。
# 使用 else 语句在恢复时防守。

while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave()
    # 写个 else: 当"cleave"没有准备好时做点别的什么。
    else:
        # 确保攻击敌人：
        hero.attack(enemy)
        
```

## 第十五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/02d3bd2dac4b4407aaf05e6c7cc94c42.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 矮人正在攻击！
# 攻击会有规律的一波波袭来。
# 可以的话，使用劈斩来清理大量敌人。

while True:
    enemy = hero.findNearestEnemy()
    # 使用带有‘isReady’的if语句来检查 "cleave"：
    if hero.isReady("cleave"):
        # 劈斩！
        hero.cleave(enemy)
    # 否则，如果 cleave 还没准备好的话：
    else:
        # 攻击最近的食人魔！
        hero.attack(enemy)


```

## 第十六关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/571d04962c294d0a910644d18847e806.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 食人魔正在森林中巡视！
# 使用distanceTo方法找到敌人在哪。
# 说出与每个敌人的距离，告诉大炮向哪开火！

enemy1 = "Gort"
distance1 = hero.distanceTo(enemy1)
hero.say(distance1)

enemy2 = "Smasher"
distance2 = hero.distanceTo(enemy2)
# 说出distance2变量！
hero.say(distance2)
# 不要攻击友方！
friend3 = "Charles"

# 最后的食人魔。
enemy4 = "Gorgnub"
# 确定并说出与enemy4之间的距离：
distance3 = hero.distanceTo(enemy4)
hero.say(distance3)

```

## 第十七关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6dfe56eabc1e40259ec2dedfa062a888.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # 如果他们与农民太近，就攻击他们
        hero.attack(enemy)
        pass
    # 否则的话，呆在农民旁边！使用else
    else:
        hero.moveXY(40, 37)
    
```

## 第十八关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9863430df8ef4300bf6938eef5a451fb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
while True:
    # 检查与最近敌人的距离。
    nearestEnemy = hero.findNearestEnemy()
    distance = hero.distanceTo(nearestEnemy)
    # 如果它接近到10m以内，使用cleave！
    if distance <= 10:
        if nearestEnemy:
            hero.cleave(nearestEnemy)
    # 否则，根据名字攻击"Chest"（宝箱）。
    else:
        hero.attack("Chest")
    
```

## 第十九关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4fa063f047934ffe8be3015c04eda093.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 又一个宝箱等待英雄打开！
# 攻击宝箱来打开它。
# 有些食人魔矮人可不会呆呆地站着，看着你攻击！
# 当食人魔离你太近时，你得学着保护你自己

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady("cleave"):
        # 如果劈斩就绪，优先使用劈斩：
        hero.cleave(enemy)
    elif distance < 5:
        # 如果离你最近的食人魔矮人离得太近，攻击它：
       hero.attack(enemy)
    else:
        # 否则，尝试打开宝箱：
        # 使用宝箱的名称来进行攻击："Chest"。
        hero.attack("Chest")
        pass
    

```
## 第二十关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b60197d37d9b45caa90ec1c605e14f3b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 在这关，别碰恶魔石！往其他方向移动避开它们！
while True:
    evilstone = hero.findNearestItem()
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:     # ==的意思是"is equal to""（等于）
            # 如果恶魔石在左边，走到右边。
            hero.moveXY(46, 22)
            pass
        else:
            # 如果恶魔石在右边，走到左边。
            hero.moveXY(34, 22)
            pass
    else:
        # 如果没有恶魔石，那就去到中间。
        hero.moveXY(40, 22)
        pass

```

## 第二十一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4c4dc97d0e824a1195ed2276193175c4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你可以将一个if语句放到另一个if语句当中。
# 你必须注意这些if语句是如何互相影响的。
# 请确保代码缩进正确！
# 从外层if/else结构开始会有帮助。
# 使用注释为内层if/else占位预留空间：

while True:
    enemy = hero.findNearestEnemy()
    # 如果有敌人出现，那么就...
    if enemy:
        # 使用distanceTo创建一个距离变量。
        distance = hero.distanceTo(enemy)
        # 如果敌人与你的距离小于5米，那么就攻击。
        if distance < 5:
            hero.attack(enemy)
        # 否则（敌人还离得很远），那么就使用shield。
        else:
            hero.shield()
            
        pass
    # 否则（没有敌人）...
    else:
        # …那么，回到X位置。
        hero.moveXY(40, 34)

```

## 第二十二关
### （1）主关卡
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/941fd530cd444ec89d641323bec2e528.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # 用 distanceTo 获取与敌人的距离。
        distance = hero.distanceTo(enemy)
        # 如果距离小于5米...
        if distance<5:
            # ...如果"cleave"技能准备好了，就用cleave干掉他们！
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            # ...否则，仅仅进行普通攻击。
            else:
                hero.attack(enemy)

```
### （2）练习A
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/36287df5ed824b91a9ae976b548a9e3a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # pass  # 用你自己的代码替换这行。
        # 用 distanceTo 获取与敌人的距离。
        distance = hero.distanceTo(enemy)
        # 如果距离小于5米...
        if distance < 5:
            # ...如果"cleave"技能准备好了，就用cleave干掉他们！
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            # ...否则，仅仅进行普通攻击。
            else:
                hero.attack(enemy)

```
### （3）练习B
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/58c1bdbfb39a47339eb4d599d43104fc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # pass  # 用你自己的代码替换这行。
        # 用 distanceTo 获取与敌人的距离。
        distance = hero.distanceTo(enemy)
        # 如果距离小于5米...
        if distance < 5:
            # ...如果"cleave"技能准备好了，就用cleave干掉他们！
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            # ...否则，仅仅进行普通攻击。
            else:
                hero.attack(enemy)

```
## 第二十三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/570e09baf9ff422f807613fa93d3ab38.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 这定义了findAndAttackEnemy函数
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# 这段代码不是函数的一部分。
while True:
    # 现在你可以使用findAndAttackEnemy在村子里巡逻
    hero.moveXY(35, 34)
    findAndAttackEnemy()
    
    # 现在移动到右侧入口。
    hero.moveXY(60, 31)
    # 使用findAndAttackEnemy
    findAndAttackEnemy()

```

# 具体闯关流程（24~45）
## 第二十四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/18d9d8f365574c80a1647432ef294832.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 这个函数攻击最近的敌人。
def findAndAttackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# 定义一个函数来劈斩敌人（只在劈斩就绪时）。
def findAndCleaveEnemy():
    # 找到最近的敌人：
    enemy = hero.findNearestEnemy()
    # 如果敌人存在：
    if enemy:
        # 而且，如果"cleave"就绪了：
        if hero.isReady("cleave"):
            # 是时候使用劈斩了！
            hero.cleave(enemy)
    pass

# 在主循环中，巡逻、劈斩和攻击。
while True:
    # 移动到巡逻点，劈斩和攻击。
    hero.moveXY(35, 34)
    findAndCleaveEnemy()
    findAndAttackEnemy()
    
    # 移动到另一点：
    hero.moveXY(60, 31)
    # 使用findAndCleaveEnemy函数：
    findAndCleaveEnemy()
    # 使用findAndAttackEnemy函数：
    findAndAttackEnemy()

```
## 第二十五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/394cdc58b1a749fabe3087c9fb0046bb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 食人魔矮人来袭！保护镇子！

# 定义你自己的函数来对抗敌人！
def cleaveOrAttack():
    # 在函数中，找到敌人，然后劈斩或是攻击它。
    ogre = hero.findNearestEnemy()
    if ogre:
        if hero.isReady("cleave"):
            hero.cleave(ogre)
        # 否则，攻击食人魔：
        else:
            hero.attack(ogre)

# 在巡逻点之间移动并调用函数。
while True:
    hero.moveXY(35, 34)
    # 使用上面定义的cleaveOrAttack函数。
    cleaveOrAttack()
    hero.moveXY(47, 27)
    # 再次调用函数。
    cleaveOrAttack()
    hero.moveXY(60, 31)
    # 再次调用函数。
    cleaveOrAttack()

```
## 第二十六关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ec52d3cf75444ba4b6f2067a345f3d5b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 差役试图偷取你的硬币！
# 编写一个函数，在差役盗取硬币前将其干掉。

def pickUpCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

# 在下方写一个攻击敌人的函数attackEnemy。
# 寻找最近的敌人，如果存在敌人就进行攻击。
def attackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    attackEnemy() # ∆ 在写好 attackEnemy 函数后取消这一行的注释。
    pickUpCoin()

```

## 第二十七关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9a95a28592f945f5a089f40e1cb84ca3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 使用 checkAndAttack 函数让代码易读。

# 这个函数有一个形式参数。
# 形式参数是一种给函数传递信息的方式。
def checkAndAttack(target):
    # 形式参数'target'只是一个变量！
    # 它会容纳函数调用时的实际参数。
    if target:
        hero.attack(target)
    hero.moveXY(43, 34)

while True:
    hero.moveXY(58, 52)
    topEnemy = hero.findNearestEnemy()
    # 使用带topEnemy变量的checkAndAttack函数。
    checkAndAttack(topEnemy)

    # 移动到底部的X标记处。
    hero.moveXY(58, 16)    
    # 创建名为 bottomEnemy 的变量并寻找最近敌人。
    bottomEnemy = hero.findNearestEnemy()
    
    # 使用 checkAndAttack 函数，并使用 bottomEnemy 变量。
    checkAndAttack(bottomEnemy)

```

## 第二十八关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f051da72eb174108b311da0f7b315023.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 森林中一座被遗忘的墓地！
# 但是食人魔紧追不舍。
# 在防御食人魔矮人的同时打开墓地之门。

# 这个函数应该在敌人存在时攻击，否则攻击门！
def checkToDefend(target):
    # 检查`target`是否存在
    if target:
        # 如果是这样，攻击`target`
        hero.attack(target)
    # 如果没有`target`，使用else去做点别的事
    else:
        # 否则攻击 "Door"
        hero.attack("Door")
    pass

while True:
    enemy = hero.findNearestEnemy()
    checkToDefend(enemy)

```

## 第二十九关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/767747269591443ea856a19add90d8d3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 唯一的出口被食人魔堵住了。
# 躲着骷髅怪，并一个个击败食人魔。

# 这个函数需要攻击敌人并隐藏。
def hitOrHide(target):
    # 如果'target'存在：
    if target:
        # 攻击'target'。
        hero.attack(target)
        # 然后移动到红色标记。
        hero.moveXY(32, 17)
    pass

while True:
    enemy = hero.findNearestEnemy()
    hitOrHide(enemy)

```

## 第三十关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/eec13d0be99443f5a84679466a44f4ca.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 收集4颗发光石，用来打败食人魔斗士。
# 如果找到发光石的话，藏起来。

def checkTakeHide(item):
    if item:
        # 物品在此，拿走它。
        hero.moveXY(item.pos.x, item.pos.y)
        # 然后移动到营地中央(40, 34)
        hero.moveXY(40, 34)

while True:
    # 移动到右上的X标记。
    hero.moveXY(68, 56)
    # 在那里搜索一块发光石。
    lightstone = hero.findNearestItem()
    # 调用checkTakeHide，并使用参数：lightstone
    checkTakeHide(lightstone)
    
    # 移动到左上角的标记。
    hero.moveXY(12, 56)
    # 搜索发光石。
    # 在那里搜索一块发光石。
    lightstone = hero.findNearestItem()
    # 调用checkTakeHide，并使用参数：lightstone
    checkTakeHide(lightstone)
    # 调用checkTakeHide函数。
    # 将搜索的结果作为参数传入。
    

```
## 第三十一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/196dca7d5ef54e8e854e8fb01846f5f9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 检查工人们能否安全挖矿。

def checkEnemyOrSafe(target):
    # 如果`target`（参数）存在：
    if target:
        # 那么攻击目标。
        hero.attack(target)
    # 否则：
    else:
        # 使用say() 说点什么来叫农民。
        hero.say("农民，快点过来啊")
    pass

while True:
    # 移动到并检查右上的X标记。
    hero.moveXY(64, 54)
    enemy1 = hero.findNearestEnemy()
    checkEnemyOrSafe(enemy1)
    
    # 移动到左下的X标记处。
    hero.moveXY(16, 14)
    # 将findNearestEnemy()的结果存到一个变量中。
    enemy2 = hero.findNearestEnemy();
    # 调用checkEnemyOrSafe，并传递
    # findNearestEnemy的结果作为参数
    checkEnemyOrSafe(enemy2)

```

## 第三十二关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4537abe878554f91a239ce90a0a75521.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 这里展示了如何定义一个叫作cleaveWhenClose的函数
# 函数定义了一个形式参数，名为`target`
def cleaveWhenClose(target):
    if hero.distanceTo(target) < 5:
        pass
        # 将你的攻击代码放到这里。
        # 如果cleave准备就绪，那就劈斩目标
        if hero.isReady("cleave"):
            hero.cleave(target)
        # 否则，使用attack攻击目标（`target`）！
        else:
            hero.attack(target)

# 这段代码不是函数的一部分。
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # 注意在cleaveWhenClose内部，我们将`enemy`称为`target`。
        cleaveWhenClose(enemy)

```

## 第三十三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d8338ad753ef4f1ea34c4dbec9b603e6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 函数maybeBuildTrap定义了两个参数！
def maybeBuildTrap(x, y):
    # 使用x和y作为移动的坐标。
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        # 使用 buildXY 在特定 x 和 y 处建造 "fire-trap"。
        hero.buildXY("fire-trap", x, y)
while True:
    # 这会调用 maybeBuildTrap，并使用上方入口的坐标。
    maybeBuildTrap(43, 50)
    
    # 现在在左侧入口处使用maybeBuildTrap！
    maybeBuildTrap(25, 34)
    # 现在在底部入口处使用maybeBuildTrap！
    maybeBuildTrap(43, 20)
    
```

## 第三十四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/95d529f425504963961d56753ce9ebb2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
def cleaveOrAttack(enemy):
    # 如果"cleave"技能冷却完毕，那就使用它！否则，使用普通攻击。
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            # 调用上面定义的"cleaveOrAttack"函数
            cleaveOrAttack(enemy)

```

## 第三十五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4b1bb39b18b34979ab88c83a6c804e0f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 只在看到敌人时进行建造。

# 该函数定义3个参数。
def maybeBuildSomething(typeToBuild, x, y):
    hero.moveXY(x, y)
    # 找到最近的敌人
    enemy = hero.findNearestEnemy()
    # 如果存在敌人
    if enemy:
        # 那么使用buildXY，参数typeToBuild、x和y
        # 使用变量typeToBuild作为第一个参数。
        hero.buildXY(typeToBuild, x, y)
    pass

# 你不需要改动下面的代码。
while True:
    # 调用 maybeBuildSomething，使用"fire-trap"及底部X的坐标。
    maybeBuildSomething("fire-trap", 40, 20)
    # 调用maybeBuildSomething，在左侧X处建造"fence"!
    maybeBuildSomething("fence", 26, 34)
    # 调用maybeBuildSomething，在顶部X处建造"fire-trap"!
    maybeBuildSomething("fire-trap", 40, 50)
    # 调用maybeBuildSomething，在右侧X处建造"fence"!
    maybeBuildSomething("fence", 54, 34)

```

## 第三十六关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c407a0f2209543409eeb7a160f8dcc33.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 巡逻并只在看到硬币时设置陷阱。

# 编写这个函数。
def maybeBuildTrap(x, y):
    # 移动到给定的xy位置
    hero.moveXY(x, y)
    # 搜寻硬币，如果发现就建造一个"fire-trap"
    item = hero.findNearestItem()
    if item:
        hero.buildXY("fire-trap", x, y)
    pass

while True:
    # 为左上方通道调用maybeBuildTrap。
    maybeBuildTrap(12, 56)
    # 现在是右上的通道。
    maybeBuildTrap(68, 56)
    # 现在是右下的通道。
    maybeBuildTrap(68, 12)
    # 现在是左下的通道。
    maybeBuildTrap(12, 12)

```
## 第三十七关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a44e464f93c346c6bb4918ef8ed548c9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你现在拥有一个宠物！

def speak(event):
    # 你的宠物需要用pet.say()进行回应
    pet.say('Meao')
    pet.trick()
    pass

# 这将告诉你的宠物，在听到声音时运行speak()函数
pet.on("hear", speak)

# 和你的宠物交流吧！
hero.say("你好小猫")

```
## 第三十八关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1abdc9e083e7493c98c62f54fbb9c098.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 我们需要知道新宠物的名字。

# 把这个函数用作宠物 "hear" 事件的处理器。
def onHear(event):
    # 不要更改这个函数
    pet.say("喵 汪 喵")
    pet.say("汪 汪")
    pet.say("喵")
    pet.say("喵")
    pet.say("喵 汪 喵 喵")
    pet.trick()

# 使用pet.on(eventType，eventHandler)方法
# 指派onHear函数来处理"hear"事件。
pet.on("hear",onHear)

# 这必须在 "pet.on" 的后面。
hero.say("伙计，你叫什么名字？")
hero.say("能重复一次吗？")

```

## 第三十九关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f62a3b738bdc406f989da02fe8dd61f3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 教你的宠物回答问题！

# 很幸运，所有的答案都是"2"
def sayTwo(event):
    # 使用pet.say()来回答"2"
    pet.say("2")
    pass

# 使用pet.on()，通过sayTwo来处理"hear"事件
pet.on("hear",sayTwo)
# 现在休息并观看表演吧！
hero.say("一加一等于…？")
hero.say("x^3 - 6x^2 + 12x - 8 = 0。那x等于多少？")
hero.say("火星有多少卫星？")

```

## 第四十关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/286a2a36db0c4be4b797d701197e6347.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 编写一个事件处理函数，名为onHear

# 完成onHear函数
def onHear(event):
    # 宠物需要在onHear中说点什么。
    pet.say("YES")
    pet.say("YES")
    pet.say(2)
    pet.say(2)
    pet.say(2)
    pass

pet.on("hear", onHear)

hero.say("能听懂我的话吗？")
hero.say("你是美洲狮吗？")
hero.say("你多大啦？")
# 再问两个问题。
hero.say("1+1=?")
hero.say("1*2=?")

```
## 第四十一关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6826026644e24166af7f16efd8dbfd24.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你被困在了树精陷阱中！
# 派遣宠物拿取治疗药水！

def goFetch():
    # 你可以在处理器函数中使用循环。
    while True:
        potion = hero.findNearestItem()
        if potion:
            # 用pet.fetch()去让你的宠物取回药水。
            pet.fetch(potion)
            pass

# 当宠物被召唤出来时，会触发 "spawn" 事件。
# 这让你的宠物在关卡开始时运行goFetch()函数。
pet.on("spawn", goFetch)

```

## 第四十二关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e49e7294141f48858cf05744f2dbe540.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你无法帮助农民过河。
# 不过，你的宠物做得到！
# 将你的狼调教成看门狗。

def onSpawn(event):
    while True:
        # 宠物一样可以发现敌人。
        enemy = pet.findNearestEnemy()
        # 如果有敌人：
        if enemy:
            # 那么让宠物说点什么：
            pet.say("有危险！")

pet.on("spawn", onSpawn);

```

## 第四十三关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1ed7342715e74340b0a9e40081510935.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 移动到右边

# 补全这个函数：
def onSpawn(event):
    pass
    # 在while-true循环内：
    while True:
        
        # 使用hero.findNearestItem()
        potion = hero.findNearestItem()
        
        # 如果有物品：
        if potion:
            # 使用pet.fetch(item)来拿取物品。
            pet.fetch(potion)

# 使用pet.on()来将onSpawn指派给"spawn"事件
pet.on("spawn",onSpawn)
hero.moveXY(78, 35)

```

## 第四十四关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a5615d65f026416bbd20c98771eb6490.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你的宠物可以使用 pet.moveXY()

def onSpawn(event):
    while True:
        # 首先，移动到左侧的X标记处：
        pet.moveXY(9, 24)
        # 接着，移动到上面的X标记处：
        pet.moveXY(30, 43)
        # 将宠物移动至右侧的X标记处：
        pet.moveXY(51, 24)
        # 将宠物移动到下面的X标记处：
        pet.moveXY(30,5)

# 使用pet.on()，通过onSpawn来处理"spawn"事件
pet.on("spawn",onSpawn)

# 给你的宠物加油！
# 不要删除下面的命令。
while True:
    hero.say("狗狗真棒！")
    hero.say("你能做到的！")
    hero.say("跑跑跑！")
    hero.say("快好了！")
    hero.say("再来一圈！")

```

## 第四十五关
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c610c66ca1b64e5882775356ad9a2e56.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
# 你的宠物需要在X标记上来回跑动。
# 英雄需要不停为宠物加油！

# 为宠物编写事件函数onSpawn。
# 这个函数要让狼来回跑动：
# 首先，跑到右侧的标记上，然后左侧的标记：
def onSpawn(event):
    while True:
        
        pet.moveXY(48,8)
        pet.moveXY(12,8)

pet.on("spawn", onSpawn)
# 为你的宠物加油。不要移除这个：
while True:
    hero.say("跑！！！")
    hero.say("速度！")

```

