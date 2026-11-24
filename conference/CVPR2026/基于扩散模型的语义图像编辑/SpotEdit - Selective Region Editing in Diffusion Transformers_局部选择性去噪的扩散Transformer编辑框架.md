# CVPR2026最新论文 ｜SpotEdit: Selective Region Editing in Diffusion Transformers ｜局部选择性去噪的扩散Transformer编辑框架

研究机构：新加坡国立大学、上海交通大学

作者：Zhibin Qin、Zhenxiong Tan、Zeqing Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.22323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.22323)

> 扩散Transformer（DiT）在图像编辑中面临全局去噪导致的计算冗余与非编辑区域潜在畸变问题。现有加速方法多采用全Token特征复用，未能区分语义上需要修改与保持的区域，导致效率与保真度难以兼得。SpotEdit通过感知相似度动态识别稳定区域并跳过其计算，同时利用动态KV融合维持上下文一致性，实现了免训练的区域选择性编辑。该方法在保持编辑质量接近原模型的前提下实现了显著加速，但其对跨区域长距离依赖的处理能力及阈值敏感性仍需进一步验证。

## 研究背景

当指令要求仅修改图像中的局部对象时，DiT模型仍需在每个时间步对所有潜变量Token执行去噪运算。这种全局处理范式源于整流流（Rectified Flow, RF）中线性插值路径的特性，即瞬时速度场 $u_t \equiv X_1 - X_0$ 是全局定义的，导致模型无法在计算层面区分“需重构”与“需保持”的区域。然而，观察去噪过程发现，非编辑区域的潜变量在早期时间步即迅速收敛至与条件图像一致的稳定状态，而编辑区域则持续演化直至最终步。这一时间收敛性的异质性，构成了局部选择性计算的理论基础。

当前主流编辑范式如FLUX.1 Kontext和Qwen-Image-Edit，均采用将条件图像编码后直接注入Transformer层的方式，虽免除了手动掩码输入，但本质上仍是全图重生成。现有加速技术如TeaCache和TaylorSeer，通过跨时间步复用中间特征来降低计算量，但它们将图像视为均匀整体，未利用编辑任务中“仅少数Token需变更”的稀疏性。这种全Token加速策略在编辑任务中往往以牺牲非编辑区域的保真度为代价，导致背景出现细微伪影或语义漂移。SpotEdit的切入点在于，利用RF的闭式重构特性，在去噪早期动态识别已稳定的非编辑Token，将其从DiT计算中剥离，仅对编辑区域执行完整去噪，从而在根源上消除冗余计算并抑制背景畸变。

## 核心方法

### 方法参照系

SpotEdit基于RF框架下的DiT编辑流程，其标准流程为：从噪声 $X_1$ 出发，通过迭代积分速度场 $v_\theta(X_t, C, t)$ 逐步去噪至 $X_0$。本文的关键差异在于，该流程不再对所有Token统一执行去噪，而是引入动态路由机制，将Token分为“再生成集”与“非编辑集”，仅对前者执行DiT前向传播，后者直接复用条件图像特征。

### SpotSelector：基于感知相似度的区域路由

SpotSelector解决的核心问题是：如何在不依赖外部掩码的情况下，准确识别非编辑区域。传统方法依赖二值掩码或注意力权重阈值，但潜空间距离与人类感知差异存在偏差。SpotSelector利用RF的线性插值特性，在时间步 $t$ 通过闭式解重构完全去噪潜变量 $\hat{X}_0 = X_t - t v_\theta(X_t, C, t)$，并解码为图像。通过计算重构图像与条件图像在VAE解码器各层特征上的LPIPS-like感知距离，定义Token $i$ 的感知偏差为：

$$
d_i = \sum_l w_l \left\| \hat{\phi}_l(\hat{X}_0)_i - \hat{\phi}_l(Y)_i \right\|_2
$$

其中 $\phi_l$ 为解码器第 $l$ 层特征，$w_l$ 为层权重，$Y$ 为条件图像潜变量。当 $d_i < \tau$ 时，Token被路由至非编辑集 $R_t$，否则进入再生成集 $A_t$。该机制将区域识别与模型自身的去噪动力学对齐，避免了静态掩码的局限性，确保识别出的稳定区域与模型生成过程一致。

### SpotFusion：动态KV融合与部分注意力

SpotSelector将非编辑Token从DiT计算中移除后，导致再生成Token失去来自非编辑区域的上下文注意力信号，引发编辑质量下降。静态KV缓存虽可复用特征，但缓存的特征冻结于特定时间步，与持续演化的再生成Token特征产生时间漂移。SpotFusion通过动态插值解决此问题：在初始步后缓存非编辑Token与条件图像Token的KV对，并在每个时间步 $t$ 对非编辑Token的隐藏状态进行插值更新：

$$
\tilde{h}_{[x_{b,t+1}]} = (1 - \alpha(t)) h_{[x_{b,t+1}]} + \alpha(t) h_{[y_b]}
$$

其中 $\alpha(t) = \cos^2(\frac{\pi t}{2})$ 随去噪进程从0平滑过渡到1，使特征从缓存状态逐渐转向参考图像状态。该插值应用于KV对，确保非编辑区域特征在时间维度上与条件图像对齐。在注意力计算中，Query仅包含再生成Token与指令Token，而Key-Value则拼接缓存的非编辑与条件图像特征，实现部分注意力计算。这一设计既保留了全局上下文一致性，又避免了非编辑区域的冗余计算，解决了静态缓存导致的时间不匹配问题。

## 实验评估

实验在imgEdit-Benchmark和PIE-Bench++上进行，基线包括缓存加速方法（TeaCache, TaylorSeer）和精确编辑方法（FollowYourShape）。值得注意的是，基线未包含FlowEdit、CVC等无反转范式SOTA方法，这限制了加速比与编辑质量的全面对比。

| 方法 | imgEdit VL Score | PIE-Bench++ PSNR | PIE-Bench++ SSIM | 加速比 |
| :--- | :--- | :--- | :--- | :--- |
| Original Inference | 3.91 | 18.76 | 0.791 | 1.00× |
| TaylorSeer | 3.65 | - | - | 3.61× |
| FollowYourShape | 3.55 | - | - | - |
| SpotEdit | 3.77 | 18.73 | 0.792 | 1.95× |

SpotEdit在imgEdit上VL Score为3.77，仅比原模型低0.14，优于TaylorSeer（3.65）和FollowYourShape（3.55）；在PIE-Bench++上PSNR为18.73，SSIM为0.792，与原模型（18.76, 0.791）基本持平，同时实现1.95×加速。消融实验显示，引入Reset机制后PSNR下降1.6 dB，DISTS增加0.018，表明缓存误差累积会显著影响质量，周期性重置是必要的稳定性保障。

评估协议采用CLIP、PSNR、SSIM、DISTS及VL Score，但未报告置信区间，且仅在1024×1024分辨率下测试。代码未开源，超参数（如 $\tau=0.2$）固定，缺乏对阈值敏感性的系统分析。

## 关联研究分析

从问题动机看，SpotEdit与RegionE、UltraDiffEdit同属高效推理加速路线，但二者针对高分辨率下的显存瓶颈，采用分块局部采样策略，而SpotEdit聚焦于局部编辑中的计算冗余，通过Token级路由实现加速。RegionE依赖区域划分与缓存机制，需预定义或动态划分区域，而SpotEdit通过感知相似度自动识别，无需手动掩码。这一差异源于任务特性：RegionE处理的是全局高分辨率图像，区域划分是空间维度的优化；SpotEdit处理的是局部编辑任务，区域识别是语义维度的优化。SpotEdit的自动识别机制在编辑区域边界模糊时可能不如显式掩码精确，但其在免掩码场景下的实用性更强。

从方法设计看，SpotEdit与FlowEdit、CVC等无反转范式存在竞争关系。FlowEdit通过速度场差异引导生成，避免反转误差，但仍是全图去噪；SpotEdit在FLUX.1 Kontext等DiT模型上实现区域选择性去噪，二者可视为互补：FlowEdit优化去噪轨迹，SpotEdit优化计算范围。然而，SpotEdit未与FlowEdit直接对比，无法证明其在编辑质量上优于无反转范式。此外，SpotEdit的SpotFusion机制与FusionEdit的自适应软掩码生成有相似之处，但FusionEdit依赖距离感知的潜变量融合，而SpotEdit基于KV插值，后者在时间一致性上更具优势，但可能牺牲空间精度的细粒度控制。

## 总结

SpotEdit针对DiT编辑中全局去噪导致的计算冗余与背景畸变矛盾，利用RF的早期收敛特性，通过SpotSelector动态识别稳定区域并跳过其计算，结合SpotFusion动态KV融合维持上下文一致性，实现了免训练的区域选择性编辑。实验表明，该方法在保持编辑质量接近原模型（PSNR 18.73, SSIM 0.792）的前提下，实现了1.95×加速，优于全Token加速方法。其边界在于，实验未覆盖FlowEdit等无反转SOTA基线，且仅在1024×1024分辨率下验证，缺乏对高分辨率及复杂跨区域依赖场景的测试。当编辑指令涉及多个分散对象或长距离语义关联时，SpotSelector的局部感知距离是否足以捕捉全局一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.22323)