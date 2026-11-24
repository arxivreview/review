# ICLR2026最新论文 ｜MISSING MASS FOR DIFFERENTIALLY PRIVATE DOMAIN DISCOVERY ｜差分隐私域发现的效用保证

研究机构：谷歌研究院、美国密歇根大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_86914899)

> 现代数据分析常面对查询、评论等先验未知或规模巨大的数据域，域发现是下游分析的前置步骤，但差分隐私（Differential Privacy, DP）约束下如何量化算法的恢复能力长期缺乏理论支撑。现有DP集合并集算法多依赖经验验证或相对效用比较，无法回答“算法能恢复多少数据质量”这一根本问题。本文通过将效用指标从计数重构为缺失质量（Missing Mass），为加权高斯机制（Weighted Gaussian Mechanism, WGM）证明了首个绝对效用保证，并扩展至Top-k与k-命中集问题。该工作填补了DP域发现从经验到理论的空白，但其保证依赖Zipfian分布假设，在非幂律数据上的适用性存疑。

## 研究背景

当分析对象是用户搜索词或购买历史时，数据域 $X$ 既未知又可能包含所有长度固定的字符串，直接枚举不可行。此时需从 $n$ 个用户持有的子集 $\{W_i\}$ 中恢复一个“信息丰富”的子集 $S$，即域发现。DP要求算法输出对单个用户的增删不敏感，但集合并集任务中，若某物品仅被一个用户持有，DP约束会强制其以高概率被丢弃，导致最坏情况下效用平凡化。因此，效用保证必须依赖数据分布结构。

DP域发现的核心矛盾在于：隐私保证要求对最坏情况相邻数据集鲁棒，而效用保证需要利用数据的统计规律。早期工作如Korolova et al. (2009) 提出基于噪声计数的阈值过滤，Gopi et al. (2020) 引入WGM通过缩放用户贡献至单位 $\ell_2$ 范数实现隐私，但均未提供绝对效用下界。Desfontaines et al. (2022) 和Chen et al. (2025) 的结果仅相对于其他算法，无法独立评估算法性能。本文切入点在于：将效用指标从“恢复物品数量”重构为“恢复质量占比”，即缺失质量，从而在Zipfian数据上建立可解释的绝对保证。

## 核心方法

### 方法参照系

DP域发现的标准流程是：限制用户贡献 → 构建加权直方图 → 注入噪声 → 阈值过滤。本文问题与该通用流程的关键差异在于：域 $X$ 未知，且效用指标从计数转为缺失质量，要求证明算法在分布假设下的绝对性能，而非相对比较。

### 缺失质量重构与WGM效用界

WGM的效用瓶颈在于：传统计数指标无法区分“恢复100个低频物品”与“恢复10个高频物品”的质量差异。本文引入缺失质量 $\text{MM}(W, S) = \sum_{x \in \bigcup_i W_i \setminus S} \frac{N(x)}{N}$，其中 $N(x)$ 为物品 $x$ 的频率，$N$ 为总物品数。该指标量化了未恢复物品占总质量的占比，直接反映域覆盖度。

$$
\text{MM}(W, S) \leq O\left( \frac{\sigma \sqrt{\log(1/\delta)} \cdot \sqrt{N}}{\sqrt{q^*}} \right)
$$

其中 $q^* = \min\{\Delta_0, \max_i |W_i|\}$，$\Delta_0$ 为用户贡献上界。该公式表明：缺失质量随总物品数 $N$ 增长而衰减，且当数据越Zipfian（$s$ 越大、$C$ 越小）时，上界越紧。这一设计解决了此前方法无法量化“恢复质量”的失效，使WGM在Zipfian数据上获得近最优 $\ell_1$ 缺失质量保证（Theorem 3.3）。

### 分布无关的 $\ell_\infty$ 缺失质量与下游任务扩展

WGM的 $\ell_1$ 保证依赖Zipfian假设，无法直接用于Top-k等需要分布无关保证的任务。本文证明WGM在任意数据集上满足 $\ell_\infty$ 缺失质量界：

$$
\max_i |W_i| \cdot \text{MM}_\infty(W, S) \leq \tilde{O}\left( \frac{\Delta_0}{\epsilon N \sqrt{q^*}} \right)
$$

该界不依赖Zipfian假设，仅依赖用户贡献上界 $\Delta_0$ 和隐私参数。基于此，本文构建两阶段算法：先用WGM以一半隐私预算发现域 $D$，再用已知域算法（如Peeling Exponential Mechanism）以另一半预算在 $D$ 上执行Top-k或k-命中集。这一设计解决了此前未知域Top-k算法（如Durfee & Rogers, 2019）仅提供相对误差保证的局限，为Top-k和k-命中集提供了首个绝对缺失质量保证（Theorem 4.3, 4.5）。

## 实验评估

实验在Reddit、Amazon Games等6个真实数据集上验证WGM基线方法。基线覆盖Sequential WGM、Chen et al. (2025) 等，但缺失Staircase或Mixture of Gaussians等机制（因任务不同）。WGM在缺失质量上接近Policy机制（差距<5%），但计算效率更高，验证了理论保证的实证竞争力。

该论文实验数据不可得，未提供实验表格。消融分析显示：$\Delta_0$ 设置对缺失质量影响显著，当 $\Delta_0 \approx \max_i |W_i|$ 时，子采样误差最小化；若 $\Delta_0 \gg \max_i |W_i|$，缺失质量上界中 $\Delta_0$ 项主导，导致效用退化。这一发现揭示了用户贡献上界与数据结构的耦合关系，是WGM部署的关键调参点。

评估边界：指标仅覆盖缺失质量，未报告隐私-效用帕累托前沿；评估协议未包含非Zipfian数据，无法验证分布无关保证的紧性；论文未提供代码URL，可复现性受限。

## 关联研究分析

从问题动机看，本文与Staircase Mechanism（Melbourne et al., 2026）同属“最优噪声设计”路线，但Staircase针对固定域向量查询，本文针对未知域集合并集。差异根源在于任务特性：Staircase假设域已知，可优化噪声分布形状；本文域未知，必须依赖数据分布假设（Zipfian）建立效用界，而非噪声优化。

从方法设计看，本文与Empirical Bayes DP Mechanism（Kim et al., 2026）同属“利用数据结构提升效用”路线，但Empirical Bayes依赖参数先验，本文依赖Zipfian分布假设。差异根源在于数据形态：Empirical Bayes处理高维统计量，可利用低秩性；本文处理集合数据，Zipfian假设是自然的结构先验。若数据非Zipfian，WGM的效用保证是否退化至平凡，论文未给出回答。

## 总结

本文要解决的核心矛盾是DP域发现缺乏绝对效用保证，现有方法仅能提供相对比较或经验验证。本文抓住的切入点是：将效用指标从计数重构为缺失质量，使WGM在Zipfian数据上获得可解释的绝对保证。本文证明了WGM在Zipfian数据上具有近最优 $\ell_1$ 缺失质量，且在任意数据集上满足分布无关的 $\ell_\infty$ 缺失质量界。本文的边界在于：$\ell_1$ 保证依赖Zipfian假设，$\ell_\infty$ 保证未验证紧性，且两阶段组合的隐私预算分配未联合优化。当数据偏离Zipfian分布时，WGM的缺失质量上界是否仍具实际意义，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_86914899)