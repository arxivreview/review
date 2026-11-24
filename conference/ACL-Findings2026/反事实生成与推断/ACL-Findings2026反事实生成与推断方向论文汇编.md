# ACL-Findings2026 · 反事实生成与推断方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DRIV-EX: Counterfactual Explanations for Driving LLMs ｜驾驶大语言模型的反事实解释生成

研究机构：法国格勒诺布尔阿尔卑斯大学

作者：Amaia Cardiel、Eloi Zablocki、Elias Ramzi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d015f88f7dad)

> 自动驾驶大语言模型（LLM）的决策过程缺乏透明度，传统思维链解释常被视为事后合理化而非因果驱动。现有离散优化方法在翻转决策时往往牺牲文本流畅性或语义邻近性，导致生成的反事实不可解释。DRIV-EX 通过解耦连续嵌入的梯度搜索与受控自回归解码，在保持文本连贯的前提下定位最小语义扰动。该方法在驾驶场景审计中有效暴露了模型对速度特征的隐性依赖，但其解释的因果忠实性受限于未显式建模外生噪声。

】

---

【Faithfulness vs. Safety: Evaluating LLM Behavior Under Counterfactual Medical Evidence ｜医学反事实证据下的LLM忠实性与安全性边界评估

研究机构：美国德克萨斯大学奥斯汀分校、美国东北大学

作者：Kaijie Mo、Siddhartha Venkatayogi、Chantal Shaib 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11886)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_612dc3e2602b)

> 在医疗问答中，大语言模型（LLM）被期望忠实于提供的证据上下文，但当证据本身是虚假或危险的（如声称海洛因降低乳腺癌风险）时，模型应如何响应？现有研究多关注有效证据下的推理准确率，忽略了证据与模型先验知识冲突时的行为模式。本文通过构建MEDCOUNTERFACT数据集，系统替换临床干预词为反事实刺激，评估9个前沿LLM在证据忠实性与安全护栏之间的权衡。结果显示，模型普遍盲目采纳反事实证据，缺乏对前提合理性的质疑能力，揭示了当前LLM在安全关键领域存在“忠实性压倒安全性”的系统性缺陷。

】
