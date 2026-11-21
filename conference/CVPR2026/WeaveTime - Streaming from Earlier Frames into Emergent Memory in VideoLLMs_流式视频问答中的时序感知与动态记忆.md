# CVPR2026最新论文 ｜WeaveTime: Streaming from Earlier Frames into Emergent Memory in VideoLLMs ｜流式视频问答中的时序感知与动态记忆

研究机构：上海科技大学、中山大学

作者：Yulin Zhang、Cheng Shi、Sibei Yang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3ece0eb31b4c)

> 流式视频问答要求模型在帧序列实时到达时，基于因果约束即时响应，而非离线处理完整视频。现有视频大语言模型（Video-LLM）将视频视为无序证据袋，导致时序歧义与过去-当前焦点盲视，无法区分当前观察与历史记忆。WeaveTime 通过轻量级时序重构训练与不确定性门控的粗到细检索缓存，在不改变模型架构的前提下解决上述问题。该方法在流式基准上显著提升了时序任务精度并降低了延迟，但其对长程因果推理的覆盖及与强化学习路线的对比仍存疑。

## 研究背景

流式视频理解的核心困境在于时间因果约束与计算效率的冲突。当视频帧按时间顺序到达时，模型必须仅利用已观察到的帧 $\{f_1, \dots, f_t\}$ 回答问题，未来帧不可用。这种约束使得传统的“预处理范式”——即通过采样或压缩将完整视频打包为固定长度上下文——失效，因为完整视觉内容在查询时不可得。更深层的问题在于，现有 Video-LLM 普遍存在“时间无关性”（Time-Agnosticism），即模型倾向于将视频帧视为无序的证据集合，而非因果有序的时间序列。

这一缺陷在流式场景中表现为两个耦合挑战：时序歧义（Temporal Order Ambiguity）与过去-当前焦点盲视（Past–Current Focus Blindness）。时序歧义指模型无法正确引用语义相似但时序不同的历史片段，导致因果推理错误；焦点盲视指模型无法动态分配注意力于当前帧与相关历史，要么过度依赖当前观察忽略必要回溯，要么盲目检索无关历史。现有流式方法要么依赖昂贵的专用数据训练，要么采用固定检索机制，均未能有效解决这两个问题。WeaveTime 的切入点在于，将时序感知从复杂的架构改造或强化学习（RL）中解耦，通过轻量级训练注入时序先验，并在推理时通过不确定性门控实现按需记忆检索。

## 核心方法

### 检索式流式基线

WeaveTime 建立在检索式流式 Video-LLM 基线之上。该基线采用滑动窗口注意力编码每帧 $f_t$，生成键值对 $(K_t, V_t)$ 并追加至记忆缓冲区 $\mathcal{M}_t$。查询时，通过余弦相似度从 $\mathcal{M}_t$ 中检索 Top-K 帧作为上下文。此基线避免了压缩式方法的信息损失，但存在两个固有缺陷：重复长程加载增加延迟，以及缺乏时序感知的固定检索导致焦点盲视。

### 流式顺序感知增强（SOPE）

SOPE 旨在解决时序歧义，通过轻量级训练显式注入时序先验。其设计动机是，现有模型在帧序打乱后性能几乎不降，表明其未真正利用时序结构。SOPE 在训练时引入时间戳交错与重排序目标：将视频 token 序列 $\mathbf{X}$ 中的帧内容打乱，但保留时间戳 token $\mathbf{ts}_i$，形成 $\mathbf{X}'$。模型被要求先恢复正确时间顺序，再回答原始问题。

$$
\mathbf{X}' = \big[ \mathbf{ts}_1, \tilde{\mathbf{v}}_{2,1}, \dots, \tilde{\mathbf{v}}_{2,N_f}, \mathbf{ts}_2, \tilde{\mathbf{v}}_{1,1}, \dots, \tilde{\mathbf{v}}_{1,N_f}, \dots \big]
$$

该公式表示，时间戳 token 被保留在原始位置，而帧内容 token $\tilde{\mathbf{v}}_{i,j}$ 被随机重排。模型通过下一 token 预测任务生成结构化响应，恢复正确顺序。这一设计无需额外模块或自定义损失函数，直接利用 LLM 的重排能力，以极低成本（仅 30k 离线数据，1 epoch LoRA 训练）使记忆从无序缓存升级为有序状态。

### 过去-当前动态焦点缓存（PCDF-Cache）

PCDF-Cache 解决焦点盲视，通过不确定性门控实现按需检索。其设计动机是，固定检索无法区分“当前可答”与“需回溯”的查询，导致冗余加载或遗漏关键历史。PCDF-Cache 计算预测熵 $H_t$ 作为触发器：

$$
a_t = \begin{cases} a_t^{(0)}, & \text{if } H_t < \delta, \\ \mathrm{Answer}\!\big (\mathrm{Load}_{\text{C2F}}(\mathcal{M}_t, q),\, q \big ), & \text{otherwise.} \end{cases}
$$

该公式表示，当熵 $H_t$ 低于阈值 $\delta$（设为 0.6）时，模型仅使用当前观察进行前向推理；当熵升高时，激活粗到细（C2F）检索模块。C2F 首先通过帧级相似度形成粗粒度候选集 $\mathcal{M}_{\text{coarse}}$，再通过晚期交互多向量匹配细化至 token 级，平衡精度与延迟。这一机制实现了“现在看，需要时回忆”的原则，显著减少冗余长程加载。

## 实验评估

实验在 OVO-Bench 和 Streaming-Bench 的实时子集上进行，基线包括 StreamBridge、ReKV 等流式方法。WeaveTime 基于 LLaVA-OV-7B 和 Qwen2-VL-7B 骨干，无需专用流式数据。

| 方法 | OVO-Bench Real-Time (AVG) | Streaming-Bench Real-Time (AVG) |
| :--- | :--- | :--- |
| LLaVA-OV-7B + StreamBridge | 61.64 | 68.39 |
| LLaVA-OV-7B + ReKV | 61.72 | 66.15 |
| LLaVA-OV-7B + WeaveTime | 68.82 | 72.13 |
| Qwen2-VL-7B + WeaveTime | 66.28 | 75.39 |

WeaveTime 在 LLaVA-OV-7B 上较 ReKV 提升 7.10%（OVO-Bench）和 5.98%（Streaming-Bench），在时序任务（ACP, EU, ACR）上提升尤为显著，分别达 +7.56%、+9.04%、+11.09%。

消融实验显示，直接微调基线导致性能下降 3.68%，而加入 SOPE 后提升 5.82%，表明时序重构任务有效解决了时序歧义。PCDF-Cache 进一步带来增益，验证了不确定性门控的价值。C2F 检索策略在 QAEGO4D 上召回率达 25.2%，较 ReKV 的 23.9% 提升，且避免了细粒度检索的内存溢出问题。

评估边界方面，论文未报告置信区间，且仅在流式基准上评估，缺乏与离线 SOTA（如 TempR1）的横向对比。代码与权重已公开，训练使用 8 GPU，超参数（如 $\delta=0.6$）已披露，可复现性良好。

## 关联研究分析

从问题动机看，WeaveTime 与 TempR1 等强化学习路线形成鲜明对比。TempR1 通过 GRPO 优化多任务时序定位，依赖复杂奖励函数与大规模训练；WeaveTime 则主张轻量级时序重构任务足以注入时序先验，无需 RL。这一差异源于任务特性：流式场景要求实时响应，RL 的训练成本与推理延迟可能不兼容；而离线定位任务可承受更高计算开销。WeaveTime 的轻量设计是否足以应对长程因果推理，论文未给出回答。

从方法设计看，WeaveTime 与 ReKV 同属检索式流式框架，但 ReKV 采用固定 Top-K 检索，WeaveTime 引入不确定性门控与 C2F 细化。这一改进解决了 ReKV 在焦点盲视上的缺陷，但 C2F 的晚期交互匹配可能引入额外计算开销。论文未报告 C2F 在不同视频长度下的延迟变化，其效率优势在极端长视频场景下是否持续，尚需验证。

## 总结

WeaveTime 针对流式视频问答中 Video-LLM 的时间无关性，通过 SOPE 轻量训练与 PCDF-Cache 动态检索，在不改变架构的前提下解决了时序歧义与焦点盲视。实验显示，其在 OVO-Bench 上较 ReKV 提升 7.10%，验证了轻量时序感知与按需检索的有效性。然而，论文仅在流式基准上评估，未与离线 SOTA 对比，且 C2F 检索在极端长视频下的延迟表现未充分披露。当视频长度超过 1 小时时，PCDF-Cache 的内存占用与检索延迟是否仍可控，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_3ece0eb31b4c)