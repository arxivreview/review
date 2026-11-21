# HuggingFace最新推荐论文 ｜Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation ｜电影级视频生成中的因子感知预测学习

研究机构：香港科技大学

作者：Songlin Yang、Zhe Wang、Xiaotong Zhao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.30926)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.30926)

> 电影级视频生成要求模型从稀疏脚本推断时序动作，并独立控制角色、场景、动作与相机等因子。现有基于多模态大语言模型（Multimodal Large Language Model, MLLM）与扩散Transformer（Diffusion Transformer, DiT）的架构中，MLLM特征常被文本或视觉参考路径绕过，导致控制失效。FAPL通过三阶段训练强制DiT依赖MLLM潜变量，利用配对视频进行因子跨度替换以监督解耦，并冻结DiT反向优化MLLM以适配生成需求。该范式显著提升了因子控制的精确度，但其在公开基准上的泛化能力及推理时的条件依赖仍存疑。

## 研究背景

当生成模型面对电影级脚本时，文本提示仅稀疏指定视觉内容，缺乏逐帧的时空细节，模型需从有限输入中推断合理的动作序列与相机运动。这一过程称为时序推断。同时，用户要求修改特定因子（如更换角色）时，其他因子（如动作、场景）必须保持不变，这称为因子感知控制。传统条件注入方式将文本、MLLM特征与视觉参考拼接，但DiT倾向于依赖信息密度更高的文本或视觉路径，导致MLLM的语义推理能力被“绕过”，无法有效指导生成。

领域内主流方法如UniVideo和Omni-Video 2虽引入了MLLM分支，但仅在视频级别进行监督，未显式关联MLLM特征中的特定片段与输出变化。这种混合条件训练使得模型难以区分哪些特征对应角色，哪些对应相机，导致因子纠缠。此外，冻结MLLM仅训练连接器和DiT，无法使MLLM产生适配视频生成的时序表征。FAPL针对这一“特征存在但无效”的瓶颈，提出在生成空间内结构化监督信号，通过隔离条件、因子干预和反向优化，确立MLLM特征在生成中的核心地位。

## 核心方法

### 方法参照系：MLLM条件化视频扩散

FAPL基于MLLM条件化视频扩散框架，其中DiT通过流匹配（Flow Matching）训练，接收文本、MLLM和视觉参考三种拼接条件。标准流程中，MLLM隐藏状态经连接器映射为条件 $C_{mllm}$。本文的关键差异在于：训练阶段强制移除文本编码器和视觉参考条件，仅保留MLLM投影潜变量作为唯一内容条件，以迫使DiT学习解码MLLM特征。

### Stage I：仅MLLM潜变量的生成器接地

为解决MLLM特征被绕过的问题，Stage I冻结MLLM和连接器，仅训练DiT。通常做法是混合多条件训练，但本文在两种观测模式（纯文本、文本+完整视频）下，仅使用MLLM潜变量作为条件。

$$
\mathcal{L}_{ground}(\phi) = \mathbb{E}_{(x,p)\sim\mathcal{D}_{obs}} \left[ \sum_{m\in\{t,tv\}} \rho_m \mathcal{L}_{FM}(x | Z_{\theta_0,\eta_0}(u_m); \phi) \right]
$$

该公式表示在混合观测分布 $\rho$ 下，DiT参数 $\phi$ 通过流匹配损失 $\mathcal{L}_{FM}$ 优化，其中 $Z$ 为MLLM投影潜变量。由于缺乏其他内容路径，DiT必须建立对MLLM潜变量的强依赖，为后续因子控制奠定接口基础。

### Stage II：因子跨度替换与感知控制

Stage I建立了特征使用能力，但未解决因子解耦。Stage II引入配对编辑数据，通过替换MLLM潜变量中的特定因子跨度来监督控制。通常做法是将编辑对作为普通样本训练，本文则显式定位角色、场景、动作、相机对应的Token跨度，并执行替换操作。

$$
\mathcal{L}_{edit}(\phi) = \mathbb{E}_{(x_a,p_a,x_b,p_b,k)\sim\mathcal{D}_{edit}} \left[ \mathcal{L}_{FM}(x_b | Z_{k}^{a\leftarrow b}; \phi) + \mathcal{L}_{FM}(x_a | Z_{k}^{b\leftarrow a}; \phi) \right]
$$

该公式中，$Z_{k}^{a\leftarrow b}$ 表示将视频A的潜变量中因子 $k$ 的跨度替换为视频B的对应跨度。通过监督替换后的潜变量生成目标视频，DiT学习到特定因子跨度变化与输出内容变化的映射关系，实现非目标因子的保持。

### Stage III：固定生成器下的预测学习

前两个阶段优化了DiT，但MLLM本身未针对生成任务优化。Stage III冻结Stage II训练后的DiT（$\phi^*$），反向优化MLLM和连接器。通常做法是端到端训练，但本文通过固定生成器，使MLLM学习产生“生成兼容”的表征。

$$
\mathcal{L}_{obs}(\theta, \eta) = \mathbb{E}_{(x,p)\sim\mathcal{D}_{obs}} \left[ \sum_{m\in\{t,tv\}} \pi_m \mathcal{L}_{FM}(x | Z_{\theta,\eta}(u_m); \phi^*) \right]
$$

该公式表示在固定DiT下，通过最小化流匹配损失更新MLLM参数 $\theta$ 和连接器 $\eta$。纯文本模式迫使MLLM从稀疏证据中推断时序信息，完整视频模式提供重建监督，两者共享目标视频，确保MLLM输出的潜变量既包含语义又适配生成器解码。

## 实验评估

论文在自建电影级数据集上评估稀疏到视频生成、因子编辑和多镜头生成任务。基线覆盖UniVideo、Omni-Video 2等主流MLLM-DiT架构。由于缺乏公开基准的直接数值对比，实验主要通过定性分析和消融实验验证有效性。

| 评估维度 | 基线方法 | FAPL表现 | 备注 |
| --- | --- | --- | --- |
| 稀疏输入生成 | UniVideo | 显著优于 | UniVideo出现语义忽略与伪影 |
| 因子编辑控制 | Omni-Video 2 | 显著优于 | Omni-Video 2中VAE参考主导，MLLM被绕过 |
| 多镜头一致性 | 无直接对比 | 验证有效 | 通过Stage III反向优化提升时序连贯性 |

消融实验显示，Stage I对建立MLLM特征依赖至关重要，移除后DiT退化为依赖文本/VAE路径；Stage II的因子跨度替换显著提升了编辑时的非目标因子保持率；Stage III使MLLM在纯文本输入下的生成质量提升，证明其产生了时序推断能力。

评估边界方面，论文未提供公开基准（如VBench）的定量分数，主要依赖自建数据的定性对比，存在过拟合风险。此外，推理时是否完全弃用文本/VAE条件未明确说明，若保留则训练-推理不一致可能影响实际效果。代码未开源，复现难度较高。

## 关联研究分析

从问题动机看，FAPL与TempoControl均关注细粒度控制，但TempoControl通过推理时注意力引导实现时间控制，属于免训练方法；FAPL则通过训练时的因子跨度替换显式监督解耦，属于训练时优化。TempoControl保留了基础模型泛化能力，但控制精度受限于注意力机制的隐式性；FAPL通过结构化监督实现了更精确的因子绑定，但牺牲了部分训练灵活性。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，FAPL与Kaleido均处理多主体一致性，但Kaleido通过多参考图像特征解耦身份，侧重于空间维度的主体保持；FAPL将控制维度扩展至角色、场景、动作、相机四个因子，并通过MLLM潜变量跨度实现统一控制。Kaleido依赖参考图像质量，FAPL依赖MLLM的语义解析能力。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

## 总结

FAPL针对MLLM-DiT架构中特征绕过与因子纠缠的核心矛盾，提出三阶段训练范式：先隔离条件强化DiT对MLLM潜变量的依赖，再通过因子跨度替换监督解耦控制，最后冻结DiT反向优化MLLM以适配生成需求。实验表明，该范式在因子编辑和稀疏输入生成上显著优于UniVideo等基线，有效解决了MLLM特征“存在但无效”的问题。然而，论文依赖自建数据评估，缺乏公开基准的定量对比，且未明确推理时的条件组合策略。当推理时重新引入文本或VAE条件以增强稳定性时，Stage I建立的MLLM独占依赖是否会因条件竞争而减弱，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.30926)