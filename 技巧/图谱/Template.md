# Template

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [原理](#%E5%8E%9F%E7%90%86)
  - [技巧转换](#%E6%8A%80%E5%B7%A7%E8%BD%AC%E6%8D%A2)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 原理

因为
- 对于数字`X`：
	- 盘面所有可能布局情况是有限的

所以
- 对于所有可能布局的交集
	- 交集中的单元格
		- 必填入数字`X`
- 对于所有可能布局的并集
	- 并集外的单元格
		- 必不填入数字`X`

> 可叠加布局图形进行理解

###  技巧转换

- [[链/鱼/复杂鱼/复杂鱼|复杂鱼]]：从某单元格的视角出发分析

> [SudokuWiki.org - Pattern Overlay](https://www.sudokuwiki.org/Pattern_Overlay)
