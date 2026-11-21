# ACL-Findings2026最新论文 ｜Context-Driven and Reference-Guided Data Augmentation for Subtitle Translation ｜上下文驱动与参考引导的数据增强

作者：Hitoshi Ito、Naoto Shirai、Kazutaka Kinugawa 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fcd883589cd)

> 字幕翻译面临单作品双语数据稀缺与风格保持的双重困境，传统数据增强方法难以兼顾世界观一致性与角色语调。本文切入点在于利用角色描述引导源句重写，并借助原句人工译文作为One-shot参考生成目标语，从而在低资源条件下构建风格对齐的平行数据。该方法通过QLoRA微调通用LLM，实现了特定电影翻译质量的提升。其价值在于降低了人工数据准备成本，但One-shot参考对目标语创造性的潜在限制尚未被充分验证。

## 研究背景

字幕翻译不仅是语言转换，更是特定作品世界观与角色个性的再现。当模型面对某部电影时，若缺乏该作品特有的双语平行数据，通用翻译模型往往产生风格扁平化的译文，导致观众沉浸感下降。这种风格缺失源于指令微调（Instruction Tuning）对高质量领域数据的依赖，而公开数据集通常仅覆盖特定电影或语言对，无法直接迁移至新作品。为突破数据瓶颈，研究者尝试数据增强（Data Augmentation），但传统改写技术仅关注语义等价，忽略了说话者个体性与作品主题范围，导致增强数据无法承载风格信息。

现有数据增强路线存在明显瓶颈。Paraphrase方法通过词级改写扩展源句，但缺乏内容控制，易偏离原意；Storytelling方法采用叙事风格重写，虽能丰富语境，却破坏了原句结构，导致下游翻译时风格对齐困难；Persona方法引入随机角色提示，但随机性导致角色语调不稳定。这些方法均未解决“如何在保持原句结构的同时注入作品特定风格”的核心矛盾。本文针对这一缺口，提出结合上下文驱动重写与参考引导翻译的双阶段数据增强框架，旨在利用少量人工翻译数据撬动大规模风格一致的合成数据生成。

## 核心方法

### 方法参照系

本文问题属于低资源字幕翻译中的数据增强范畴，与通用机器翻译的数据增强流程相似，但关键差异在于：通用方法追求语义覆盖广度，而本文追求单作品风格保真度。标准流程通常仅基于源句生成目标语，本文则引入目标语参考作为风格锚点，将增强过程从单向生成转变为双向约束。

### 上下文驱动源句重写

传统Paraphrase方法直接改写源句，导致角色语调丢失。本文在源句重写阶段引入角色描述（Character Description）作为条件，通过LLM将原句$D_i$重写为$m$个变体$S_i = (s^{(i)}_1, s^{(i)}_2, ..., s^{(i)}_m)$。重写过程保持原句结构，仅改变说话对象或语境细节，公式表示为：

$$s^{(i)}_k = \text{LLM}(D_i, F_j, \text{structure\_constraint})$$

其中$F_j$为从$x$句片段中提取的角色描述。这一设计解决了传统改写中风格信息缺失的问题，确保增强数据承载作品特定的语调特征。

### 参考引导目标语生成

源句重写后，直接机器翻译可能破坏风格一致性。本文采用One-shot学习，将原句$D_i$的人工译文$H_i$作为参考，生成增强句$s^{(i)}_k$的目标语译文$t^{(i)}_k$。对齐对$P_i = \langle s^{(i)}_1, t^{(i)}_1 \rangle, ..., \langle s^{(i)}_m, t^{(i)}_m \rangle$构成平行数据。公式表示为：

$$t^{(i)}_k = \text{LLM}(s^{(i)}_k, H_i, \text{style\_imitation})$$

该设计利用结构相似性确保One-shot参考的有效性，解决了无参考翻译中风格漂移的问题，使目标语译文继承原作的语调与角色身份。

## 实验评估

实验在SubtitleMetaData数据集上进行，涵盖四部电影（Spider-Man 3, The Duchess, The Princess and the Frog, Elio）和四个语言对（EN→FR, EN→FI, EN→ES, EN→DE）。基线包括Base model、In-context learning、Original parallel data only、Paraphrase、Storytelling和Persona。本文方法在EN→FR任务上取得最高BLEU分数，Spider-Man 3达43.91，The Duchess达49.11，显著优于Persona（39.05和47.89）和Storytelling（40.01和47.76）。COMET分数保持稳定，表明风格提升未牺牲语义准确性。

| 方法 | Spider-Man 3 BLEU | The Duchess BLEU | Princess and the Frog BLEU | Elio BLEU |
| :--- | :--- | :--- | :--- | :--- |
| Base model | 37.44 | 42.76 | 29.81 | 21.79 |
| Paraphrase | 37.99 | 46.75 | 31.57 | 22.78 |
| Storytelling | 40.01 | 47.76 | 31.60 | 21.41 |
| Persona | 39.05 | 47.89 | 31.83 | 22.39 |
| Proposed | 43.91 | 49.11 | 33.97 | 24.57 |

消融实验显示，参考引导（Reference guidance）对BLEU提升贡献显著。在EN→FI任务中，Proposed方法BLEU达30.11，高于无参考的Paraphrase（27.29）和Storytelling（28.94）。Elio作为模型训练截止后发布的作品，Proposed方法仍取得24.57 BLEU，高于Base model的21.79，表明方法对未见作品具有泛化能力。

评估协议采用SacreBLEU和COMET，统计显著性通过近似随机化检验验证。局限在于仅评估四部电影，缺乏跨类型作品验证；One-shot参考可能限制目标语创造性表达，论文未提供无参考对照实验以量化此影响。代码未开源，超参数细节见附录，可复现性依赖LLM版本一致性。

## 关联研究分析

从问题动机看，本文与ALPO（Cui et al., 2026）同属字幕翻译风格优化，但ALPO聚焦局部偏好优化以提升自然度，而本文聚焦低资源数据增强以解决风格稀缺。ALPO依赖大量人工标注偏好数据，本文仅需数百句双语对，适用场景不同。本文未对比ALPO，可能因任务设定差异：ALPO针对通用字幕风格，本文针对单作品特定风格。

从方法设计看，本文与Persona（Ge et al., 2024）均使用角色提示，但Persona采用随机采样，本文采用上下文驱动的角色描述提取。随机性导致Persona在The Duchess上BLEU仅47.89，低于本文的49.11，表明上下文驱动的角色描述能更精准地捕捉作品特定语调。本文未探索角色描述自动提取的鲁棒性，当片段长度$x$变化时，描述质量如何影响增强效果，论文未给出回答。

## 总结

本文解决的核心矛盾是单作品字幕翻译中双语数据稀缺与风格保持的冲突。现有方法因缺乏风格锚点导致增强数据风格漂移，本文通过角色描述引导重写和One-shot参考生成，将风格信息嵌入数据增强流程。实验证明该方法在四部电影上BLEU提升3-5分，COMET保持稳定。边界在于One-shot参考可能限制目标语创造性，且仅验证四部电影，缺乏跨类型泛化证据。当支持集从数百句扩展至数千句时，One-shot参考的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_0fcd883589cd)