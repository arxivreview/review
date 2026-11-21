# HuggingFace最新推荐论文 ｜FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive Resolution ｜自适应分辨率视觉文本压缩

作者：FangZhi Zhong、Xuerui Qiu、Yuqi Pan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.36651)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.36651)

> 长上下文推理中，视觉文本压缩（Visual Text Compression, VTC）将文本渲染为图像以节省Token，但固定分辨率下全局覆盖与局部可读性相互绑定，导致压缩率与性能不可兼得。现有方法如Glyph通过密集渲染优化全局Token预算，却无法在低DPI下恢复关键字符细节。FOCUSVTC通过两阶段训练（REL-SFT+GRPO）让模型在低DPI全局视图上推理，并主动调用工具增强特定区域至高DPI，从而解耦全局覆盖与局部精度。该框架在RULER v1上以2.9×压缩率取得87.4分，显著优于Glyph的57.5分，但其性能高度依赖特定字体与渲染配置，泛化边界尚不明确。

## 研究背景

当LLM处理长文档时，注意力计算与KV缓存内存随上下文长度呈二次方增长，而单纯扩大窗口无法保证检索可靠性。视觉文本压缩（VTC）通过将文本渲染为页面图像，利用VLM的视觉编码器生成紧凑Token序列，从而在保持文档覆盖的同时降低输入Token数量。然而，固定分辨率渲染引入了根本性矛盾：低DPI节省Token但模糊字符，高DPI提升可读性却将Token预算消耗在无关段落上。

VTC领域的主流路线包括密集渲染优化（如Glyph）与光学上下文压缩（如DeepSeek-OCR），它们均假设局部可读性与全局Token预算必须同步调整。这一假设忽略了文档问答任务中证据分布的稀疏性：问题通常仅依赖文档中极小部分的区域。FOCUSVTC的切入点在于打破这一绑定，通过自适应分辨率策略，让模型在压缩的全局视图中定位证据，再选择性增强局部区域，从而在低初始DPI下维持高任务性能。

## 核心方法

### 方法参照系

VTC的标准流程是将文本渲染为固定DPI图像，由VLM编码为视觉Token后输入LLM。该流程的关键局限在于渲染分辨率全局统一，导致局部精度受限于全局Token预算。FOCUSVTC的核心差异在于引入工具介导的区域增强机制，将压缩策略从静态渲染转变为动态交互过程。

### 多分辨率证据定位监督微调

REL-SFT阶段解决模型在低DPI下无法精确定位证据区域的问题。传统VTC模型缺乏空间定位能力，导致后续增强操作盲目。本文构建29.4K条Reasoning–Evidence Localization（REL）链式思维样本，每条样本将推理轨迹与页面索引、归一化边界框关联。训练时，文档在7个DPI（48–144）下渲染，模型学习在任意分辨率下输出包含定位标记的推理序列。损失函数为：

$$
\mathcal{L} = -\mathbb{E}_{(I,q,u)\sim\mathcal{D}_{\text{REL}}} \left[ \sum_{k=1}^{|u|} \log p_\theta(u_k \mid I, q, u_{<k}) \right]
$$

该公式联合优化推理生成、证据定位与答案预测，使模型建立分辨率无关的空间感知能力，为后续自适应增强提供初始化基础。

### 组相对策略优化自适应增强

GRPO阶段解决“何时增强、增强哪里、何时停止”的决策问题。REL-SFT仅提供定位能力，但无法学习增强策略与推理的协同。本文将交互建模为马尔可夫决策过程，状态包含问题、低DPI页面及历史推理/动作/观察。策略网络生成推理段与动作（最终答案或区域增强调用），工具返回对齐的高DPI区域图像。奖励函数为：

$$
R(\tau) = 0.8R_{\text{acc}}(\tau) + 0.2R_{\text{fmt}}(\tau) + \mathbb{I}_{R_{\text{acc}}(\tau)=1} R_{\text{tool}}(\tau)
$$

其中$R_{\text{tool}}$结合分辨率必要性、定位质量与调用效率，仅对完全正确的答案生效。GRPO通过组内相对优势更新策略，使模型学会在压缩视图中精准请求高DPI观察，避免冗余调用，从而在低初始DPI下恢复局部精度。

## 实验评估

实验在LongBench、MRCR、VTCBench与RULER上评估，基线覆盖文本输入模型（Qwen3.5-9B）、固定分辨率VTC模型（Glyph、Qwen3-VL-8B）及训练阶段变体。基线未包含主流Token剪枝方法（如FastV、VisionZip），限制了与通用压缩技术的横向对比。

| 模型 | 输入 | LongBench Avg | MRCR 2-needle | MRCR 8-needle | VTCBench Avg |
|---|---|---|---|---|---|
| Qwen3.5-9B | Text | 55.86 | 48.52 | 18.56 | 20.94 |
| Glyph | Vision | 52.34 | 42.63 | 16.57 | 19.92 |
| FocusVTC | Vision | 56.40 | 60.76 | 30.71 | 26.33 |

FocusVTC在LongBench上超越文本骨干（56.40 vs 55.86），在MRCR所有针数设置下显著优于Glyph，表明自适应增强在长上下文检索与记忆任务上有效。

| 模型 | RULER v1 | LongBench | MRCR 2-needle | VTCBench Retrieval |
|---|---|---|---|---|
| FocusVTC | 87.38 | 56.40 | 60.76 | 91.00 |
| FocusVTC w/o GRPO | 32.28 | 37.86 | 44.94 | 80.27 |
| FocusVTC w/o SFT | 73.21 | 49.30 | 57.05 | 87.17 |
| Qwen3.5-9B+tools | 22.50 | 27.22 | 20.70 | 49.38 |

消融显示GRPO贡献最大：移除后RULER v1从87.38降至32.28，LongBench从56.40降至37.86。SFT提供必要初始化，移除后LongBench降至49.30。工具调用本身无训练时有害（Qwen3.5-9B+tools仅27.22），但经GRPO训练后显著提升，验证了策略学习对工具使用的关键作用。

评估边界存在局限：实验仅使用DejaVu Sans字体，未测试其他字体或渲染配置的鲁棒性；MRCR延迟评估显示2.79×加速，但未报告工具调用引入的额外交互延迟对端到端吞吐的影响；代码与超参数已公开，但29.4K REL-CoT数据的构建依赖Gemini-3.5-Flash与GPT-5-mini，复现成本较高。

## 关联研究分析

从问题动机看，FOCUSVTC与Glyph均针对VTC的压缩-性能权衡，但Glyph通过密集渲染优化全局Token效率，假设局部精度与全局预算同步；FOCUSVTC则基于证据稀疏性假设，将局部精度与全局预算解耦。这一差异源于任务特性：文档问答中证据分布高度稀疏，而密集渲染任务（如OCR）中信息分布均匀，因此自适应增强在稀疏证据场景下更具优势。

从方法设计看，FOCUSVTC借鉴DeepEyes的主动视觉检查范式，但将其从通用视觉推理迁移至文本压缩场景。DeepEyes通过RL学习何时观察图像区域，FOCUSVTC则通过GRPO学习何时增强文本区域分辨率。关键差异在于信号来源：DeepEyes依赖视觉显著性，FOCUSVTC依赖推理链中的证据定位。这一设计选择暗示文本压缩中的区域重要性更依赖于语义推理而非视觉显著性，但论文未对比两种信号源在相同任务上的性能差异。

## 总结

FOCUSVTC解决的核心矛盾是固定分辨率VTC中全局覆盖与局部可读性的绑定。其切入点在于利用文档问答的证据稀疏性，通过工具介导的区域增强解耦全局与局部精度。方法上，REL-SFT建立多分辨率定位能力，GRPO学习自适应增强策略。实验证明其在RULER v1上以2.9×压缩率取得87.4分，显著优于Glyph的57.5分。边界在于性能高度依赖DejaVu Sans字体与特定渲染配置，且未与通用Token剪枝方法对比。当文档类型从问答转向密集OCR时，证据稀疏性假设是否仍成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.36651)