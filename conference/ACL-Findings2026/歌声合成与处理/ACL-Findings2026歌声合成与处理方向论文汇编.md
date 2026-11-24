# ACL-Findings2026 · 歌声合成与处理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【MimicLM: Zero-Shot Voice Imitation through Autoregressive Modeling of Pseudo-Parallel Speech Corpora ｜语音模仿（Voice Imitation）中的分布鸿沟与角色互换策略

研究机构：清华大学、香港中文大学

作者：Tao Feng、Yuxiang Wang、Yuancheng Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_42ebfd7a1016)

> 语音模仿旨在将源语音转换为目标说话人的音色与韵律，同时保留语言内容，其核心难点在于缺乏大规模平行语料。现有方法要么依赖复杂的解耦架构，要么受限于合成数据的音质上限。本文提出 MimicLM，通过反转合成语音在训练数据中的角色（作为源而非目标），结合文本-音频交错建模与偏好对齐，实现零样本语音模仿。该方法在自然度上表现优异，但真实输入下的词错误率仍较高，暴露了风格迁移对时序结构的破坏。

】

---

【VocalRep: Structure-Aware Vocal Representations for Multimodal Generation ｜结构感知人声表示学习

研究机构：清华大学

作者：Da Shen、Zhenqiang Weng、Tianyu Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec1673092c2f)

> 音乐源分离（MSS）旨在从混合录音中提取纯净人声，但传统方法将主唱与和声聚合为单一流，导致下游歌声转换（SVC）出现音高抖动与唇形同步模糊。现有重建导向指标（如SDR）无法捕捉这种语义歧义对生成任务的破坏。本文提出VocalRep，通过全局身份条件化与排名式结构约束，显式解耦主唱、和声与乐器，以生成导向的表示质量替代信号保真度作为优化目标。该方法在下游SVC与唇形同步任务中显著提升了音高稳定性与语义清晰度，但其对自建数据集的依赖及缺乏大规模主观听测对比，限制了结论的普适性验证。

】
