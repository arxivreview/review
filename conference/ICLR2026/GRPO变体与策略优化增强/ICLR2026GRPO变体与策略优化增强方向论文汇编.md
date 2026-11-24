# ICLR2026 · GRPO变体与策略优化增强方向论文汇编

> 本方向共 21 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【_wd1_ : WEIGHTED POLICY OPTIMIZATION FOR REASONING IN DIFFUSION LANGUAGE MODELS ｜加权对数似然策略优化

研究机构：英国伦敦大学学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_89974783)

> 扩散语言模型（dLLM）的强化学习后训练面临似然函数不可解的困境，导致传统组相对策略优化（GRPO）在计算策略比率时产生指数级误差放大与高方差。现有方法依赖多次近似似然来构建比率，不仅计算冗余且训练不稳定。本文提出 wd1，通过推导反向KL约束下的闭式解，将优化目标重构为仅依赖单次似然近似的加权对数似然，彻底消除策略比率。该方法在 LLaDA-8B 上无需监督微调即超越基线，但其在高难度数学任务上的表现仍显著落后于自回归模型的最先进结果，且步骤级扩展的泛化能力有待验证。

】

---

【Attention as a Compass: Efficient Exploration for Process-Supervised RL in Reasoning Models ｜注意力引导的过程监督强化学习

研究机构：清华大学、快手

作者：Runze Liu、Jiakang Wang、Yuling Shi 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26628)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26628)

> 过程监督强化学习（PSRL）旨在通过蒙特卡洛采样估计步骤级优势，以解决组相对策略优化（GRPO）中序列级奖励导致的信用分配粗糙问题。现有PSRL方法依赖固定长度或熵阈值进行响应分割，忽略了模型输出的语义结构，且采用均匀采样导致计算资源浪费在低价值样本上。AttnRL利用前向上下文影响（FCI）分数定位高注意力步骤作为分支点，并结合难度感知自适应采样与单步离策略训练流水线，在保持步骤级优势估计精度的同时显著提升了探索效率与训练吞吐量。该方法在数学推理基准上超越了GRPO与TreeRL基线，但其性能增益主要源于采样效率优化而非优势估计机制的根本性突破，且未验证其在非数学任务或不同骨干架构下的泛化能力。

】

---

【BALANCING THE EXPERTS: UNLOCKING LORA-MOE FOR GRPO VIA MECHANISM-AWARE REWARDS ｜路由优化组相对策略优化

研究机构：南京大学、上海交通大学

作者：Changlian Ma、Zizheng Huang、Xiangyu Zeng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_72106494)

> 导读 参数高效混合专家（PEFT-MoE）架构在强化学习微调中面临路由机制退化与专家利用率低下的核心矛盾，传统监督学习中的辅助负载均衡损失无法直接迁移至无监督的强化学习框架。现有方法要么依赖外部任务奖励而忽视内部路由状态，要么强行引入辅助损失导致优化目标冲突。本文提出RO-GRPO，将生成过程中的路由熵与负载分布统计转化为机制感知奖励信号，直接嵌入组相对策略优化（GRPO）目标函数。该框架实现了任务性能与内部机制对齐的统一优化，但在高难度多模态推理任务上的增益幅度有限，且未验证其对策略探索空间的影响。

】

---

【BOOSTING MULTI-DOMAIN REASONING OF LLMS VIA CURVATURE-GUIDED POLICY OPTIMIZATION ｜曲率引导策略优化

研究机构：中国科学技术大学、华为

作者：Xize Liang、Lin Yang、Jie Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75803991)

> 多域强化学习旨在让大语言模型同时提升数学、代码及写作等多种能力，但不同领域的奖励信号往往相互冲突，导致单一能力的提升以牺牲另一能力为代价。现有梯度平衡方法要么忽略损失面的几何结构，要么因需同时存储所有域梯度而面临内存瓶颈。本文提出CGPO，通过随机顺序逐域更新并引入插值机制，利用一阶泰勒展开近似诱导跨域曲率-梯度交互，从而在不显式计算Hessian矩阵的前提下缓解冲突。该方法在四个领域七个基准上验证了有效性，但其对超参数$\alpha$的敏感性及在极端难度任务上的泛化边界仍需进一步审视。

】

---

【CurES: From Gradient Analysis to Efficient Curriculum Learning for Reasoning LLMs ｜基于梯度方差最小化的动态课程学习

研究机构：中国科学院、中国科学院大学

作者：Yongcheng Zeng、Zexu Sun、Bokai Ji 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01037)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01037)

> 强化学习后训练中，计算资源在异质难度样本上的低效分配是制约收敛速度的核心瓶颈。现有静态课程或简单过滤方法无法动态对齐模型能力与样本难度，导致梯度信号稀疏或噪声过大。CurES 从策略梯度方差最小化视角出发，联合优化提示词采样概率与 Rollout 数量分配，通过贝叶斯后验估计实现轻量级动态难度追踪。该方法在效率上显著优于基线，但在高难度推理任务上的精度提升有限，其理论边界尚待验证。

】

---

【DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage ｜难度自适应变体优势优化

研究机构：中科院计算所、中国科学院大学

作者：Haowen Gao、Zhenyu Zhang、Liang Pang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01106)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01106)

> 多模态大语言模型（MLLM）在强化学习后训练中面临组内奖励一致性过高导致的优势消失问题，现有静态变体扩展或样本筛选方法无法动态维持组内方差。本文切入点在于将题目难度视为随模型能力演化的动态变量，通过难度自适应变体生成与局部-全局双重优势估计重构优化信号。该方法在7B规模下实现SOTA性能并加速训练，但其依赖闭源模型生成推理变体且未验证跨模态泛化性。

】

---

【FastGRPO: Accelerating Policy Optimization via Concurrency-aware Speculative Decoding and Online Draft Learning ｜并发感知推测解码加速组相对策略优化

研究机构：兰州大学、新加坡国立大学

作者：Yizhou Zhang、Ning Lv、Teng Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21792)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21792)

> GRPO训练的主要瓶颈在于自回归生成阶段占据91%至98%的总耗时，而传统推测解码在高并发场景下因计算开销激增导致加速失效。本文切入点在于识别GRPO生成阶段并发度从高位向低位动态演变的特性，并针对目标模型参数更新导致的草稿模型分布漂移问题。通过动态调整草稿树大小与验证Token数，结合在线草稿学习机制，实现了端到端2.35x至2.72x的加速。该方案在系统层面有效缓解了训练吞吐瓶颈，但未验证加速对模型最终推理精度的潜在影响。

】

---

【FlowRL: Matching Reward Distributions for LLM Reasoning ｜奖励分布匹配策略优化

研究机构：上海交通大学、微软研究院

作者：Xuekai Zhu、Daixuan Cheng、Dinghuai Zhang 等 23 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15207)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15207)

> 现有强化学习后训练范式聚焦于最大化期望奖励，导致策略收敛至单一主导解法模式，抑制了推理路径的多样性与泛化能力。本文指出，这种模式坍缩源于对奖励分布中低频有效模式的忽略，而非单纯的探索不足。FlowRL 通过引入可学习配分函数将标量奖励转化为目标分布，并最小化策略与该分布间的反向 KL 散度，实现了从“奖励最大化”到“奖励分布匹配”的范式转移。该方法在数学与代码推理任务上显著优于 PPO 和 GRPO，但其绝对性能低于当前领域 SOTA，且未验证细粒度信用分配下的有效性。

】

---

【GEOMETRIC-MEAN POLICY OPTIMIZATION ｜几何均值策略优化

研究机构：香港中文大学、微软研究院

作者：Yuzhong Zhao、Yue Liu、Junpeng Liu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_78773882)

> 导读 GRPO 在强化学习后训练中面临的核心矛盾是：算术平均聚合 Token 级奖励时对离群值敏感，导致重要性采样比率方差爆炸，进而引发策略更新不稳定与探索受限。现有方案如 DAPO 通过扩大裁剪范围缓解探索不足，但未能从根源上抑制比率方差，导致稳定性与探索性难以兼得。本文切入点在于将奖励聚合算子从算术平均替换为几何平均，利用其对离群值的天然鲁棒性，在维持稳定性的同时允许更宽的裁剪范围。该设计以极小的代码改动实现了训练动态的显著改善，但其性能上限是否受限于未解决的信用分配粗糙问题，仍需进一步验证。

】

---

【Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation ｜难度感知组相对策略优化与多侧面问题重构

研究机构：中国人民大学、阿里巴巴集团

作者：Yanqi Dai、Yuxiang Ji、Xiao Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20614)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20614)

> 导读 组相对策略优化（Group Relative Policy Optimization, GRPO）在数学推理后训练中面临一个被忽视的结构性缺陷：其优势估计机制对中等难度问题的更新幅度最大，而对高难度可解问题的更新幅度被系统性抑制。现有改进方法多聚焦于Token级信用分配或动态采样，却未触及这一源于归一化方式的底层偏差。本文通过平均绝对偏差归一化与难度感知加权修正算法偏差，并配合多侧面问题重构扩展数据难度边界，在相同骨干下将平均性能提升4.56%。该框架验证了“难题优先”原则的有效性，但其难度加权是否加剧策略熵坍缩，论文未提供直接证据。

】

---

【Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards ｜前瞻树状Rollout

研究机构：南京大学、美国南加州大学

作者：Shangyu Xing、Siyuan Wang、Chenyuan Yang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97145319)

> 强化学习可验证奖励（RLVR）范式下，组相对策略优化（GRPO）依赖组内轨迹差异计算优势函数，但Token级随机采样导致组内轨迹高度同质，使得相对优势信号坍缩，策略更新失效。现有提升多样性的方法要么仅增加Token级噪声，要么事后过滤低质组，均无法在有限生成预算内保证轨迹级发散。LATR通过在高不确定性位置强制分支、前瞻模拟并剪枝相似路径，显式构建轨迹级多样性。该方法在保持计算复杂度$O(nk)$的前提下加速了策略收敛，但其依赖编辑距离的剪枝标准在语义复杂任务中的鲁棒性存疑。

】

---

【Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards ｜随机策略估值驱动的大语言模型推理优化

研究机构：香港科技大学、快手

作者：Haoran He、Yuxiao Ye、Qingpeng Cai 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24981)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24981)

> 大语言模型强化学习后训练长期受困于广义策略迭代（GPI）循环导致的训练不稳定与熵坍缩，现有方法依赖复杂的启发式技巧维持平衡。本文指出数学推理任务具有确定性树状马尔可夫决策过程（MDP）结构，证明仅评估固定均匀随机策略的Q值即可推导最优动作，从而绕过迭代评估-改进循环。ROVER算法通过Softmax采样随机策略Q值实现质量与多样性的平衡，在竞赛数学任务上显著优于传统基线，但其理论边界局限于特定MDP结构，对复杂动态环境的适用性存疑。

】

---

【RiskPO: Risk-based Policy Optimization via Verifiable Reward for LLM Post-Training ｜风险敏感策略优化

研究机构：北京大学

作者：Tao Ren、Jinyang Jiang、Hui Yang 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00911)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00911)

> 导读

】

---

【Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning ｜脚手架式组相对策略优化

研究机构：香港科技大学、香港中文大学

作者：Xichen Zhang、Sitong Wu、Yinghao Zhu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.19807)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.19807)

> 导读 强化学习可验证奖励（RLVR）范式下，模型面对超出当前能力的难题时，所有探索轨迹均获得零奖励，导致优势函数坍缩为零，梯度消失，形成“学习悬崖”。现有前缀引导方法虽能提供正奖励信号，但引入分布不匹配并限制探索自由度。Scaf-GRPO 借鉴教育学脚手架理论，通过注入层级化、最小化的提示（Hint）而非固定前缀，在保持策略一致性的前提下恢复学习信号。该方法在 Qwen2.5-Math-7B 上实现了 AIME24 相对提升 44.3%，但其依赖外部强模型生成提示，且仅针对可验证任务，泛化边界尚待明确。

】

---

【Single-stream Policy Optimization ｜单流策略优化

作者：Zhongwen Xu、Zihan Ding

论文原文见 [arXiv](https://arxiv.org/abs/2509.13232)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13232)

> 组相对策略优化（Group Relative Policy Optimization, GRPO）在消除价值网络依赖的同时，引入了退化组导致的计算浪费与分布式训练中的同步瓶颈。现有工程化补丁如动态采样虽能缓解信号缺失，却未解决架构层面的根本低效。本文提出单流策略优化（Single-stream Policy Optimization, SPO），通过持久化贝叶斯价值追踪器与全局优势归一化重构基线估计机制，回归经典单流范式。该设计在数学推理基准上优于GRPO，但其对非二元奖励的泛化能力及跨任务分布偏差的控制仍存疑。

】

---

【Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning ｜慢快策略优化

研究机构：美国佐治亚理工学院、美国伊利诺伊大学厄巴纳-香槟分校

作者：Ziyan Wang、Zheng Wang、Xingwei Qu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04072)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04072)

> 导读 GRPO 在训练初期因单次更新的高方差梯度导致优化方向不稳定，且单次迭代仅利用一次 Rollout 数据，样本效率低下。现有改进多聚焦于奖励信号重构或采样策略，忽视了更新机制本身的结构性缺陷。SFPO 通过“快速轨迹-重定位-慢速校正”三阶段结构，在不改变基础损失与 Rollout 流程的前提下，将噪声单次更新转化为结构化轨迹。该方案在数学推理基准上平均提升 2.80 分，但绝对精度未超越最新细粒度信用分配方法，其价值在于以极低工程成本换取稳定性与效率的平衡。

】

---

【SQUEEZE THE SOAKED SPONGE: EFFICIENT - OFF POLICY RFT FOR LARGE LANGUAGE MODEL ｜离策略强化微调：ReMix 机制与效率-精度权衡

研究机构：天津大学

作者：Jing Liang、Jinyi Liu、Yi Ma 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_24960764)

> 导读

】

---

【SSVPO: EFFECTIVE STEP-LEVEL CREDIT ASSIGN MENT FOR RL TRAINING OF LANGUAGE MODELS ｜顺序沙普利值策略优化

研究机构：澳大利亚悉尼大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_17841245)

> 组相对策略优化（GRPO）在消除价值网络依赖的同时，将序列级奖励均匀分配给所有Token，导致中间推理步骤缺乏差异化监督，引发链长膨胀与冗余生成。现有信用分配方法如VinePPO和SPO虽尝试分解奖励，但缺乏公平性理论保证，且在部分正确推理链中失效。本文提出顺序沙普利值策略优化（SSVPO），通过插入马尔可夫决策过程（Insertion MDP）重排推理步骤，计算各步骤的顺序边际贡献（SMC）并聚合为顺序沙普利值（SSV），作为无偏最小方差基线指导策略更新。该方法在7个数学基准上提升了准确率并减少了Token消耗，但其重排机制对语义连贯性的破坏程度及在大模型上的泛化能力尚存疑。

】

---

【Stabilizing Policy Gradients for Sample-Efficient Reinforcement Learning in LLM Reasoning ｜曲率感知策略优化

研究机构：英国牛津大学

作者：Luckeciano C. Melo、Alessandro Abate、Yarin Gal

论文原文见 [arXiv](https://arxiv.org/abs/2510.00819)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00819)

> 导读 组相对策略优化（GRPO）在激进更新参数下常遭遇策略坍缩，迫使研究者采用保守超参数以牺牲样本效率换取训练稳定性。现有基于裁剪或KL正则化的方法无法从优化几何层面预判并拦截导致分布剧烈偏移的特定样本。本文通过构建最后层二阶曲率计算模型，在策略更新前识别并掩码高风险Token，实现了激进更新下的稳定训练。该机制在数学推理任务上取得了30倍样本效率提升，但其对深层网络优化几何的表征保真度仍存疑。

】

---

【Trust-Region Adaptive Policy Optimization ｜信任域自适应策略优化

研究机构：清华大学

作者：Mingyu Su、Jian Guan、Yuxian Gu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17636)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17636)

> 当前大语言模型后训练主流范式采用“先监督微调（Supervised Fine-Tuning, SFT）后强化学习（Reinforcement Learning, RL）”的两阶段流程，但SFT导致的模式僵化与灾难性遗忘严重制约了RL阶段的探索上限。现有方案要么将SFT与RL割裂，要么简单叠加损失函数导致训练崩溃，缺乏在实例粒度上动态平衡外部监督与自主探索的机制。TRAPO通过引入信任域SFT（Trust-Region SFT, TrSFT）与微组采样机制，在单次训练实例中交错执行SFT与RL，实现了知识内化与探索能力的协同。该框架在数学推理基准上超越了传统两阶段基线，但其对专家前缀质量的依赖及在极高难度竞赛题上的性能瓶颈，限制了其作为通用后训练范式的普适性。

】

---

【Variational Reasoning for Language Models ｜变分推理语言模型

研究机构：新加坡国立大学

作者：Xiangxin Zhou、Zichen Liu、Haonan Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22637)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22637)

> 该方向旨在解决大语言模型后训练中，监督微调（SFT）泛化差与强化学习（RL）训练不稳定、输出多样性坍缩的矛盾。现有RL方法（如GRPO）隐含的“按准确率加权”机制导致模型系统性偏向简单题，忽视高难度推理路径。本文切入点是将思维链视为潜变量，构建基于证据下界（ELBO）的变分推理框架，通过前向KL目标稳定后验训练。该方法在Qwen系列模型上显著提升了数学与代码推理性能，但其对答案提示的依赖及多轮训练缺失限制了其通用性。

】
