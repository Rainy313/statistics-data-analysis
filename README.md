# 统计与数据分析 · 学习仓库

本仓库用于记录「统计与数据分析」课程的学习笔记、练习代码与项目，同时承载「用 AI 构建个人概念学习资料生成 Skill」课程作业的成果。

## 目录结构

```
statistics-data-analysis/
├── README.md                 # 仓库说明
├── .gitignore                # Git 忽略规则
├── notes/                    # 统计课程学习笔记（Markdown）
│   └── 01-统计学基础概念.md
├── examples/                 # 统计课程示例代码
│   └── descriptive_stats.py  # 描述性统计示例
├── .workbuddy/skills/        # 项目级 AI Skill
│   └── concept-study-guide/
│       └── SKILL.md          # 概念学习资料生成 Skill
└── learning-materials/       # AI 作业：概念学习资料
    ├── agent.html            # 概念一：Agent（智能体）
    ├── llm-context.html      # 概念二：大模型的上下文
    ├── skill.html            # 概念三：Skill（智能体技能）
    └── concept-relationship.md # 三个概念的关系说明（含 Mermaid 图）
```

## 项目级 Skill：concept-study-guide

**用途**：输入任意一个学习概念，按固定的学习设计生成一份结构化 HTML 学习资料（学习目标、核心问题、个人解释、核心机制、应用场景、概念辨析、自测题、可核查的参考来源），用于本仓库的概念积累与复习。

**存放路径**：`.workbuddy/skills/concept-study-guide/SKILL.md`

**在 WorkBuddy 中调用**：

1. 在 WorkBuddy 中打开本仓库所在目录（Skill 为项目级，仅在本仓库内可用）；
2. 直接用自然语言下达任务，例如：「用 concept-study-guide 学习"检索增强生成（RAG）"，输出到 learning-materials/ 目录」；
3. Skill 生成后按其自检清单逐项核对，人工修正后再提交。

**已生成的学习资料**：

- [Agent（智能体）](learning-materials/agent.html)
- [大模型的上下文](learning-materials/llm-context.html)
- [Skill（智能体技能）](learning-materials/skill.html)
- [三个概念的关系说明](learning-materials/concept-relationship.md)

## AI 使用与人工核查说明

本仓库的 Skill 与学习资料由 AI（WorkBuddy）辅助生成，本人完成了以下核查与修改：

- **来源核查**：三份资料中的全部参考链接均已逐一点击访问，确认页面真实存在、内容与标注的支撑部分一致；不确定的来源一律未收录。
- **内容改写**：各资料的"个人解释"基于我自己的原有认知与类比改写，未整段照搬 AI 对话或来源原文；AI 初稿中偏空泛的场景描述已替换为具体场景。
- **结构修正**：按 SKILL.md 的自检清单逐项检查（概念边界、核心问题是否有对应章节、自测题答案要点是否正确），修正后定稿。
- **关系说明**：concept-relationship.md 中的 Mermaid 图与"我的判断"一节为本人理解的组织与表达。
- **敏感信息**：仓库不含 API Key、密码等敏感信息；.gitignore 中已加入排除规则，凭据类文件（.env 等）不会被提交。

## 统计课程学习大纲（持续更新）

- [x] 统计学基础概念（总体、样本、变量类型）
- [x] 描述性统计（均值、中位数、方差、标准差）
- [ ] 概率与分布
- [ ] 假设检验
- [ ] 回归分析
- [ ] 数据分析实战

## 运行示例

统计课程示例代码使用 Python 3 编写，依赖 `numpy` 与 `pandas`：

```bash
pip install numpy pandas
python examples/descriptive_stats.py
```

## 关于

作者：Rainy313
