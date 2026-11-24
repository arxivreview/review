# ACL2026 · AI生成视频评估与编辑方向论文汇编

> 本方向共 4 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond the Last Frame: Process-aware Evaluation for Generative Video Reasoning ｜过程感知评估：超越末帧的视频推理基准

研究机构：中国人民大学

作者：Yifan Li、Yukai Gu、Yingqian Min 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.24952)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.24952)

> 视频生成模型正从像素逼真转向逻辑推理，但现有评估仅看末帧，导致“过程错误、结果正确”的样本被误判为成功。本文指出这一“结果黑客”现象，提出VIPER基准与POC@r指标，强制要求中间帧与末帧同时满足约束。该工作揭示了当前SOTA模型在过程一致性上的巨大缺口，但其绝对分数极低，是否因任务过难而非模型缺陷，仍存疑。

】

---

【From Detection to Understanding: Multi-Turn Reasoning for Video Misinformation Analysis ｜从检测到理解：视频虚假信息的多轮推理分析

作者：Zhi Zeng、Jiaying Wu、Minnan Luo 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c06149742475)

> 视频虚假信息分析长期被简化为真伪二分类，忽视了模型解释“如何误导”与“为何误导”的推理能力。现有基准缺乏对操纵机制的细粒度归因，导致模型输出脆弱且缺乏证据接地的解释。本文通过构建覆盖12类操纵策略的多轮推理基准MISVIDEOQA，并提出基于德尔菲（Delphi）共识机制的多智能体框架MISAGENT，实现了从感知到意图的完整推理链。该工作填补了过程级评估的空白，但其对VLM自身偏见的依赖及外部检索的延迟成本，仍是制约其实际部署的关键瓶颈。

】

---

【MTAVG-Bench: A Diagnostic Benchmark for Multi-Talker Dialogue-Centric Audio-Video Generation ｜多说话人对话音视频生成诊断基准

作者：Yanghao Zhou、Haitian Li、Rexar Lin 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ae6ec8dba470)

> 多说话人对话视频生成面临身份漂移与轮替逻辑断裂等结构性缺陷，现有基准仅关注单模态保真度或单说话人属性，无法捕捉跨说话人的交互一致性。本文切入点在于构建一个失败驱动的诊断框架，将评估从标量打分转向细粒度错误定位。通过半自动管线生成包含37种失败模式的问答对，并采用四级九维分层协议评估全模态模型。该基准揭示了当前模型在高层语义推理上的显著短板，但其依赖人工标注失败模式的构建方式限制了自动化扩展能力。

】

---

【OSCBench: Benchmarking Object State Change in Text-to-Video Generation ｜对象状态变化基准

研究机构：新加坡国立大学、新加坡管理大学

作者：Xianjing Han、Bin Zhu、Shiqi Hu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.11698)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11698)

> 文本到视频生成模型在视觉保真度上已接近人类感知，但无法忠实执行语言指令中隐含的物体状态转变。现有基准侧重整体物理合理性或语义对齐，忽略了动作引发的具体状态结果这一细粒度维度。OSCBench 通过构建常规、新颖与组合三类烹饪场景，利用结构化思维链引导多模态大模型进行帧级证据提取，系统评估了六个前沿模型在对象状态变化上的表现。该基准揭示了当前模型在状态一致性上的显著短板，但受限于单一领域场景，其结论向通用物理交互的泛化能力尚存疑问。

】
