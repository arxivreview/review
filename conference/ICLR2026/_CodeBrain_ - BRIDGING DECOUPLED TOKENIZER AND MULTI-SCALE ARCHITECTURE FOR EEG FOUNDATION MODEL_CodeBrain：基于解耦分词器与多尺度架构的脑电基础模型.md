# ICLR2026最新论文 ｜_CodeBrain_ : BRIDGING DECOUPLED TOKENIZER AND MULTI-SCALE ARCHITECTURE FOR EEG FOUNDATION MODEL ｜CodeBrain：基于解耦分词器与多尺度架构的脑电基础模型

研究机构：新加坡国立大学、新加坡南洋理工大学

作者：Jingying Ma、Feng Wu、QIKA LIN 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6889847)

> 导读 脑电基础模型（EEG Foundation Models, EFMs）旨在从非平稳神经信号中提取跨任务通用表示，以突破手工特征在临床场景下的泛化瓶颈。现有方法依赖单一向量量化码本与全连接Transformer，导致表示缺乏神经生理学可解释性，且无法高效建模脑信号的小世界拓扑结构。CodeBrain通过时频解耦分词器与状态空间模型（State Space Model, SSM）变体架构，在保留信号细节的同时实现了Token级别的语义对齐。该模型在异常检测与事件检测上表现优异，但其可解释性证据仅基于激活统计，缺乏因果推断验证，且未解决跨被试身份混淆问题。

## 研究背景

脑电信号解码面临的核心困境是信号的非平稳性与个体异质性。为应对这一挑战，研究者引入自监督预训练范式，通过掩码重建学习通用表示。然而，直接重建原始信号受噪声干扰严重，促使领域转向基于码本的离散化表示学习。这一转变虽提升了鲁棒性，却引入了新的问题：单一码本将时频域信息混合，导致Token难以对齐至具体的神经事件或频谱节律，且全连接注意力机制与脑信号的稀疏长程依赖结构不匹配。

当前EEG基础模型的主流路线包括对比学习（如BENDR）与重建预测（如LaBraM、CBraMod）。LaBraM通过向量量化神经频谱预测实现了跨数据集通用表征，但其单一码本设计混淆了时频域特征；CBraMod采用Criss-Cross Transformer提升时空建模能力，但全连接注意力的二次复杂度限制了长序列效率。这些方法在提升性能的同时，牺牲了表示的神经生理学可解释性，且未能有效捕获补丁内部的局部瞬态事件。CodeBrain的切入点在于，通过解耦时频域表示与引入稀疏高效的多尺度架构，同时解决可解释性缺失与计算效率低下的问题。

## 核心方法

### 方法参照系

CodeBrain属于“重建主导”路线的改进分支，遵循“分词-预训练-微调”的标准范式。与LaBraM等使用单一VQ码本的方法不同，CodeBrain将分词过程解耦为时频两个独立分支，并将骨干网络从Transformer替换为基于状态空间模型（SSM）的卷积结构，以适配脑信号的稀疏拓扑特性。

### TFDual-Tokenizer：时频解耦分词

传统VQ-VAE框架假设视觉特征同质，使用单一码本即可有效量化。然而，EEG信号具有异构性，时域波形与频域节律反映不同的脑活动方面。CodeBrain提出TFDual-Tokenizer，将EEG补丁 $\mathbf{x} \in \mathbb{R}^L$ 分解为时域与频域两个独立码本 $V_t, V_f \in \mathbb{R}^{K \times D}$。时域分支结合对比学习与重建损失，频域分支重建幅度与相位。其核心损失函数为：

$$
\mathcal{L}_{total} = \mathcal{L}_{rec}^{t} + \mathcal{L}_{con}^{t} + \mathcal{L}_{rec}^{f}
$$

其中 $\mathcal{L}_{rec}^{t}$ 为时域重建损失，$\mathcal{L}_{con}^{t}$ 为SimCLR对比损失，$\mathcal{L}_{rec}^{f}$ 为频域幅度相位重建损失。这种解耦设计二次扩展了表示空间，使Token能够分别对齐至瞬态神经事件（如睡眠纺锤波）与频谱节律（如Delta波），解决了单一码本混淆域特定模式导致的判别力下降问题。

### EEGSSM：小世界拓扑多尺度架构

现有EFM采用全连接Transformer，其二次复杂度与脑信号的稀疏长程依赖结构不匹配，且忽略补丁内部局部依赖。CodeBrain提出EEGSSM，结合结构化全局卷积（SGConv）与滑动窗口注意力（SWA）。SGConv基于SSM理论，通过FFT加速卷积计算，复杂度为 $O(N \log N)$，其卷积核 $K$ 由稀疏参数化与衰减系数 $\alpha$ 初始化：

$$
K = \sum_{i=0}^{N-1} \alpha^i \cdot \text{Upsample}(w_i)
$$

该公式通过指数衰减结构模拟脑信号的长程依赖稀疏性。SWA则捕获补丁内部的局部瞬态事件。动态位置编码进一步学习空间通道相关性，使模型适应异构电极布局。这一设计在保持全局建模能力的同时，显著降低了计算开销，并弥补了先前方法忽略局部神经事件的缺陷。

## 实验评估

CodeBrain在TUEG语料库上预训练，并在10个数据集的8个下游任务上进行评估。基线覆盖EEGNet、LaBraM、CBraMod等主流方法，但缺失NeuroTTT等在线适应方法。在TUAB异常检测任务上，CodeBrain取得0.9030的AUROC，显著优于CBraMod的0.8811；在TUEV事件检测任务上，其Cohen’s Kappa达到0.6912，高于CBraMod的0.6671。这些结果表明，解耦分词器与SSM架构在临床事件检测上具有优势。

| 数据集 | 任务 | 指标 | CodeBrain | CBraMod | LaBraM |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TUAB | 异常检测 | AUROC | 0.9030 ± 0.0009 | 0.8811 ± 0.0015 | 0.8426 ± 0.0237 |
| TUEV | 事件检测 | Cohen’s Kappa | 0.6912 ± 0.0101 | 0.6671 ± 0.0107 | 0.6409 ± 0.0065 |
| FACED | 情绪识别 | Cohen’s Kappa | 0.5406 ± 0.0084 | 0.5118 ± 0.0118 | 0.5320 ± 0.0083 |
| ISRUC S3 | 睡眠分期 | Cohen’s Kappa | 0.7671 ± 0.0091 | 0.7598 ± 0.0109 | 0.7168 ± 0.0119 |

消融实验显示，移除滑动窗口注意力（SWA）导致FACED数据集Cohen’s Kappa从0.5406骤降至0.1936，表明局部依赖建模对情绪识别至关重要。移除SGConv层则使ISRUC S3性能从0.7671降至0.5478，验证了全局稀疏卷积的有效性。时频解耦码本（Dual）在所有数据集上均优于单一时域（Temporal）或频域（Frequency）码本，其中FACED上Dual比Mixed码本高0.0730的Kappa值，证实了解耦设计的必要性。

评估边界方面，论文报告了5个随机种子的均值与标准差，代码与权重已开源。然而，TUAB与TUEV数据源自预训练语料库TUEG，尽管论文声称通过早期停止（Epoch 10）缓解过拟合，但数据泄露风险仍未完全排除。此外，论文未报告计算效率的具体对比，仅通过FLOPs分析表明SSM架构优于Transformer，缺乏实时部署的吞吐量实测数据。

## 关联研究分析

从问题动机看，CodeBrain与LaBraM均致力于解决EEG表示的噪声鲁棒性，但LaBraM依赖单一VQ码本，其Token缺乏明确的神经生理学对应关系。CodeBrain通过时频解耦，将Token映射至具体的频谱节律与瞬态事件，回应了领域内关于“可解释性缺失”的批评。然而，CodeBrain的可解释性证据仅基于Token激活统计，未提供因果推断或生理探针验证，这与领域共识中“需神经生理学机制验证”的要求存在差距。LaBraM的单一码本设计虽牺牲了可解释性，但其离散化过程更简洁，可能在某些低资源场景下具有更高的训练稳定性。

从方法设计看，CodeBrain与CBraMod均关注时空依赖建模，但CBraMod采用Criss-Cross Transformer，其全连接注意力机制在长序列上效率较低。CodeBrain引入SGConv，基于SSM理论实现 $O(N \log N)$ 复杂度，理论上更适合长序列EEG。然而，论文未在长序列任务（如连续睡眠监测）上直接对比两者的效率与精度，仅通过FLOPs分析间接证明优势。此外，CodeBrain未采用在线适应策略（如NeuroTTT），其跨被试泛化能力主要依赖大规模预训练与动态位置编码，未验证在个体差异显著场景下的鲁棒性。CBraMod的Criss-Cross结构虽计算成本高，但其时空解耦设计可能在某些特定任务上提供更精细的特征提取，两者在效率与精度的权衡上尚需更多实证支持。

## 总结

CodeBrain旨在解决EEG基础模型中可解释性缺失与计算效率低下的矛盾。现有方法依赖单一码本与全连接Transformer，导致表示难以对齐神经事件且长序列建模成本高。CodeBrain通过TFDual-Tokenizer解耦时频域，并引入SGConv与SWA构建多尺度架构，在TUAB上取得0.9030的AUROC，在TUEV上取得0.6912的Cohen’s Kappa，验证了其在临床事件检测上的优势。然而，论文的可解释性证据仅基于激活统计，缺乏因果推断验证，且未解决跨被试身份混淆问题。当支持集增大或个体差异显著时，解耦Token的神经生理学对齐是否仍具鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6889847)