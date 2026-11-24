# ACL-Findings2026 · 电子健康记录表示学习与预测建模方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HypEHR: Hyperbolic Modeling of Electronic Health Records for Efficient Question Answering ｜超球面电子健康记录问答

研究机构：美国石溪大学

作者：Yuyu Liu、Sarang Rajendra Patil、Mengjia Xu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21027)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21027)

> 电子健康记录（EHR）问答旨在从患者纵向记录中回答自然语言临床问题，但现有主流方案要么依赖计算昂贵且难以本地部署的大语言模型（LLM），要么忽略临床数据固有的层级结构。本文切入点在于利用医学本体与患者轨迹的超球面几何特性，构建一个仅含22M参数的紧凑模型。通过Lorentz流形上的序列编码与几何一致交叉注意力，HypEHR在无需LLM的设定下实现了与LLM基线相当的性能。其价值在于验证了小模型在结构化数据上的潜力，但超球面计算的工程稳定性与生成式问答的扩展性仍存疑。

】

---

【MedCPI: A Construct–Personalize–Integrate Framework for KG-enhanced Clinical Prediction ｜任务引导式知识图谱增强临床预测框架

研究机构：英国埃克塞特大学

作者：Hang Wang、Hang Dong、Lu Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7151df4fd0d7)

> 电子健康记录（EHR）数据稀疏且异构，传统序列模型难以捕捉细粒度临床语义，而直接引入多源医学知识图谱（MKG）又面临Schema噪声与任务无关性干扰。现有方法在知识提取与患者个性化环节缺乏针对性控制，导致弱相关节点稀释预测证据。MedCPI通过“构建-个性化-整合”三阶段框架，利用大语言模型（LLM）进行任务引导的Schema归纳，并实施受控局部扩展构建患者级知识图谱，实现了知识选择与纵向时序的动态对齐。该框架在MIMIC-III/IV上取得了SOTA性能，但其对LLM离线归纳的依赖及跨机构泛化能力仍存疑。

】

---

【RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models ｜递归提示调优整合结构化电子健康记录编码器与大语言模型

研究机构：美国堪萨斯大学

作者：Arya Hadizadeh Moghaddam、Drew Ross、Mohsen Nayebi Kerdabadi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17725)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17725)

> 大语言模型（LLM）在处理结构化电子健康记录（EHR）时面临时序结构丢失与群体模式缺失的双重困境，导致其难以捕捉临床轨迹的纵向依赖与跨患者共性。现有方法要么依赖文本线性化而忽略时间维度，要么孤立推理而无法利用群体统计特征。RePrompT 通过状态递归提示与结构编码提示的双软提示机制，在不修改 LLM 架构的前提下实现了时序感知与群体对齐。该方法在 MIMIC-III/IV 上优于传统 EHR 基线，但精度显著低于当前 SOTA，且缺乏对知识图谱等外部语义增强的利用，其临床部署价值仍受限于骨干模型能力与融合机制的瓶颈。

】
