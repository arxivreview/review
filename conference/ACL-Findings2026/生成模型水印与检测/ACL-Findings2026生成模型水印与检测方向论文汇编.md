# ACL-Findings2026 · 生成模型水印与检测方向论文汇编

> 本方向共 7 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond A Fixed Seal: Adaptive Stealing Watermark in Large Language Models ｜自适应窃取水印算法

研究机构：北京邮电大学、香港科技大学

作者：Shuhao Zhang、Yuli Chen、Jiale Han 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10893)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10893)

> 大语言模型（LLM）水印面临的核心威胁不仅是内容篡改，更是水印机制本身的逆向工程。现有窃取水印算法（SWA）依赖固定策略，无法适应不同水印对上下文位置的非均匀依赖，导致攻击效率受限。本文提出自适应窃取（AS），通过基于位置的印章构建与动态选择机制，将静态模式复制转化为动态决策过程。该工作揭示了现有水印在有限查询下的严重信息泄露，但仅聚焦攻击侧，未提供防御方案。

】

---

【DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack ｜双流自适应水印防御伪造攻击

作者：Hao Li、Yubing Ren、Yanan Cao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_503f104b61d0)

> 生成模型水印旨在解决AI内容版权归属与真实性验证矛盾，核心在于不可感知性与鲁棒性的平衡。现有方案为抵御改写攻击而强化信号稳定性，却导致恶意篡改文本仍被误判为模型生成，引发归因错误。本文提出DualGuard，通过语义感知的双头映射动态注入标准与对抗水印，实现伪造攻击的检测与溯源。该方法在伪造鲁棒性上显著优于基线，但纯改写场景性能略逊于SOTA，且依赖语义嵌入的准确性。

】

---

【LR-DWM: Efficient Watermarking for Diffusion Language Models ｜双向局部约束的扩散语言模型水印

研究机构：以色列巴伊兰大学

作者：Ofek Raban、Gal Chechik、Ethan Fetaya

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0476c5350ec)

> 扩散语言模型（DLMs）的非顺序生成特性导致依赖左侧上下文的自回归水印范式失效，现有适配方案或需高计算开销的期望计算，或需$|V|^2$内存的查表机制。LR-DWM通过独立利用左右邻居的局部哈希约束，以加性logits偏置实现顺序无关的水印嵌入，在保持检测率的同时将计算与内存开销降至接近无水印基线。该方案解决了DLM水印的效率瓶颈，但其对语义级对抗攻击的鲁棒性未在实验中验证，且未报告具体TPR数值，仅通过困惑度间接反映检测能力。

】

---

【Measuring Watermarking under Jailbreaking: ASR Inflation and Goal-Compliance Mismatch ｜水印解码扰动下的安全对齐解耦：ASR与目标合规的背离

作者：Sungwoo Han、Sangjun Moon、Jingun Kwon 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa9a5e943ff7)

> 生成式AI水印旨在解决内容溯源与版权保护问题，但现有研究多聚焦于水印检测率与鲁棒性，忽视了水印嵌入对模型安全对齐的潜在干扰。当水印解码逻辑与越狱攻击交互时，自动评估指标（ASR）可能因拒绝标记的抑制而虚高，导致对模型安全性的误判。本文通过引入目标合规度量（StrongREJECT）与人工评估，系统量化了六类水印方法在三种越狱设置下的ASR-SR背离现象。该研究揭示了单一ASR指标在对抗场景下的脆弱性，但其结论局限于特定模型与攻击组合，未涵盖水印感知攻击者。

】

---

【Position: LLM Watermarking Should Align Stakeholders’ Incentives for Practical Adoption ｜利益相关者激励对齐的大语言模型水印部署框架

作者：Yepeng Liu、Xuandong Zhao、Dawn Song 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0bda31dc58ae)

> 生成模型水印旨在解决生成式AI内容在版权归属与真实性验证上的核心矛盾，其技术演进本质是在不可感知性与鲁棒性之间寻找平衡。现有算法在检测率与鲁棒性上已趋近理论极限，但实际部署率极低，根源在于提供商、平台与用户间的激励错位。本文提出以“激励对齐”为核心约束，重新评估模型水印、文本水印与上下文水印的适用场景。该立场论文揭示了技术性能与商业生态的脱节，但缺乏量化验证，其提出的上下文水印范式尚处于概念阶段。

】

---

【Rethinking LLM Watermark Detection in Black-Box Settings: A Non-Intrusive Third-Party Framework ｜黑盒第三方大语言模型水印检测框架

研究机构：中国科学院、中国科学院大学

作者：Zhuoshang Wang、Yubing Ren、Yanan Cao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f294926fe4a7)

> 现有大语言模型水印方案将检测逻辑与注入密钥强耦合，导致独立审计机构无法在不泄露密钥的前提下验证内容来源，阻碍了司法与监管场景的应用。本文提出TTP-Detect，通过解耦检测与注入，将验证重构为相对假设检验问题。该方法利用代理模型提取表征，结合局部一致性、全局几何与自适应秩测试等多维相对测量，实现密钥无关的黑盒检测。该框架在多种水印方案上实现了接近白盒SOTA的检测性能，但其对无偏水印方案的检测率显著下降，暴露了统计信号弱化下的检测瓶颈。

】

---

【SLIM: Stealthy Low-Coverage Black-Box Watermarking via Latent-Space Confusion Zones ｜潜空间混淆区数据水印

作者：Hengyu WU、Yang Cao

论文原文见 [arXiv](https://arxiv.org/abs/2601.03242)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc5dfb4d1bfe)

> 训练数据水印旨在解决个体数据贡献者在大规模语料库中无法验证其数据是否被模型训练使用的问题。现有放射性水印方法需修改大量数据且易受攻击，而显式注入方法缺乏隐蔽性，导致在超低覆盖率场景下失效。SLIM通过前缀重述与发散续写构造潜空间混淆区，利用生成不稳定性进行黑盒假设检验。该框架在仅修改单条序列时实现了可靠溯源，但其检测信号随数据规模扩大而稀释，且对模型参数量的依赖尚未完全量化。

】
