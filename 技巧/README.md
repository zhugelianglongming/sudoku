# 数独技巧

> [技巧图谱](https://www.processon.com/embed/61c17b5f0791290c9efaf141)
> - 绿色虚线：技巧演进-分析数扩展
> - 蓝色虚线：技巧演进-分析区域扩展
> - 红色虚线：技巧组合
> 
> ![](http://assets.processon.com/chart_image/61c17b5f0791290c9efaf145.png)

## 入门级
- 摒除法 / 排除法 / [Hidden Single]
  - 宫摒除 / [Hidden Single in Box][] `参考难度系数`1.2
  - 行列摒除 / [Hidden Single in Row/Column] `参考难度系数`1.5
  > [练习](https://www.12634.com/learning/hs/index)
- 唯余法 / 唯一数 / 唯一法 / Last Value / [Naked Single][] `参考难度系数`2.3
  > [练习](http://www.sudokufans.org.cn/tools/finder.php)

## 初级
- 区块摒除 / [Locked Candidates][]
  - 宫区块摒除法 / [Pointing][]
    - 直观宫区块摒除法 / [Direct Pointing] `参考难度系数`1.7
    > [练习](https://www.12634.com/learning/pointing/index)
  - 列区块摒除法 / [Claiming][]
    - 直观列区块摒除法 / [Direct Claiming] `参考难度系数`1.9
    > [练习](https://www.12634.com/learning/claiming/index)
  - 组合区块 / [Cascading Locked Candidates][] `参考难度系数`2.8

## 中级
- 隐性数组 / [Hidden Subset][]
  - 隐性数对 / [Hidden Pair][]
    - 直观隐性数对 / [Direct Hidden Pair][] `参考难度系数`3.4
      > [练习](https://www.12634.com/learning/direct-hidden-pair/index)
    > [练习](https://www.12634.com/learning/hidden-pair/index)
  - 隐性三数组 / 隐性三数集 / [Hidden Triple][]
    - 直观隐性三数集 / [Direct Hidden Triple][] `参考难度系数`4.0
    > [练习](https://www.12634.com/learning/hidden-triplet/index)
  - 隐性四数组 / [Hidden Quadruple][] `参考难度系数`5.4
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
- 区块数组 / Naked Subset With Locked Candidates / [Naked Subset+][]
  - 区块三数组 `参考难度系数`3.7
  - 区块四数组 `参考难度系数`5.1
- 鱼 / 链列 / [Fish][]
  - 标准鱼
    - 二阶鱼 / 二链列 / [X-Wing][] `参考难度系数`3.2
      > [练习](https://www.12634.com/learning/x-wing/index)
    - 三阶鱼 / 剑鱼 / 三链列 / [Swordfish][] `参考难度系数`3.8
    - 四阶鱼 / 水母 / 四链列 / [Jellyfish][] `参考难度系数`5.2
  - 带鳍鱼 / 外鳍鱼 / [Finned Fish][]
    - 带鳍二阶鱼 / [Finned X-Wing][] `参考难度系数`3.4
    - 带鳍三阶鱼 / [Finned Swordfish][] `参考难度系数`4.0
    - 带鳍四阶鱼 / [Finned Jellyfish][] `参考难度系数`5.4
  - 宫内鱼 / Franken Fish
    - [标准宫内鱼][宫内鱼]
      - 宫内二阶鱼 / 宫内二阶鱼 /  Franken X-Wing
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
- 待定数组（标准） / ALS / Almost Locked Subset
  - 欠一数组 / ALC / [Almost Locked Candidates](https://zhuanlan.zhihu.com/p/33612543)
    - 欠一数对 / [Almost Locked Pair][] `参考难度系数`4.5
    - 欠一三数组 / Almost Locked Triple `参考难度系数`5.2
  - 伪数组 / ESP / [Extended Subset Principle][伪数组和跨区数组] `参考难度系数`7.5
  - 跨区数组 / DDS / [Distributed Disjointed Subset][伪数组和跨区数组] `参考难度系数`7.0
    - 融合式待定数组 / 双区域分布式跨区数组 / SDC / SdC / [Sue de Coq](https://zhuanlan.zhihu.com/p/33615105)
      - 无公共数型 / 基本融合版本 `参考难度系数`4.8+
      - 共享公共数型 / 带有交互数字的融合版本 `参考难度系数`4.9+
      - 独占公共数型 / 自噬SDC / Cannibalistic SDC `参考难度系数`4.9+
- 链
  - 标准链 / AIC / Alternating Inference Chain
    - [规则 Wing](https://zhuanlan.zhihu.com/p/33087864)
      - 双分支匹配法 / Y-Wing / [XY-Wing][] `参考难度系数`4.2
        > [练习](https://www.12634.com/learning/xy-wing/index)
      - 三分支匹配法 / [XYZ-Wing][] `参考难度系数`4.4
        > [练习](https://www.12634.com/learning/xyz-wing/index)
      - 四分支匹配法 / WXYZ-Wing `参考难度系数`4.6
      - 五分支匹配法 / VWXYZ-Wing `参考难度系数`4.85
      - ~~六分支匹配法 / UVWXYZ-Wing~~
      - ~~七分支匹配法 / TUVWXYZ-Wing~~
      - ~~八分支匹配法 / STUVWXYZ-Wing~~
      - ~~九分支匹配法 / RSTUVWXYZ-Wing~~
    - 双强链 / 多宝鱼 / [Turbot Fish][] `参考难度系数`4.2
      - 摩天楼 / 孪生二链列 / [Skyscraper][] `参考难度系数`4.05
        > [练习](https://www.12634.com/learning/skyscraper/index)
      - 双线风筝 / [Two Strings Kite][] `参考难度系数`4.1
- 空矩形 / [Empty Rectangle][]
- X链 / [X-Chain][]
- X环 / [X-Cycle][]
- 守护者/ [Guardians][]
- [XY-Chain](http://www.sudokufans.org.cn/forums/topic/38/?do=findComment&comment=210)
- Forcing Chain
  > [练习](https://www.12634.com/learning/forcing-chain/index)

## 骨灰级
- 致命结构
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
  - 可规避矩形 / AR / [Avoidable Rectangle][] `参考难度系数`4.5+
    - 标准型 / Type 1
    - 区块组性 / Type 2
    - 待定数组型 / Type 3
    - 正交共轭对型 / 隐形可规避矩形 / AR Type 4C / Hidden AR
  - 全双值坟墓 / BUG / [Bivalue Universal Grave][]  `参考难度系数`5.4+
    - 标准型 / Type 1
      > [练习](https://www.12634.com/learning/bug-type-1/index)
    - 待定数型 / Type 2
      > [练习](https://www.12634.com/learning/bug-type-2/index)
    - 待定数组型 / Type 3 
    - 共轭对型 / Type 4 
- [Group X-Chain](http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5227)
- [Multi X-Wing/XY-Cycle](http://www.sudokufans.org.cn/forums/topic/38/?do=findComment&comment=237)
- 远程数对 / [Remote Pairs][]
- [Y-Wing/W-Wing](http://www.sudokufans.org.cn/forums/topic/83/?do=findComment&comment=625)
- [M-Wing](http://www.sudokufans.org.cn/forums/topic/111/?do=findComment&comment=857)
- [Double Loop](http://www.sudokufans.org.cn/forums/topic/1660/)
- [Unique Rectangle 6-cell](http://www.sudokufans.org.cn/forums/topic/91/?do=findComment&comment=1114)

> - [技巧分类](分类/README.md)

# 流派
- 竞速（面向比赛） 
- 技巧（面向数独难题） 
- 编程（面向数独的计算机程序解决方案）

> - 文字
>   - [数独技巧教程](https://sunnieshine.gitbook.io/sudoku-tutorial/)
>   - [独·数之道](http://www.sudokufans.org.cn/forums/topic/69/)
>   - [三思](https://www.12634.com/learning/index)
>   - [数独术语](https://zh.wikipedia.org/wiki/%E6%95%B0%E7%8B%AC%E6%9C%AF%E8%AF%AD)
>   - [数独术语索引表](https://zhuanlan.zhihu.com/p/33475225) 
>   - [小向的标准数独技巧教程](http://sunnie-shine.gitee.io/sudokutechniquetutorial/SortByTutorial.html)
>   - [Collection of solving techniques](http://forum.enjoysudoku.com/collection-of-solving-techniques-t3315.html)
>   - HoDoKu: [Solving techniques](http://hodoku.sourceforge.net/en/techniques.php)
>   - [How to solve sudoku](https://wordsup.co.uk/how-to-solve-sudoku)
>   - [Solving Technique](http://sudopedia.enjoysudoku.com/Solving_Technique.html)
>   - [Solving sudokus](https://homepages.cwi.nl/~aeb/games/sudoku/index.html) 
>   - [Strategy Families](https://www.sudokuwiki.org/Strategy_Families) 
>   - [Sudoku Examples from Xsudo](http://sudoku.allanbarker.com/sweb/examples.htm)
>   - [Terminology](http://sudopedia.enjoysudoku.com/Terminology.html) 
> - 视频
>   - [标准数独技巧教程](https://www.bilibili.com/read/readlist/rl291187)


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
[XY-Wing]: http://www.sudokufans.org.cn/forums/topic/48/?do=findComment&comment=211
[XYZ-Wing]: http://www.sudokufans.org.cn/forums/topic/42/?do=findComment&comment=203
[伪数组和跨区数组]: https://zhuanlan.zhihu.com/p/33632335
[Skyscraper]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5213
[Two Strings Kite]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5214
[Turbot Fish]: https://zhuanlan.zhihu.com/p/33677126
[X-Chain]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5226
[X-Cycle]: http://www.sudokufans.org.cn/forums/topic/69/?do=findComment&comment=5225
[Guardians]: http://www.sudokufans.org.cn/forums/topic/38/?do=findComment&comment=247
[Empty Rectangle]: http://www.sudokufans.org.cn/forums/topic/1053/?do=findComment&comment=4859
[Remote Pairs]: http://www.sudokufans.org.cn/forums/topic/42/?do=findComment&comment=471
[Almost Locked Pair]: http://www.sudokufans.org.cn/forums/topic/57/?do=findComment&comment=360