# ICLR2026最新论文 ｜Large Scale Diffusion Distillation via Score-Regularized Continuous-Time Consistency ｜分数正则化连续时间一致性模型

研究机构：清华大学

作者：Kaiwen Zheng、Yuji Wang、Qianli Ma 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08431)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08431)

> 少步扩散蒸馏旨在将教师模型数十步的推理压缩至1-4步，但现有方法在质量与多样性间存在不可调和的矛盾：一致性模型（CM）保留多样性却丢失细节，分布匹配蒸馏（DMD）提升质量却导致模式坍缩。rCM通过联合前向散度（sCM）与反向散度（分数蒸馏）解决这一冲突，首次将连续时间一致性扩展至14B参数视频模型。该方法在GenEval和VBench上持平或超越DMD2，且多样性显著占优，但其对超参数λ的敏感性及未覆盖的自回归场景限制了通用性。

## 研究背景

扩散模型通过迭代去噪生成高保真样本，但推理成本高昂。为加速采样，少步蒸馏成为核心路径，其本质是在极低网络评估次数（NFE）下最小化学生分布 $p_S$ 与教师分布 $p_T$ 的散度。连续时间一致性模型（sCM）通过Jacobian-vector product (JVP) 消除离散化误差，理论上优于离散CM，但此前仅验证于1.5B参数的ImageNet基准，未触及大规模应用级模型。

主流蒸馏路线分为轨迹一致性与分布匹配两类。轨迹一致性路线（如CM、MeanFlow）依赖前向散度，具有“模式覆盖”特性，能保持多样性，但易产生模糊与失真；分布匹配路线（如DMD2）依赖反向散度，具有“模式寻求”特性，质量高但易模式坍缩。现有研究多将二者视为互斥选项，缺乏在大规模强条件任务（如文生视频）中联合优化的实证。rCM的切入点在于：利用前向与反向散度的互补性，通过分数蒸馏作为长跳正则项，同时解决sCM的细节缺失与DMD的多样性损失。

## 核心方法

### 方法参照系

本文问题属于少步扩散蒸馏，标准流程为训练学生网络 $f_\theta$ 映射噪声至数据。与通用流程的关键差异在于：rCM不单独优化单一散度，而是将sCM的前向损失与分数蒸馏的反向损失加权联合，且需解决JVP在BF16精度与并行计算中的数值稳定性问题。

### 连续时间一致性与JVP稳定化

sCM的核心是瞬时自一致性，其损失函数为：

$$ \mathcal{L}_{sCM} = \mathbb{E}_{\mathbf{x}_0 \sim p_{data}, \mathbf{\epsilon}, t} \left[ \left\| \mathbf{F}_\theta(\mathbf{x}_t, t) - \mathbf{F}_{\theta^-}(\mathbf{x}_t, t) - w(t) \frac{d f_{\theta^-}}{dt}(\mathbf{x}_t, t) \right\|_2^2 \right] $$

该公式强制学生网络在任意时间步 $t$ 的输出与其沿教师ODE轨迹的切线方向一致。设计动机在于解决离散CM的误差累积问题，但原始sCM依赖FP16与特定噪声调度，在BF16与FlashAttention环境下JVP计算易溢出。rCM通过TrigFlow调度与教师模型的SNR匹配构造“wrapped teacher”，并将权重 $w(t)$ 吸收进JVP计算，实现了无需重训练教师的稳定训练。

### 分数正则化长跳机制

针对sCM“模式覆盖”导致的细节模糊，rCM引入分数蒸馏作为长跳正则项。总损失为：

$$ \mathcal{L}_{rCM} = \mathcal{L}_{sCM} + \lambda \mathcal{L}_{SiD} $$

其中 $\mathcal{L}_{SiD}$ 为分数恒等蒸馏损失，基于反向KL散度，监督信号来自学生自生成样本。设计动机在于利用反向散度的“模式寻求”特性提升局部细节质量，同时前向散度维持全局多样性。$\lambda$ 控制质量-多样性权衡，实验表明 $\lambda=0.01$ 为“甜点”，过小则质量下降，过大则多样性坍缩。

## 实验评估

实验在Cosmos-Predict2（T2I）与Wan2.1（T2V）上进行，基线涵盖DMD2、FLUX.1-schnell、SDXL-LCM等。rCM在4步NFE下，Cosmos-Predict2 14B模型GenEval Overall得分0.83，优于DMD2的0.80；Wan2.1 14B模型VBench Total得分85.05（2步），优于DMD2的84.56（4步）。

| 模型 | 参数量 | NFE | GenEval Overall | VBench Total |
| :--- | :--- | :--- | :--- | :--- |
| Cosmos-Predict2 + DMD2 | 14B | 4 | 0.80 | - |
| Cosmos-Predict2 + rCM | 14B | 4 | 0.83 | - |
| Wan2.1 T2V + DMD2 | 14B | 4 | - | 84.56 |
| Wan2.1 T2V + rCM | 14B | 2 | - | 85.05 |

消融实验显示，$\lambda$ 对性能影响显著：$\lambda=1$ 时VBench得分84.32，$\lambda=0.01$ 时84.43，$\lambda=0.001$ 时82.68。这表明反向散度权重需精细调节，过大导致多样性损失，过小则质量不足。

评估边界方面，rCM未报告FID，仅使用GenEval与VBench，可能忽略分布保真度的全局度量。代码已开源，但JVP内核依赖FlashAttention-2，复现需特定硬件支持。

## 关联研究分析

从问题动机看，rCM与DMD2均解决少步生成质量，但DMD2仅用反向散度，导致模式坍缩；rCM引入前向散度，保留了sCM的多样性优势。这一差异源于任务特性：视频生成对运动一致性要求高，单一模式寻求易导致物体位置固化，而前向散度的模式覆盖特性有助于维持动态多样性。

从方法设计看，rCM与MeanFlow同属连续时间一致性路线，但MeanFlow仅优化前向散度，rCM增加分数蒸馏正则项。MeanFlow在ImageNet上表现优异，但未验证于强条件T2V任务；rCM通过JVP稳定化与联合优化，填补了大规模视频蒸馏的空白。然而，rCM未探索自回归视频扩散中的因果教师强制，这是否会影响长视频生成的时序一致性，论文未给出回答。

## 总结

rCM解决的核心矛盾是少步蒸馏中质量与多样性的权衡。其切入点在于利用前向与反向散度的互补性，通过分数蒸馏正则化sCM，解决了大规模模型中JVP数值不稳定与细节缺失问题。实验证明，rCM在14B参数模型上，4步T2I GenEval得分0.83，2步T2V VBench得分85.05，持平或超越DMD2且多样性更优。边界在于：$\lambda$ 超参数敏感，且未覆盖自回归视频场景。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08431)