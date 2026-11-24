# ACL-Findings2026 · 多模态大语言模型中的视觉定位方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MGPO: Thinking with Images via Multi-Turn Grounding-Based Reinforcement Learning ｜多轮定位强化学习

研究机构：复旦大学、新加坡南洋理工大学

作者：Xinyu Huang、Yuhao Dong、Weiwei Tian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2ee7517732f7)

> 高分辨率图像输入导致视觉令牌数量呈二次方增长，大量无关区域干扰模型对关键细节的捕捉，且受限于上下文长度，模型往往无法直接处理原始分辨率图像。现有方法多依赖昂贵的定位标注或中间奖励信号来引导模型关注特定区域，数据获取成本高且泛化性受限。本文提出多轮定位策略优化（Multi-turn Grounding-based Policy Optimization, MGPO），仅利用最终答案的二元奖励，通过多轮对话中的自动裁剪机制激发模型的定位能力。该方法在无需额外定位标注的情况下，显著提升了高分辨率视觉问答性能，但其定位精度是否足以替代像素级分割在精细交互中的角色，仍存疑。

】

---

【PlaM: Training-Free Plateau-Guided Model Merging for Better Visual Grounding in MLLMs ｜基于层级视觉Token掩码的免训练模型合并

研究机构：美国东北大学、德国慕尼黑大学

作者：Zijing Wang、YongKang Liu、Mingyang Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70720bb65af4)

> 多模态大语言模型（MLLMs）在指令微调后常出现文本推理能力退化，导致视觉定位依赖语言先验而非图像证据。现有修复方案多依赖额外训练或架构修改，缺乏零成本干预手段。本文通过层级视觉Token掩码定位性能平台期，并在该区间线性插值基座语言模型权重，以恢复晚期层的语义决策结构。该方法在通用多模态基准上带来一致提升，但其在专用定位任务上的有效性及与强化学习路线的相对优势尚未得到验证。

】

---

【Unveiling Inherent Visual Grounding in Multimodal LLMs for Text-Rich Images ｜文档视觉文本定位的注意力内化

研究机构：美国纽约州立大学布法罗分校、Adobe研究院

作者：Shijie Zhou、Jihyung Kil、Ming Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9fa29afda614)

> 文档问答中的视觉证据定位长期依赖外部OCR工具提供候选框，导致模型在稀疏文本或复杂图表场景下失效，且推理效率低下。Doc-AGround 摒弃了坐标生成与OCR依赖，直接利用多模态大语言模型（MLLMs）内部的多头自注意力（MHSA）作为定位信号。通过引入专用聚合token与基于全局相关性模式的注意力头加权机制，该方法在OCR-free设定下实现了SOTA性能。其价值在于证明了MLLM内部注意力已具备足够的细粒度定位潜力，但该方法对骨干模型预训练质量的依赖及在极端遮挡场景下的鲁棒性仍存疑。

】
