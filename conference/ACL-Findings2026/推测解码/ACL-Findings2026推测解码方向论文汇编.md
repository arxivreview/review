# ACL-Findings2026 · 推测解码方向论文汇编

> 本方向共 13 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Accelerating Prefilling via Decoding-time Contribution Sparsity ｜解码时贡献稀疏性驱动的预填充加速

作者：Zhiyuan He、Yike Zhang、Chengruidong Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3a8549e2add1)

> 长上下文大语言模型（LLM）的预填充阶段受限于注意力机制的二次方计算复杂度，导致首字延迟（TTFT）随输入长度急剧增加。现有动态稀疏方法依赖注意力分数幅值进行块筛选，忽略了部分高分块对后续解码实际贡献极低的特性，导致计算冗余。本文通过梯度分析识别出“解码时贡献稀疏性”，提出TriangleMix静态注意力模式，在部分层跳过中间查询-键（Middle Q-K）区域的计算。该方法在128K输入下实现15.3倍注意力内核加速，精度损失小于0.5%，但其静态掩码机制在动态负载下的鲁棒性尚存疑。

】

---

【DiffuSpec: Unlocking Diffusion Language Models for Speculative Decoding ｜扩散语言模型投机解码框架

研究机构：清华大学、南方科技大学

作者：Guanghao Li、Zhihui Fu、Min Fang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02358)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02358)

> 自回归解码的串行瓶颈长期依赖轻量级自回归草稿模型缓解，但草稿阶段本身的串行前向传播限制了并行验证的收益上限。现有无训练方案受限于草稿生成吞吐量或分布对齐精度，而扩散语言模型（DLM）虽能单次前向生成多token块，却因双向条件生成导致局部最优token无法构成因果一致路径，且固定草稿长度引发速度-质量权衡失衡。DiffuSpec通过因果一致性路径搜索（CPS）在DLM生成的token格子上提取左到右最优路径，并结合自适应草稿长度（ADL）控制器动态调整块大小，实现了无需训练的即插即用加速。该框架在Spec-Bench上取得3.08x加速比，接近训练式方法，但其性能上限是否受限于DLM本身的推理延迟而非验证阶段，论文未给出明确归因。

】

---

【Fast-Decoding Diffusion Language Models via Progress-Aware Confidence Schedules ｜进度感知置信度调度

作者：Amr Mohamed、Yang Zhang、Michalis Vazirgiannis 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4909e67c1268)

> 扩散大语言模型（Diffusion Large Language Models, dLLM）的解码效率受限于固定的去噪步数预算，导致在简单输入上产生大量冗余计算。现有早停方法依赖离散阈值或局部信号，在长文本任务中易崩溃。本文提出 SchED，通过聚合全答案区域的 Top-2 Logit 边际，并与平滑的进度感知阈值比较，实现无损早停。该方法在指令微调模型上实现约 4 倍加速且质量保持 99.8% 以上，但其加速收益高度依赖指令微调带来的熵衰减特性，在基础模型上收益有限。

】

---

【From Tokens to Steps: Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning ｜从Token到Step：验证感知的投机解码

作者：Kiran Purohit、Ramasuri Narayanam、Soumyabrata Pal

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93a681b62387)

> 多步推理任务中，标准投机解码（Speculative Decoding, SD）的Token级验证常因拒绝语义正确但概率低的草稿Token而引发错误级联，导致加速失效。现有方案依赖外部奖励模型（Process Reward Model, PRM）进行步骤级验证，但引入了高延迟与任务泛化性差的问题。SPECGUARD通过集成模型内部的注意力接地与对数概率信号，在步骤级执行自适应验证，无需外部验证器。该方法在推理基准上提升了准确率并降低了延迟，但其对标准SD无损性假设的偏离及在通用文本生成中的适用性仍存疑。

】

---

【LogitSpec: Accelerating Retrieval-based Speculative Decoding via Next Next Token Speculation ｜基于末位Logit推测的检索式投机解码

研究机构：中国科学技术大学

作者：Tianyu Liu、Qitan Lv、Hao Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f7cbcdda5709)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但传统无训练检索方法常因上下文匹配失败导致加速失效。LogitSpec 发现目标模型末位 Logit 具备预测“下下个 Token”的高鲁棒性，将其作为检索锚点以扩展搜索空间。该方法无需额外草稿模型，通过双锚点检索显著提升了草稿命中率。其价值在于以零训练成本实现了接近训练式方法的加速比，但受限于检索机制本身，在长上下文或低重复率场景下的上限仍低于特征对齐路线。

】

---

【MARS: Unleashing the Power of Speculative Decoding via Margin-Aware Verification ｜边际感知投机验证

研究机构：加拿大麦吉尔大学、北京大学

作者：Jingwei Song、Xinyu Wang、Hanbin Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15498)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15498)

> 投机解码（Speculative Decoding, SD）旨在通过草稿-验证范式突破大语言模型（LLM）自回归解码的内存带宽瓶颈，但现有方法在验证阶段普遍采用严格的精确匹配或拒绝采样，导致在目标模型置信度低时产生大量无效回滚。本文指出这种“验证严格性与模型内在不确定性”的错配是加速比停滞的关键，提出边际感知投机验证（Margin-Aware Speculative Verification, MARS），一种基于目标模型 Logit 边际的免训练自适应验证策略。该方法在保持生成质量近乎无损的前提下，显著提升了接受长度与端到端加速比，但其有损特性对传统无损 SD 的定义边界提出了挑战。

】

---

【Multi-Drafter Speculative Decoding with Alignment Feedback ｜多草稿器投机解码与对齐反馈

作者：Taehyeon Kim、Hojung Jung、Se-Young Yun

论文原文见 [arXiv](https://arxiv.org/abs/2604.05417)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e5336fb8d57e)

> 投机解码（Speculative Decoding, SD）旨在通过草稿-验证机制无损加速大语言模型（LLM）推理，但单一草稿器在动态多任务场景下泛化能力受限。现有静态路由或独立草稿器方案无法实时适应输入分布变化，导致接受率波动。METASD 将草稿器选择建模为多臂老虎机（Multi-Armed Bandit, MAB）问题，利用块散度（Block Divergence, BD）奖励实现在线动态路由。该框架在混合任务负载下显著优于静态基线，但其理论假设的平稳性在极端非平稳场景下的鲁棒性尚存疑。

】

---

【RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding ｜检索增强上下文快速投机解码

研究机构：武汉大学、上海交通大学

作者：Zihong Zhang、Zuchao Li、Lefei Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14885)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14885)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但无训练方法面临检索信号稀疏与Logits信号局部性互补失效的困境。RACER通过构建Logits Tree与Retrieval Tree双树结构，将精确模式匹配作为结构锚点，将历史Logits复用作为动态外推线索，实现了无需额外模型训练的无损加速。该方法在多个基准上稳定超越纯检索与纯Logits基线，但其加速比仍低于训练式方法，且对长上下文下的内存管理缺乏深入验证。

】

---

【SpecBound: Adaptive Bounded Self-Speculation with Layer-wise Confidence Calibration ｜自草稿投机解码中的浅层置信度校准与有界推测

研究机构：中国科学院、中国科学院大学

作者：Zhuofan Wen、Yang Feng

论文原文见 [arXiv](https://arxiv.org/abs/2604.12247)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12247)

> 自草稿投机解码试图利用基座模型自身的浅层输出替代独立草稿模型，以消除额外训练与部署开销，但浅层缺乏直接监督信号导致虚假高置信预测，且困难 token 迫使整个草稿序列进行冗余深层计算，限制了加速潜力。SpecBound 通过层依赖温度退火抑制浅层虚假置信，并引入深度与宽度双边界机制，在触发验证时并行补全所有草稿 token 的剩余层计算，实现了无损加速。该方法在多个长文本生成任务上取得了最高 2.33 倍的墙钟时间加速，但其加速比上限仍显著低于特征对齐路线，且对基座模型架构的依赖尚未被充分解耦。

】

---

【Speculative Decoding with a Speculative Vocabulary ｜词表推测（SpecVocab）：动态子集选择缓解草稿模型输出分布计算瓶颈

作者：Miles Williams、Young D. Kwon、Rui Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4eed40cc58bb)

> 导读 投机解码（Speculative Decoding, SD）通过草稿模型并行预测与目标模型单次验证实现无损加速，但大词表投影导致草稿阶段延迟高企，成为加速比的主要限制因素。现有静态词表裁剪方法（如 FR-Spec、VocabTrim）虽降低计算量，却因上下文无关性导致目标 token 落在子集外时接受率骤降，抵消加速收益。本文提出 SpecVocab，通过上下文感知的动态词表子集预测，在保持无损性的同时提升接受长度与吞吐量。该方法在 EAGLE-3 框架内实现最高 8.1% 的吞吐量提升，但其绝对加速比仍低于领域内特征对齐路线的 SOTA，且未验证长上下文与多模态场景下的泛化能力。

】

---

【Speculative Verification: Exploiting Information Gain for Speculative Decoding ｜投机验证：利用信息增益优化推测解码

研究机构：韩国汉阳大学、韩国首尔大学

作者：Sungkyun Kim、Jaemin Kim、Dogyeong Yun 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0290d2647add)

> 投机解码（Speculative Decoding, SD）旨在通过草稿模型并行生成与目标模型验证来降低大语言模型（LLM）推理延迟，但草稿-目标分布对齐的不稳定性导致验证开销在大批量场景下激增，甚至使SD性能劣于直接解码。现有基于草稿模型内部信号（如熵或历史接受率）的预测方法在复杂上下文下失效，本文提出投机验证（Speculative Verification, SV），引入与草稿模型同规模的伴随模型，通过量化两者分布相似性来预测接受概率并动态调整验证长度。SV在保持无损性的前提下，将大批量下的吞吐量提升最高1.9倍，但其效果依赖于伴随模型与草稿模型的非独立性假设，在极端异构模型组合下的鲁棒性仍有待进一步验证。

】

---

【SPIDE: Serial and Parallel Intertwined Speculative Decoding ｜串行与并行交织的投机解码

作者：Wenru Xu、Peixuan Xu、Ziqi Yang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_27684e6714fe)

> 投机解码（Speculative Decoding, SD）旨在通过草稿模型并行生成候选词元，再由目标模型一次性验证，以突破自回归解码的内存带宽瓶颈。然而，现有并行SD框架（如PEARL）强制目标模型持续参与验证，导致高昂的调用成本，且固定草稿长度常引发无效词元生成的浪费。SPIDE提出一种免训练的动态调度框架，通过置信度-接受率映射表实时评估草稿序列可靠性，在串行草稿与并行验证间灵活切换。该方法在保持无损性的前提下，将LLM额外调用成本降低83.7%，但其在长序列高不确定性场景下的接受率上限仍受限于线性验证结构。

】

---

【Training-Free Adaptive Speculative Decoding via Linguistic Priors ｜语言学先验驱动的无训练投机解码

作者：Jingyi Wang、Jiaqi Huang、Zunnan Xu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_da296e374f35)

> 投机解码旨在通过并行验证打破自回归解码的串行瓶颈，但现有方法普遍采用统一的验证标准，忽视了自然语言中不同词性Token在熵分布上的固有差异。LinguaSpec指出这种“一刀切”策略导致高熵内容词被误拒或低熵功能词验证冗余，提出利用静态语言学先验实现自适应草稿与验证。该方法通过零延迟的词性探针、句法归一化惊讶度及POS自适应延迟验证，在无训练约束下实现了比训练式基线更高的加速比。其价值在于证明了语言学结构对推理效率的增益，但松弛验证机制对严格无损性的潜在妥协仍需审慎评估。

】
