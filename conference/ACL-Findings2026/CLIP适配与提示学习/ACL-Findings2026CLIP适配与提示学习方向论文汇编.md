# ACL-Findings2026 · CLIP适配与提示学习方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Soft Head Selection for Injecting ICL-Derived Task Embeddings ｜软头选择注入ICL任务嵌入

研究机构：韩国首尔大学

作者：Jungwon Park、Jimyeong Kim、Changin Choi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_911366acf3cd)

> 大语言模型（LLM）任务适配长期受困于参数高效微调（PEFT）的高训练成本与上下文学习（ICL）的高推理开销，现有嵌入注入方法虽试图折中，却因缺乏对注意力头功能差异的精准定位而性能不稳定。SITE 将头选择建模为连续优化问题，通过梯度下降学习每个注意力头的注入权重，在零样本推理时仅替换关键头的激活。该方法以 1024 个可训练参数逼近 LoRA 性能，但其在复杂推理任务上的绝对精度仍低于 PEFT，且依赖内部激活访问，限制了其在闭源模型中的应用。

】
