# Others2026 · 机器人、自动驾驶与具身智能方向论文汇编

> 本方向共 6 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Out-of-Sight Embodied Agents: Multimodal Tracking, Sensor Fusion, and Trajectory Forecasting ｜视野外智能体多模态轨迹预测

研究机构：美国东北大学

作者：Haichao Zhang、Yi Xu、Yun Fu

论文原文见 [arXiv](https://arxiv.org/abs/2509.15219)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15219)

> 轨迹预测旨在从历史观测推断智能体未来状态，但现有方法普遍假设视觉观测完整且传感器噪声可忽略，无法处理视野外智能体仅存在噪声定位信号的场景。本文切入点在于利用场景内可见智能体的视觉-传感器对应关系，构建无监督去噪与视觉投影机制，从而在缺乏直接视觉监督的情况下预测视野外智能体的无噪视觉轨迹。该方法通过相机标定建立定位-视觉映射，结合Transformer编码器实现传感器去噪与轨迹预测。其价值在于填补了视觉完全缺失场景下的预测空白，但实验局限于特定数据集且未与主流生成式预测模型对比，泛化能力存疑。

】

---

【事件触发自适应共识多机器人任务分配

作者：Fidel Aznar、Mar Pujol、Álvaro Díez

论文原文见 [arXiv](https://arxiv.org/abs/2604.06813)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06813)

> 多机器人系统在通信受限环境下执行搜索救援任务时，传统共识算法因周期性通信导致带宽饱和与资源浪费。现有方案要么依赖固定调度周期造成冗余交互，要么采用学习策略但缺乏安全关键任务所需的可解释性。本文切入点在于将共识触发机制从时间驱动改为事件驱动，通过行为树识别状态突变并动态调整协调频率。该框架在保持任务完成率与周期性方法相当的同时，将通信开销降低一个数量级，但其有效性仅验证于无物理障碍的仿真环境，真实动态场景下的收敛延迟仍存疑。

】

---

【基于C3k2骨干优化的文本引导无人机小目标检测

作者：Hyun-Ki Jung

论文原文见 [arXiv](https://arxiv.org/abs/2602.19503)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19503)

> 无人机航拍图像中目标像素占比极低，导致深层卷积网络特征迅速退化，而传统固定类别检测器无法响应用户指定的自然语言查询需求。现有YOLO系列架构虽具备实时性，但其骨干网络在保留细粒度空间细节方面存在局限，且缺乏开放词汇能力。本文切入点在于将YOLOv11中的C3k2模块移植至YOLO-World的YOLOv8骨干，以增强小目标特征提取并维持轻量化。该方法在VisDrone数据集上实现了mAP@0.5从30.4%到30.7%的微幅提升，但其性能显著低于专用小目标检测SOTA，且未验证跨域泛化能力，价值在于验证了组件移植的可行性，存疑于其改进幅度是否足以支撑实际部署。

】

---

【波恩团队新研究：扩展潜在三维扩散用于语言条件多任务操作

研究机构：德国波恩大学

作者：Jonas Bode、Raphael Memmesheimer、Sven Behnke

论文原文见 [arXiv](https://arxiv.org/abs/2511.13312)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13312)

> 视觉-语言-动作模型（Vision-Language-Action, VLA）旨在将自然语言指令直接映射为机器人连续控制信号，以突破传统策略在复杂非结构化环境中泛化能力差的瓶颈。现有基于离散Token的VLA受制于控制频率低与动作不连续，而早期连续生成方法在语义接地与场景感知精度上存在缺陷。本文切入点在于改进3D Diffuser Actor (3DDA) 架构，通过引入潜在扩散模型（Latent Diffusion Model, LDM）、像素级视觉编码器与增强文本编码，提升长程任务中的轨迹生成稳定性。该工作验证了潜在空间扩散在长程操作中的有效性，但缺乏跨本体泛化与实时性验证，其工程落地价值存疑。

】

---

【洛桑联邦理工团队新研究：基于聚合编程的多机器人任务分配原型

研究机构：瑞士洛桑联邦理工学院

作者：Giorgio Audrito、Andrea Basso、Daniele Bortoluzzi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06876)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06876)

> 多机器人系统在通信受限与节点故障场景下维持任务分配的鲁棒性，是分布式协调的核心难题。传统优化算法依赖全局状态或集中式通信，难以应对网络分裂与动态拓扑变化。本文切入点在于利用聚合编程（Aggregate Programming, AP）的自稳定算子，将任务分配逻辑内嵌于编程模型本身，而非依赖外部共识协议。通过实现首个部署于真实物理机器人的AP协调系统，验证了无中央基础设施下多跳通信与故障恢复的可行性，但其缺乏与经典分布式算法的量化性能对比，限制了结论的普适性。

】

---

【轻量级时空Transformer用于无人机网络入侵检测

作者：Tarun Kumar Biswas、Ashrafun Zannat、Waqas Ishtiaq 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02711)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02711)

> 无人机通信网络面临DoS、MITM等网络层攻击，但现有检测模型因计算开销大或泛化能力弱，难以在资源受限的边缘设备上实时部署。本文切入点在于利用轻量级Transformer架构统一处理多分类攻击识别与二分类异常检测，通过重塑非序列流量数据以捕获时空依赖。TSLT-Net将输入重塑为序列并引入多头自注意力机制，在ISOT数据集上实现了99.99%的准确率，但缺乏跨数据集泛化验证及物理层攻击的覆盖，其性能是否源于数据分布特性而非架构优势存疑。

】
