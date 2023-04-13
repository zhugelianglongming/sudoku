# ALS+双分支匹配法

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [原理](#%E5%8E%9F%E7%90%86)
  - [技巧组合](#%E6%8A%80%E5%B7%A7%E7%BB%84%E5%90%88)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 原理

因为
- 存在单元格`Cell1`，候选为`XY`
- 存在 2 个区域`Region1`、`Region2`：
	- `Region1`中存在[[定区域准集合数组]]`ALS1`：
		- 准集合候选数包含`XN`
		- 包含候选`X`的单元格都在`Cell1`的影响区域内
	- `Region2`中存在[[定区域准集合数组]]`ALS2`：
		- 准集合候选数包含`YN`
		- 含候选`Y`的单元格都在`Cell1`的影响区域内

所以
- `ALS1`和`ALS2`的共同影响区域
	- 必不填入数字`N`

###  技巧组合

- [[双分支匹配法]]
- [[定区域准集合数组]]
