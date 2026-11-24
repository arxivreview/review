# CVPR2026 · 基于LLM的Web智能体与基准测试方向论文汇编

> 本方向共 5 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DualMirage: Hunting Stealthy Multimodal LLM Agents via CAPTCHAs with Contour and Adversarial Illusions ｜双重幻象：基于轮廓与对抗错觉的隐蔽多模态智能体狩猎

作者：Bei Chen、Gaolei Li、Jun Wu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49ed7f88450d)

> 多模态大语言模型（MLLM）智能体在网页自动化中日益隐蔽，传统验证码（CAPTCHA）难以区分其与人类，导致安全验证失效。现有防御依赖语义理解或系统沙箱，但无法主动识别并暴露智能体身份。本文提出 DualMirage，通过融合人类视觉特有的轮廓错觉与针对 MLLM 视觉编码器的对抗扰动，构建双重幻象屏障。该方法在阻断智能体解题的同时，诱导其泄露模型名称，实现了从被动防御到主动狩猎的转变。其有效性依赖于 MLLM 视觉编码器对特定扰动的脆弱性，随着模型鲁棒性提升，该防御机制的长期有效性存疑。

】

---

【Ego2Web: A Web Agent Benchmark Grounded in Egocentric Videos ｜第一人称视频接地的Web智能体基准

研究机构：谷歌DeepMind

作者：Shoubin Yu、Lei Shu、Antoine Yang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22529)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22529)

> 现有Web智能体基准仅评估数字环境内的交互能力，无法衡量智能体从物理世界视觉感知到线上动作执行的跨域一致性。VisualWebArena等基准虽引入多模态输入，但视觉源局限于网页截图，缺乏对用户周围真实环境的接地。本文提出Ego2Web，将第一人称视频作为智能体的感知输入，构建500个需结合视频理解与Web操作的混合任务。该基准揭示了当前主流智能体在物理-数字跨域任务上的显著性能瓶颈，但其评估协议对视频时序细节的依赖可能引入新的裁判偏差。

】

---

【Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration ｜认知边界驱动的自主探索框架

研究机构：浙江大学

作者：Weile Chen、Bingchen Miao、Qifan Yu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.31365)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.31365)

> 多模态大语言模型（MLLM）驱动的Web智能体在动态开放环境中面临泛化能力不足与高质量交互数据稀缺的双重困境。现有方法依赖人工设计的执行流水线或昂贵的专家轨迹，导致智能体行为被动且难以适应未见过的网页布局。本文提出SCALE框架，通过Selector、Predictor和Judger三个角色的自我对抗机制，让智能体主动定位并扩展自身的认知边界，无需外部监督即可生成训练数据。该框架在InternVL2.5-8B和Qwen2.5-VL-7B上分别实现了231.8%和176.3%的平均任务成功率提升，但其绝对性能仍显著低于当前SOTA，且缺乏对安全防御的考量。

】

---

【WebChain: A Large-Scale Human-Annotated Dataset of Real-World Web Interaction Traces ｜WebChain：基于真实人工轨迹的大规模 Web 智能体数据集与双阶段训练范式

研究机构：复旦大学

作者：Sicheng Fan、Rui Wan、Yifei Leng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05295)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05295)

> 导读 Web 智能体领域长期受困于训练数据规模不足与真实环境覆盖缺失，导致模型在长程任务中泛化能力受限。现有合成数据方法因反爬机制无法覆盖高价值认证场景，而开源人工数据集又缺乏验证 Scaling 效应所需的体量。本文通过构建包含 31,725 条真实人工标注轨迹的 WebChain 数据集，并提出解耦空间接地与长程规划的双阶段训练范式，旨在填补数据空白并优化训练效率。该工作提供了可复现的数据基础设施，但其对人工标注成本的依赖及跨基准泛化能力的边界仍存疑。

】

---

【WebGym: Scaling Training Environments for Long-Horizon Visual Web Agents with Realistic Tasks ｜视觉Web智能体的异步强化学习训练环境

作者：Hao Bai、Alexey Taymanov、Tong Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e180b1d091de)

> 视觉Web智能体在真实开放网络中面临长程任务成功率低与训练数据稀缺的双重瓶颈，现有同步强化学习（RL）系统因浏览器模拟的延迟瓶颈导致采样效率低下，且缺乏大规模多样化任务集以支撑泛化策略学习。WebGym通过构建包含近30万条程序化生成任务的真实环境，并设计异步高吞吐Rollout系统消除同步屏障，解决了视觉智能体RL训练中的计算效率与数据规模问题。该方法利用简单的REINFORCE算法将Qwen3-VL-8B在分布外测试集上的成功率从26.2%提升至42.9%，超越了GPT-4o与GPT-5-Thinking，但其性能高度依赖特定任务采样策略，且未验证在更复杂对抗环境下的鲁棒性。

】
