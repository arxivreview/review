# ACL2026 · GRPO变体与策略优化增强方向论文汇编

> 本方向共 9 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AG-GRPO: Answer-Guided GRPO for Masked Diffusion Language Models ｜答案引导的组相对策略优化

作者：Juhyeong Kim、Gyunyeop Kim、Sangwoo Kang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_262b2331881f)

> 掩码扩散语言模型（dLLM）在强化学习后训练中面临稀疏奖励导致的推理不一致问题，传统自回归模型无法在采样阶段利用答案信息。AG-GRPO 利用 dLLM 的非自回归特性，将答案作为生成条件而非仅验证目标，通过混合无答案（AF）与答案引导（AG）轨迹计算共享优势，实现了训练信号向测试时策略的有效迁移。该方法在数学与代码任务上显著优于基线，但其对 dLLM 架构的依赖及条件化强度对泛化的影响尚存疑。

】

---

【Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization ｜组回合策略优化

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、亚马逊网络服务人工智能

作者：Yifeng Ding、Hung Le、Songyang Han 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.14846)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14846)

> 多轮工具集成推理（Tool-Integrated Reasoning, TIR）中，模型需跨多个回合迭代调用代码工具并依据执行结果修正推理，这一动态过程使得传统序列级奖励无法准确归因各回合的贡献。现有强化学习算法如组相对策略优化（Group Relative Policy Optimization, GRPO）将最终结果奖励均匀分配至所有Token，导致多轮交互中关键决策点信号被稀释，训练陷入停滞。GTPO通过引入回合级奖励分配、折扣回报优势估计及基于代码相似度的自监督奖励塑形，重构了TIR场景下的信用分配机制。该方法在数学推理基准上较GRPO提升3.0%，但在通用推理性能上仍低于前沿步骤级方法，其自监督奖励的泛化边界尚存疑。

】

---

【MDP-GRPO: Stabilized Group Relative Policy Optimization for Multi-Constraint Instruction Following ｜多约束指令遵循下的组相对策略优化稳定性

研究机构：伊朗德黑兰大学

作者：Mohammad Mahdi Salmani-Zarchi、Zahra Rahimi、Heshaam Faili 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.06058)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.06058)

> 组相对策略优化（GRPO）在离散、低方差奖励下因组内同质性导致优势估计失效，表现为低方差放大、均值中心化盲点及零方差坍缩。现有方法多针对数学推理中的稀疏奖励，却忽视了指令遵循任务中确定性检查器引发的极端低方差场景。本文通过多温度采样、双锚点优势及前景理论整形重构优势估计，在保持计算效率的同时恢复学习信号。该方法在Llama-3.2-3B上将严格约束满足率提升5.0%，但其对通用推理能力的潜在影响及小样本组下的泛化边界尚存疑。

】

---

【On the Hidden Objective Biases of Group-based Reinforcement Learning ｜组相对策略优化的隐藏目标偏差

作者：Aleksandar Fontana、Marco Simoni、Giulio Rossolini 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05002)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05002)

> 导读 组相对策略优化（Group Relative Policy Optimization, GRPO）通过消除价值网络依赖降低了大语言模型后训练成本，但其代理目标与真实训练目标之间存在结构性错位。现有改进工作多聚焦于性能提升或工程稳定，缺乏对优化动力学内在偏差的统一理论解释。本文构建统一形式化框架，将十种主流GRPO变体视为特例，揭示非均匀权重导致的共享前缀梯度偏差、AdamW优化器对奖励缩放的不变性以及动量机制引发的信任域越界现象。该分析为理解GRPO类方法的优化不透明性提供了理论参照，但其结论主要基于理想化假设，实际训练中的噪声干扰与复杂交互尚未被完全覆盖。

】

---

【Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning ｜结果锚定优势重塑

研究机构：复旦大学、中国科学院

作者：Ziheng Li、Liu Kang、Feng Xiao 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07408)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07408)

> 组相对策略优化（GRPO）通过消除价值网络依赖降低了大语言模型（LLM）后训练成本，但其序列级奖励均匀分配机制导致信用分配粗糙，无法区分推理链中的关键决策点与冗余步骤。现有基于熵或置信度的代理信号仅反映模型不确定性，而非对最终答案的实际因果影响，导致梯度方差增大与熵坍缩加速。本文提出结果锚定优势重塑（Outcome-grounded Advantage Reshaping, OAR），通过反事实扰动或梯度近似量化Token对最终答案分布的影响，并采用双层门控机制在保持总优势质量不变的前提下重新分配Token级优势。该方法在数学推理基准上稳定超越GRPO基线，但其归因信号与真实因果贡献的对齐度及计算开销的平衡仍是核心争议。

】

---

【SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks ｜序列级近端策略优化

研究机构：南方科技大学、北京邮电大学

作者：Tianyi Wang、Yixia Li、Long Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08865)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08865)

> 长链思维推理中的强化学习面临信用分配偏差与计算吞吐量的双重瓶颈。标准 PPO 的 Token 级价值估计在稀疏奖励下产生高偏差，而 GRPO 虽消除 Critic 却依赖多采样导致训练效率低下。本文提出 SPPO，将推理重构为序列级上下文赌博机，利用轻量级标量 Critic 实现单样本高效更新。该方案在同等算力下显著优于 GRPO，但牺牲了细粒度步骤监督，其性能上限是否受限于序列级信号的粗糙性仍存疑。

】

---

【Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting ｜协方差感知组相对策略优化

研究机构：新加坡国立大学、美国加州大学戴维斯分校

作者：Cheng Wang、Qin Liu、Wenxuan Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11538)

> 组相对策略优化（GRPO）在消除价值网络依赖后，面临训练过程中策略熵剧烈波动导致的探索-利用失衡问题。现有方法多通过调整裁剪比率或引入额外正则项来稳定训练，但未能从梯度更新的微观机制上解释熵不稳定的根源。本文指出极端协方差Token主导了策略更新，提出基于高斯核的协方差加权机制以自动抑制这些异常值。该方法在1.5B和7B模型上提升了数学推理性能，但其效果是否源于对特定小模型分布的过拟合，尚需更大规模验证。

】

---

【Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via sequence-level likelihood ｜序列级似然与选择性KL掩码的Token级策略优化

研究机构：吉林大学、清华大学

作者：Xingyu Lin、Yilin Wen、Du Su 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0329f43ccd14)

> 组相对策略优化（Group Relative Policy Optimization, GRPO）在消除价值网络依赖后，面临思维链（Chain-of-Thought, CoT）推理中Token级奖励稀疏导致的梯度方差大与熵坍缩问题。现有方法依赖无差别的熵正则化或KL散度约束，在稀疏奖励下往往引发策略退化或模型崩溃，无法有效平衡探索与稳定性。TEPO通过引入序列级几何平均似然替代Token级重要性采样，并施加基于优势与熵变的双条件KL掩码，重构了信用分配与正则化机制。该方法在数学推理基准上实现了比基线快50%的收敛速度及约2%的精度提升，但其对非数学任务及长序列泛化性的验证仍显不足。

】

---

【Too Correct to Learn: Reinforcement Learning on Saturated Reasoning Data ｜饱和数据下的探索干预：混合约束均匀Top-K采样

研究机构：腾讯AI实验室、美国圣母大学

作者：Zhenwen Liang、Yujun Zhou、Sidi Lu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18493)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18493)

> 组相对策略优化（GRPO）在强基座模型面对已饱和的推理数据集时，因组内奖励方差坍缩导致优势信号消失，引发模式坍缩。现有熵正则化或课程学习方法无法在“全对”场景下恢复学习信号，本文切入点在于解码阶段的概率分布重塑。通过引入约束均匀Top-K采样（CUTS）算子并构建双流Rollout框架，强制在保持结构连贯性的前提下注入探索多样性。该方法在Qwen3-4B上将AIME25 Pass@1提升15.1%，但缺乏对解码干预与策略收敛性交互的理论保证。

】
