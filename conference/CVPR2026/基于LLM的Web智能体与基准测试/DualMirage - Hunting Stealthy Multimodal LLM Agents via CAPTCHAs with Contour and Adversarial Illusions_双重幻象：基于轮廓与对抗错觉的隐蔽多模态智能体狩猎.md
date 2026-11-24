# CVPR2026最新论文 ｜DualMirage: Hunting Stealthy Multimodal LLM Agents via CAPTCHAs with Contour and Adversarial Illusions ｜双重幻象：基于轮廓与对抗错觉的隐蔽多模态智能体狩猎

作者：Bei Chen、Gaolei Li、Jun Wu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49ed7f88450d)

> 多模态大语言模型（MLLM）智能体在网页自动化中日益隐蔽，传统验证码（CAPTCHA）难以区分其与人类，导致安全验证失效。现有防御依赖语义理解或系统沙箱，但无法主动识别并暴露智能体身份。本文提出 DualMirage，通过融合人类视觉特有的轮廓错觉与针对 MLLM 视觉编码器的对抗扰动，构建双重幻象屏障。该方法在阻断智能体解题的同时，诱导其泄露模型名称，实现了从被动防御到主动狩猎的转变。其有效性依赖于 MLLM 视觉编码器对特定扰动的脆弱性，随着模型鲁棒性提升，该防御机制的长期有效性存疑。

## 研究背景

当 MLLM 智能体执行网页任务时，其视觉输入通道成为主要攻击面。人类视觉系统具备自下而上的生理感知能力，能自动补全缺失轮廓（如 Kanizsa 三角形），而 MLLM 依赖数据驱动的自下而上处理，缺乏这种生理机制。这种感知差异构成了区分人类与机器的物理基础，但现有 CAPTCHA 设计未充分利用此差异。

主流防御路线分为两类：一是基于 LLM 语义理解的检测（如 WebSentinel），通过分析页面意图识别注入，但难以应对隐蔽的视觉攻击；二是系统级沙箱（如 ceLLMate），通过权限控制限制行为，但牺牲了智能体灵活性。两者均无法主动识别智能体身份，且对视觉层面的隐蔽攻击缺乏针对性。

本文切入点在于利用人类与机器视觉的生理鸿沟。通过生成人类可识别但 MLLM 无法解析的轮廓错觉图像，结合针对 MLLM 视觉编码器的对抗扰动，DualMirage 不仅阻止智能体解题，还诱导其输出特定身份字符串，实现主动暴露。

## 核心方法

### 方法参照系

传统 CAPTCHA 依赖图像识别或逻辑推理，假设人类与机器在视觉感知上无本质差异。本文问题与该通用流程的关键差异在于：利用人类视觉生理特性（轮廓错觉）与 MLLM 数据驱动特性的根本对立，构建双重防御屏障。

### 彩色邻接光栅错觉生成

设计动机：解决现有轮廓错觉生成算法仅适用于二值图像、计算成本高且语义模糊的问题。本文提出彩色邻接光栅失真算法，将经典错觉推广至全彩图像。对于输入 RGB 图像 $x \in \mathbb{R}^{H \times W \times 3}$，生成前景掩码 $M_f$ 和背景掩码 $M_b = 1 - M_f$。对于每个颜色通道 $c$，生成两个相位差为 $\pi$ 的方波光栅 $G_1$ 和 $G_2$，其强度由下式定义：

$$
G_c(x, y) = \begin{cases} A_c & \text{if } \lfloor \frac{x \cos \theta + y \sin \theta}{T} \rfloor \text{ is even} \\ B_c & \text{otherwise} \end{cases}
$$

最终错觉图像 $x_{cag}$ 通过合成生成：

$$
x_{cag} = (G_1 \odot M_f) + (G_2 \odot M_b)
$$

该公式确保错觉轮廓在两个掩码区域边界形成，通过调整方向 $\theta$、周期 $T$ 和颜色向量，生成多样化的认知挑战。

### 隐私诱导对抗错觉注入

设计动机：解决传统对抗攻击仅导致误分类、无法主动暴露智能体身份的问题。本文提出隐私诱导对抗错觉注入，在轮廓错觉图像基础上注入对抗扰动 $\delta$，诱导 MLLM 输出特定目标字符串 $y_t$（如模型名称）。白盒攻击优化目标为最大化目标序列对数似然：

$$
\max_{\delta} \sum_{i=1}^{L} \log p_g(y_i | x_{cag} + \delta, p, y_{<i}), \quad \text{s.t. } \|\delta\|_\infty \le \epsilon
$$

黑盒攻击通过 CLIP 模型集成优化图像与目标文本嵌入的余弦相似度：

$$
\max_{\delta} \frac{1}{N} \sum_{i=1}^{N} \cos(E_{img}^{(i)}(x_{cag} + \delta), E_{text}^{(i)}(y_t)), \quad \text{s.t. } \|\delta\|_\infty \le \epsilon
$$

该设计将对抗扰动从“干扰识别”转变为“诱导泄露”，实现主动狩猎。

## 实验评估

实验在 Selfie2Anime 和 MNIST 数据集上构建两类挑战，对比 reCAPTCHA、hCAPTCHA、Angular 等基线。基线覆盖图像类、推理类和轮廓类 CAPTCHA，但缺乏基于 LLM 语义理解的防御基线。

| 方法 | LLaVA ABR | LLaVA ASR | GPT-4o ABR | GPT-4o ASR |
| :--- | :--- | :--- | :--- | :--- |
| reCAPTCHA | 72.1 | - | 50.0 | - |
| Angular | 99.9 | - | 86.7 | - |
| IllusionCAPTCHA | 100.0 | - | 100.0 | - |
| DualMirage | 100.0 | 62.25 | 97.5 | 20.75 |

DualMirage 在 LLaVA 上实现 100% 阻断率（ABR）和 62.25% 身份暴露率（ASR），显著优于基线。在 GPT-4o 上，ABR 为 97.5%，ASR 为 20.75%，表明黑盒攻击有效性较低。

消融实验显示，移除轮廓错觉后，ASR 降至 0%，证明轮廓错觉是诱导泄露的关键。移除对抗扰动后，ABR 降至 99.1%，表明对抗扰动对阻断率贡献较小。

评估边界：指标仅包含 HSR、ABR、ASR，缺乏对推理延迟和内存占用的评估。代码未公开，超参数（如 $\epsilon = 8/255$）固定，可复现性受限。

## 关联研究分析

从问题动机看，DualMirage 与 WebSentinel 均针对安全防御，但 WebSentinel 依赖 LLM 语义理解检测注入，而 DualMirage 利用视觉生理差异。WebSentinel 的局限在于无法应对视觉层面的隐蔽攻击，DualMirage 通过轮廓错觉弥补此盲区。差异根源在于任务特性：WebSentinel 针对文本注入，DualMirage 针对视觉攻击。

从方法设计看，DualMirage 与 ceLLMate 均提供安全边界，但 ceLLMate 依赖系统级沙箱，DualMirage 依赖感知级防御。ceLLMate 的局限在于限制智能体灵活性，DualMirage 无需修改浏览器架构，部署门槛更低。差异根源在于防御层级：ceLLMate 在系统层，DualMirage 在感知层。

## 总结

本文核心矛盾是 MLLM 智能体隐蔽性导致传统 CAPTCHA 失效。切入点在于利用人类视觉生理特性与 MLLM 数据驱动特性的根本对立。方法通过融合轮廓错觉与对抗扰动，实现主动狩猎。实验证明 DualMirage 在 LLaVA 上实现 100% ABR 和 62.25% ASR，在 GPT-4o 上实现 97.5% ABR 和 20.75% ASR。边界在于黑盒攻击有效性较低，且依赖 MLLM 视觉编码器脆弱性。当 MLLM 视觉编码器对轮廓错觉的鲁棒性提升时，该防御机制的有效性是否衰减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_49ed7f88450d)