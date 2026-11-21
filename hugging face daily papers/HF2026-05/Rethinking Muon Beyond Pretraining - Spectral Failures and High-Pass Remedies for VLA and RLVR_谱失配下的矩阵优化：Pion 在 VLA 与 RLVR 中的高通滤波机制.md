# HuggingFace最新推荐论文 ｜Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR ｜谱失配下的矩阵优化：Pion 在 VLA 与 RLVR 中的高通滤波机制

研究机构：美国密歇根州立大学、美国明尼苏达大学

作者：Chongyu Fan、Gaowen Liu、Mingyi Hong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.19282)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.19282)

> 矩阵感知优化器 Muon 通过 Newton-Schulz (NS) 迭代实现谱范数下的最速下降，在 LLM 预训练中显著优于 AdamW，但其均匀谱白化机制在后训练场景面临失效风险。现有变体如 Low-Rank Muon 虽能处理低秩结构，却依赖高开销的 SVD 或固定秩投影，无法适应动态变化的梯度信噪比。本文提出 Pion，通过重构 NS 多项式系数实现“促进主导奇异值、抑制噪声尾部”的高通滤波，并在注意力头维度独立应用以保留预训练异构性。该设计在 VLA 与 RLVR 任务中稳定了训练过程，但其在非预训练长尾分布下的泛化边界尚待进一步验证。

## 研究背景

理解 Muon 的局限需先厘清其核心机制与后训练梯度的本质差异。Muon 利用 NS 迭代近似矩阵符号函数，将动量矩阵的所有奇异值映射至 1，从而在谱域内实现各向同性的更新。这种均匀白化在预训练阶段有助于探索高维参数空间，避免少数主导方向垄断优化路径。然而，后训练阶段（如 VLA 与 RLVR）的梯度谱结构截然不同：VLA 的动作头梯度呈现极低的有效秩，而 RLVR 的策略梯度则具有极低的信噪比 (SNR)。在这种异质且含噪的谱分布下，Muon 的均匀白化会将噪声尾部方向放大至与信息头部方向同等量级，导致更新方向被噪声污染，引发训练不稳定甚至崩溃。

矩阵优化器在 LLM 预训练中的成功引发了对其适用边界的重新审视。主流研究聚焦于提升预训练效率，如 NorMuon 引入块级自适应学习率，Dion2 通过随机采样降低计算开销，但这些工作均默认梯度谱结构相对均匀或可通过固定策略处理。当场景转向多模态 VLA 训练或基于可验证奖励的强化学习 (RLVR) 时，梯度谱的异质性成为核心挑战。Low-Rank Muon 尝试通过投影至 top-k 子空间来适应低秩结构，但其固定秩假设无法跨层或跨步自适应，且 SVD 开销严重限制了可扩展性。本文切入点在于识别出“谱失配”这一根本原因，即 Muon 的均匀白化与后训练梯度中“信息集中于头部、噪声主导尾部”的结构不兼容，从而提出无需显式 SVD 的自适应谱滤波方案。

## 核心方法

### 方法参照系

标准 Muon 将动量矩阵 $\mathbf{M}_t$ 视为单一块，通过固定系数 $(a,b,c)$ 的 NS 迭代 $\mathbf{X} \leftarrow a\mathbf{X} + b\mathbf{XX}^\top\mathbf{X} + c\mathbf{X}(\mathbf{X}^\top\mathbf{X})^2$ 实现均匀谱白化。本文的关键差异在于：不再追求所有奇异值趋近 1，而是根据后训练梯度的低秩/低 SNR 特性，重新设计多项式映射以区分信息头部与噪声尾部，并引入 per-head 粒度以尊重预训练形成的注意力头异构性。

### 两阶段高通 NS 迭代

标准 NS 迭代的问题在于其多项式映射对所有奇异值施加相同的变换，导致噪声尾部被放大。Pion 将 NS 迭代重构为“促进 (Promotion) + 抑制 (Suppression)”两阶段序列，通过约束条件确定新的多项式系数，使得映射函数 $f(\sigma)$ 在 $\sigma \approx 1$ 处保持高增益（锚定主导奇异值），而在 $\sigma \approx 0$ 处呈现低增益（抑制尾部噪声）。这一设计动机直接针对 Muon 在低 SNR 梯度下放大噪声的失效模式。

$$
\mathbf{X}_{k+1} = P(\mathbf{X}_k) = \sum_{i=0}^{d} c_i \mathbf{X}_k^{2i+1}
$$

该公式表示 Pion 的每步更新，其中 $c_i$ 为通过两阶段约束求解的高通滤波系数。物理含义是：该多项式作为一个软高通滤波器，将动量矩阵的奇异值谱重塑为“头部保留、尾部衰减”的形态，从而在保持计算复杂度与 Muon 相同的前提下，实现了对噪声方向的自适应抑制。

### Per-Head 独立谱滤波

Muon 将每个权重矩阵作为整体进行正交化，忽略了 Transformer 注意力投影中不同头 (head) 在预训练中形成的专业化分工。Pion 引入 per-head 模式，将注意力投影矩阵沿头维度 reshape，对每个头独立应用上述高通 NS 迭代。这一设计解决了 Muon 无法适应后训练中各头所需异质更新尺度的问题。由于 reshape 操作不增加矩阵乘法次数，per-head 模式的计算开销与标准 Muon 完全一致，实现了零成本的结构适配。

## 实验评估

实验在 VLA 训练（LIBERO/LIBERO-Plus，VLA-Adapter/VLANeXt）和 RLVR 后训练（Qwen3-1.7B/4B，MATH/GSM8K）上进行，基线包括 AdamW、Muon 及 Low-Rank Muon (LRMuon)。基线覆盖充分，但缺失 NorMuon、Dion2 等高效变体的直接对比，可能影响对 Pion 相对效率优势的完整评估。

| 任务/模型 | 优化器 | 指标 | 数值 |
|---|---|---|---|
| LIBERO Object (VLA-Adapter) | AdamW | Success Rate | 32.2 |
| LIBERO Object (VLA-Adapter) | Muon | Success Rate | 97.0 |
| LIBERO Object (VLA-Adapter) | Pion | Success Rate | 100.0 |
| LIBERO-Plus Avg (VLANeXt) | AdamW | Success Rate | 64.57 |
| LIBERO-Plus Avg (VLANeXt) | Muon | Success Rate | 72.34 |
| LIBERO-Plus Avg (VLANeXt) | Pion | Success Rate | 75.93 |
| Real-Robot Avg (π0.5) | AdamW | Success Rate | 31.1 |
| Real-Robot Avg (π0.5) | Muon | Success Rate | 38.9 |
| Real-Robot Avg (π0.5) | Pion | Success Rate | 85.6 |

Pion 在 VLA 任务中全面超越 Muon 和 AdamW，尤其在真实机器人抓取任务中，Pion 的平均成功率 (85.6%) 显著高于 Muon (38.9%)，验证了高通滤波对低秩动作梯度的有效性。在 RLVR 任务中，Muon 出现训练崩溃（准确率接近零），而 Pion 稳定收敛并优于 AdamW，证明了其在低 SNR 策略梯度下的鲁棒性。

消融实验通过反向构造 Low-pass Muon (LPMuon) 验证了高通设计的必要性。LPMuon 翻转系数以放大小奇异值、收缩大奇异值，结果在 RLVR 中同样崩溃，证实了 Pion 的性能增益直接源于“抑制尾部噪声”的高通特性，而非其他因素。此外，Pion 在 LIBERO-Plus 的扰动场景（如 Language, Noise）下优势放大，表明其生成的策略对分布偏移更具鲁棒性。

评估边界方面，论文未报告 Wall-clock Time 或 FLOPs 的详细对比，仅定性声称计算效率与 Muon 相同，缺乏量化证据。代码已开源，但超参数设置（如 NS 迭代步数、两阶段系数求解细节）在正文中未完全披露，可能影响复现精度。

## 关联研究分析

从问题动机看，Pion 与 Low-Rank Muon (LRMuon) 均针对 Muon 在低秩梯度下的失效，但路线截然不同。LRMuon 通过显式 SVD 或随机草图将动量投影至 top-k 子空间，其核心假设是信息集中在固定秩的子空间内；而 Pion 认为秩是动态变化的，通过多项式系数自适应地“软”过滤尾部，避免了固定秩的僵化。这一差异源于任务特性：VLA 动作头的有效秩在训练过程中波动，固定秩投影可能误伤信息或保留噪声，而 Pion 的连续谱滤波能更平滑地适应这种动态变化。LRMuon 的 SVD 开销（约 15 倍于 Muon）使其难以扩展至大规模模型，Pion 则通过保留 NS 迭代结构规避了这一瓶颈。

从方法设计看，Pion 的 per-head 模式与 NorMuon 的块级自适应学习率思想有异曲同工之妙，均旨在解决参数更新尺度的异质性问题。NorMuon 在欧几里得空间通过维护二阶动量向量归一化更新范数，而 Pion 在谱域通过独立正交化各注意力头来保留预训练形成的头特异性。NorMuon 的自适应作用于步长，Pion 的自适应作用于方向。这种差异暗示，对于继承自预训练的模型，谱域的结构性约束（如 per-head 正交性）可能比欧几里得空间的范数归一化更能保留先验知识。Pion 在 RLVR 中的成功也表明，谱域滤波对低 SNR 梯度的噪声抑制效果优于单纯的步长调整。

## 总结

本文核心矛盾在于 Muon 的均匀谱白化机制与后训练阶段梯度谱的异质性（低秩/低 SNR）之间的冲突。现有方法如 LRMuon 依赖高开销的显式秩投影，无法动态适应且可扩展性差；Pion 通过重构 NS 多项式系数实现自适应高通滤波，以零额外计算成本解决了噪声放大问题。实验证明 Pion 在 VLA 真实机器人任务中将成功率从 Muon 的 38.9% 提升至 85.6%，并在 RLVR 中避免了 Muon 的训练崩溃。然而，Pion 的两阶段系数求解依赖于对梯度谱分布的特定假设，当后训练任务涉及非平稳或极端重尾噪声时，其滤波强度是否仍能保持最优，论文未提供理论保证或大规模验证。当梯度谱的头部与尾部界限模糊时，高通滤波的阈值敏感性如何影响长期泛化性能，仍需进一步探究。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.19282)