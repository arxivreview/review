# CVPR2026 · RAW图像信号处理与增强方向论文汇编

> 本方向共 6 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Edit-aware RAW Reconstruction ｜编辑感知RAW重构

作者：Abhijith Punnappurath、Luxi Zhao、Ke Zhao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.05859)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.05859)

> 消费级摄影中，用户常需对相机输出的sRGB图像进行后期编辑，但直接编辑压缩后的sRGB会损失动态范围与色彩精度，因此需要从sRGB逆向恢复RAW数据以支持高质量编辑。现有RAW重构方法仅优化像素级RAW保真度，导致重建的RAW在应用不同曝光、白平衡或色调编辑时，sRGB渲染结果与真实RAW渲染存在显著偏差。本文提出一种即插即用的编辑感知损失，通过可微分ISP模拟多样化编辑参数，在sRGB空间计算渲染误差以指导RAW重构。该方法在多种基线模型上提升了编辑后的sRGB重建质量，但牺牲了少量RAW空间保真度，且未验证跨传感器泛化能力。

】

---

【Linear Image Generation by Synthesizing Exposure Brackets ｜基于曝光括号合成的线性图像生成

研究机构：新加坡南洋理工大学、Adobe研究院

作者：Yuekun Dai、Zhoutong Zhang、Shangchen Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21008)

> 现有文本到图像生成模型仅能输出显示参考（display-referred）的sRGB图像，其动态范围受限且无法支持无损后期编辑，导致专业摄影工作流中必须经历有损转换。本文切入点在于利用曝光括号分解高动态范围，规避预训练变分自编码器（VAE）对极端亮暗细节的压缩瓶颈。通过构建基于流匹配（Flow Matching）的扩散架构，联合生成多曝光帧与辐射度尺度，实现场景参考（scene-referred）线性图像的直接合成。该方法在FID指标上优于直接微调基线，但缺乏对辐射度保真度的定量验证，且未解决跨传感器噪声建模问题。

】

---

【MERIT: Multi-domain Efficient RAW Image Translation ｜多域高效RAW图像翻译

研究机构：美国加州大学尔湾分校、美国宾夕法尼亚大学

作者：Wenjun Huang、Shenghao Fu、Yian Jin 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20836)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20836)

> 导读 多域RAW图像翻译旨在解决不同相机传感器间因光谱响应与噪声特性差异导致的域偏移问题，使单一模型能复用下游视觉任务。现有方法局限于一对一映射，无法扩展至多相机场景，本文切入点为构建统一的多域翻译框架。通过引入显式噪声建模与多尺度大核注意力，实现任意域间的高效转换。该框架在质量与可扩展性上取得突破，但缺乏下游任务性能验证，其实际效用仍存疑。

】

---

【RawMetaDiff: Unlocking Extreme Darkness from Dual-Exposure RAW with Meta-Guided Diffusion ｜元数据引导的双曝光RAW恢复

研究机构：中国科学技术大学

作者：Panjun Liu、Jiyuan Xia、Yuanshen Guan 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77aa42dfc60c)

> 极端低光下，单帧RAW图像因噪声与传感器截断导致信号不可逆丢失，恢复问题本质上是病态的。现有双曝光融合方法依赖显式像素对齐，在大曝光差与运动模糊下极易失效，导致细节注入错误与色彩偏移。本文提出RawMetaDiff，将双曝光恢复重构为条件生成问题，利用RAW元数据引导扩散模型进行全局颜色转移与阴影细节注入。该方法在合成与真实数据上均取得SOTA性能，但其一步扩散范式在极端低光下的细节保真度与多步采样方法的权衡尚存疑。

】

---

【SpiralDiff: Spiral Diffusion with LoRA for RGB-to-RAW Conversion Across Cameras ｜信号依赖扩散与相机适配的RGB-to-RAW转换

研究机构：天津大学

作者：Huanjing Yue、Shangbin Xie、Cong Cao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14885)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.14885)

> RGB-to-RAW转换旨在从海量RGB数据逆向合成RAW图像，以突破传感器特定数据集规模与多样性不足的瓶颈。现有生成式方法采用各向同性噪声，忽略了重建难度随像素强度变化的物理特性，且多相机联合训练导致ISP特征混淆。本文提出SpiralDiff，通过引入信号依赖噪声权重图与相机感知LoRA模块，实现强度自适应重建与跨相机统一建模。该方法在四个基准上刷新了转换质量记录，但其对真实ISP非线性响应的泛化边界仍存疑。

】

---

【Task-Aware Image Signal Processor for Advanced Visual Perception ｜任务感知图像信号处理器

研究机构：电子科技大学

作者：Kai Chen、Jin Xiao、Leheng Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.13762)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13762)

> 现有RAW域视觉感知方法面临计算开销与表征能力不可兼得的困境：重型ISP网络难以部署，轻量参数调优又无法捕捉空间变化。本文提出TA-ISP，通过全局、区域、像素三级调制算子替代密集卷积，在保持极低参数量与推理延迟的同时提升下游任务精度。该方法在多个基准上验证了有效性，但其调制算子能否替代卷积的非线性拟合能力，以及在极端低光下的鲁棒性，仍存疑。

】
