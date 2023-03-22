# X环

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [原理](#%E5%8E%9F%E7%90%86)
  - [技巧组合](#%E6%8A%80%E5%B7%A7%E7%BB%84%E5%90%88)
  - [技巧转换](#%E6%8A%80%E5%B7%A7%E8%BD%AC%E6%8D%A2)
- [标签](#%E6%A0%87%E7%AD%BE)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 原理

因为
- 对于数字`X`
	- 存在一条`*-强关系-弱关系-*`交替形成的环`Loop`

所以
- 若将环`Loop`中单元格间隔标记为颜色`Color+`和`Color-`，则
	- 任一`Color+`单元格与任一`Color-`单元格的共同影响区域，必不填入数字`X`

> 数字`X`在环`Loop`内，要么都在`Color+`单元格中，要么都在`Color-`单元格中。

![X-Cycle](https://www.sudokuwiki.org/PuzImages/NiceL2.png)

###  技巧组合

- [[环]]：头尾可以通过[[共轭对]]连接的同数链
	- [[共轭对]] * 2n

###  技巧转换

- [[链/鱼/复杂鱼/复杂鱼|复杂鱼]]：从全盘视角观察

## 标签

- #Level/d

> [SudokuWiki.org - X-Cycles](https://www.sudokuwiki.org/X_Cycles)
