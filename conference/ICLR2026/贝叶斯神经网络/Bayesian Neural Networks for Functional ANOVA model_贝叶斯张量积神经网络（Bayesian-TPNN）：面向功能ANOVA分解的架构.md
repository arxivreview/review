# ICLR2026最新论文 ｜Bayesian Neural Networks for Functional ANOVA model ｜贝叶斯张量积神经网络（Bayesian-TPNN）：面向功能ANOVA分解的架构后验推断

研究机构：韩国首尔大学、荷兰特文特大学

作者：Seokhun Park、Choeun Kim、Jihu Lee 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00545)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00545)

> 导读 可解释AI模型需将高维函数分解为低维交互项，但现有神经ANOVA方法因组件数量随维度指数增长，被迫限制在低阶交互，导致高阶信号丢失。本文切入点是将网络架构本身（节点数与输入变量子集）视为随机变量，通过MCMC采样推断其联合后验。具体做法是设计步进式Metropolis-Hastings提案分布，引导采样器高效探索高阶交互区域。该方法在保持可解释性的同时实现了比固定架构基线更优的预测精度与不确定性量化，但其对预训练变量重要性分布的依赖及离散空间混合效率仍是关键存疑点。

## 研究背景

可解释性模型的核心困境在于函数分解的唯一性与计算可行性的冲突。功能ANOVA分解（Functional ANOVA Decomposition）要求将回归函数 $f$ 唯一分解为满足零和条件（sum-to-zero condition）的低维组件 $f_S$，其中 $S \subseteq [p]$ 为输入变量子集。张量积神经网络（Tensor Product Neural Network, TPNN）通过构造满足零和条件的基础函数 $\phi(\mathbf{x}_S | S, \mathbf{B}, \mathbf{R})$ 来参数化这些组件，但其架构（即每个组件对应的变量子集 $S$ 和基础函数数量 $K$）通常需预先指定。当输入维度 $p$ 较大时，所有可能的 $S$ 组合呈指数增长，导致固定架构方法（如ANOVA-TPNN）无法容纳高阶交互项，或需承受不可承受的计算与内存开销。

现有神经ANOVA方法（如NAM、NBM、NODE-GAM）均面临这一组合爆炸瓶颈，实践中仅使用1-2阶组件，当真实数据中存在显著高阶交互时，预测性能出现系统性偏差。贝叶斯神经网络（Bayesian Neural Networks, BNN）提供了将架构参数纳入后验推断的框架，但标准变分推断（Variational Inference, VI）依赖重参数化技巧，无法处理离散架构变量（如节点数 $K$ 和变量子集 $\mathbf{S}_K$）。本文继承Kong et al. (2023) 的节点稀疏BNN思想，将架构搜索问题转化为离散-连续混合参数空间的后验采样问题，利用MCMC算法在保持ANOVA唯一性约束的前提下，自动识别重要的高阶交互组件。

## 核心方法

### 架构后验的贝叶斯建模

本文方法参照系为固定架构的ANOVA-TPNN，其关键差异在于将组件索引集 $\mathbf{S}_K = (S_1, \dots, S_K)$ 和组件数量 $K$ 从超参数提升为随机变量。模型定义为 $f(\mathbf{x}) = \sum_{k=1}^K \beta_k \phi(\mathbf{x}_{S_k} | S_k, \mathbf{b}_{S_k,k}, \mathbf{\Gamma}_{S_k,k})$，其中 $\phi$ 为满足零和条件的TPNN基础函数。先验分布采用分层结构：$K$ 服从截断几何分布，$S_k$ 条件独立地服从混合分布，该分布通过递归定义的添加概率 $p_{\text{adding}}(\ell) = \alpha_{\text{adding}}(1+\ell)^{-\gamma_{\text{adding}}}$ 控制组件阶数的先验偏好。这一设计动机在于，固定架构方法无法在数据驱动下自动平衡组件复杂度与过拟合风险，而贝叶斯框架通过先验-似然权衡实现架构选择。

### 步进式MCMC提案机制

离散架构参数无法通过梯度下降更新，本文采用Metropolis-Hastings（MH）算法进行后验采样。核心创新在于 $K$ 更新时的提案分布设计：以概率 $K/(M+K)$ 执行步进式（Stepwise）移动，即从现有组件 $S_{k^*}$ 中随机选择一个，并根据预训练变量重要性分布 $p_{\text{input}}(\cdot | S_{k^*})$ 采样新变量 $j_{k^*}$，生成 $S_{\text{new}} = S_{k^*} \cup \{j_{k^*}\}$；以概率 $M/(M+K)$ 执行随机（Random）移动，直接从先验中采样全新 $S_{\text{new}}$。步进式移动通过保留原组件并添加一个变量，确保新架构是现有架构的局部扩展，避免剧烈性能波动。该机制的MH接受概率为：

$$
\alpha = \min\left(1, \frac{\pi(\theta_{\text{new}}) L(\theta_{\text{new}})}{\pi(\theta) L(\theta)} \cdot \frac{q(\theta | \theta_{\text{new}})}{q(\theta_{\text{new}} | \theta)}\right)
$$

其中 $\pi$ 为先验，$L$ 为似然，$q$ 为提案密度。由于步进式移动中辅助变量采用恒等变换，Jacobian行列式为1，简化了接受概率计算。这一设计解决了固定架构方法中高阶交互项因组合爆炸而被排除的问题，使采样器能高效访问高后验概率的高阶区域。

## 实验评估

实验在8个真实数据集（ABALONE, BOSTON, MPG, SERVO, FICO, BREAST, CHURN, MADELON）上进行，采用0.8/0.2训练测试划分，重复5次随机分割。基线覆盖可解释模型（ANOVA-TPNN, NAM, Linear）和黑盒模型（XGB, BART, mBNN），但缺失深度集成（Deep Ensembles）及最新几何推断方法（如MetricBNN）的对比。

| 数据集 | 指标 | Bayesian-TPNN | ANOVA-TPNN | XGB | BART |
|---|---|---|---|---|---|
| BOSTON | RMSE↓ | **3.654**(0.49) | 3.671(0.56) | 4.130(0.56) | 4.073(0.67) |
| MADELON | AUROC↑ | 0.854(0.013) | 0.587(0.013) | **0.884**(0.006) | 0.751(0.011) |
| FICO | ECE↓ | **0.036**(0.004) | — | — | 0.054(0.011) |
| SERVO | CRPS↓ | 0.194(0.01) | — | — | 0.202(0.02) |

在BOSTON回归任务中，Bayesian-TPNN以3.654 RMSE优于ANOVA-TPNN（3.671）和黑盒基线XGB（4.130）、BART（4.073）。在MADELON分类任务中，其AUROC（0.854）低于XGB（0.884），但显著高于其他可解释模型（NAM 0.644, ANOVA-TPNN 0.587）。不确定性量化方面，Bayesian-TPNN在FICO数据集上以0.036 ECE优于BART（0.054）和mBNN（0.219），在SERVO上CRPS（0.194）略高于mBNN（0.185）但优于BART（0.202）。

合成数据实验验证了高阶组件识别能力：在包含3阶交互的真实模型中，Bayesian-TPNN以0.661的识别率显著优于ANOVA-TPNN（0.704，但ANOVA-TPNN无法处理3阶）和NAM（0.542）。MADELON数据集上，Bayesian-TPNN识别出4阶交互 $(49, 242, 319, 339)$ 为最重要组件，归一化重要性得分1.000，而ANOVA-TPNN最高仅识别到3阶。这一结果直接解释了其在MADELON上相对ANOVA-TPNN的性能优势。

评估边界方面，论文未报告计算时间对比，仅提及附录中有运行时实验；未提供代码链接；超参数 $p_{\text{input}}$ 的选择依赖预训练过程，论文承认该非信息性选择在高维高阶场景下表现不佳，但未给出自适应更新方案。指标覆盖RMSE、AUROC、CRPS、NLL、ECE，但未包含校准曲线或可靠性图，不确定性量化评估维度有限。

## 关联研究分析

从方法设计看，本文与mBNN（Kong et al., 2023）同属节点稀疏BNN框架，但mBNN仅处理节点稀疏性（隐藏层神经元数量），而本文扩展至边稀疏性（输入变量子集 $S_k$），并针对ANOVA零和约束设计了特定基础函数 $\phi$。这一差异源于任务特性：mBNN面向通用回归，无需满足函数分解唯一性；本文面向可解释ANOVA模型，必须保证每个组件 $f_S$ 独立满足零和条件。mBNN未涉及高阶交互识别问题，其稀疏先验仅控制模型复杂度，而本文的步进式提案机制专门针对高阶交互搜索优化，这是任务需求驱动的设计分化。

从问题动机看，本文与BART（Chipman et al., 2010）同属贝叶斯非参数回归，但BART通过树结构自动处理变量交互，无需显式指定交互阶数；本文通过神经网络架构搜索实现类似功能，但保留了ANOVA分解的可解释性优势。BART的MCMC算法处理树结构（分裂变量、阈值），本文处理神经网络架构（变量子集、基础函数参数），两者在离散-连续混合参数空间的MH设计上有结构相似性，但本文的步进式提案利用了变量重要性先验 $p_{\text{input}}$，而BART的分裂变量提案基于数据分布。这一差异暗示，当输入变量间存在强相关性时，$p_{\text{input}}$ 的预训练质量可能成为性能瓶颈，论文未对此进行敏感性分析。

## 总结

本文核心矛盾是可解释ANOVA模型中高阶交互项的组合爆炸与计算可行性冲突。切入点是将架构参数纳入贝叶斯后验，利用MCMC处理离散架构变量，这是固定架构方法无法实现的。方法上，通过步进式MH提案机制引导采样器高效探索高阶交互区域，证明了后验一致性。实验表明，在BOSTON上RMSE达3.654，在FICO上ECE达0.036，均优于固定架构基线。边界在于，MADELON上AUROC（0.854）仍低于黑盒XGB（0.884），且对预训练 $p_{\text{input}}$ 的依赖未得到自适应更新机制的缓解。当输入维度 $p$ 进一步增大时，步进式提案的混合时间是否仍能保证采样器充分探索高阶后验区域，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00545)