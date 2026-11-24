# ICLR2026 · 稠密三维重建与SLAM方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ARTDECO: TOWARDS EFFICIENT AND HIGH - FIDELITY ON THE-FLY 3D RECONSTRUCTION WITH STRUCTURED SCENE REPRESENTATION ｜ARTDECO：基于结构化高斯表示的实时单目三维重建

研究机构：复旦大学、上海交通大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_36015940)

> 导读 单目三维重建旨在从无序图像序列中恢复度量一致的几何结构与相机位姿，以支撑具身智能与增强现实应用。现有方法在离线高精度与在线实时性之间难以兼顾：逐场景优化方法依赖脆弱的运动恢复结构（Structure from Motion, SfM）流程，而前馈基础模型虽具备鲁棒性却缺乏全局一致性。ARTDECO 通过整合前馈先验与轻量级后端优化，并引入层级半隐式高斯表示，在单一管线中平衡了精度、速度与鲁棒性。该框架在渲染质量上接近逐场景优化水平，但在动态场景处理与极端视角变化下的稳定性仍存疑。

】

---

【SKYEVENTS: A LARGE-SCALE EVENT ENHANCED UAV DATASET FOR ROBUST 3D SCENE RECONSTRUCTION ｜大规模无人机事件增强三维重建数据集

研究机构：香港科技大学、香港中文大学

作者：Wenzong Ma、Zhuoxiao Li、Jinjing Zhu 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_2681429)

> 大规模无人机三维重建长期受限于传统RGB相机在低光与运动模糊下的成像失效，导致城市级场景重建保真度不足。现有事件相机数据集缺乏同步RGB、稠密深度与6-DoF位姿，无法支撑神经渲染基准。本文构建了首个专为事件增强无人机三维重建设计的数据集SkyEvents，并配套提出时间对齐模块与区域事件渲染损失。该工作填补了数据空白并验证了事件模态的有效性，但低光场景采用合成退化策略，限制了真实泛化能力的评估。

】

---

【WinT3R: Window-Based Streaming Reconstruction with Camera Token Pool ｜滑动窗口与相机令牌池的流式三维重建

研究机构：中国科学技术大学、浙江大学

作者：Zizun Li、Jianjun Zhou、Yifan Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.05296)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.05296)

> 流式三维重建需在恒定内存下实时恢复几何与位姿，但离线全局注意力方法因计算复杂度随帧数平方增长而无法在线运行，现有递归状态模型又因帧间信息仅通过状态令牌间接传递导致重建质量受限。WinT3R 通过滑动窗口机制让相邻帧图像令牌直接交互，并引入紧凑相机令牌池实现全局视角位姿估计，在 17.2 FPS 下取得在线重建 SOTA。该方法在实时性与质量间取得了当前最优平衡，但其对超长序列中相机令牌池扩展性的影响尚未被充分验证。

】
