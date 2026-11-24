# ACL-Findings2026 · 神经音频编码与压缩方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AffectCodec: Emotion-Preserving Neural Speech Codec for Expressive Speech Modeling ｜情感保留神经语音编解码器

研究机构：美国威廉与玛丽学院、美国埃默里大学

作者：Jiacheng Shi、Hongfei Du、Xinyuan Song 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fcb8cd83b9d0)

> 神经语音编解码器将连续波形映射为离散Token以适配大语言模型，但现有方法在优化声学重建或语义保真时，往往导致情感表达在量化过程中发生不可逆退化。AffectCodec将情感保留从下游评估指标提升为核心表征学习目标，通过情感-语义引导潜变量调制、关系保持蒸馏及情感加权语义对齐三阶段框架，在离散化前显式注入情感结构。该设计在情感一致性指标上显著优于主流基线，但其对通用声学保真度的增益是否独立于情感特征增强，仍需更严格的控制实验验证。

】

---

【Hierarchical Representation Alignment Learning of Diffusion Transformers for Neural Audio Codec ｜条件流匹配神经音频编解码器

作者：Sang-Hoon Lee、Ha-Yeong Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_55e4b6e26a0a)

> 极低码率下，传统生成对抗网络（GAN）解码器因信息压缩过度导致语义丢失与高频重建崩塌。现有单码本方案虽简化了大语言模型（LLM）接口，但缺乏概率式生成机制对缺失细节的补偿能力。FlowTokenizer 将条件流匹配（Conditional Flow Matching, CFM）引入解码器，并设计分层表征对齐（REPA-H）与稠密向量量化（DVQ），在 25 TPS 下实现 24 kHz 波形重建。该方法在语义一致性上优于同码率 GAN 基线，但绝对重建质量仍受限于低帧率信息瓶颈，其流式推理延迟与说话人相似度损失尚存疑。

】
