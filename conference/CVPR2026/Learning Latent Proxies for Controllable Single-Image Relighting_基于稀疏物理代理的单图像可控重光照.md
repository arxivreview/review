# CVPR2026最新论文 ｜Learning Latent Proxies for Controllable Single-Image Relighting ｜基于稀疏物理代理的单图像可控重光照

研究机构：香港中文大学

作者：Haoze Zheng、Zihao Wang、Xianfeng Wu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.15555)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15555)

> 单图像重光照旨在改变照明条件同时保持几何与材质不变，但逆渲染的病态性导致纯生成模型易产生几何幻觉，而传统物理分解方法依赖昂贵的密集监督。现有扩散模型方案在精细控制方向、强度与色温时缺乏物理约束，导致外观漂移。LightCtrl 通过引入少样本潜在代理编码器、光照感知掩码及DPO后训练，以稀疏物理线索引导扩散去噪过程。该方法在物体级基准上实现了SOTA性能，但在复杂场景泛化上仍落后于最新SOTA，其“稀疏代理足够”的假设在极端光照下的鲁棒性存疑。

## 研究背景

单图像重光照的核心困境在于从单一RGB输入中恢复不可观测的几何与材质属性。这一病态性意味着光照方向的微小变化会引发阴影、高光及漫反射的非线性剧烈变化。为约束这种不确定性，传统方法依赖逆渲染（Inverse Rendering）显式分解反照率、法线与光照，但该方法需要密集的G-buffer监督，且在高频细节上易失效。与此同时，基于扩散模型（Diffusion Models）的生成式方法虽具备强大的视觉先验，却因缺乏物理结构约束，常出现表面颜色漂移或几何结构幻觉，难以实现光源方向、强度及色温的精确连续控制。

主流路线在物理一致性与生成质量间存在显著张力。IC-Light等纯数据驱动方法在肖像重光照中表现良好，但泛化至复杂场景时物理建模不足；Neural LightRig等物理引导方法虽引入多阶段G-buffer管道，但依赖昂贵的密集PBR监督，扩展性差。LightCtrl的切入点在于识别出“全量内在分解并非精确重光照的必要条件”。其核心假设是：稀疏且空间定位的物理线索（如局部反照率与法线）足以约束扩散模型的去噪轨迹，从而在避免密集监督成本的同时，保留物理一致性所需的结构信息。

## 核心方法

### 方法参照系

LightCtrl属于图像重光照生成中的物理引导子路线。与标准流程依赖完整G-buffer或环境图作为条件不同，本文采用“源图像+参考图像相对光照差”作为输入，旨在通过轻量级物理代理替代全量内在分解，解决纯潜在空间扩散缺乏物理 grounding 的问题。

### 少样本潜在代理编码

针对扩散模型在大幅光照变化下易改变几何与材质的失效，LightCtrl引入轻量级编码器-解码器 $E_\phi$，从源图像预测紧凑的潜在代理 $\hat{B} = \{a, n, r, m\} \in \mathbb{R}^{H \times W \times 8}$，包含反照率、法线、粗糙度与金属度。该代理仅在训练子集上使用PBR监督，通过以下损失稳定学习：

$$ \mathcal{L}_{proxy} = \lambda_1 \mathcal{L}_{albedo} + \lambda_2 \mathcal{L}_{normal} + \lambda_3 \mathcal{L}_{metal} $$

此公式通过正则化项捕捉反照率平滑性、法线单位向量一致性及金属度二值特性。代理特征经空间池化投影为单一条件token $t_{phys}$，注入去噪器。这一设计以极低的标注成本提供了材质-几何先验，约束去噪轨迹，避免了全量内在分解的过拟合风险。

### 光照感知掩码与DPO后训练

为解决扩散模型将编辑扩散至全图导致不变区域失稳的问题，LightCtrl引入光照感知掩码。基于源-目标对的线性亮度差异计算软掩码 $M_{gt}$，训练轻量预测器 $m_\theta$ 从源外观与相对光照编码推断该掩码：

$$ \hat{M} = m_\theta(x_s, \Delta_l) $$

该掩码转化为空间权重图 $W$，调制噪声重建损失，引导去噪器聚焦光照敏感区域。此外，针对稀疏PBR监督下编码器可靠性不足的问题，采用DPO（Direct Preference Optimization）后训练。以GT PBR图为正样本，当前编码器输出为负样本，计算基于物理的奖励差并优化编码器，冻结主骨干。此步骤显著提升了稀疏监督下物理线索的稳定性，抑制了反照率与法线预测中的伪影。

## 实验评估

LightCtrl在自建ScaLight数据集（300K+物体，1M+图像）及MIIW场景级基准上评估。基线覆盖IC-Light、LumiNet、RGB↔X等主流方法，但缺失TokenLight、PI-Light等2026年最新SOTA对比。在ScaLight物体级测试中，LightCtrl（Full）在色温、位置、能量变化下均取得最优PSNR，其中色温变化下PSNR达30.2 dB，显著优于LumiNet的15.8 dB。在MIIW场景级测试中，LightCtrl PSNR为18.30 dB，高于IC-Light的7.94 dB，但低于LumiNet的17.20 dB（注：此处原文数据LumiNet PSNR 17.20低于LightCtrl 18.30，但SSIM更高，原文指出SSIM反映感知-失真权衡，LightCtrl因生成锐利阴影导致SSIM较低但PSNR更高）。

| Method | Temperature PSNR (dB) | Position PSNR (dB) | Energy PSNR (dB) | MIIW PSNR (dB) |
|---|---|---|---|---|
| IC-Light | 8.21 | 8.65 | 8.63 | 7.94 |
| LumiNet | 15.8 | 17.8 | 16.2 | 17.20 |
| LightCtrl (Full) | 30.2 | 25.6 | 27.1 | 18.30 |

消融实验显示，移除DPO后训练导致性能损失最大，PSNR下降显著，证实DPO对稳定稀疏监督下物理线索的关键作用。移除潜在代理后，色温与强度变化下的RMSE增加，表明代理提供了必要的材质-几何约束。移除掩码后，模型过度编辑不变区域，导致反照率平滑化与阴影边界弱化。用户偏好研究显示，LightCtrl在物体级（81.45%）与场景级（55.73%）均获最高偏好率，验证了其视觉真实感优势。

评估边界方面，ScaLight为合成数据，虽提供精确光照元数据，但缺乏真实世界复杂光照的多样性；MIIW测试中PSNR低于领域SOTA（如Dior的24.10 dB），暗示场景级泛化能力有限。论文未提供代码与超参数细节，可复现性受限。

## 关联研究分析

从问题动机看，LightCtrl与PI-Light（Liang et al., 2026）均强调物理一致性，但PI-Light依赖两阶段全图像内在分解，需高质量合成数据训练，而LightCtrl主张稀疏代理足够，降低了数据依赖。这一差异源于任务特性：PI-Light面向全图像重光照，需处理背景复杂光照；LightCtrl聚焦物体级精细控制，稀疏线索足以约束局部材质。LightCtrl在MIIW上的PSNR（18.30 dB）低于PI-Light（21.92 dB），暗示稀疏代理在复杂场景全局光照传输中可能不足。

从方法设计看，LightCtrl与TokenLight（Chaturvedi et al., 2026）同属参数化控制路线，但TokenLight将光源属性编码为离散Token，通过交叉注意力实现全局控制；LightCtrl则通过相对光照差 $\Delta_l$ 与稀疏代理实现连续物理引导。TokenLight侧重光源属性的精确编辑，LightCtrl侧重材质-几何保持。LightCtrl在ScaLight上的PSNR（30.2 dB）远高于TokenLight在Indoor基准的PSNR（23.50 dB），但两者评估协议不同，直接对比需谨慎。LightCtrl未探索视频序列的时间一致性，其稀疏代理在动态场景中的稳定性未经验证。

## 总结

LightCtrl旨在解决单图像重光照中物理一致性与精细控制的矛盾，抓住“稀疏物理线索足以约束扩散模型”这一被忽略的点，通过少样本潜在代理、光照感知掩码及DPO后训练实现轻量级物理引导。实验证明其在物体级基准上PSNR达30.2 dB，用户偏好率81.45%，显著优于IC-Light等基线。然而，其在MIIW场景级PSNR仅18.30 dB，低于领域SOTA，暴露了稀疏代理在复杂场景全局光照传输中的局限。当场景包含复杂遮挡与间接光照时，稀疏代理是否足以替代全量内在分解，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15555)