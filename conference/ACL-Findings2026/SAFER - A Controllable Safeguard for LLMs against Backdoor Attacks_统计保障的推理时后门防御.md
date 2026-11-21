# ACL-Findings2026最新论文 ｜SAFER: A Controllable Safeguard for LLMs against Backdoor Attacks ｜统计保障的推理时后门防御

研究机构：新加坡南洋理工大学

作者：Zirui Hu、Zheng Zhang、Yingjie Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_67768403d2df)

> 大语言模型在金融、医疗等高利害场景中部署时，推理时后门防御面临的核心矛盾是：现有评分函数虽能区分干净与投毒样本，但缺乏对假接受率（False Acceptance Rate, FAR）的显式统计控制，导致安全阈值无法量化。本文切入点在于，将后门检测重构为多重假设检验问题，通过估计样本为干净的局部似然概率，求解约束优化问题以在满足用户指定FAR阈值的同时最大化干净样本接受率。该方法无需已知后门样本校准，仅依赖干净校准集与混合测试集。其价值在于提供了渐近FAR保证，但实验仅覆盖词法触发器，对语义级攻击的鲁棒性存疑。

## 研究背景

当防御者面对一个已被投毒的模型时，其核心困境在于无法预知攻击者植入的具体触发器模式。传统推理时防御方法（如STRIP、RAP）通过计算模型激活或表示分布的差异来生成评分，但评分阈值通常基于启发式规则或固定分位数设定。这种设定缺乏统计基础，导致在投毒比例变化或攻击类型切换时，FAR可能突破安全阈值。FAR定义为被错误接受的投毒样本占所有被接受样本的比例，在贷款审批等场景中，即使FAR仅为1%，也可能导致巨额信用风险。

现有推理时防御路线主要分为两类：一类基于鲁棒性指标（如STRIP），另一类基于表示分布差异（如SCM）。这些方法在特定攻击下表现良好，但缺乏跨攻击类型的统一误差控制机制。SCM虽设计了假拒绝率控制，但对FAR的控制并不稳定。本文的切入点在于，借鉴多重假设检验中的局部FDR（Local False Discovery Rate）概念，将评分函数输出的隐式信号转化为显式的统计量，从而在无需已知后门样本的条件下，实现FAR的渐近控制。

## 核心方法

### 方法参照系

本文问题属于推理时后门检测，与通用异常检测流程的关键差异在于：防御者无法获取投毒样本进行校准，且需同时控制FAR与最大化Power（干净样本正确接受率）。通用流程通常假设正负样本分布已知，而本文仅拥有干净校准集 $D_{cal}$ 与混合测试集 $D_{test}$。

### 不确定性量化

设计动机在于解决评分函数无法直接提供统计保证的问题。本文首先估计干净样本先验概率 $\hat{\pi}_0$。基于Storey估计法，对每个测试样本 $x_j$ 计算经验p值 $\hat{p}_j = \frac{\sum_{i \in [n_0]} I(G(w_i) < G(w_j))}{n_0 + 1}$，其中 $G(\cdot)$ 为单调变换。随后，通过阈值 $\lambda$ 估计干净样本比例：

$$ \hat{\pi}_0 = \frac{\sum_{j \in [n_1]} I(\hat{p}_j > \lambda)}{n_1 \cdot (1 - \lambda)} $$

该公式利用p值在干净样本下服从均匀分布的性质，通过高p值样本的数量反推干净样本占比，解决了先验概率未知的问题。

### 决策优化

设计动机在于将FAR控制转化为可求解的优化问题。定义不确定性分数 $\hat{L}_j = \frac{\hat{\rho}_c(w_j) \cdot \hat{\pi}_0}{\hat{\rho}_{mix}(w_j)}$，其中 $\hat{\rho}_c$ 和 $\hat{\rho}_{mix}$ 分别为干净与混合评分分布的密度估计。FAR可表示为：

$$ \widehat{FAR}(\hat{\delta}) = \frac{\sum_{j \in [n_1]} (1 - \hat{L}_j) \cdot (1 - \hat{\delta}_j)}{1 \vee \sum_{j \in [n_1]} (1 - \hat{\delta}_j)} $$

本文求解约束优化问题：最大化 $\sum (1 - \hat{\delta}_j)$，使得 $\widehat{FAR}(\hat{\delta}) \le \alpha$。该优化通过贪心策略按 $\hat{L}_j$ 降序排列样本，依次接受直至FAR估计值触及阈值 $\alpha$，实现了FAR与Power的帕累托最优平衡。

## 实验评估

实验在Yelp、AGNews、HSOL三个文本分类数据集上，使用BERT-base-uncased、RoBERTa-Base、Pythia-1B作为受害模型，测试BadNets、AddSent、StyleBkd、SynBkd四种攻击。基线覆盖STRIP、BKI、RAP、CUBE、SCM，但缺失CSO-LLM、Semantic Drift等2025-2026年基于内部表示的最新方法。

| 方法 | Yelp-BadNets FAR | Yelp-BadNets Power | AGNews-StyleBkd FAR | AGNews-StyleBkd Power |
| :--- | :--- | :--- | :--- | :--- |
| BKI | 0.158 | 1.000 | 0.435 | 0.325 |
| CUBE | 0.002 | 0.997 | 0.004 | 0.901 |
| STRIP | 0.195 | 0.908 | 0.184 | 0.863 |
| RAP | 0.340 | 0.486 | 0.214 | 0.913 |
| SCM-md | 0.208 | 0.936 | 0.005 | 0.940 |
| SAFER-md | 0.033 | 0.833 | 0.000 | 0.847 |
| SAFER-badacts | 0.050 | 0.993 | 0.044 | 0.998 |

SAFER-badacts在Yelp-BadNets上FAR为0.050，Power为0.993，显著优于BKI（FAR 0.158）和STRIP（FAR 0.195）。在AGNews-StyleBkd上，SAFER-md实现FAR 0.000，但Power降至0.847，而SAFER-badacts保持FAR 0.044与Power 0.998，表明激活统计评分函数在风格攻击下更具鲁棒性。

投毒率从0.2增至0.6时，SAFER的FAR始终低于阈值 $\alpha=0.1$，而RAP的FAR在0.4投毒率下升至0.214，Power降至0.751。阈值 $\alpha$ 从0.01增至0.15时，SAFER的Power单调递增，FAR严格控制在 $\alpha$ 以下，验证了渐近保证的有效性。$\lambda=0.9$ 时性能最优，$\lambda$ 增大导致方差增加，FAR波动加剧。

评估边界在于：实验仅使用词法/句法触发器，未测试Cordyceps等语义级攻击；未报告计算效率；代码已开源，但超参数 $\lambda$ 的敏感性分析仅在Yelp上进行，跨数据集泛化性未充分验证。

## 关联研究分析

从问题动机看，SCM（Xian et al., 2023）控制假拒绝率，本文控制假接受率，二者互补。SCM的局限在于其阈值设定依赖校准集分布假设，当投毒比例变化时，FAR可能失控。本文通过局部FDR估计，将FAR控制与投毒比例解耦，这是任务特性决定的：高利害场景更关注“漏放”而非“误杀”。

从方法设计看，CSO-LLM（Li et al., 2026）基于类子空间正交化实现100%触发器逆向，但需白盒访问中间层特征。本文仅需模型输出与干净校准集，属于受限白盒。差异根源在于部署场景：API服务无法提供内部特征，本文方法更具工程落地性。但CSO-LLM在SST-2上ASR降至0.0%，本文在Yelp上FAR控制在0.05，因数据集与任务不同，不可直接比较。

## 总结

本文解决的核心矛盾是推理时后门防御缺乏FAR的显式统计控制。现有方法依赖启发式阈值，无法在投毒比例变化时保证安全。本文通过局部FDR估计与约束优化，实现了无需已知后门样本的渐近FAR控制。实验证明，在Yelp上SAFER-badacts的FAR为0.050，Power为0.993，优于所有基线。其边界在于仅测试词法触发器，未验证语义级攻击下的鲁棒性。当攻击者采用Cordyceps等隐写术触发器时，评分函数 $\hat{\rho}_c$ 与 $\hat{\rho}_{mix}$ 的分布假设是否仍成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_67768403d2df)