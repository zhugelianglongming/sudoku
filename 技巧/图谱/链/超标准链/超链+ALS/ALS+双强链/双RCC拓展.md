# ALS+双强链（双RCC拓展）

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [原理](#%E5%8E%9F%E7%90%86)
  - [技巧拓展](#%E6%8A%80%E5%B7%A7%E6%8B%93%E5%B1%95)
  - [技巧组合](#%E6%8A%80%E5%B7%A7%E7%BB%84%E5%90%88)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 原理

因为
- 存在 2 个区域`Region1`、`Region2`:
	- `Region1`存在[[定区域准集合数组]]`ALS1`：
		- 准集合候选数为`XYP[1,i]`
	- `Region2`存在[[定区域准集合数组]]`ALS2`：
		- 准集合候选数包含`XYQ[1,j]`
	- `X`是`ALS1`和`ALS2`的[[严格共享候选数]]
	- `Y`是`ALS1`和`ALS2`的[[严格共享候选数]]

所以
- `ALS1`和`ALS2`中的`X`的共同影响区域
	- 必不填入数字`X`
- `ALS1`和`ALS2`中的`Y`的共同影响区域
	- 必不填入数字`Y`
- `Region1`中
	- `ALS1`的单元格
		- 只有1个`X`或1 个`Y`
		- 必有`P[1,i]`
	- 其他单元格
		- 只有1个`X`或1 个`Y`
		- 必没有`P[1,i]`
- `Region2`中
	- `ALS2`的单元格
		- 只有1个`X`或1 个`Y`
		- 必有`Q[1,j]`
	- 其他单元格
		- 只有1个`X`或1 个`Y`
		- 必没有`Q[1,j]`

###  技巧拓展

- [[ALS+双强链]]：扩展[[严格共享候选数]]的数量
- [[标准环]]：扩展[[强关系]]的类型
	- [[同单元格异数强关系]]、[[同区域同数强关系]]→[[同区域异数强关系]]

###  技巧组合

- [[环]]
- [[定区域准集合数组]]

 > [SudokuWiki.org - Almost Locked Sets](https://www.sudokuwiki.org/Almost_Locked_Sets)
