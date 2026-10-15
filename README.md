# Scientific Figure Skills

两个可独立安装的科研图表 Skill：用真实数据绘制统计图，再根据图与统计口径撰写英文图注。

| Skill | 输入 | 输出 |
|---|---|---|
| [figure-draw](skills/figure-draw/SKILL.md) | 数据、实验/计算单位、统计口径、目标 Nature 或 Science 主刊、投稿阶段与尺寸 | 可编辑统计图、绘图代码、数据交接信息、中文证据与质量审查 |
| [figure-legend-writer](skills/figure-legend-writer/SKILL.md) | 科研图或面板描述、数据与统计口径、目标期刊 | 英文 figure legend、中文证据缺口与统计审查、期刊要求及字数核对 |

## 安装

在 Codex 中发送：

```text
$skill-installer
从 https://github.com/Han-Tao-scut/figure-legend-writer 安装：
skills/figure-draw
skills/figure-legend-writer
```

可以只安装其中一个。安装器按 Skill 子目录处理；仓库克隆到本地后，也需要将所选 Skill 加入当前环境的技能目录。私有仓库需要相应 GitHub 访问权限。若此前已安装旧版，请说明要更新已有 Skill，避免重复安装同名目录。

本仓库原来位于根目录的图注 Skill 已迁移至 `skills/figure-legend-writer/`；安装时请使用上面的新路径。原文件仍可从 Git 历史查看。

## 使用

绘制统计图：

```text
$figure-draw
根据附件中的数据绘制用于 Nature 主刊的统计图。
每行代表一个独立样本，分组和指标定义见数据说明。
请核对当前期刊要求，输出 PDF、可编辑 SVG、PNG 预览及中文审查。
```

撰写图注：

```text
$figure-legend-writer
根据这张图和随附统计口径，为 Science 主刊撰写英文图注，
并列出中文证据缺口与统计审查清单。
```

组合使用：

```text
使用 $figure-draw 绘制统计图，再使用 $figure-legend-writer
根据实际图、数据和统计口径撰写英文图注。
```

两个 Skill 各自可独立使用。绘图 Skill 会交接面板、指标/单位、样本量、误差定义、检验和来源；图注 Skill 根据这些信息检查图与文字的一致性。

## 内容与证据规则

- 不补造数据、n、P 值、误差范围、显著性、随机基准或机制解释。
- 不从均值与误差棒重建虚假的原始散点，不将技术重复、随机种子或重叠窗口默认视为独立样本。
- 统计图使用数据驱动的绘图库；生成式图像工具不用于绘制数据标记、坐标轴或统计结果。
- 区分 Nature 正刊、Nature Communications、Science 主刊及各自子刊；每次使用都核对目标期刊的官方实时要求。
- 信息不足时输出明确标注的草稿与缺口清单，不把美观或预设样式当作证据充分或投稿合规。

图注指南涵盖 Nature、Nature Communications、Science、Cell 和 PLOS Biology。绘图指南重点覆盖 Nature 与 Science 主刊的统计图。

## 来源与核对状态

期刊规范记录在各 Skill 的 references 中，快照日期为 2026-10-15。

- [图注期刊指南](skills/figure-legend-writer/references/journal-guidance.md)
- [绘图规范与来源记录](skills/figure-draw/references/journal-specifications.md)

Science 官方 HTML 和直接链接的绘图 PDF 已读取；其中尺寸、线宽和上传格式存在差异，指南保留这些差异并说明默认采用的规则。Cell 的部分官方正文在快照核对时无法读取，已注明。仓库提供摘要和官方链接，不包含期刊指南全文或第三方图像。

## 绘图脚本与验证

Skill 本身主要由指令和 references 组成。`figure-draw/scripts/figure_style.py` 是可选 Matplotlib 辅助脚本，不计算统计检验，也不能独自证明完整期刊合规。运行它时，所选环境需有 Matplotlib 和相应可用字体。

贡献者可运行结构检查：

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

结构检查覆盖 Skill 元数据、相对引用、UI 配置及 Python 语法。图表的数据正确性、统计有效性、最终尺寸下的视觉质量及实时期刊规则仍须按 Skill 工作流检查。
