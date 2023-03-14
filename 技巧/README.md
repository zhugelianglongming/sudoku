# 数独技巧

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [入门级](#%E5%85%A5%E9%97%A8%E7%BA%A7)
  - [摒除法](#%E6%91%92%E9%99%A4%E6%B3%95)
  - [唯余法](#%E5%94%AF%E4%BD%99%E6%B3%95)
- [初级](#%E5%88%9D%E7%BA%A7)
  - [区块摒除](#%E5%8C%BA%E5%9D%97%E6%91%92%E9%99%A4)
- [中级](#%E4%B8%AD%E7%BA%A7)
  - [隐性数组](#%E9%9A%90%E6%80%A7%E6%95%B0%E7%BB%84)
  - [显性数组](#%E6%98%BE%E6%80%A7%E6%95%B0%E7%BB%84)
- [高级](#%E9%AB%98%E7%BA%A7)
  - [区块数组](#%E5%8C%BA%E5%9D%97%E6%95%B0%E7%BB%84)
  - [鱼](#%E9%B1%BC)
  - [待定数组（基础）](#%E5%BE%85%E5%AE%9A%E6%95%B0%E7%BB%84%E5%9F%BA%E7%A1%80)
  - [链（基础）](#%E9%93%BE%E5%9F%BA%E7%A1%80)
    - [标准链](#%E6%A0%87%E5%87%86%E9%93%BE)
    - [烟花](#%E7%83%9F%E8%8A%B1)
- [骨灰级](#%E9%AA%A8%E7%81%B0%E7%BA%A7)
  - [致命结构](#%E8%87%B4%E5%91%BD%E7%BB%93%E6%9E%84)
  - [待定死锁集合](#%E5%BE%85%E5%AE%9A%E6%AD%BB%E9%94%81%E9%9B%86%E5%90%88)
  - [待定唯一矩形](#%E5%BE%85%E5%AE%9A%E5%94%AF%E4%B8%80%E7%9F%A9%E5%BD%A2)
  - [毛刺](#%E6%AF%9B%E5%88%BA)
  - [链（高级）](#%E9%93%BE%E9%AB%98%E7%BA%A7)
    - [超标准链](#%E8%B6%85%E6%A0%87%E5%87%86%E9%93%BE)
    - [强制链组](#%E5%BC%BA%E5%88%B6%E9%93%BE%E7%BB%84)
    - [环](#%E7%8E%AF)
    - [动态链](#%E5%8A%A8%E6%80%81%E9%93%BE)
  - [涂色法](#%E6%B6%82%E8%89%B2%E6%B3%95)
  - [袋鼠](#%E8%A2%8B%E9%BC%A0)
  - [鱼雷](#%E9%B1%BC%E9%9B%B7)
  - [待定数组（高级）](#%E5%BE%85%E5%AE%9A%E6%95%B0%E7%BB%84%E9%AB%98%E7%BA%A7)
  - [Template](#template)
- [流派](#%E6%B5%81%E6%B4%BE)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

> [技巧分类](分类/README.md)
>
> [技巧图谱](https://www.processon.com/embed/61c17b5f0791290c9efaf141)
>
> - 绿色虚线：技巧演进-分析数扩展
> - 蓝色虚线：技巧演进-分析区域扩展
> - 红色虚线：技巧组合
>
> ![技巧脑图](http://assets.processon.com/chart_image/61c17b5f0791290c9efaf145.png)

## 入门级

### 摒除法

- 摒除法 / 排除法 / [Hidden Single]
  - 宫摒除 / [Hidden Single in Box][] `参考难度系数`1.2
  - 行列摒除 / [Hidden Single in Row/Column] `参考难度系数`1.5
  > 练习
  >
  > - 微信小程序：联网数独
  > - 网页：[三思](https://www.12634.com/learning/hs/index)

### 唯余法

- 唯余法 / 唯一数 / 唯一法 / Last Value / [Naked Single][] `参考难度系数`2.3
  > [练习](http://www.sudokufans.org.cn/tools/finder.php)

## 初级

### 区块摒除

- 区块摒除 / [Locked Candidates][]
  - 宫区块摒除法 / [Pointing][]
    - 直观宫区块摒除法 / [Direct Pointing] `参考难度系数`1.7
      > [练习](https://www.12634.com/learning/pointing/index)
  - 行列区块摒除法 / [Claiming][]
    - 直观列区块摒除法 / [Direct Claiming] `参考难度系数`1.9
      > [练习](https://www.12634.com/learning/claiming/index)
  - 组合区块 / [Cascading Locked Candidates][] `参考难度系数`2.8

## 中级

### 隐性数组

- 隐性数组 / [Hidden Subset][]
  - 隐性数对 / [Hidden Pair][]
    - 直观隐性数对 / [Direct Hidden Pair][] `参考难度系数`3.4
      > [练习](https://www.12634.com/learning/direct-hidden-pair/index)
      > [练习](https://www.12634.com/learning/hidden-pair/index)
  - 隐性三数组 / 隐性三数集 / [Hidden Triple][]
    - 直观隐性三数集 / [Direct Hidden Triple][] `参考难度系数`4.0
      > [练习](https://www.12634.com/learning/hidden-triplet/index)
  - 隐性四数组 / [Hidden Quadruple][] `参考难度系数`5.4

### 显性数组

- 显性数组 / [Naked Subset][]
  - 一般显性数组
    - 显性数对 / [Naked Pair][] `参考难度系数`3.0
      > [练习](https://www.12634.com/learning/naked-pair/index)
    - 显性三数组 / 显性三数集 / [Naked Triple][] `参考难度系数`3.6
      > [练习](https://www.12634.com/learning/naked-triplet/index)
    - 显性四数组 / [Naked Quadruple][] `参考难度系数`5.0
  - 死锁数组 / 割补数组 / [Locked Subset][]
    - 死锁数对 `参考难度系数`2.0
    - 死锁三数组 `参考难度系数`2.5

## 高级

### 区块数组

- 区块数组 / Naked Subset With Locked Candidates / [Naked Subset+][]
  - 区块三数组 `参考难度系数`3.7
  - 区块四数组 `参考难度系数`5.1

### 鱼

- 鱼 / 链列 / [Fish][]
  - 标准鱼
    - 二阶鱼 / 二链列 / ~~X翼~~ / [X-Wing][] `参考难度系数`3.2
      > [练习](https://www.12634.com/learning/x-wing/index)
    - 三阶鱼 / 剑鱼 / 三链列 / [Swordfish][] `参考难度系数`3.8
    - 四阶鱼 / 水母 / 四链列 / [Jellyfish][] `参考难度系数`5.2
  - 带鳍鱼 / 外鳍鱼 / [Finned Fish][]
    - 带鳍二阶鱼 / [Finned X-Wing][] `参考难度系数`3.4
    - 带鳍三阶鱼 / [Finned Swordfish][] `参考难度系数`4.0
    - 带鳍四阶鱼 / [Finned Jellyfish][] `参考难度系数`5.4
  - 宫内鱼 / Franken Fish
    - [标准宫内鱼][宫内鱼]
      - 宫内二阶鱼 / 宫内二阶鱼 / Franken X-Wing
      - 宫内三阶鱼 / Franken Swordfish
      - 宫内四阶鱼 / Franken Jellyfish
    - 带鳍宫内鱼
      - [外鳍宫内鱼][宫内鱼]
      - 内鳍宫内鱼 / [Endo-finned Franken Fish](https://zhuanlan.zhihu.com/p/35126174)
        - 内鳍宫内三阶鱼 / Endo-finned Franken Swordfish
        - 内鳍宫内四阶鱼 / Endo-finned Franken Jellyfish
      - 自噬鳍宫内鱼 / [Cannibal-finned Franken Fish](https://zhuanlan.zhihu.com/p/35180765)
        - 自噬鳍宫内三阶鱼
        - 自噬鳍宫内四阶鱼
  - 交叉鱼 / [Mutant Fish](https://zhuanlan.zhihu.com/p/35245385)
    - 标准交叉鱼
      - 交叉三阶鱼 / Mutant Swordfish
      - 交叉四阶鱼 / Mutant Jellyfish
    - 带鳍交叉鱼
      - 外鳍交叉鱼
        - 外鳍交叉三阶鱼 / Exo-finned Mutant Swordfish
        - 外鳍交叉四阶鱼 / Exo-finned Mutant Jellyfish
      - 内鳍交叉鱼
        - 内鳍交叉三阶鱼
        - 内鳍交叉四阶鱼
      - 自噬鳍交叉鱼
        - 自噬鳍交叉三阶鱼
        - 自噬鳍交叉四阶鱼
  - 复杂鱼 / [Complex Fish](https://zhuanlan.zhihu.com/p/35348865)
    - X环 / [X-Cycle][]

### 待定数组（基础）

- 待定数组（标准） / ALS / Almost Locked Subset
  - 欠一数组 / ALC / [Almost Locked Candidates](https://zhuanlan.zhihu.com/p/33612543)
    - 欠一数对 / ALP / [Almost Locked Pair][] `参考难度系数`4.5
    - 欠一三数组 / Almost Locked Triple `参考难度系数`5.2
  - 伪数组 / ESP / [Extended Subset Principle][伪数组和跨区数组] `参考难度系数`7.5
  - 跨区数组 / DDS / [Distributed Disjointed Subset][伪数组和跨区数组] `参考难度系数`7.0
    - 融合式待定数组 / 双区域分布式跨区数组 / 一度SDC / SDC / SdC / `SDC Degree 1`
      / [Sue de Coq](https://zhuanlan.zhihu.com/p/33615105)
      - 无公共数型 / 基本融合版本 `参考难度系数`4.8+
      - 共享公共数型 / 带有交互数字的融合版本 `参考难度系数`4.9+
      - 独占公共数型 / 自噬SDC / Cannibalistic SDC `参考难度系数`4.9+
  - [均衡性数组][]
    - 均衡性数对 / Aligned Pair Exclusion `参考难度系数`6.2
    - 均衡性三数组 / Aligned Triple Exclusion `参考难度系数`7.5

### 链（基础）

#### 标准链

- 标准链 / AIC / [Alternating Inference Chain][Common Types Chain] `参考难度系数`5.7+
  - [规则 Wing](https://zhuanlan.zhihu.com/p/33087864)
    - 双分支匹配法 / Y-Wing / [XY-Wing][] `参考难度系数`4.2
      > [练习](https://www.12634.com/learning/xy-wing/index)
    - 三分支匹配法 / [XYZ-Wing][] `参考难度系数`4.4
      > [练习](https://www.12634.com/learning/xyz-wing/index)
    - 四分支匹配法 / Bent Quads / WXYZ-Wing `参考难度系数`4.6
    - 五分支匹配法 / VWXYZ-Wing `参考难度系数`4.85
    - ~~六分支匹配法 / UVWXYZ-Wing~~
    - ~~七分支匹配法 / TUVWXYZ-Wing~~
    - ~~八分支匹配法 / STUVWXYZ-Wing~~
    - ~~九分支匹配法 / RSTUVWXYZ-Wing~~
  - [不规则 Wing](https://zhuanlan.zhihu.com/p/33730739)
    - Y-Wing 拓展构型 / Y-Wing Style
      - 首尾格内对匹配法 / [W-Wing][] `参考难度系数`4.4
    - 隔一格内对匹配法 / [M-Wing][]  `参考难度系数`4.5
    - 分裂匹配法 / Split-Wing `参考难度系数`5.9
    - 拐角匹配法 / Local-Wing `参考难度系数`5.9
    - 杂合匹配法 / Hybrid-Wing `参考难度系数`5.9
  - 同数链 / X链 / [X-Chain][] `参考难度系数`4.0+
    - 双强链 / 多宝鱼 / [Turbot Fish][] `参考难度系数`4.2
      - 摩天楼 / 孪生二链列 / [Skyscraper][] `参考难度系数`4.05
        > [练习](https://www.12634.com/learning/skyscraper/index)
      - 双线风筝 / [Two Strings Kite][] `参考难度系数`4.1
    - [Group X-Chain](http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5227)
  - 双值格链 / 双值格标准链 / [XY-Chain][] `参考难度系数`4.0+
    - 远程数对 / [Remote Pairs][] `参考难度系数`4.5+
  - 首尾异数链 / 首尾异数标准链 / [XY-X-Chain][Common Types Chain] `参考难度系数`5.7+
  - 自噬链 / [Cannibalistic AIC][Common Types Chain]
  - 不连续环 / [Discontinuous (Nice) Loop][Common Types Chain] `参考难度系数`5.7+
  - 守护者 / [Guardians][] `参考难度系数`6.6+
  - 死环 / Guardian Pair / [Dead Loop][]
  - [区块组链](https://zhuanlan.zhihu.com/p/33748094)
    - 空矩形 / [Empty Rectangle][] `参考难度系数`4.8
    - 区块链 / Grouped AIC
    - 区块不连续环 / Grouped Disc. (Nice) Loop

#### 烟花

- 烟花 / [Fireworks]
  - 三重烟花 / [Triple Firework]
  - 四重烟花 / [Quadruple Firework]

## 骨灰级

### 致命结构

- 唯一矩形 / UR / [Unique Rectangle][]
  - 普通唯一矩形
    - 标准型 / [UR Type 1][UR Type 1] `参考难度系数`4.5
      > [练习](https://www.12634.com/learning/unique-rectangle-type-1/index)
    - 待定数型 / 区块组型 / [UR Type 2][UR Type 2]
      - UR Type 2A `参考难度系数`4.6
      - 对角待定数型 / UR Type 2B / UR Type 5 `参考难度系数`4.6
    - 待定数组型 / [UR Type 3][UR Type 3]
      - UR Type 3A `参考难度系数`4.4+
      - UR Type 3B `参考难度系数`4.5+
    - 共轭对型 / [UR Type 4][UR Type 4]
      - UR Type 4A  `参考难度系数`4.6
      - 平行共轭对型 / UR Type 4B / UR Type 6 `参考难度系数`4.6
      - 正交共轭对型 / UR Type 4C / UR Type 7 / HUR / Hidden UR / [Hidden Unique Rectangle][] `参考难度系数`4.8
  - 残缺唯一矩形 / [Incomplete UR][]
    - 标准型 / Incomplete UR Type 1
    - 待定数型 / Incomplete UR Type 2
      - Incomplete UR Type 2A
      - 对角待定数型 / Incomplete UR Type 2B
    - 待定数组型 / Incomplete UR Type 3
      - Incomplete UR Type 3A
      - Incomplete UR Type 3B
    - 共轭对型 / Incomplete UR Type 4
      - Incomplete UR Type 4A
      - 平行共轭对型 / Incomplete UR Type 4B
      - 正交共轭对型 / Incomplete UR Type 4C
  - 强制唯一矩形 / [Forcing UR][活用唯一矩形]
    - 星座强制唯一矩形 / Constellation
      - 水瓶座 / `UR + 2 / 1 CP` / Aquarius
      - 天鹅座 / `UR + 3 / 2 CP` / Cygnus
      - 飞马座 / `UR + 4 / 3 CP` / Pegasus
    - 普通强制唯一矩形 / Basic Forcing UR
    - 残缺强制唯一矩形 / Incomplete Forcing UR
  - 死锁唯一矩形 / [Locked UR][活用唯一矩形]
    - 标准型 / Locked UR Type 1
    - 待定数组型 / Locked UR Type 2
  - [构造唯一矩形][活用唯一矩形]
  - 直推唯一矩形 / [Direct Inference UR][活用唯一矩形]
  - 超链置唯一矩形 / [Hyper AIC With UR][活用唯一矩形]
- 唯一环 / UL / [Unique Loop][] `参考难度系数`4.3+
- 拓展矩形 / [Extended Rectangle][Unique Loop] `参考难度系数`4.3+
  - [Unique Rectangle 6-cell](http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=1114)
- 可规避矩形 / AR / [Avoidable Rectangle][] `参考难度系数`4.5+
  - 普通可规避矩形
    - 标准型 / Type 1
    - 区块组性 / Type 2
    - 待定数组型 / Type 3
    - 正交共轭对型 / 隐形可规避矩形 / AR Type 4C / Hidden AR
  - 强制可规避矩形 / [Forcing AR][]
  - 直推可规避矩形 / [Directed Inference AR][Forcing AR]
- 全双值坟墓 / BUG / [Bivalue Universal Grave][]  `参考难度系数`5.4+
  - 标准型 / Type 1
  > [练习](https://www.12634.com/learning/bug-type-1/index)
  - 待定数型 / Type 2
  > [练习](https://www.12634.com/learning/bug-type-2/index)
  - 待定数组型 / Type 3
  - 共轭对型 / Type 4
- 探长致命结构 / [Borescoper Deadly Pattern](https://zhuanlan.zhihu.com/p/34426283)
  - 三数探长致命结构 / ABC-Borescoper Deadly Pattern / ABC-Borescoper DP
  - 四数探长致命结构 / ABCD-Borescoper Deadly Pattern / ABCD-Borescoper DP
- 淑芬致命结构 / [Qiu's Deadly Pattern](https://www.bilibili.com/read/cv12935009)
- 唯一方阵 / [Unique Square Matrix](https://zhuanlan.zhihu.com/p/34741297)
- [宇宙法](https://www.bilibili.com/video/BV1Mx411z7uq?p=121)
- UCC / [Unique Clue Cover](https://zhuanlan.zhihu.com/p/42157930)

### 待定死锁集合

- 待定死锁集合 / ALS / [Almost Locked Set](https://zhuanlan.zhihu.com/p/33769864)
  - 显性 ALS / NALS / nALS / Naked ALS / ~~ALS(简称)~~
  - 隐性 ALS / HALS / hALS / Hidden ALS
  - 虚ALS / VALS / vALS / [Virtual ALS](https://zhuanlan.zhihu.com/p/33820368)
    - 虚拟显性待定死锁集合 / 虚拟显性ALS / 虚nALS / VNALS / vnALS / Virtual nALS / Virtual Naked ALS / Virtual Naked
      Almost Locked Set
    - 虚拟隐性待定死锁集合 / 虚拟隐性ALS / 虚hALS / VHALS / vhALS / Virtual hALS / Virtual Hidden ALS / Virtual
      Hidden Almost Locked Set
- 二次待定数组 / Almost Almost Locked Set / Almost ALS / AALS
- 三次待定数组 / Almost Almost Almost Locked Set / Almost AALS / AAALS
- 四次待定数组 / Almost Almost Almost Almost Locked Set / Almost AAALS

### 待定唯一矩形

- 待定唯一矩形 / AUR / [Almost UR][]
  - 候选强关系型 / AUR Type 1
  - 区块强关系型 / AUR Type 2
  - 其他强关系型 / AUR Type 3

### 毛刺

- 毛刺结构 / Single Kraken Logic
  - [毛刺数组][]
    - 显性毛刺数组 / Almost Naked Subset
      - 显性毛刺数对 / Almost Naked Pair
    - 隐性毛刺数组 / AHS / Almost Hidden Subset
  - 毛刺鱼 / [Kraken Fish](https://zhuanlan.zhihu.com/p/34018343)
    - 标准型 / Kraken Fish Type 1 `参考难度系数`8.3
    - 矛盾型 / Kraken Fish Type 2 `参考难度系数`8.4
- 毛边结构 / [Double Kraken Logic](https://zhuanlan.zhihu.com/p/34085796)
  - 弱毛边 / Weak Inference in Double Kraken
- 三毛刺结构 / [Triple Kraken Logic](https://zhuanlan.zhihu.com/p/34085796)

### 链（高级）

#### 超标准链

- 超标准链 / 超链 / Hyper AIC
  - 超链置ALS / ALS超链 / 超链+ALS / [Hyper AIC With ALS](https://zhuanlan.zhihu.com/p/33769864)
    - _按组合技巧分类：_
      - ALS-双强链 / 双强显性待定数组链 / [ALS-XZ][ALS初步] `参考难度系数`7.5
        - 带有单RCC的ALS-XZ结构 / Single-linked ALS-XZ
        - 带有双RCC的ALS-XZ结构 / Double-linked ALS-XZ
      - ALS-双分支匹配法 / [ALS-XY-Wing][ALS初步] `参考难度系数`8.0
      - ALS-双值格链 / [ALS-XY-Chain][ALS的一般拓展结构]
      - ALS-首尾格内对匹配法 / [ALS-W-Wing][ALS的一般拓展结构] `参考难度系数`7.8
      - 死亡绽放 / [Death Blossom][ALS的一般拓展结构] `参考难度系数`8.3
    - _按 ALS 分类：_
      - 超链置nALS / Hyper AIC With nALS
      - 超链置hALS / [Hyper AIC With hALS](https://zhuanlan.zhihu.com/p/33819712)
      - 阴阳法 / Mixed hALS Logic / [nALS & hALS Logic][ALS的综合运用]
  - 超链置显性数组 / [Hyper AIC With Naked Subset][毛刺数组]
    - 超链置显性数对 / 显性毛刺数对链 / Kraken Naked Pair / Hyper AIC With Naked Pair
  - 超链置隐性数组 / 隐性毛刺数组链 / [Hyper AIC With Hidden Subset][毛刺数组]
  - 超链置AUR / [Hyper AIC With AUR][Almost UR]
  - [超链置Wing](https://zhuanlan.zhihu.com/p/33998350)
  - 超链置鱼 / [Hyper AIC With Fish](https://zhuanlan.zhihu.com/p/34018343)
  - 超链置链 / [Hyper AIC With AIC](https://zhuanlan.zhihu.com/p/34085796)
  - 超链置可规避矩形 / [Hyper AIC With AR][Forcing AR]
  - 超链置SDC / SDC超链 / [Hyper AIC With SDC](https://zhuanlan.zhihu.com/p/35977314)
  - ...
    - 间接删数的链 / [Indirected Chain][ALS的综合运用]

#### 强制链组

- 强制链组 / FC / [Forcing Chains](https://zhuanlan.zhihu.com/p/33861014)
  - 矛盾强制链组 / Contradiction Forcing Chains `参考难度系数`8.2+
    - 西尾彻也强制链组 / Nishio Forcing Chains
  - 单元强制链组 / Unit Forcing Chains `参考难度系数`8.2+
    - 行强制链组 / Row Forcing Chains
    - 列强制链组 / Column Forcing Chains
    - 宫强制链组
    - 单元格强制链组
  - 逆向矛盾强制链组
  - 逆向单元强制链组
  > [练习](https://www.12634.com/learning/forcing-chain/index)

#### 环

- 环
  - 标准环 / ~~环(简称)~~ / [Continuous (Nice) Loop](https://zhuanlan.zhihu.com/p/33887094)
    - 不规则Wing结构的环结构
    - 双值格数组的环结构 / Multi X-Wing
      / [XY-Cycle](http://www.sudokufans.org.cn/forums/topic/38/?do=findComment&comment=237)
  - 超标准环 / [Hyper Continuous (Nice) Loop](https://zhuanlan.zhihu.com/p/33917735)
    - 超环置ALS / Hyper Cont. (Nice) Loop With ALS
    - 超环置AUR / Hyper Cont. (Nice) Loop With AUR
    - 超环置毛刺数组 / Hyper Cont. (Nice) Loop With Almost Subset

#### 动态链

- 动态链 / Dynamic AIC / [DAIC](https://zhuanlan.zhihu.com/p/33967982)
  - 动态不连续环
    - Dynamic Discontinuous Loop
    - Dynamic Discontinuous (Nice) Loop
  - 多端点链 / Multi Endpoint Chain
    - 三国争雄 / Three-kingdom W-Wing
    - ...
  - 带鳍链 / Kraken Unit
  - 动态环 / 动态标准环
    - _按删数分类：_
      - Dynamic Continuous Loop
      - Dynamic Continuous (Nice) Loop
    - _按分支分类：_
      - 双环 / [Double Loop](https://www.bilibili.com/read/cv12656263)
      - ...
  - 动态超环 / 动态超标准环
    - Dynamic Hyper Continuous Loop
    - Dynamic Hyper Continuous (Nice) Loop

### 涂色法

- 涂色法 / [Coloring](https://zhuanlan.zhihu.com/p/34187700)
  - 色链 / Simple Coloring Type 1
  - 色分 / 分色法 / Simple Coloring Type 2
  - 复合色链 / Multi Coloring
  - 进阶涂色 / 三维美杜莎 / 3D Medusa / Advanced Coloring

### 袋鼠

- 袋鼠 / 代数 / [Kangaroo](https://zhuanlan.zhihu.com/p/34212080)

### 鱼雷

- 飞鱼导弹 / 鱼雷
  - 初级飞鱼导弹 / Junior Exocet / [JE](https://zhuanlan.zhihu.com/p/35576944)
    - 初级标准飞鱼导弹
      - [对角型](https://zhuanlan.zhihu.com/p/35576944)
      - [同侧型](https://zhuanlan.zhihu.com/p/35952793)
      - [共轭对型](https://zhuanlan.zhihu.com/p/35952793)
      - [待定数组型](https://zhuanlan.zhihu.com/p/35952793)
    - 宫内飞鱼导弹 / [Franken JE](https://zhuanlan.zhihu.com/p/35821903)
    - 交叉飞鱼导弹 / [Mutant JE](https://zhuanlan.zhihu.com/p/35821903)
  - 高级飞鱼导弹 / Senior Exocet / [SE](https://zhuanlan.zhihu.com/p/35868227)
    - 高级标准飞鱼导弹 / Senior Basic Exocet
    - 高级宫内飞鱼导弹 / Senior Franken Exocetda
    - 高级交叉飞鱼导弹 / Senior Mutant Exocet
  - 复合飞鱼导弹 / [Double JE](https://zhuanlan.zhihu.com/p/35576944)
- 袋鼠飞鱼导弹 / [假飞鱼导弹](https://zhuanlan.zhihu.com/p/35952793)

### 待定数组（高级）

- [SDC拓展](https://zhuanlan.zhihu.com/p/35977314)
  - 多度SDC / Multi-sector DDS
    - 二度SDC / 三区域分布式跨区数组 / Three-sector DDS / SDC Degree 2
  - 多段SDC / 多米诺链 / Domino Chain
    - 三段SDC
    - 四段SDC
    - 五段SDC
    - 六段SDC
    - ...
  - 多米诺环 / 柯尔扎斯环 / SK环 / SK Loop / [Domino Loop]
    - [直观多米诺环](https://zhuanlan.zhihu.com/p/37611197)
    - 自噬变种多米诺环 / BB型多米诺环 / [Bigger's Loop](https://zhuanlan.zhihu.com/p/37611197)
- 网 / 多区域（跨区）数组 / Multi-sector Locked Sets / MSLS
  - _按涉及区域分类：_
    - 标准网 / [Basic MSLS](https://zhuanlan.zhihu.com/p/36007498)
      - [直观标准网](https://zhuanlan.zhihu.com/p/37611197)
    - 宫内网 / [Franken MSLS](https://zhuanlan.zhihu.com/p/37352318)
    - 交叉网 / [Mutant MSLS](https://zhuanlan.zhihu.com/p/37352318)
  - _按结构形状分类：_
    - 非矩形网 / [Non-Rectangle MSLS](https://zhuanlan.zhihu.com/p/37352318)

### Template

- [Template](http://hodoku.sourceforge.net/en/tech_last.php#ts)
  - Template Set
  - Template Delete

## 流派

- 竞速（面向比赛）
- 技巧（面向数独难题）
- 编程（面向数独的计算机程序解决方案）

> 文字:
>
> - [数独技巧教程](https://sunnieshine.gitbook.io/sudoku-tutorial/)
> - [独·数之道](http://www.sudokufans.org.cn/forums/topic/69/)
> - [三思](https://www.12634.com/learning/index)
> - [数独术语](https://zh.wikipedia.org/wiki/%E6%95%B0%E7%8B%AC%E6%9C%AF%E8%AF%AD)
> - [数独术语索引表](https://zhuanlan.zhihu.com/p/33475225)
> - Bilibili: SunnieShine [标准数独技巧教程](https://www.bilibili.com/read/readlist/rl291187)
> - [小向的标准数独技巧教程](http://sunnie-shine.gitee.io/sudokutechniquetutorial/SortByTutorial.html)
> - [Collection of solving techniques](http://forum.enjoysudoku.com/collection-of-solving-techniques-t3315.html)
> - HoDoKu: [Solving techniques](http://hodoku.sourceforge.net/en/techniques.php)
> - [How to solve sudoku](https://wordsup.co.uk/how-to-solve-sudoku)
> - [Solving Technique](http://sudopedia.enjoysudoku.com/Solving_Technique.html)
> - [Solving sudokus](https://homepages.cwi.nl/~aeb/games/sudoku/index.html)
> - [Strategy Families](https://www.sudokuwiki.org/Strategy_Families)
> - [Sudoku Examples from Xsudo](http://sudoku.allanbarker.com/sweb/examples.htm)
> - [Terminology](http://sudopedia.enjoysudoku.com/Terminology.html)
>
> 视频:
>
> - [标准数独技巧教程](https://www.bilibili.com/read/readlist/rl291187)

[Hidden Single]: https://sunnieshine.gitbook.io/sudoku-tutorial/002-hidden-single

[Hidden Single in Box]: https://sunnieshine.gitbook.io/sudoku-tutorial/002-hidden-single#part-1-gong-pai-chu-hidden-single-in-block

[Hidden Single in Row/Column]: https://sunnieshine.gitbook.io/sudoku-tutorial/002-hidden-single#part-2-hang-lie-pai-chu-hidden-single-in-line

[Naked Single]: https://sunnieshine.gitbook.io/sudoku-tutorial/003-naked-single

[Locked Candidates]: https://sunnieshine.gitbook.io/sudoku-tutorial/004-locked-candidates

[Pointing]: https://sunnieshine.gitbook.io/sudoku-tutorial/008-candidate-introduction#21-gong-qu-kuai-pointing

[Direct Pointing]: https://sunnieshine.gitbook.io/sudoku-tutorial/004-locked-candidates#part-1-gong-qu-kuai-pointing

[Claiming]: https://sunnieshine.gitbook.io/sudoku-tutorial/008-candidate-introduction#22-hang-lie-qu-kuai-claiming

[Direct Claiming]: https://sunnieshine.gitbook.io/sudoku-tutorial/004-locked-candidates#part-2-hang-lie-pai-chu-claiming

[Cascading Locked Candidates]: https://sunnieshine.gitbook.io/sudoku-tutorial/004-locked-candidates#part-3-zu-he-qu-kuai-ji-lian-qu-kuai-cascading-locked-candidates

[Hidden Subset]: https://sunnieshine.gitbook.io/sudoku-tutorial/005-hidden-subsets

[Hidden Pair]: https://sunnieshine.gitbook.io/sudoku-tutorial/008-candidate-introduction#321-yin-xing-shu-dui-hidden-pair

[Direct Hidden Pair]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5178

[Hidden Triple]: https://sunnieshine.gitbook.io/sudoku-tutorial/008-candidate-introduction#322-yin-xing-san-shu-zu-hidden-triple

[Direct Hidden Triple]: https://sunnieshine.gitbook.io/sudoku-tutorial/005-hidden-subsets#part-2-yin-xing-san-shu-zu-hidden-triple

[Hidden Quadruple]: https://sunnieshine.gitbook.io/sudoku-tutorial/005-hidden-subsets#part-3-yin-xing-si-shu-zu-hidden-quadruple

[Naked Subset]: https://sunnieshine.gitbook.io/sudoku-tutorial/006-naked-subsets

[Naked Subset+]: https://sunnieshine.gitbook.io/sudoku-tutorial/006-naked-subsets#part-6-yin-cang-zai-xian-xing-shu-zu-nei-bu-de-qu-kuai

[Naked Pair]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5193

[Naked Triple]: https://sunnieshine.gitbook.io/sudoku-tutorial/006-naked-subsets#part-2-xian-xing-san-shu-zu-naked-triple

[Naked Quadruple]: https://sunnieshine.gitbook.io/sudoku-tutorial/006-naked-subsets#part-3-xian-xing-si-shu-zu-naked-quadruple

[Locked Subset]: https://sunnieshine.gitbook.io/sudoku-tutorial/006-naked-subsets#part-7-si-suo-shu-zu-he-ge-bu-shu-zu-locked-subset

[Fish]: https://sunnieshine.gitbook.io/sudoku-tutorial/009-normal-fish

[宫内鱼]: https://zhuanlan.zhihu.com/p/34808058

[X-Wing]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5196

[Swordfish]: https://sunnieshine.gitbook.io/sudoku-tutorial/009-normal-fish#part-3-san-lian-lie-jian-yu-swordfish

[Jellyfish]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5198

[Finned Fish]: https://sunnieshine.gitbook.io/sudoku-tutorial/011-fin-1-normal-fin

[Finned X-Wing]: https://sunnieshine.gitbook.io/sudoku-tutorial/011-fin-1-normal-fin#part-1-dai-yu-qi-de-er-jie-yu-finned-xwing

[Finned Swordfish]: https://sunnieshine.gitbook.io/sudoku-tutorial/011-fin-1-normal-fin#part-2-dai-yu-qi-de-san-jie-yu-finned-swordfish

[Finned Jellyfish]: https://sunnieshine.gitbook.io/sudoku-tutorial/011-fin-1-normal-fin#part-3-dai-yu-qi-de-si-jie-yu-finned-jellyfish

[Bivalue Universal Grave]: https://zhuanlan.zhihu.com/p/33546333

[Unique Rectangle]: https://zhuanlan.zhihu.com/p/33282261

[Incomplete UR]: https://zhuanlan.zhihu.com/p/34240377

[活用唯一矩形]: https://zhuanlan.zhihu.com/p/34319844

[UR Type 1]: http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=685

[UR Type 2]: http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=706

[UR Type 3]: http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=803

[UR Type 4]: http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=883

[Hidden Unique Rectangle]: http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=1059

[Unique Loop]: https://zhuanlan.zhihu.com/p/33444291

[Avoidable Rectangle]: https://zhuanlan.zhihu.com/p/33521739

[XY-Wing]: 图谱/链/标准链/规则Wing/双分支匹配法.md

[XYZ-Wing]: 图谱/链/标准链/规则Wing/三分支匹配法.md

[伪数组和跨区数组]: https://zhuanlan.zhihu.com/p/33632335

[均衡性数组]: https://zhuanlan.zhihu.com/p/33661648

[Skyscraper]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5213

[Two Strings Kite]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5214

[Turbot Fish]: https://zhuanlan.zhihu.com/p/33677126

[Common Types Chain]: https://zhuanlan.zhihu.com/p/33703144

[X-Chain]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5226

[XY-Chain]: http://www.sudokufans.org.cn/forums/topic/38/?do=findComment&comment=210

[W-Wing]: http://www.sudokufans.org.cn/forums/topic/83/?do=findComment&comment=625

[M-Wing]: http://www.sudokufans.org.cn/forums/topic/111/?do=findComment&comment=857

[Dead Loop]: https://zhuanlan.zhihu.com/p/33741146

[ALS初步]: https://zhuanlan.zhihu.com/p/33769864

[ALS的一般拓展结构]: https://zhuanlan.zhihu.com/p/33770218

[X-Cycle]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5225

[Guardians]: http://www.sudokufans.org.cn/forums/topic/38/?do=findComment&comment=247

[Empty Rectangle]: http://www.sudokufans.org.cn/forums/topic/1053/?do=findComment&comment=4859

[Fireworks]: 图谱/链/烟花/烟花.md

[Triple Firework]: 图谱/链/烟花/三重烟花.md

[Quadruple Firework]: 图谱/链/烟花/四重烟花.md

[Remote Pairs]: http://www.sudokufans.org.cn/forums/topic/42/?do=findComment&comment=471

[Almost Locked Pair]: 图谱/待定数组/欠一数组/欠一数对.md

[毛刺数组]: https://zhuanlan.zhihu.com/p/33820355

[ALS的综合运用]: https://zhuanlan.zhihu.com/p/33820410

[Almost UR]: https://zhuanlan.zhihu.com/p/33849857

[Forcing AR]: https://zhuanlan.zhihu.com/p/34393585

[Domino Loop]: http://www.sudokufans.org.cn/forums/topic/1660/
