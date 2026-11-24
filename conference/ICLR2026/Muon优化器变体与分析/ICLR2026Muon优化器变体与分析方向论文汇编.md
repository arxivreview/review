# ICLR2026 · Muon优化器变体与分析方向论文汇编

> 本方向共 6 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Convergence of Muon with Newton-Schulz ｜非凸收敛性下的 Newton-Schulz 近似误差量化

研究机构：韩国首尔大学

作者：Gyu Yeol Kim、Min-hwan Oh

论文原文见 [arXiv](https://arxiv.org/abs/2601.19156)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19156)

> Muon 优化器在 LLM 训练中因忽略矩阵结构而导致的梯度病态问题，其核心矛盾在于实际部署的 Newton-Schulz (NS) 近似正交化与理论分析的精确 SVD 极分解之间存在鸿沟。现有理论工作多假设理想化的 SVD 步骤，无法解释为何少量 NS 迭代即可在墙钟时间上实现高效收敛。本文通过显式建模 NS 多项式迭代，证明了其极近似误差随步数双指数衰减，从而弥合了理论与实践的差距。这一结果确立了 NS-Muon 在非凸优化中的理论合法性，但其对高维稀疏矩阵的稳健性仍存疑。

】

---

【Error Feedback for Muon and Friends ｜非欧几里得分布式优化中的误差反馈机制

研究机构：沙特阿拉伯阿卜杜拉国王科技大学、月之暗面

作者：Kaja Gruntkowska、Alexander Gaponov、Zhirayr Tovmasyan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00643)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00643)

> 大规模语言模型训练面临通信瓶颈，而 Muon 等基于线性最小化预言机（LMO）的优化器因依赖密集矩阵运算，无法适配标准参数分片策略。现有分布式变体缺乏理论保证，导致其在超大规模集群中无法稳定落地。本文通过引入双向压缩与误差反馈机制，首次为这类非欧几里得优化器提供了严格的收敛性证明。该工作填补了理论空白，但其实验仅覆盖小规模 DDP 场景，在极端异构数据下的泛化能力尚存疑。

】

---

【FedMuon: Federated Learning with Bias-corrected LMO-based Optimization ｜联邦学习中 LMO 优化器的偏置校正与收敛性分析

研究机构：日本京都大学、日本冲绳科学技术大学院大学

作者：Yuki Takezawa、Anastasia Koloskova、Xiaowen Jiang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26337)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26337)

> 联邦学习场景下，直接复用 Muon 优化器会导致训练停滞，其根源在于线性最小化预言机（LMO）在异构数据分布中表现出系统性偏置。现有分布式 Muon 变体如 MuLoCo 仅适用于同质数据，缺乏理论保证。本文通过引入 SCAFFOLD 式控制变量校正 LMO 偏置，并首次量化了 Newton-Schulz 迭代次数对收敛范数的影响。该工作填补了 Muon 在联邦学习中的理论空白，但其实验规模与部分参与场景的缺失限制了结论的普适性。

】

---

【How Muon's Spectral Design Benefits Generalization: A Study on Imbalanced Data ｜谱感知优化器的泛化机制：基于不平衡数据的理论解析

研究机构：美国南加州大学、加拿大不列颠哥伦比亚大学

作者：Bhavya Vasudeva、Puneesh Deora、Yize Zhao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22980)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22980)

> 谱感知优化器如 Muon 和 Shampoo 在大规模模型训练中展现出显著的效率优势，但其为何能带来更好的泛化性能，尤其是相对于标准梯度下降（GD）和 Adam，长期缺乏理论解释。现有研究多聚焦于收敛速率或终端相的隐式偏差，忽略了训练早期动态对泛化的决定性影响，且未回答在何种数据分布下谱几何优势转化为泛化收益。本文通过引入类不平衡数据作为测试床，将 Muon 和 Shampoo 抽象为谱梯度下降（SpecGD），证明了其在早期训练阶段以等速率学习所有谱分量的特性，从而在少数类泛化上优于 GD。这一发现填补了从优化动态到泛化性能的因果链条空白，但结论依赖于正交均值假设，且在平衡数据下的普适性尚存疑。

】

---

【Muon Outperforms Adam in Tail-End Associative Memory Learning ｜关联记忆视角下的 Muon 优化机制解析

研究机构：新加坡国立大学、美国明尼苏达大学

作者：Shuche Wang、Fengzhuo Zhang、Jiaxiang Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26030)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26030)

> Muon 在 LLM 训练中比 Adam 快近 2 倍，但“谱范数最速下降”的几何解释无法说明为何矩阵范数优化优于向量范数优化。现有收敛性分析仅关注全局速率，忽略了 Transformer 内部不同组件对优化器的差异化响应。本文通过组件级消融与单层线性关联记忆理论模型，揭示 Muon 的优势源于其对 Value-Output (VO) 矩阵和 FFN 中尾部事实的均衡学习。这一机制解释填补了“为何有效”的理论空白，但受限于单层线性假设，其结论向深层非线性架构外推的普适性尚存疑。

】

---

【MuonBP: Faster Muon via Block-Periodic Orthogonalization ｜块周期正交化优化器

研究机构：美国普林斯顿大学、美国明尼苏达大学

作者：Ahmed Khaled、Kaan Ozkara、Tao Yu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16981)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16981)

> Muon 优化器在模型并行训练中存在通信瓶颈，导致其单步迭代速度低于 AdamW，尽管其数据效率更高。现有方案要么牺牲收敛性（如纯块级正交化），要么依赖低秩近似增加计算复杂度。本文切入点在于通过“块级独立正交化 + 周期性全局正交化”的混合策略，在保留 Muon 数据效率的同时消除额外通信开销。其核心机制是引入双学习率机制，在块步与全步间平滑插值收敛率。该方案在 8B 模型上实现了 8% 的吞吐提升且精度无损，但固定周期策略在动态负载下的适应性尚存疑。

】
