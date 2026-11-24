# ACL-Findings2026 · 基于大语言模型的知识图谱构建方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Topology: Generative Node Importance Estimation via Structure-Guided Semantic Reasoning ｜超越拓扑：基于结构引导语义推理的节点重要性估计

研究机构：北京邮电大学

作者：Kuofei Fang、Siyan Wu、Yu Guo 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed6425111283)

> 节点重要性估计（NIE）旨在量化知识图谱（KG）中实体的显著性，但现有方法受限于监督范式与局部拓扑聚合，导致跨域泛化能力薄弱。GenNIE 将 NIE 重构为生成式推理任务，通过混合参数高效微调（Hybrid PEFT）联合优化生成损失与结构对比损失，使大语言模型（LLM）在冻结骨干下直接输出重要性分数。该方法在 FB15K 上 NDCG@100 达 0.9755，显著优于 GNN 基线，但其对大规模稀疏图的感知瓶颈及端到端架构的误差累积风险仍存疑。

】

---

【CogNet-KG: Empowering Tutoring Dialogues with a Cognitively-Structured Knowledge Graph for STEM Learning ｜认知结构化教育知识图谱驱动的教学对话生成

研究机构：北京师范大学

作者：Ding Yu、Yu Lu、Tengju Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df64b9f4a5b8)

> 智能辅导系统（Intelligent Tutoring System, ITS）面临的核心困境是，大语言模型（Large Language Model, LLM）虽具备流畅的对话能力，却缺乏基于认知逻辑的引导式推理能力，导致无法有效诊断学生误区或促进概念迁移。现有教育知识图谱（Educational Knowledge Graph, EKG）多局限于单一学科或简单的语义/顺序关系，且未与具体学习目标绑定，致使图谱结构无法直接转化为教学决策。本文通过构建跨学科、认知结构化的 CogNet-KG，并以此生成自适应教学对话数据集，训练出内化图谱逻辑的专用模型 CogTutor-LM。该方案在自建基准上显著提升了教学连贯性与指导合理性，但其有效性依赖于特定 STEM 领域的结构化数据，且缺乏对图谱结构因果贡献的独立验证。

】

---

【SocraticKG: Knowledge Graph Construction via QA-Driven Fact Extraction ｜问答驱动的知识图谱构建

研究机构：韩国首尔大学

作者：Sanghyeok Choi、Woosang Jeon、Kyuseok Yang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5480c8804628)

> 大语言模型（LLM）直接抽取三元组常因缺乏全局语义视角导致图谱碎片化，而预定义实体结构又易造成事实遗漏。SocraticKG 将问答对（QA）形式化为结构化中间表示，通过 5W1H 引导的语义展开平衡事实覆盖与结构连贯。该方法在 MINE 基准上以 96.3% 的事实保留率领先，但其对 LLM 推理能力的依赖及计算成本尚未充分量化，限制了其在资源受限场景下的适用性。

】
