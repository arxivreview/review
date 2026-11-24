# Others2026 · 视觉-语言模型幻觉方向论文汇编

> 本方向共 3 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token ｜预生成幻觉风险探测

研究机构：美国石溪大学、美国芝加哥丰田技术学院

作者：Sai Akhil Kogilathota、Sripadha Vallabha E G、Luzhe Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05465)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05465)

> 视觉语言模型（VLMs）在生成文本时常因语言先验压制视觉信号而产生对象或属性幻觉，现有抑制方法多依赖解码过程中的动态干预或生成后的完整序列比对，导致实时风险预判能力缺失。HALP 抓住“幻觉风险在生成前已编码于内部表征”这一被忽略的点，通过单次前向传播提取视觉特征、视觉 token 及查询 token 状态，训练轻量级 MLP 探针输出风险分数。该框架实现了零解码成本的幻觉预测，但仅作为诊断工具而非抑制手段，其分数能否直接转化为解码控制信号仍存疑。

】

---

【不确定性引导的视觉重注意自校正

作者：Kassoum Sanogo、Renzo Ardiccioni

论文原文见 [arXiv](https://arxiv.org/abs/2512.07564)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07564)

> 视觉语言模型（VLMs）在生成图像描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。现有推理时干预策略如视觉对比解码（VCD）虽能抑制幻觉，但缺乏对幻觉发生位置的显式定位机制，且单次前向传播难以解决分辨率受限导致的细粒度感知错误。本文提出一种无需训练的自校正框架，通过多维不确定性量化触发对低注意力区域的迭代式裁剪与验证，将幻觉抑制从全局logits调整转向局部视觉证据重构。该框架在Qwen2.5-VL-7B上实现了对抗性设置下4.7%的准确率提升，但其单架构验证与显著高于领域SOTA的幻觉率，暴露了方法泛化性与绝对性能的双重局限。

】

---

【宾夕法尼亚团队新研究：医疗大视觉语言模型中的稀疏视觉对比解码

研究机构：美国宾夕法尼亚大学、美国哥伦比亚大学

作者：Zahra Mahdavi、Zahra Khodakaramimaghsoud、Hooman Khaloo 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.01922)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01922)

> 医疗大视觉语言模型（Med-LVLMs）在生成临床报告时，常因语言先验压制视觉信号而产生幻觉，这在高风险医疗场景中直接威胁诊断安全。现有推理时干预方法如视觉对比解码（VCD）虽能抑制幻觉，但依赖二次前向传播或外部定位工具，导致推理延迟倍增，难以满足实时临床需求。本文提出Med-VCD，通过视觉感知token选择与稀疏化对比解码，在单遍解码中重构视觉接地，消除二次计算开销。该策略在医疗垂直域内显著提升了事实准确性与解码速度，但其基于嵌入层的对比机制是否牺牲了高层语义的判别精度，仍需更严格的跨域验证。

】
