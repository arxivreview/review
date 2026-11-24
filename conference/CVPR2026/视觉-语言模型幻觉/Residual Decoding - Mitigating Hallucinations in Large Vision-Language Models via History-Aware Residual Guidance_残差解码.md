# CVPR2026最新论文 ｜Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance ｜残差解码

研究机构：北京大学、北京邮电大学

作者：Xinrong Chen、Xu Chu、Yingmin Qiu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.01047)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01047)

> 大视觉语言模型（LVLMs）在生成图像描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。现有推理时干预策略如视觉对比解码（VCD）虽能抑制幻觉，但需额外前向传播，计算开销大且超参数敏感。ResDec 利用解码过程中历史 logits 的时序演化规律，通过 Jensen–Shannon Divergence (JSD) 定位语义锚定阶段，提取稳定残差信号融合至当前解码，实现单次前向传播的零成本幻觉抑制。该方法在 POPE 和 CHAIR 基准上显著优于基线，但其 JSD U 型曲线的普适性及长序列生成后期的有效性尚存疑。

## 研究背景

当 LVLM 面对模糊视觉输入时，其内部语言模型（LLM）组件倾向于依赖预训练习得的统计规律而非视觉证据，导致生成内容在语法上连贯但在视觉上无接地。这种语言先验（Language Prior）与视觉信号的冲突是幻觉的核心根源，早期研究试图通过数据对齐或指令微调从源头纠正，但受限于标注成本与泛化瓶颈，效果有限。2024 年，研究范式转向推理时干预，VCD 等解码策略证明无需重训即可通过对比原始与扰动输入的 logits 分布动态调整生成概率，显著降低了部署成本。

然而，VCD 及其变体需要额外前向传播，计算开销大且对超参数敏感，难以满足实时应用需求。同时，现有方法多聚焦于全局对比或注意力重加权，缺乏对解码过程中内部时序动态的细粒度利用。ResDec 的切入点在于发现 LVLM 在解码前已隐含地“预知”部分未来输出，即正确答案的信号已嵌入历史 tokens 的 logits 分布中。通过挖掘这一内部隐式推理机制，ResDec 旨在以极低的计算成本实现精准的视觉接地重构。

## 核心方法

### 解码策略参照系

ResDec 属于推理时干预中的解码策略优化路线，作用于 Logits 层。与 VCD 依赖外部视觉扰动构建负样本不同，ResDec 不引入额外输入，而是挖掘模型内部历史 logits 的时序演化规律。其关键差异在于将干预点从“对比外部扰动”移至“聚合内部历史稳定信号”，从而避免额外前向传播带来的计算冗余。

### 基于 JSD 的语义锚定阶段定位

ResDec 首先利用 JSD 分析历史窗口内候选 token 概率分布的时序变化，发现其呈现 U 型趋势。该趋势分为三个阶段：前语义清晰阶段（PSAP）、语义锚定阶段（SAP）和表达发散阶段（EDP）。SAP 阶段 JSD 接近零，表明分布稳定，语义收敛，受语言先验影响最小。ResDec 选取 SAP 及 EDP 初期作为历史聚合窗口 $\Delta_t$，以捕获语义稳定且具表达多样性的 logits 信号。

$$
\text{JSD}(P_t, P_{t+1}) = \frac{1}{2} D_{KL}(P_t || M) + \frac{1}{2} D_{KL}(P_{t+1} || M), \quad M = \frac{1}{2}(P_t + P_{t+1})
$$

此公式量化相邻时间步概率分布的差异，JSD 谷底标志着语义锚定的完成，为后续残差信号提取提供时间边界。

### 置信度加权残差融合

在确定历史窗口后，ResDec 计算每个历史时间步 $i$ 的置信度 $C_i$，基于 token 分布熵衡量其确定性。高置信度时间步对当前解码的指导价值更高。历史残差信号 $\hat{y}_{res}$ 通过置信度加权聚合历史 logits 得到，并与当前解码 logits 融合。

$$
\text{logit}_{final} = (1-\alpha) \cdot \text{logit}_{current} + \alpha \cdot \text{logit}_{res}, \quad \text{logit}_{res} = \sum_{i \in \Delta_t} C_i \cdot \text{logit}_i
$$

其中 $\alpha \in [0,1]$ 平衡当前与历史信号权重。该设计解决了 VCD 中全局对比信号在特定样本上可能过度校正或不足的问题，通过实例自适应的置信度加权，实现细粒度的视觉接地增强，同时保持单次前向传播的低开销特性。

## 实验评估

ResDec 在 LLaVA-1.5、InstructBLIP 和 Qwen2.5-VL 三个骨干上，于 POPE、CHAIR、MME 等 11 个基准上进行评估。基线覆盖 VCD、OPERA、ICD、DoLa 等主流解码策略，但缺失 HulluEdit 等表征编辑类方法。在 POPE Random 设置下，ResDec 在 Qwen2.5-VL 上取得 89.83% 准确率，接近 HDD 的 90.1%；在 CHAIRs 指标上，LLaVA-1.5 的 ResDec 值为 12.7，显著优于 VCD 的 43.5，表明其在自由形式描述中能有效抑制幻觉。

| 模型 | 方法 | POPE Random Acc (%) | CHAIRs |
| :--- | :--- | :--- | :--- |
| Qwen2.5-VL | ResDec | 89.83 | - |
| Qwen2.5-VL | VCD | 88.0 | - |
| LLaVA-1.5 | ResDec | - | 12.7 |
| LLaVA-1.5 | VCD | - | 43.5 |

消融实验显示，候选 token 池大小在 64-512 之间性能最佳，过小导致 JSD 定位不准，过大则引入噪声。超参数 $\alpha$ 在 0.5 时表现最优，过高（如 1.0）会导致性能下降，表明历史信号与当前信号的平衡至关重要。ResDec 在不同解码策略（贪心、Top-K、Nucleus）下均有效，验证了其鲁棒性。

评估边界方面，ResDec 未报告置信区间，数值比较需谨慎。其 JSD 分析基于静态图像，未涉及视频时序幻觉。代码未公开，但超参数 $\alpha=0.5, \beta=0.1$ 已明确，复现性中等。

## 关联研究分析

从方法设计看，ResDec 与 RUDDER 同属零成本解码策略，但 RUDDER 注入隐状态，ResDec 融合 Logits。RUDDER 依赖残差流特性，ResDec 依赖 JSD 时序规律。ResDec 的优势在于无需校准数据，且对上下文具有特异性；RUDDER 的优势在于直接修改隐状态，可能更精准。两者在计算效率上形成竞争，ResDec 的 JSD 计算开销极低，但依赖历史 logits 的稳定性。

从问题动机看，ResDec 与 HTDC 均针对解码过程中的不稳定步骤进行干预。HTDC 通过识别“犹豫”信号触发校准，ResDec 通过 JSD 谷底定位语义锚定阶段。HTDC 的干预时机基于层级犹豫，ResDec 基于分布稳定性。ResDec 的 JSD 分析提供了更细粒度的时序定位，但 HTDC 的犹豫信号可能更直接反映接地不稳定。两者在干预精度与计算开销间的取舍不同，ResDec 更侧重全局稳定性，HTDC 更侧重局部不稳定。

## 总结

ResDec 旨在解决推理时干预中计算开销大与幻觉抑制效果之间的矛盾。其切入点在于发现 LVLM 解码前已隐含地预知部分未来输出，即正确答案信号嵌入历史 logits 中。通过 JSD 定位语义锚定阶段并置信度加权融合历史残差信号，ResDec 实现了单次前向传播的零成本幻觉抑制。实验表明，其在 POPE Random 上达 89.83%，CHAIRs 上 LLaVA-1.5 为 12.7，显著优于 VCD 基线。然而，其 JSD U 型曲线的普适性依赖特定骨干架构，且在长序列生成后期，历史 logits 的视觉接地能力是否衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01047)