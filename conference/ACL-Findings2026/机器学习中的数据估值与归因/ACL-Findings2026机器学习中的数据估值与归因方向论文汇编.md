# ACL-Findings2026 · 机器学习中的数据估值与归因方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EULoInf: Efficient Hessian-Free Entropy Based Uncertainty-Aware Data Influence Approximation ｜基于预测熵与单层梯度的无Hessian数据影响近似

研究机构：新加坡国立大学

作者：Runxin Cai、Jingtan Wang、Bryan Kian Hsiang Low

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_457afefd083e)

> 大语言模型微调中的数据估值面临逆Hessian-向量积（iHVP）计算带来的二次复杂度瓶颈，导致现有影响函数近似方法在大规模模型上内存与时间开销不可接受。EULoInf 抓住高影响数据与高预测熵之间的统计相关性，利用前向传播获取的Rényi熵替代昂贵的梯度范数计算，并引入仅针对最后一层的梯度点积符号以区分有益与有害样本。该方法将计算复杂度从二次降至线性，在GSM8K等任务上以41.13%的计算时间超越了最佳基线2.93%的精度，但其单层梯度近似在深层网络中的方向判别保真度仍存疑。

】
