# ICLR2026最新论文 ｜EXPONENTIAL-WRAPPED MECHANISMS: DIFFEREN TIAL PRIVACY ON HADAMARD MANIFOLDS MADE PRACTICAL ｜指数包装机制：Hadamard流形上的实用化差分隐私

研究机构：新加坡南洋理工大学、加拿大阿尔伯塔大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94173753)

> 导读 流形数据（如SPD矩阵）的隐私保护面临几何兼容性与计算效率的双重困境。现有黎曼拉普拉斯机制依赖MCMC采样，在高维空间下计算成本呈指数级增长，且无法统一支持多种隐私定义。本文提出指数包装（Exponential-Wrapped）机制，通过在切空间采样后利用指数映射推至流形，规避了MCMC瓶颈。该框架首次将$(\epsilon, \delta)$-DP、GDP和RDP统一扩展至一般Hadamard流形，实现了理论完备性与工程可行性的平衡，但在非Hadamard流形上的适用性仍存疑。

## 研究背景

当医疗影像中的扩散张量数据被建模为对称正定矩阵（SPDM）时，其内在几何结构要求隐私机制必须尊重流形约束。欧氏空间中的高斯机制直接嵌入流形会扭曲几何结构，导致效用损失。这一困境催生了黎曼几何下的差分隐私（Differential Privacy, DP）研究，其核心在于利用切空间（Tangent Space）作为线性化桥梁，在保持几何一致性的前提下注入噪声。

流形上的DP机制早期由Reimherr et al. (2021)奠基，其黎曼拉普拉斯机制虽实现了$\epsilon$-DP，但采样过程依赖马尔可夫链蒙特卡洛（MCMC），在SPDM等高维空间需上万次迭代才能收敛，计算开销巨大。后续工作如Utpala et al. (2023b)将$(\epsilon, \delta)$-DP扩展至SPDM，但仅限于对数欧氏（Log-Euclidean）度量下的平坦空间，缺乏通用性；Jiang et al. (2023)虽推广了高斯DP（GDP），但校准算法受限于常曲率空间。这些方法均未能解决“高维流形上高效采样”与“多隐私定义统一”这两个核心瓶颈。本文切入点在于利用Hadamard流形（非正曲率完备单连通流形）的Cartan-Hadamard定理，将流形分布构造转化为切空间分布的指数映射推前，从而在理论上统一多种DP定义，在工程上消除MCMC依赖。

## 核心方法

### 方法参照系

流形DP的标准流程是在流形上定义概率密度并采样。传统做法直接构造流形上的拉普拉斯或高斯分布，其密度函数涉及流形体积元与测地距离，采样需MCMC。本文的关键差异在于：不直接在流形上定义分布，而是定义切空间上的标准分布，通过指数映射$\text{Exp}_{p_0}$推前至流形，利用Hadamard流形上$\text{Log}_{p_0}$的全局定义性保证映射的双射性。

### 指数包装分布构造

设计动机在于解决MCMC采样在高维SPDM空间中的计算爆炸问题。传统黎曼拉普拉斯机制需迭代求解流形上的随机微分方程，而本文通过推前映射将采样简化为切空间上的标准分布采样。对于Hadamard流形$M$，设$p_0 \in M$为基点，$\eta \in M$为中心，$\sigma > 0$为速率，指数包装拉普拉斯分布（EWL）定义为切空间分布$h(u) \propto \exp(-\|u - \text{Log}_{p_0}\eta\|/\sigma)$经$\text{Exp}_{p_0}$推前的概率测度：

$$
\Lambda(A) = \mu(\text{Log}_{p_0}(A)), \quad \forall A \in \mathcal{B}(M)
$$

其中$\mu$为切空间$T_{p_0}M$上的概率测度。该公式的物理含义是：流形上的样本$X$等价于切空间样本$U$经指数映射后的结果，即$X = \text{Exp}_{p_0}(U)$。采样时仅需从切空间分布$h$中抽取$U$，再计算$\text{Exp}_{p_0}(U)$，避免了流形上的迭代优化。

### 多隐私定义统一校准

设计动机在于解决现有方法仅支持单一隐私定义（如$\epsilon$-DP或GDP）且校准算法依赖特定曲率的问题。本文通过指数包装高斯分布（EWG）统一支持$(\epsilon, \delta)$-DP、GDP和RDP。对于GDP，机制输出$Y \sim \text{EWG}(p_0, f(D), \sigma)$，其满足$\mu$-GDP当且仅当$\sigma = \Delta/\mu$，其中$\Delta$为查询函数的敏感度。该校准公式简洁且无需数值积分，与Jiang et al. (2023)中需求解无穷积分不等式的复杂校准形成鲜明对比。对于RDP，机制满足$(\alpha, \epsilon)$-RDP当且仅当$\sigma = \Delta/\sqrt{2\epsilon/\alpha}$。这种统一性源于切空间高斯分布的解析性质，使得隐私预算与噪声强度的关系在不同流形几何下保持一致。

## 实验评估

实验在SPDM空间（Log-Cholesky、Log-Euclidean、仿射不变度量）及双曲空间上进行，基线为Reimherr et al. (2021)的黎曼拉普拉斯（RL）机制。RL机制依赖MCMC采样，burn-in设为10,000次；本文EWG机制仅需切空间采样与指数映射。在OCTMNIST数据集（5×5 SPDM，Log-Euclidean度量）上，EWG在四个类别中均优于RL的效用（即释放的Fréchet均值与真实均值的黎曼距离更小），且运行时间降低数个数量级。

| 机制 | 采样方法 | 隐私定义 | 校准复杂度 | 高维可扩展性 |
| :--- | :--- | :--- | :--- | :--- |
| RL (Reimherr et al., 2021) | MCMC | $\epsilon$-DP | 高（需迭代） | 差 |
| EWG (本文) | 切空间采样+Exp | $(\epsilon, \delta)$-DP, GDP, RDP | 低（解析式） | 优 |

该论文实验数据不可得，未提供具体数值表格。据领域综述，SPDM聚类任务中FMC算法达到100%准确率，但本文聚焦隐私机制而非聚类，二者评估指标不同。本文未对比Utpala et al. (2023b)的切空间高斯机制，尽管后者在Log-Euclidean度量下是本文EWG的特例，这一缺失限制了通用性优势的完整验证。

评估边界方面，实验仅覆盖Hadamard流形（非正曲率），未测试正曲率流形（如球面）上的性能，而球面在形状分析中常见。代码未公开，但算法1提供了伪代码，超参数（如footpoint $p_0$）的选择对效用有影响，论文建议根据数据分布先验选择，但未提供自适应选择算法。

## 关联研究分析

从问题动机看，本文与Riemannian Flow Matching (Ruscelli et al., 2025)同属流形生成/隐私方向，但前者聚焦统计量释放（如Fréchet均值），后者聚焦生成模型训练。Ruscelli et al.利用测地线插值实现无模拟流匹配，而本文利用指数映射实现无MCMC采样。二者差异根源在于任务特性：统计量释放需精确的隐私-效用权衡，而生成模型更关注样本多样性。本文未探索生成模型场景，其指数包装机制是否适用于流匹配中的噪声注入，论文未给出回答。

从方法设计看，本文与Utpala et al. (2023b)的切空间高斯机制存在包含关系：后者是前者在Log-Euclidean度量下的特例。Utpala et al.限于平坦空间，而本文推广至一般Hadamard流形。这一推广的关键在于利用Cartan-Hadamard定理保证$\text{Log}_{p_0}$的全局定义性，使得切空间采样与流形样本的一一对应成立。然而，Utpala et al.的封闭形式计算在Log-Euclidean度量下更简单，本文的通用性是否以牺牲计算效率为代价，论文未提供详细对比。

## 总结

本文要解决的核心矛盾是流形DP机制在高维空间下的计算不可行性与隐私定义碎片化。现有方法依赖MCMC采样且仅支持单一隐私定义，而本文利用Hadamard流形的几何性质，通过指数包装将采样简化为切空间操作，并统一推导了$(\epsilon, \delta)$-DP、GDP和RDP的校准公式。实验证明EWG在OCTMNIST上效用优于RL且运行时间降低数个数量级。本文的边界在于仅适用于非正曲率流形，未测试正曲率场景，且footpoint选择依赖先验知识。当数据分布高度非均匀时，固定footpoint是否导致效用显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94173753)