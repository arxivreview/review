# ACL-Findings2026 · 高效大语言模型架构方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【SCALE: Upscaled Continual Learning of Large Language Models ｜宽度扩展持续学习架构

作者：Jin-woo Lee、Junhwa Choi、Bongkyu Hwang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0b05b7bda0f3)

> 大语言模型在持续预训练中面临容量扩展与知识保留的结构性冲突，深度扩展虽增加层数却扰动原有表示，导致灾难性遗忘。现有参数高效微调方法不增加新容量，而深度扩展方法缺乏函数保持保证。SCALE 通过宽度扩展冻结原参数并插入轻量级线性模块，结合令牌级路由在保持与适应路径间动态切换，实现了稳定性与可塑性的可控权衡。该架构在合成传记任务上显著抑制了遗忘，但在真实多语言语料上的新知识获取能力仍显有限。

】

---

【Vocab Diet: Reshaping the Vocabulary of LLMs via Vector Arithmetic ｜组合式词表重构

研究机构：以色列耶路撒冷希伯来大学

作者：Yuval Reif、Guy Kaplan、Roy Schwartz

论文原文见 [arXiv](https://arxiv.org/abs/2510.17001)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d84b8fd285dc)

> 大语言模型词表设计长期面临资源分配失衡：高频词的形态变体（如 walk, walked）占据大量独立 Token 槽位，挤压了多语言覆盖与低频词空间。现有 BPE 算法将形态变体视为独立单元，忽略了嵌入空间中已存在的线性结构。本文提出通过向量算术将词表重构为“基础词+变换向量”的组合形式，在冻结骨干的前提下释放 10-40% 的词表空间。该方法验证了 LLM 对组合式表示的内在理解能力，但派生词的低准确率暴露了线性假设在复杂形态学中的局限。

】
