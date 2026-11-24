# CVPR2026最新论文 ｜Paper2Figure: A Multi-Agent Collaborative System for Figure Generation Towards Academic Research Paper ｜学术示意图生成中的语义-美学解耦

作者：Siwei Han、Haonian Ji、Siyang Xin 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_263a1e5b7d42)

> 学术示意图的自动化生成长期受困于语义准确性与视觉美学的不可兼得：代码生成范式（SVG/Mermaid）结构严谨但布局僵化，图像生成范式（GPT-Image-1）视觉丰富但逻辑混乱。本文切入点在于引入结构化中间语言FigScript，通过双智能体协作实现语义解析与视觉精修的解耦。其核心做法是生成智能体将文本转为FigScript，精修智能体基于渲染图像反馈迭代修正。该方案在自建基准上显著优于基线，但其评估依赖LLM评分，且缺乏对复杂拓扑结构的通用性验证。

## 研究背景

当研究者试图将论文中的复杂方法流程转化为可视化图表时，面临的核心困境是文本逻辑与视觉布局的非线性映射。传统方法依赖LLM直接生成SVG或Mermaid代码，这种“文本-代码”范式虽保留了结构可编辑性，但代码的冗长性与渲染器的固定布局规则导致生成的图表常出现元素重叠、间距失衡等视觉缺陷。为突破代码范式的布局瓶颈，研究者转向文本到图像（Text-to-Image）生成模型，如GPT-Image-1，这类模型能产生具有丰富纹理的图像，却因缺乏符号推理能力，常出现文字扭曲、箭头连接错误等语义失真问题。

现有方法在“结构保真”与“视觉质量”之间呈现明显的零和博弈。代码生成路线（如MoCA、DaVinci）将代码视为图表的精确表示，优势在于可执行验证与结构一致性，但牺牲了美学自由度；图像生成路线则相反，视觉表现力强但难以保证逻辑正确性。这一矛盾在学术示意图生成中尤为突出，因为此类图表不仅要求数据准确，还需符合出版级的排版规范。Paper2Figure的切入点在于识别出“中间表示”的缺失：现有方法要么直接生成像素（不可编辑），要么生成底层代码（难以控制美学），缺乏一种既能承载语义逻辑又能指导视觉布局的抽象层级。

## 核心方法

### 结构化中间语言 FigScript

本文问题与通用代码生成流程的关键差异在于，传统SVG/Mermaid生成是“文本-代码”的直接映射，而本文引入FigScript作为“文本-结构-视觉”的中介。FigScript定义图表为包含节点、边、容器及样式属性的层次化图，其抽象层级介于SVG的底层绘图指令与Mermaid的高层声明之间。这种设计动机在于解决LLM直接生成SVG时因代码冗长导致的注意力稀释问题，以及Mermaid固定语法无法表达复杂布局的局限。FigScript允许智能体在概念层面推理图表结构，同时通过参数化控制实现细粒度的视觉定制。

### 双智能体协作与视觉反馈闭环

生成阶段由Plan、Module、Layout三个智能体协作，将文本描述转化为初始FigScript $S_{initial}$ 并渲染为图像 $F_{initial}$。精修阶段引入Critic、Refine、Edit智能体，形成基于视觉反馈的闭环。Critic Agent分析 $F_{current}$ 检测视觉缺陷，Refine Agent制定修正计划 $R$，Edit Agent更新FigScript。该闭环的迭代过程可形式化为：

$$ S_{i+1} = \text{Edit}(S_i, \text{Refine}(\text{Critic}(F_i))), \quad F_{i+1} = \text{Render}(S_{i+1}) $$

其中 $i$ 为迭代次数，默认 $N=1$。这一设计解决了纯文本推理无法感知渲染后视觉冲突（如文字重叠、颜色冲突）的问题，通过“渲染-评估-修正”循环，使图表在语义准确性的基础上逐步收敛至美学最优。

## 实验评估

实验在自建Paper2Figure Bench（100个学术图表）上进行，基线涵盖SVG生成（GPT-5, Claude 4 Opus等）、Mermaid生成及图像生成（GPT-Image-1, Nano Banana）。基线覆盖审计显示，本文未对比MoCA、REChart等专用图表生成SOTA，这些方法在数据图表结构保真上表现优异，但本文聚焦示意图美学，任务特性不同导致基线选择侧重通用LLM。

| 方法 | 类型 | Accuracy | Beauty | Completeness | Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-5 | SVG | 81.5 | 72.5 | 57.0 | 65.1 |
| Claude 4.5 Sonnet | SVG | 82.0 | 72.0 | 58.0 | 63.8 |
| GPT-Image-1 | Image | 30.5 | 50.5 | 34.0 | 34.9 |
| Paper2Figure (w/o Refinement) | FigScript | 73.0 | 83.0 | 71.0 | 74.8 |
| Paper2Figure (full) | FigScript | 77.5 | 82.5 | 77.5 | 79.2 |

Paper2Figure (full)在平均得分上领先最强基线GPT-5达14.1%。消融实验显示，精修阶段对Beauty和Completeness提升显著，但Accuracy提升有限（73.0至77.5），表明精修主要优化视觉布局而非语义纠错。

评估边界方面，本文采用LLM-as-a-Judge评分，虽与人类评分相关性高（Pearson 0.7345），但LLM自身的美学偏好可能引入偏差。可复现性上，论文未提供代码URL，且FigScript的具体语法规范未完全公开，限制了外部复现。

## 关联研究分析

从问题动机看，Paper2Figure与MoCA、DaVinci同属代码生成范式，但MoCA侧重数据图表的结构保真与可执行性，而本文聚焦示意图的美学布局与出版级质量。这一差异源于任务特性：数据图表需精确数值映射，而示意图需视觉叙事。MoCA未解决布局美学问题，因其评估指标（执行率）不涵盖视觉质量，这暗示代码范式在美学控制上存在盲区。

从方法设计看，Paper2Figure与REChart均利用智能体框架，但REChart聚焦编辑效率与推理预算控制，本文聚焦初始生成质量与视觉反馈精修。REChart的混合奖励机制（效率+保真度）未涉及美学维度，而本文的Critic Agent显式评估视觉缺陷。这种设计差异表明，智能体框架在图表生成中的价值取决于其反馈信号的类型：REChart优化过程效率，Paper2Figure优化结果质量。

## 总结

Paper2Figure旨在解决学术示意图生成中语义准确性与视觉美学的矛盾。其切入点在于引入FigScript作为结构化中间语言，通过双智能体协作实现语义解析与视觉精修的解耦。实验证明，该方法在自建基准上平均得分79.2，较最强基线提升14.1%。然而，其边界在于评估依赖LLM评分，且FigScript的抽象层级可能限制复杂拓扑结构的表达能力。当图表包含非线性循环或动态交互元素时，FigScript的层次化图结构是否仍能保持语义-视觉的一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_263a1e5b7d42)