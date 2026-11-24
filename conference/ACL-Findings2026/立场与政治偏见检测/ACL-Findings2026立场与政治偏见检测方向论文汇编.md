# ACL-Findings2026 · 立场与政治偏见检测方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Cause-CSD: A Challenge Multimodal Conversational Stance Cause Detection Dataset and Effective Method ｜对话式立场-原因对检测

研究机构：中国科学技术大学、哈尔滨工业大学

作者：Fuqiang Niu、Bowen Zhang、Junting Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1b0e0cad6bda)

> 对话式立场检测（CSD）长期面临“标签准确但证据缺失”的困境，导致模型无法区分立场源于事实、情绪还是外部信息，限制了其在危机响应等高风险场景的干预能力。现有方法将立场视为孤立标签，忽略了支撑立场的语境单元，而本文提出对话式立场-原因对检测（CSCPD）任务，旨在联合预测立场极性及其可观测语境证据。通过构建首个大规模数据集Cause-CSD并提出两阶段框架SCD-LM，该工作实现了立场与证据的联合解码。尽管在自建基准上取得SOTA，但Pair-F1绝对值偏低且缺乏跨数据集验证，其泛化边界尚待厘清。

】

---

【Content Fuzzing for Escaping Information Cocoons on Digital Social Media ｜内容模糊测试以逃逸数字社交媒体信息茧房

研究机构：美国加州大学戴维斯分校

作者：Yifeng He、Ziye Tang、Hao Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b1860ad53cf3)

> 信息茧房由推荐算法基于立场标签的过滤机制固化，导致用户仅接触同质化观点。现有去偏或重排序方法依赖平台侧控制，内容创作者无法干预，而传统对抗攻击往往破坏文本语义，难以在保持原意的前提下改变机器分类结果。本文提出 ContentFuzz，一种基于置信度反馈的模糊测试框架，利用大语言模型生成语义保持的重写，以翻转立场检测器的预测标签。该框架验证了立场模型在语义不变条件下的对抗脆弱性，但其对生成式大语言模型分析器的逃逸成功率显著低于编码器模型，且未提供针对该脆弱性的防御机制。

】

---

【POLAR: A Benchmark for Multilingual, Multicultural, and Multi-Event Online Polarization ｜多语言极化检测基准

研究机构：澳大利亚麦考瑞大学、阿联酋扎耶德大学

作者：Usman Naseem、Robert Geislinger、Juan Ren 等 43 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0be1e9c769cb)

> 在线极化检测旨在识别文本中群体间对抗的修辞表现，但现有研究局限于单一语言或特定事件，无法反映全球数字话语的多样性。主流模型在低资源语言上泛化能力崩塌，且缺乏对极化类型与修辞表现的细粒度区分。本文构建了覆盖22种语言、11万实例的多文化极化数据集，并系统评估了小型与大型语言模型在零样本及少样本下的表现。该基准揭示了资源层级对模型性能的决定性影响，但标注一致性的文化依赖性仍制约着跨语言结论的普适性。

】

---

【StanceAttack: Adversarial Attack for Stance Detection ｜立场检测中的对抗攻击：StanceAttack

作者：Chenye Zhao、Cornelia Caragea

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_88494ce3e748)

> 立场检测模型在真实政治舆论场景中面临被恶意篡改的风险，现有研究多关注分类精度而忽视模型对语义保持型扰动的脆弱性。传统词级替换攻击难以生成自然且语义一致的对抗样本，导致攻击成功率低或文本可读性差。本文提出 StanceAttack，利用 ChatGPT 结合思维链（Chain-of-Thought, CoT）提示与决策反馈机制，生成能欺骗预训练语言模型（Pretrained Language Models, PLMs）的立场翻转样本。该方法在效率与成功率上优于基线，但仅针对黑盒 PLM 且排除中立类，其鲁棒性边界尚待验证。

】
