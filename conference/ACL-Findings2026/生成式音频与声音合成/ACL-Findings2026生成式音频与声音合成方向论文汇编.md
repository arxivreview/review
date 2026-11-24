# ACL-Findings2026 · 生成式音频与声音合成方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AudioStealer: Extracting Audio Prompts via Shapley Value-Guided Query Search ｜音频提示词窃取：基于Shapley值引导的黑盒逆向工程

作者：Yingbin Jin、Xingjian Du、Hanjun Luo 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_00fb09453431)

> 文本到音乐模型将高价值提示词转化为可复现的音频资产，但现有图像或文本域的提示词窃取方法无法直接迁移至音频域，因为音频语义在时频域呈弥散分布且高度纠缠，导致静态分类或独立修饰符解耦策略失效。AudioStealer通过两阶段黑盒框架解决这一难题：首先利用对比音频-语言嵌入进行启发式搜索锚定语义方向，随后引入基于Shapley值的博弈论精化策略量化各语义组件的边际贡献。该方法在不访问目标模型内部参数的情况下，实现了语义忠实且感知对齐的提示词重建，揭示了文本到音乐生态系统中被忽视的知识产权漏洞，但其效果高度依赖本地影子模型的质量与CLAP嵌入的语义分辨率。

】

---

【Bypassing Neural Evaluations for Fast Audio Editing via Adaptive Trajectory Extrapolation ｜自适应轨迹外推加速音频编辑

研究机构：美国东北大学、上海交通大学

作者：Xiaoqian Liu、Zhengkun Ge、Jianjin Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d77c7af3e1c4)

> 基于扩散模型的音频编辑依赖确定性反转，但固定步数采样导致推理延迟过高，阻碍了实时交互应用。现有加速方法如高阶ODE求解器在大幅减少步数时保真度急剧下降，无法兼顾效率与质量。本文提出AdaTE，通过监测潜空间轨迹的曲率加速度与信息增益，在稳定段执行线性外推以跳过冗余神经评估，实现模型无关的加速。该方法在三个主流骨干上取得最高3.9倍加速且保真度不降反升，但其线性外推假设在极端语义突变下的鲁棒性边界尚待更严苛的测试验证。

】

---

【Masked Text-to-Audio Flow-Matching and Reward Feedback Optimization ｜掩码流匹配音频生成

研究机构：香港中文大学、浙江大学

作者：Rongjie Huang、Dongchao Yang、Wenxiang Guo 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5f84526f79cc)

> 文本到音频（Text-to-Audio, T2A）生成面临推理延迟与生成质量难以兼得的矛盾，传统增加去噪步数收益递减，而离散掩码解码存在量化信息损失。本文切入点在于将掩码生成机制引入连续流匹配框架，通过迭代解码扩展推理时计算量。MaskAudioFlow 在训练时掩码连续音频帧，推理时随机重预测被掩码部分，并结合奖励加权微调对齐人类偏好。该方法在 AudioCaps 基准上实现了 SOTA 的主观质量与文本对齐，但缺乏与最新流匹配加速方法的客观指标直接对比，其长音频连贯性表现存疑。

】
