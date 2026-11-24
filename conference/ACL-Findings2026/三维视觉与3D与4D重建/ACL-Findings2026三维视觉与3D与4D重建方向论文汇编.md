# ACL-Findings2026 · 三维视觉与3D与4D重建方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Answering Cross-Dimensional Geometric Visual Questions by Multi-constraint Spatial Reasoning ｜跨维度空间推理问答

作者：Dongling Li、Qi Chen、Jianxing Yu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45d4029840bf)

> 现有视觉语言模型在处理2D平面与3D立体结构映射时，往往依赖浅层视觉特征匹配，导致在拓扑关系重构与纹理方向对齐上出现系统性错误。本文提出SpatialQA任务，指出仅靠端到端学习难以捕捉跨维度变换中的不变量，转而利用拓扑同构检索与强化学习生成的验证问题，构建宏观轮廓到微观纹理的分层过滤机制。该方法通过显式约束检查替代隐式特征对齐，在自建数据集上显著优于通用大模型，但其性能高度依赖闭源推理骨干，且未验证在动态场景下的泛化能力。

】

---

【CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation ｜条件感知离散扩散语言模型用于目标导向分子生成

研究机构：香港科技大学

作者：Yanting Li、Zhuoyang Jiang、Enyan Dai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11483)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11483)

> 目标导向分子生成需在满足蛋白结合亲和力与多重药物属性（如ADMET）的同时保持化学有效性，现有方法往往在结构精度与优化灵活性间妥协。自回归模型因左到右生成机制缺乏全局视野，难以应对非可微奖励信号；纯3D生成模型则计算昂贵且忽略非几何属性。CAGenMol将分子生成建模为条件离散扩散问题，通过统一约束适配器（UCA）融合异构生物信号，并引入步级近端策略优化（Step-PPO）实现精细信用分配。该框架在CrossDocked2020基准上取得了69.7%的成功率，但其依赖1D序列表示，未直接验证3D几何约束下的性能上限。

】

---

【Can LLMs See Without Pixels? Benchmarking Spatial Intelligence from Textual Descriptions ｜文本空间智能基准

研究机构：北京理工大学

作者：Zhongbin Guo、Zhen Yang、Yushan Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03590)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03590)

> 视觉-语言模型（Vision-Language Models, VLMs）在空间推理上的高分往往掩盖了语言骨干（LLM）独立符号推理能力的缺失，现有视觉基准无法区分模型是依赖视觉模式匹配还是具备内在几何逻辑。本文切入点在于剥离像素输入，构建纯文本空间推理基准以诊断 LLM 的空间认知上限。通过构建包含 3,892 个样本的 SiT-Bench 并评估 SOTA 模型，揭示了“空间鸿沟”及思维链（Chain-of-Thought, CoT）的增益机制。该工作提供了关键的诊断工具，但其纯文本设定是否完全排除了视觉预训练的残留影响，仍存疑。

】

---

【CoV: Chain-of-View Prompting for Spatial Reasoning ｜视角链提示

研究机构：浙江大学、澳大利亚莫纳什大学

作者：Haoyu Zhao、Akide Liu、Zeyu Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05172)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05172)

> 具身问答（EQA）要求智能体在3D场景中回答空间问题，但现有视觉语言模型（VLM）受限于固定且有限的输入视角，无法在推理时获取足够的问题相关上下文，导致复杂空间推理失败。本文提出Chain-of-View（CoV）提示框架，通过粗粒度视图选择与细粒度视角调整的主动探索机制，将VLM从被动观察者转变为主动探索者。该框架无需额外训练，在OpenEQA基准上平均提升11.56%。其价值在于验证了测试时缩放策略的有效性，但离散动作空间对复杂轨迹探索能力的限制尚未充分探讨。

】

---

【Infinite Babble: Inflating 3D Vision-Language Model Inference Overhead via Adversarial Geometric Perturbation ｜3D视觉语言模型资源耗尽攻击

作者：Shuoyang Sun、Jiaxin Hong、Yv Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7ba55849250a)

> 3D视觉语言模型（3D-VLM）依赖自回归解码处理点云输入，其计算开销随输出长度线性增长，但现有安全研究仅聚焦于2D图像或纯文本模态，忽视了3D几何输入特有的攻击面。本文指出，由于3D数据获取成本高，用户常依赖互联网下载的未信任点云资产，这为对抗扰动提供了隐蔽入口。Inflate3D通过语义感知扰动与轨迹干扰机制，在不破坏几何结构的前提下诱导模型生成冗长输出。该工作揭示了3D-VLM在推理效率上的脆弱性，但其攻击效果高度依赖特定骨干架构，对多视图渲染类模型的泛化能力存疑。

】

---

【PseudoGD: Enhancing Spatial Reasoning in Vision-Language Models through Pseudo Geometric Knowledge Distillation ｜伪几何知识蒸馏

作者：Gwanghee Lee、Yeeun Choi、Kyoungson Jhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2983755d5737)

> 视觉语言模型（Vision-Language Model, VLM）在3D空间推理中面临的核心困境是视觉编码器缺乏度量尺度与结构先验，导致定量距离估计与视角转换任务表现不佳。现有方案或依赖昂贵的3D点云数据，或仅通过合成数据微调无法改变编码器内部的2D语义偏置。本文切入点在于利用单目2D图像，通过深度与分割教师模型生成伪标签，将几何信息蒸馏进视觉编码器。该方法在OmniSpatial基准上提升了多种架构的空间推理能力，但其对教师模型误差的依赖及静态图像限制使其在复杂动态场景中的泛化性存疑。

】

---

【SceneLM: 3D-Aware Language Models for Editable 3D Scene Synthesis ｜单图可编辑3D场景合成

研究机构：香港科技大学、复旦大学

作者：Xingbo Yao、Xiaoyu Chen、Doudou Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3594e92dc4c4)

> 单图3D场景合成旨在从一张RGB图像恢复可交互的三维环境，以支撑内容创作与具身智能数据生成。现有几何重建方法虽能生成高保真场景，但缺乏编辑能力；而基于大语言模型（LLM）的程序化合成虽支持交互，却受限于文本输入的歧义性及视觉语言模型（VLM）在度量3D定位上的精度不足。本文提出SceneLM，通过图像接地的度量布局预测与工具链执行，实现从单图到可编辑3D场景的转换。该方法在2B参数规模下显著提升了布局估计精度，但依赖相机内参且未解决长程一致性，其通用性仍存疑。

】
