# -*- coding: utf-8 -*-
"""
描述性统计示例
统计与数据分析课程 · 练习

用 numpy 和 pandas 计算一组考试成绩的
均值、中位数、方差、标准差、极差等指标。
"""

import numpy as np
import pandas as pd


def main():
    # 一组模拟的学生考试成绩（满分 100）
    scores = [78, 85, 92, 88, 76, 95, 90, 60, 88, 82, 73, 91, 84, 79, 86]

    # 转为 numpy 数组
    arr = np.array(scores)

    print("=" * 40)
    print("描述性统计结果")
    print("=" * 40)

    # 集中趋势
    print(f"样本量 n        : {arr.size}")
    print(f"均值 mean       : {arr.mean():.2f}")
    print(f"中位数 median   : {np.median(arr):.2f}")
    print(f"众数 mode       : 见下方 pandas 结果")

    # 离散程度
    print(f"极差 range      : {arr.max() - arr.min():.2f}")
    print(f"方差 var        : {arr.var(ddof=1):.2f}  (样本方差)")
    print(f"标准差 std      : {arr.std(ddof=1):.2f}  (样本标准差)")

    # 分布
    print(f"最小值 min      : {arr.min()}")
    print(f"最大值 max      : {arr.max()}")

    print()
    print("=" * 40)
    print("pandas describe 一览表")
    print("=" * 40)

    s = pd.Series(scores, name="成绩")
    print(s.describe().round(2))

    print()
    print("众数 mode:", s.mode().tolist())


if __name__ == "__main__":
    main()
