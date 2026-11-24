# ACL-Findings2026 · 自然语言处理中的对抗攻击与防御方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【OSCR-Attack: One-Shot Character Level Attacks through Self-Optimizing Continuous Relaxation ｜字符级对抗攻击的连续松弛优化

研究机构：西北工业大学

作者：Lingyi Kong、Zhuo Liu、Zhanghao Hu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e9fd3cecc8ee)

> 字符级文本对抗攻击旨在通过插入少量字符诱导大语言模型（LLM）产生错误预测，同时保持语义不变。传统方法依赖逐步贪心搜索，在离散空间中存在效率低下且易陷入局部最优的瓶颈。OSCR-Attack 提出将离散的插入位置与字符选择松弛为连续分布，通过端到端梯度优化实现一次性多位置扰动。该方法在攻击成功率与语义保持的平衡上优于现有基线，但其连续松弛到离散映射的冲突解决机制在复杂分词边界下的鲁棒性尚待检验。

】

---

【TinyAttack: Exploring Stylistic Vulnerabilities in Large Language Models ｜基于Unicode样式变换的大语言模型对抗攻击

作者：Mamta Mamta、Bogdan Grecu、Oana Cocarascu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2eadcea15a32)

> 大语言模型（LLM）在自然语言处理任务中表现优异，但其对输入扰动的脆弱性在安全敏感场景（如仇恨言论检测、事实核查）中构成严重威胁。现有对抗攻击多聚焦于词级同义词替换或字符级增删，忽略了真实用户生成内容中日益普遍的Unicode样式变形（如上标、下标、特殊字体）这一隐蔽攻击向量。TinyAttack提出了一种利用五种Unicode样式变换的黑盒攻击框架，通过LLM自归因机制以极低查询成本定位关键词并实施扰动。该框架揭示了LLM分词器对非标准字符的处理缺陷，但其在不同模型间的鲁棒性差异及防御有效性仍存疑。

】
