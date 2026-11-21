# HuggingFace最新推荐论文 ｜MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion ｜多轮图像编辑的自回归扩散训练范式

作者：Houyuan Chen、Fanzhou Wang、Xiangyu Fan 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.25404)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.25404)

> 多轮图像编辑旨在通过连续指令序列逐步修改图像，但现有方法在数轮编辑后常出现视觉质量退化与内容漂移。传统单轮编辑模型无法显式建模完整交互历史，而基于自回归扩散的统一多模态模型（Unified Multimodal Models, UMMs）在推理时依赖自身生成的不完美历史，导致训练与推理条件不匹配（即曝光偏差）。本文提出MT Forcing训练范式，通过单轮分布匹配蒸馏（Single-Turn Distribution Matching Distillation, Single-Turn DMD）将学生自生成轨迹对齐至单轮教师分布，并引入教师强制引导（Teacher-Forcing Guidance）约束跨轮次内容一致性。该范式在自回归UMM骨干上显著抑制了多轮漂移，但其有效性高度依赖单轮教师对复杂组合指令的理解能力，且未验证在长程多轮编辑中的累积误差控制极限。

## 研究背景

当用户通过连续指令对图像进行多轮编辑时，模型需同时满足当前指令并保留前序编辑成果。这一任务天然具有因果性，与自回归扩散模型（Autoregressive Diffusion）的生成机制契合：后续编辑依赖前序交互历史。然而，自回归扩散模型在训练时通常条件于参考历史（Teacher Forcing），而在推理时递归条件于自身生成的历史（Self-Rollout）。这种训练-推理条件不匹配导致曝光偏差（Exposure Bias），使模型在数轮编辑后产生视觉伪影累积与背景意外修改。

领域内现有路线对此问题的处理存在局限。单轮编辑模型（如InstructPix2Pix）通过递归应用单轮编辑器实现多轮编辑，但未显式建模完整交互历史，难以保留早期约束。近期基于UMMs的方法（如FreqEdit、AnchorEdit）尝试通过高频特征保持或因果自滚动训练缓解退化，但前者侧重推理时后处理，后者侧重主体身份保持，均未从训练范式层面解决自回归扩散的曝光偏差。MT Forcing将分布匹配蒸馏（Distribution Matching Distillation, DMD）从视频生成迁移至多轮图像编辑，利用单轮编辑无累积误差的特性，为多轮学生模型提供高质量视觉参考，填补了训练阶段分布对齐的空白。

## 核心方法

### 方法参照系：自回归扩散的多轮编辑建模

多轮图像编辑可形式化为：给定源图像 $x_{src}$ 和 $N$ 条指令 $c_{1:N}$，模型 $G_\theta$ 在第 $i$ 轮根据当前指令 $c_i$ 和自生成历史 $H_{<i} = (x_{src}, c_1, x_1, \dots, c_{i-1}, x_{i-1})$ 生成 $x_i$。因果模型缓存前序指令与图像的键值（Key-Value, KV）向量供后续编辑使用。该流程的关键差异在于：传统单轮编辑仅条件于源图像与单条指令，而多轮编辑需处理自生成历史中的误差累积，训练时条件于参考历史 $H^*_{<i}$ 与推理时条件于自生成历史 $H_{<i}$ 的分布差异构成核心瓶颈。

### Single-Turn DMD：单轮教师监督下的分布匹配

Single-Turn DMD旨在消除自生成历史导致的视觉质量漂移。其设计动机源于两个观察：单轮编辑引入的退化有限，且编辑模型可在单轮内执行多动作。因此，将前 $i$ 轮指令重组为单轮“捆绑提示”（Bundled Prompt）$\bar{c}_i = \text{Reorganize}(c_{1:i})$，使冻结教师 $T_\phi$ 在单轮内直接对源图像执行累积编辑，提供无跨轮误差累积的质量参考。学生 $G_\theta$ 在训练中执行自滚动，条件于自身不完美历史。

在第 $i$ 轮，学生条件 $C^S_i = (H_{<i}, c_i)$ 与教师条件 $C^T_i = (x_{src}, \bar{c}_i)$ 存在映射关系 $C^S_i \Rightarrow C^T_i$，但 $C^T_i \nRightarrow C^S_i$，即学生接收更强条件，教师接收更弱条件。通过学生因果滚动诱导的边际分布 $p_{\theta,i}(\cdot | C^T_i)$ 建立连接。对两分布施加相同前向加噪过程 $x^t_i = \alpha_t x_i + \sigma_t \epsilon$，定义逐轮分布匹配损失：

$$
L^{(i)}_{\text{DMD}} = \mathbb{E}_t \left[ D_{\text{KL}} \left( p_{\theta,i,t}(\cdot | C^T_i) \parallel p_{\phi,i,t}(\cdot | C^T_i) \right) \right]
$$

该损失在相同源图像与捆绑提示下比较加噪图像分布，通过分数梯度估计更新学生，使其在推理时遇到的历史条件下维持视觉质量。为提升效率，梯度截断于当前轮去噪步，历史KV嵌入被分离。

### Teacher-Forcing Guidance：跨轮次内容一致性约束

Single-Turn DMD匹配边际分布，但未唯一确定学生对每个历史的响应。若学生忽略前序生成图像并独立采样，仍可满足零DMD损失，但导致跨轮内容不一致。Teacher-Forcing Guidance通过参考轨迹 $\tau \sim D_{\text{ref}}$ 监督历史依赖转换，补充边际匹配无法捕捉的依赖关系。

在参考历史 $H^*_{<i}$ 与当前指令 $c_i$ 下，通过流匹配（Flow Matching）监督目标 $x^*_i$：

$$
L_{\text{TF}} = \frac{1}{N} \sum_{i=1}^N \mathbb{E}_{\tau, t_i, \epsilon_i} \left[ \| v_\theta(x^{*,t_i}_i, t_i, H^*_{<i}, c_i) - v^{*,t_i}_i \|^2 \right]
$$

其中 $v_\theta$ 为学生速度预测，$v^{*,t_i}_i$ 为参考速度目标。该损失分两阶段应用：蒸馏前通过教师强制预热（Teacher-Forcing Warmup）建立历史依赖行为；蒸馏期间以权重 $\lambda_{\text{TF}}$ 作为正则化项保留，防止分布匹配更新破坏跨轮一致性。总目标为 $L_{\text{MT}} = L_{\text{DMD}} + \lambda_{\text{TF}} L_{\text{TF}}$。

## 实验评估

实验在MTEdit-Bench的step-wise子基准上进行，包含100个会话，每会话含源图像与8条顺序编辑指令。基线为SenseNova-U1与SenseNova-U1.5两个UMM骨干，对比有无MT Forcing的性能。评估指标包括指令遵循（Instruction Following, IF）、内容一致性（Content Consistency, CC）、漂移鲁棒性分数（Drift Robustness Score, DRS）及新增的几何对齐指标Pixel。基线覆盖缺失InstructPix2Pix、MagicBrush等主流单轮编辑模型在多轮场景下的直接对比，仅验证了同骨干下的增益。

| Method | Turn | IF↑ | CC↑ | DRS↑ | Pixel↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SenseNova-U1.5 | 8 | 4.52 | 3.22 | 3.03 | 6.89 |
| SenseNova-U1.5 + MT Forcing | 8 | 9.17 | 7.68 | 4.35 | 0.71 |

在第8轮，MT Forcing使SenseNova-U1.5的IF提升4.65，CC提升4.46，DRS从3.03提升至4.35，八轮平均Pixel从6.34降至0.74，几何位移减少88.4%。消融实验验证了组件互补性：

| Single-Turn DMD | Teacher-Forcing Guidance | IF↑ | CC↑ | DRS↑ | Pixel↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| × | × | 8.47 | 7.09 | 3.83 | 6.34 |
| ✓ | × | 9.02 | 7.64 | 4.12 | 2.51 |
| × | ✓ | 9.10 | 7.83 | 3.92 | 2.74 |
| ✓ | ✓ | 9.66 | 8.40 | 4.30 | 0.74 |

单独使用Single-Turn DMD改善视觉质量但跨轮内容不一致，单独使用Teacher-Forcing Guidance保留参考历史行为但未解决自生成历史下的曝光偏差，两者结合在四项指标上均达最优。正则化权重 $\lambda_{\text{TF}}$ 在0.25至0.1时平衡内容一致性与视觉清晰度，权重过大导致纹理模糊。评估协议局限在于Pixel指标仅衡量几何位移，未覆盖纹理细节的语义漂移；代码开源状态未明确，可复现性存疑。

## 关联研究分析

从问题动机看，MT Forcing与FreqEdit（Li et al., 2026）均针对多轮编辑退化，但FreqEdit通过小波变换在推理时注入高频信息缓解渐进退化，属于后处理策略；MT Forcing在训练阶段通过分布匹配消除曝光偏差，从根源抑制误差累积。该差异源于对退化机制的归因不同：FreqEdit将退化归因于高频信息丢失，MT Forcing归因于训练-推理条件不匹配。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，MT Forcing与AnchorEdit（Wan et al., 2025）均使用因果自滚动训练，但AnchorEdit侧重主体身份保持，通过记忆机制约束特定对象；MT Forcing侧重全局视觉质量与内容一致性，通过单轮教师监督整个编辑轨迹。该差异由任务特性决定：AnchorEdit针对身份漂移，MT Forcing针对通用多轮编辑。捆绑提示在指令存在强时序依赖（如“基于上一步结果”）时是否导致语义丢失，论文未验证。

## 总结

MT Forcing针对自回归扩散模型在多轮图像编辑中的曝光偏差问题，利用单轮编辑无累积误差的特性，通过Single-Turn DMD将学生自生成轨迹对齐至单轮教师分布，并以Teacher-Forcing Guidance约束跨轮内容一致性。在SenseNova-U1.5上，该方法使第8轮IF提升4.65、CC提升4.46，八轮平均Pixel降低88.4%。其边界在于依赖单轮教师对复杂组合指令的理解能力，若单轮模型对捆绑提示的语义重组存在偏差，教师监督信号将失效；且实验仅验证8轮编辑，未测试长程多轮场景下的累积误差控制极限。当编辑指令包含强时序依赖或隐含推理时，捆绑提示的语义重组是否会引入新的理解偏差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.25404)