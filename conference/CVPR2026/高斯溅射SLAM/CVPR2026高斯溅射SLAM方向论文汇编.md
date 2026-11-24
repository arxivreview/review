# CVPR2026 · 高斯溅射SLAM方向论文汇编

> 本方向共 8 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM ｜自动曝光鲁棒的高斯泼溅SLAM

研究机构：华南理工大学

作者：Zhiyu Zhou、Feng Hui、Yu Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_17fe11c73229)

> 现有基于3DGS的SLAM系统普遍假设输入图像满足光度一致性，但相机自动曝光（AE）机制在真实场景中引入非平稳的外观变化，导致定位漂移与渲染失真。MonoGS等耦合方法通过可学习曝光参数调整亮度，但无法建模复杂的AE非线性响应；Photo-SLAM等解耦方法依赖手工特征，在光照剧烈变化下匹配失效。本文提出AERGS-SLAM，通过相机曝光网络（CEN）解耦渲染与曝光过程，并结合学习特征实现鲁棒定位。该框架在曝光扰动场景下显著提升了定位精度与渲染质量，但其对动态场景及多相机同步曝光的适用性尚未验证。

】

---

【Flow4DGS-SLAM: Optical Flow-Guided 4D Gaussian Splatting SLAM ｜光流引导的混合4D高斯泼溅SLAM

研究机构：新加坡国立大学

作者：Yunsong Wang、Gim Hee Lee

论文原文见 [arXiv](https://arxiv.org/abs/2604.22339)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.22339)

> 动态场景下的SLAM系统面临静态背景重建与动态物体建模的双重挑战，传统方法要么剔除动态物体导致地图信息缺失，要么依赖昂贵的MLP变形场导致实时性崩溃。Flow4DGS-SLAM通过光流分解相机自运动生成类别无关掩码，并采用显式关键帧位置与GMM参数化混合表示，实现了高效动态重建。该方法在跟踪精度与渲染质量上均优于4DGS-SLAM，但其对预训练光流模型的依赖及长序列累积漂移风险尚未得到充分验证。

】

---

【MAGICIAN: Efficient Long-Term Planning with Imagined Gaussians for Active Mapping ｜基于想象高斯的主动映射长时程规划

研究机构：法国国家科学研究中心

作者：Shiyao Li、Antoine Guédon、Shizhe Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22650)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22650)

> 主动映射旨在解决移动智能体如何移动以最高效地重建未知环境的问题。现有方法多依赖贪心式下一最佳视点选择，导致探索路径短视且全局覆盖不足。本文提出MAGICIAN框架，利用预训练占用网络生成“想象高斯”表示，通过快速体渲染计算覆盖增益，并结合束搜索实现长时程轨迹规划。该框架在室内外基准上显著提升了场景覆盖率，但其性能高度依赖占用网络的先验质量，且未验证在动态或光照剧烈变化场景下的鲁棒性。

】

---

【ODGS-SLAM: Omnidirectional Gaussian Splatting SLAM ｜全向高斯泼溅同步定位与建图

研究机构：奥地利因斯布鲁克大学

作者：Stefan Spiss、Joey Hieronimy、Marcel Ritter 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2adfdc392e21)

> 全向视觉SLAM旨在解决透视相机视场角受限导致的盲区问题，但现有3DGS-SLAM系统均基于针孔模型，无法直接处理全景图像。ODGS-SLAM通过扩展等距圆柱投影下的可微光栅化梯度，首次实现了全向输入下的实时高斯地图构建与位姿估计。该方法利用纬度加权补偿极区畸变，并引入基于旋转不变性的关键帧冗余移除策略以控制内存。其价值在于验证了3DGS在全向场景下的可行性，但极区信息损失对几何精度的长期影响尚存疑。

】

---

【OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting ｜在线开放词汇全景映射

研究机构：浙江大学

作者：Hongjia Zhai、Qi Zhang、Xiaokun Pan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18510)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18510)

> 在线机器人需要在探索未知环境的同时，通过自然语言指令实时定位并区分场景中的具体物体实例。现有方法要么依赖离线预采集数据，要么仅能进行语义分割而无法区分同语义的不同实例，导致无法支撑精细的具身交互。OnlinePG 提出了一种局部到全局的在线建图范式，利用多线索图聚类从噪声2D先验中恢复3D实例一致性，并通过双向二分匹配实现全局地图的鲁棒融合。该方法在在线方法中取得了SOTA性能，但其对动态场景的失效及深度/位姿输入的强依赖，限制了其在复杂真实环境中的泛化能力。

】

---

【Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty ｜基于不确定性感知的3D高斯泼溅位姿细化

研究机构：韩国延世大学

作者：Mangyu Kong、Jaewon Lee、Seongwon Lee 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16538)

> 视觉重定位旨在已知场景中估计查询图像的6自由度相机位姿，传统基于稀疏点云的方法受限于几何表达力，而基于3D高斯泼溅（3DGS）的渲染-比较范式虽提升了精度，却对初始位姿先验与重建几何质量高度敏感。现有确定性细化方法将单一位姿估计与均匀可信的渲染深度作为前提，导致在位姿偏差或几何伪影区域失效。UGS-Loc通过蒙特卡洛采样探索位姿分布，并利用费雪信息量化几何不确定性以引导PnP求解，实现了免训练的鲁棒定位。该方法在多个基准上显著提升了定位精度与稳定性，但其计算开销是否满足严格实时约束仍存疑。

】

---

【SGAD-SLAM: Splatting Gaussians at Adjusted Depth for Better Radiance Fields in RGBD SLAM ｜深度调整深度的像素对齐高斯SLAM

作者：Pengchong Hu、Zhizhong Han

论文原文见 [arXiv](https://arxiv.org/abs/2603.21055)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21055)

> RGBD SLAM在实时性与渲染保真度间长期存在矛盾，全局高斯优化受限于显存，而固定深度高斯又牺牲了新视角合成质量。SGAD-SLAM通过允许像素对齐高斯沿射线自由移动并简化其属性，在局部优化中实现了全局级的渲染效果。该方法结合基于几何分布的GICP跟踪，显著提升了大规模场景下的可扩展性与效率。其核心价值在于以极低的显存开销换取了接近SOTA的渲染精度，但跟踪精度在部分复杂场景下仍略逊于依赖预训练先验的方法。

】

---

【VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM ｜显式外观方差建模的3DGS-SLAM系统

研究机构：美国乔治梅森大学、德国慕尼黑工业大学

作者：Anh Thuan Tran、Jana Kosecka

论文原文见 [arXiv](https://arxiv.org/abs/2603.09673)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09673)

> 3DGS-SLAM在低纹理或反射表面易因光度误差不可靠而漂移，现有方法多依赖几何深度方差或预训练预测器，忽略了渲染本身的不确定性。VarSplat将外观方差作为高斯原语的一等参数，通过全方差定律在光栅化阶段直接渲染逐像素不确定性图，用于跟踪、配准与回环。该方法在ScanNet上取得6.53 cm ATE RMSE，较无不确定性基线降低20.2%，但在TUM-RGBD上精度（3.20 cm）仍低于RGS-SLAM（1.2 cm）。其价值在于首次将渲染不确定性内化为地图属性，但方差冻结策略对动态场景的适应性存疑。

】
