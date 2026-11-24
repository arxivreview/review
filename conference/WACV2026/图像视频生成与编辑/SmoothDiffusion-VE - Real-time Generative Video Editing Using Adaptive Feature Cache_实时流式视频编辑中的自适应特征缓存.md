# WACV2026最新论文 ｜SmoothDiffusion-VE: Real-time Generative Video Editing Using Adaptive Feature Cache ｜实时流式视频编辑中的自适应特征缓存

研究机构：美国德克萨斯大学奥斯汀分校

作者：Mustafa Munir、Sophia Zalewski、Shiqiu Liu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77732c41922d)

> 实时视频编辑面临因果性约束与时间一致性的根本矛盾：流式处理仅能访问历史帧，而离线方法依赖全视频预处理。现有流式方法如 StreamV2V 虽引入特征库，但固定大小与 Token Merging 导致信息丢失与延迟累积。本文通过基于感知相似度的自适应特征缓存（AFC）与运动引导注意力，在保持因果性的同时提升帧间连贯性。该方法在 RTX 4090 上实现 27.8 FPS，较 PNP 加速 1564 倍，但在复杂动态场景下的鲁棒性仍存疑。

## 研究背景

视频编辑的核心挑战在于平衡语义修改与结构保持，而实时场景进一步引入了因果性约束。传统扩散模型如 PNP 和 DMT 依赖 DDIM 反转对全视频进行预处理，导致无法处理实时流数据，且处理速度极慢（0.014-0.018 FPS）。为突破此瓶颈，流式方法如 StreamDiffusion 和 StreamV2V 采用逐帧批处理去噪，仅依赖历史帧信息。然而，StreamV2V 使用的固定大小特征库与 Token Merging 机制存在固有缺陷：前者限制了时间视野，后者在合并过程中丢失早期帧细节，导致长序列编辑中出现闪烁与一致性漂移。

本文切入点在于解决流式编辑中“计算效率”与“时间一致性”的权衡问题。现有方法要么牺牲一致性追求速度（如 StreamDiffusion），要么牺牲速度追求一致性（如 StreamV2V）。SmoothDiffusion-VE 提出动态调整缓存策略，根据帧间感知相似度自适应选择缓存深度，并结合光流引导的稀疏注意力，旨在以接近实时的速度实现接近离线方法的时间稳定性。

## 核心方法

### 方法参照系

本文基于预训练 Stable Diffusion（U-Net 架构）与 SDEdit 框架，采用 Stream Batch 逐帧去噪流程。与标准流式方法的关键差异在于：不将自注意力扩展为跨帧注意力（需全视频处理），而是通过缓存历史帧的键值对（K/V）来模拟长程依赖，从而在因果约束下实现时间一致性。

### 自适应特征缓存（AFC）

AFC 的核心创新在于动态调整缓存深度以平衡计算负载与时间连贯性。传统方法如 StreamV2V 使用固定大小特征库，导致在场景剧烈变化时信息不足，或在静态场景中计算冗余。本文引入 LPIPS 度量当前帧 $x_i$ 与历史帧 $x_{i-N}$ 的感知差异 $\Delta_i$：

$$ \Delta_i = \text{LPIPS}(x_i, x_{i-N}) $$

若 $\Delta_i < \delta_{\text{lpips}}$，系统切换至 mini-cache 模式（默认缓存 2 帧），降低计算开销；若 $\Delta_i \ge \delta_{\text{lpips}}$，切换至 extended-cache 模式（默认缓存 8 帧），保留更多历史上下文。此机制解决了固定缓存策略在动态场景下的一致性失效问题，使模型能根据视频内容自适应分配计算资源。

### 运动引导注意力（MGA）

MGA 针对静态区域计算冗余的问题，利用光流场 $F_i$ 生成二值运动掩码 $M_i$：

$$ M_i(u, v) = \begin{cases} 1 & \text{if } \text{mag}(u, v) > \tau \\ 0 & \text{otherwise} \end{cases} $$

其中 $\text{mag}(u, v) = \sqrt{dx(u, v)^2 + dy(u, v)^2}$。通过构建复合帧 $X_c = M_i \odot X + (1 - M_i) \odot B$，其中 $B$ 为静态背景缓冲区，自注意力仅在动态区域 $M_i=1$ 处计算。这一设计避免了在静态背景上重复计算注意力，显著降低了延迟，同时通过复用稳定背景特征防止了静态区域的闪烁累积。

## 实验评估

| 方法 | CLIP Score ↑ | Warp Error ↓ | Latency (ms/frame) ↓ | FPS |
| :--- | :--- | :--- | :--- | :--- |
| SmoothDiffusion-VE | 97.8 | 88.1 | 36.0 | 27.8 |
| StreamV2V | - | - | 117.5 | 8.5 |
| StreamDiffusion | - | - | 72.5 | 13.8 |
| PNP | - | - | 56306 | 0.018 |
| DMT | - | - | 68977 | 0.014 |

实验在 DAVIS 和 LongVideoBench 数据集上进行，对比了 StreamDiffusion、StreamV2V、PNP、DMT 及 T2V-Zero。SmoothDiffusion-VE 在 CLIP Score（97.8）与 Warp Error（88.1）上均优于流式基线，且延迟仅为 StreamV2V 的 30%。值得注意的是，本文未对比最新的 DiT 架构实时方法（如 SANA-Streaming），这可能限制了其在当前 SOTA 格局中的定位准确性。

| 配置 | CLIP Score ↑ | Warp Error ↓ | Latency (ms/frame) ↓ |
| :--- | :--- | :--- | :--- |
| Full Model | 98.1 | 88.1 | 34.3 |
| w/o Temporal Embedding | 97.7 | 92.3 | 34.4 |
| w/o AFC | 97.3 | 99.0 | 55.2 |
| w/o Interpolation | 97.3 | 99.2 | 55.2 |

消融实验显示，移除 AFC 导致 Warp Error 从 88.1 升至 99.0，验证了动态缓存对时间一致性的关键作用。移除时间嵌入（Temporal Embedding）仅轻微影响 CLIP Score，但显著增加延迟，表明其主要用于优化计算效率而非直接提升语义对齐。帧插值（FHB）通过跳过部分帧的扩散编辑，将延迟从 55.2 ms 降至 34.3 ms，对质量影响可忽略。

评估指标主要依赖 CLIP Score 与 Warp Error，缺乏对细粒度编辑精度（如 FiVE-Bench 中的 SC/BC 指标）的评估。实验仅在 512×512 分辨率下验证，未测试高分辨率下的性能衰减。代码未公开，超参数 $\delta_{\text{lpips}}$ 与 $\tau$ 的敏感性分析缺失，限制了可复现性。

## 关联研究分析

从方法设计看，SmoothDiffusion-VE 与 StreamV2V 的核心差异在于特征存储策略。StreamV2V 依赖 Token Merging 压缩历史帧信息，导致早期帧细节丢失，尤其在长序列中累积误差明显。本文的 AFC 通过动态调整缓存深度，避免了强制合并带来的信息损失，但代价是内存占用随缓存深度增加而线性增长。这种设计在静态场景下效率极高，但在高频动态场景中，extended-cache 模式可能仍不足以覆盖足够长的时间窗口，导致一致性下降。

从问题动机看，本文与 TokenFlow 同属免训练路线，但目标不同。TokenFlow 聚焦于离线编辑中的时间闪烁问题，通过最近邻 Token 传播实现全局一致性，但计算复杂度随帧数二次方增长，无法实时运行。SmoothDiffusion-VE 牺牲了全局视野，换取因果性下的实时性，其 AFC 机制本质上是一种局部近似的全局一致性策略。这种取舍使得本文在实时场景下具有优势，但在需要长程语义一致性的复杂编辑任务中，可能不如离线方法稳健。

## 总结

SmoothDiffusion-VE 旨在解决实时视频编辑中因果性约束与时间一致性的矛盾，通过自适应特征缓存与运动引导注意力，在流式处理中实现了接近离线方法的时间稳定性。实验表明，该方法在 RTX 4090 上达到 27.8 FPS，Warp Error 降至 88.1，较 PNP 加速 1564 倍。然而，其依赖 U-Net 架构与固定分辨率，且在高频动态场景下的缓存深度是否足够维持长程一致性，论文未提供充分验证。当视频包含快速场景切换时，AFC 的 extended-cache 模式能否有效防止一致性漂移，仍是该方法的潜在边界。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_77732c41922d)