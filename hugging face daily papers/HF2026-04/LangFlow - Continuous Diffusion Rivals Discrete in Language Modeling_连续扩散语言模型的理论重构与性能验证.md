# HuggingFace最新推荐论文 ｜LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling ｜连续扩散语言模型的理论重构与性能验证

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Yuxin Chen、Chumeng Liang、Hangke Sui 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11748)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11748)

> 连续扩散语言模型（Continuous DLM）长期受困于稀疏概率单纯形导致的评分估计困难，以及缺乏可靠的似然评估手段，使其性能始终落后于离散掩码扩散。LangFlow 通过建立嵌入空间扩散与流匹配（Flow Matching）的理论联系，引入基于 Bregman 散度的交叉熵训练目标与 ODE 负对数似然（NLL）上界，解决了评估缺失与训练目标启发式的问题。该框架结合语言特有的 Gumbel 噪声调度与修正的自条件机制，在 130M 参数规模下实现了困惑度（PPL）对离散扩散的超越。其价值在于确立了连续扩散在语言建模中的理论可行性，但受限于小模型规模与多步采样，其优势能否扩展至大规模模型仍存疑。

## 研究背景

理解 LangFlow 需先厘清连续扩散在离散数据上的困境。传统连续扩散在图像等连续模态上成功，因其潜空间轨迹平滑且支持 ODE/SDE 采样。然而，语言数据本质是离散符号，直接将其映射到概率单纯形（Simplex）进行扩散时，空间极度稀疏，导致评分函数（Score Function）估计困难。为规避此问题，早期工作如 Diffusion-LM 和 Plaid 选择在嵌入空间（Embedding Space）进行扩散，即从高斯噪声逐步生成 Token 嵌入向量。这一路径避免了单纯形的稀疏性，但面临两个核心障碍：训练目标多为启发式或实现复杂，且缺乏基于确定性 ODE 的困惑度评估方法，导致无法准确衡量模型似然，进而阻碍了训练策略的优化。

离散扩散（Discrete Diffusion）如 MDLM 通过掩码机制在 Token 空间直接操作，虽性能强劲，但牺牲了连续潜空间的表达力，限制了可控生成与少步加速的可能性。与此同时，连续扩散在语言领域的探索长期停滞，主要因为缺乏统一的理论框架来连接离散似然训练与连续流估计。LangFlow 的切入点在于识别出嵌入空间扩散的 ODE 形式与流匹配（Flow Matching）的自然对齐性，通过 Bregman 散度理论将交叉熵损失确立为流匹配训练的原则性特例，并推导了 ODE 基于的 NLL 上界，从而填补了连续扩散语言模型在理论评估与设计空间上的空白。

## 核心方法

### 方法参照系

流匹配（Flow Matching）通过学习速度场 $u_t(z_t)$ 将先验分布传输至数据分布，通常采用仿射高斯路径 $z_t = \alpha_t z + \sigma_t \epsilon$。标准流程依赖时间 $t \in [0,1]$ 进行条件化，但这一参数化将目标与特定时间调度绑定，导致噪声水平与去噪难度的关系不直观。LangFlow 的关键差异在于引入对数噪声信号比 $\gamma$ 作为时间条件，并建立 Bregman 散度与交叉熵的理论联系，使连续流估计与离散似然优化统一。

### Bregman 散度流匹配与 ODE 评估

LangFlow 首先将流路径重参数化为 $\gamma$-path，其中 $\gamma_t = \log(\sigma_t^2 / \alpha_t^2)$，在方差保持（VP）路径下满足 $\alpha_\gamma^2 + \sigma_\gamma^2 = 1$。这一变换使去噪难度直接由噪声水平 $\gamma$ 控制，而非任意时间索引。在此基础上，论文证明交叉熵（CE）损失是 Bregman 散度最小化的特例。对于凸函数 $f(p) = p \cdot \log p$，Bregman 散度 $D_f(1_x, q) = -\log q_{x_i}$ 恰好对应交叉熵。训练目标定义为：

$$
\mathcal{L}_{CE} = \mathbb{E}_{\gamma \sim \pi(\gamma)} \mathbb{E}_{x} \left[ -\log \hat{x}_{\theta, x_i} (z_\gamma, \gamma) \right]
$$

该公式表明，模型在 Token 空间通过交叉熵优化，而对应的连续去噪器 $\hat{z}_\theta$ 由 Token 概率的嵌入期望确定，实现了离散似然训练与连续流估计的耦合。为解决评估难题，LangFlow 推导了 ODE 基于的 NLL 上界：

$$
\log p(x) \geq \mathbb{E}_{z_a \sim N(\alpha_a E[T]x, \sigma_a^2 I)} \left[ \log p(z_a | x) - \int_a^b \nabla \cdot \hat{z}_\theta(z_\gamma, \gamma) d\gamma \right]
$$

此上界替代了传统的 SDE 基于 ELBO，允许通过确定性 ODE 采样准确评估困惑度，消除了随机性对评估的干扰，为训练策略优化提供了可靠反馈。

### 信息均匀噪声调度与自条件修正

LangFlow 发现语言数据的最优噪声几何与图像领域显著不同。通过信息均匀原则（Information-Uniform Principle），即要求去噪过程中信息增益均匀分布，论文推导出 $\gamma$ 的最优分布服从 Gumbel 分布。具体而言，训练时 $\gamma$ 从 Gumbel 分布采样，采样时中间步 $\gamma_k$ 设为 Gumbel 分布的 $k/N$ 分位数。这一设计避免了图像扩散中常用的线性或余弦调度在语言任务上的次优性，显著提升了采样质量。此外，论文揭示了自条件（Self-Conditioning）在连续与离散扩散中的效果差异。在离散扩散中，自条件可能引入偏差，但在连续扩散中，以概率 0.25 激活自条件机制，即利用前一步预测 $\hat{x}_{\theta, k-1}$ 辅助当前步去噪，能显著降低生成困惑度。这一修正解决了此前连续扩散语言模型因自条件协议不当导致的性能瓶颈，使模型在 LM1B 上的 PPL 从 49.0 降至 30.0。

## 实验评估

LangFlow 在 LM1B 和 OpenWebText (OWT) 上进行了评估，模型规模为 130M 参数，采用 DiT 架构。基线覆盖离散扩散（MDLM, SEDD, UDLM, Duo）、连续扩散（Plaid, FLM）及自回归（AR）Transformer。实验设置中，LM1B 使用 128 上下文长度与 BERT 分词器，OWT 使用 1024 上下文长度与 GPT-2 分词器，训练步数均为 1M。

| 模型 | LM1B PPL ↓ | LM1B Gen. PPL ↓ | OWT PPL ↓ | OWT Gen. PPL ↓ |
| :--- | :--- | :--- | :--- | :--- |
| AR Transformer | 22.8 | 35.9 | 17.5 | – |
| MDLM | 31.0 | 103.9 | 23.2 | 104.9 |
| Duo | 33.6 | 97.6 | 25.2 | 77.6 |
| FLM | – | 96.9 | – | 62.2 |
| **LangFlow** | **30.0** | **92.2** | **24.6** | **36.5** |

LangFlow 在 LM1B 上取得 30.0 的 PPL，优于 MDLM 的 31.0；在 OWT 上 Gen. PPL 为 36.5，显著低于 MDLM 的 104.9 和 FLM 的 62.2。零样本迁移实验中，LangFlow 在 PTB、Wikitext 和 Lambada 上排名第一，并在 7 个基准中的 4 个上超越 AR Transformer，表明其泛化能力。

| 模型 | LM1B Gen. PPL ↓ | LM1B PPL ↓ |
| :--- | :--- | :--- |
| MDLM | 103.9 | 31.0 |
| MDLM + SC | 94.9 | 32.7 |
| LangFlow | 154.2 | 49.0 |
| LangFlow + SC | 81.5 | 30.0 |

消融实验显示，自条件对 LangFlow 的影响巨大：启用自条件后，LM1B Gen. PPL 从 154.2 降至 81.5，PPL 从 49.0 降至 30.0。相比之下，MDLM 启用自条件后 PPL 反而从 31.0 升至 32.7，证实了连续与离散扩散在自条件机制上的根本差异。Gumbel 调度器将 Gen. PPL 从约 1000 降至 154.2，验证了信息均匀原则的有效性。

评估边界方面，LangFlow 仅在 130M 参数规模下验证，未与 LLaDA 等 7B+ 规模模型对比，限制了结论的普适性。ODE 采样仍需 128-1024 步，未实现少步加速。代码已开源，但超参数如 Gumbel 分布的截断范围 $[a,b]$ 依赖经验分位数，缺乏理论最优性证明。

## 关联研究分析

从问题动机看，LangFlow 与 FLM（Flow Map Language Models）同属连续扩散路线，但 FLM 假设语言嵌入空间存在平滑流结构，直接学习一步生成，而 LangFlow 强调噪声调度的模态特异性。FLM 在 OWT Gen. PPL 上为 62.2，LangFlow 为 36.5，差异源于 LangFlow 的 Gumbel 调度更贴合语言数据的噪声几何，而 FLM 的线性调度可能未充分利用语言序列的局部依赖特性。这一差异暗示，连续扩散在语言上的成功不仅依赖架构，更依赖对数据分布特性的精细建模。

从方法设计看，LangFlow 与 MDLM 在训练目标上形成对比。MDLM 采用掩码预测，直接优化离散似然，而 LangFlow 通过 Bregman 散度将交叉熵嵌入连续流匹配框架。MDLM 在 LM1B PPL 上为 31.0，LangFlow 为 30.0，微小差距表明两者在似然估计上趋于收敛，但 LangFlow 的 ODE 评估提供了更精确的似然上界，而 MDLM 依赖 SDE 边界。这一对比揭示，连续扩散在语言建模中的优势并非来自架构本身，而是来自评估与训练目标的理论一致性。

## 总结

LangFlow 旨在解决连续扩散语言模型因缺乏理论评估与优化噪声调度而导致的性能滞后问题。其切入点在于通过 Bregman 散度统一交叉熵与流匹配，并推导 ODE 基于的 NLL 上界，从而建立可靠的评估与训练反馈闭环。方法上，LangFlow 引入 Gumbel 噪声调度与修正的自条件机制，在 130M 参数规模下实现 LM1B PPL 30.0 与 OWT Gen. PPL 36.5，超越离散扩散基线。其边界在于实验规模有限，未验证大规模扩展性，且 ODE 采样步数未压缩。当模型规模扩展至 7B 以上时，Gumbel 调度的优势是否依然显著，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11748)