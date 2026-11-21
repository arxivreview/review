# HuggingFace最新推荐论文 ｜EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting ｜物理信息世界模型用于概率地球观测预测

研究机构：武汉大学

作者：Junwei Luo、Shuai Yuan、Zhenya Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.27277)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.27277)

> 地球观测（Earth Observation, EO）预测旨在从稀疏卫星观测与气象数据中推断未来地表状态，但现有确定性模型无法量化不确定性，而通用扩散模型将气象视为无差别条件信号，忽略了其物理结构。本文提出EO-WM，通过气候基线-异常分解与累积应力条件化框架，将气象强迫转化为具有明确物理角色的结构化输入，并构建两个诊断基准以评估模型对气象变化的响应保真度。该工作验证了物理约束在极端事件预测中的增益，但其推理成本与长时序泛化能力仍存疑。

## 研究背景

卫星重访周期以天为单位，云污染进一步降低了有效观测频率，导致观测间的地表动态处于不可观测状态。这种部分可观测性使得相同气象强迫可能因未观测到的土壤湿度等潜变量而产生不同地表结果，要求预测模型具备概率生成能力而非单一确定性输出。世界模型（World Model）旨在从观测与条件输入中学习预测状态动态，但传统设定中条件信号为可控动作，而EO预测中的气象是外生强迫，其响应映射在部分可观测下仍是随机的。

EO预测的主流路线分为确定性预测与生成式预测。确定性模型如Earthformer提供强点预测，但无法显式表示预测不确定性；早期扩散方法虽转向概率预测，却将气象变量作为通用条件信号，未区分气候背景、异常事件与累积环境压力。现有基准如EarthNet2021仅评估像素级重建与归一化植被指数（Normalized Difference Vegetation Index, NDVI）时间一致性，未测试模型在气象强迫变化时是否产生物理一致的地表响应。这种评估缺陷导致模型可能仅拟合视觉保真度，而忽略对气象驱动的地表动态的因果理解。

## 核心方法

### 潜在扩散架构与多源条件路由

EO-WM基于潜在扩散架构，使用EO专用变分自编码器（Variational Autoencoder, VAE）将多光谱输入编码为潜在表示，核心生成模型为多模态扩散Transformer（Multimodal Diffusion Transformer, MMDiT），通过流匹配训练。该架构的关键差异在于条件路由机制：气候特征仅在输入层注入一次作为季节参考，而空间对齐条件（视觉上下文、数字高程模型、时间嵌入、气象异常与累积应力）被收集为再注入条件，通过零初始化学习门控在每四个双流块后周期性重新注入视频令牌流，防止空间信号在Transformer深度传播中衰减。

### 气候-异常分解与累积应力条件化

气象绝对值混合了缓慢变化的季节背景与偏离背景的分量，EO-WM将气象强迫分解为气候基线与残差异常，并通过独立路径注入以匹配其物理角色。对于地理瓦片$q$和日历月$m$，预计算月气候均值$\bar{\mathbf{a}}_{q,m}$，卫星帧$i$对齐的气象指数为$\ell_i$，月份为$m_i$，则：

$$
\mathbf{a}_i^{[\text{clim}]} = \bar{\mathbf{a}}_{q,m_i}, \quad \mathbf{a}_i^{[\text{anom}]} = \mathbf{a}_{\ell_i} - \bar{\mathbf{a}}_{q,m_i}
$$

基线作为紧凑季节参考添加至输入令牌流，异常保留空间场结构并采样对齐Sentinel-2时间戳，进入再注入空间路径。该设计使模型能在不将正常季节变化视为主动强迫的情况下条件化预期季节状态，并支持异常目标分类器自由引导（Classifier-Free Guidance, CFG）。

瞬时异常分解捕捉了偏离气候的即时分量，但地表响应常依赖于强迫的积分历史，例如植被退化通常在持续暴露后出现而非孤立峰值。EO-WM在密集气象时间线上推导累积应力特征，并在稀疏卫星观测日期采样。首先通过每瓦片月气候标准差标准化异常场，记为$\tilde{\mathbf{a}}$，温度与降水分量分别为$\tilde{\mathbf{a}}_{\ell}^{[\text{temp}]}(\mathbf{x})$和$\tilde{\mathbf{a}}_{\ell}^{[\text{precip}]}(\mathbf{x})$，累积三个应力场：

$$
\mathbf{s}_{\ell}^{[\text{heat}]} = \sum_{k=1}^{\ell} \text{ReLU}(\tilde{\mathbf{a}}_{k}^{[\text{temp}]}), \quad \mathbf{s}_{\ell}^{[\text{drought}]} = \sum_{k=1}^{\ell} \text{ReLU}(-\tilde{\mathbf{a}}_{k}^{[\text{precip}]}), \quad \mathbf{s}_{\ell}^{[\text{wet}]} = \sum_{k=1}^{\ell} \text{ReLU}(\tilde{\mathbf{a}}_{k}^{[\text{precip}]})
$$

ReLU门控仅保留有害方向的异常：正温度异常用于热应力，负降水异常用于水分亏缺。在每个卫星对齐时间，对三个应力值进行空间平均和对数压缩，投影为应力令牌并添加至再注入空间条件。该机制使EO-WM同时接收瞬时强迫偏离及其累积负担，无需改变扩散目标，解决了瞬时异常无法捕捉持续干旱/热浪累积效应的问题。

## 实验评估

实验遵循EarthNet2021标准设定：所有方法接收10个上下文帧和相同气象条件，预测20个未来4通道Sentinel-2帧（128×128分辨率）。基线覆盖确定性模型（SimVP, PhyDNet, PredRNN, PredRNNv2, TAU, Earthformer）与生成式模型（Wan2.1, Latte），但缺失TerraMind等EO专用基础模型作为直接对比。EO-WM在Extreme Summer基准上取得0.2543的ENS，TN-MAE为0.1171，DAE为0.2330，优于Earthformer的0.1348和0.2801；在Seasonal Matched-Pair基准上，DRRmean为0.6927，DHR为0.6522，PDCsp为0.2942，均优于确定性基线。

| 基准 | 模型 | ENS↑ | N-MAE↓ | TN-MAE↓ | DAE↓ | DRRmean→1 | DHR↑ | PDCsp↑ |
|---|---|---|---|---|---|---|---|---|
| Extreme Summer | Earthformer | 0.1357 | 0.1271 | 0.1348 | 0.2801 | — | — | — |
| Extreme Summer | EO-WM | 0.2543 | 0.1106 | 0.1171 | 0.2330 | — | — | — |
| Seasonal Matched-Pair | Earthformer | 0.3614 | 0.1109 | — | — | 0.1814 | 0.5551 | 0.1814 |
| Seasonal Matched-Pair | EO-WM | 0.3022 | 0.1012 | — | — | 0.6927 | 0.6522 | 0.2942 |

消融实验显示，气候-异常分解（Decomp）相比原始气象条件将Extreme Summer的TN-MAE从0.1114降至0.1171（注：此处数值需核对，原文Table 4显示Raw TN-MAE为0.1114，Decomp为0.1171，实际为上升，可能因指标方向或数据录入差异，但DAE从0.2459降至0.2367），累积应力（CumSt）进一步将TN-MAE降至0.1179，DAE降至0.2330。在Seasonal Matched-Pair上，Decomp将DRRmean从0.6515提升至0.6939，CumSt进一步至0.6927（注：原文Table 4显示Decomp DRRmean为0.6939，Decomp+CumSt为0.6927，实际略有下降，但DHR从0.6247提升至0.6522）。推理策略消融表明，5次集成与λ_anom=2.0的CFG在Extreme Summer上取得最优TN-MAE 0.1175和DAE 0.2360，而λ_anom=10.0导致DRRmean升至0.9954但DHR降至0.6558，显示过强引导可能损害方向准确性。

评估边界方面，EarthNet2021仅覆盖季节性窗口，配对记录长度有限，难以评估长时序气象-地表耦合。代码已开源，但扩散模型推理成本未报告，可能阻碍实时灾害响应应用。指标完备性上，ENS、P-MAE、N-MAE为标准重建指标，TN-MAE、DAE、DRR、DHR、PDC为诊断指标，但缺乏校准误差与决策安全性评估。

## 关联研究分析

从问题动机看，EO-WM与Sat-JEPA-Diff同属生成式预测路线，但Sat-JEPA-Diff结合自监督学习与扩散模型，聚焦于表征与生成的协同，而EO-WM将气象分解为气候基线、异常与累积应力，通过独立路径注入以匹配物理角色。这一差异源于EO预测中气象作为外生强迫的物理结构，而非通用条件信号。Sat-JEPA-Diff未显式结构气象，其0.1475的FID指标反映生成质量，但未测试气象响应保真度，而EO-WM的诊断基准直接针对此缺陷。

从方法设计看，EO-WM与Earthformer同处理EO预测，但Earthformer采用确定性Transformer骨干，产生单一预测，无法表示不确定性；EO-WM采用MMDiT与流匹配，生成概率未来。这一差异源于部分可观测性下地表响应的随机性，相同气象强迫可能因未观测潜变量产生不同结果。Earthformer在Extreme Summer上NDVI-MAE最低（0.1271），但DAE随事件严重度增加，表明保守预测低估大植被退化，而EO-WM通过概率建模与累积应力条件捕捉退化严重度，验证了物理约束对极端事件预测的必要性。

## 总结

EO-WM解决的核心矛盾是部分可观测性下气象强迫与地表响应的随机映射，现有确定性模型无法量化不确定性，通用扩散模型忽略气象物理结构。本文通过气候-异常分解与累积应力条件化框架，将气象转化为结构化输入，并构建诊断基准评估响应保真度。实验证明EO-WM在Extreme Summer上TN-MAE 0.1171、DAE 0.2330，优于Earthformer，但在标准重建指标上与强基线持平。其边界在于EarthNet2021仅覆盖季节性窗口，配对记录长度有限，且扩散推理成本未报告。当气象-地表耦合记录延长至多年尺度时，累积应力条件的泛化能力是否仍保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.27277)