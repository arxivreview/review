# ACL-Findings2026最新论文 ｜Representation-Guided Parameter-Efficient LLM Unlearning ｜表示几何引导的低秩大语言模型遗忘

作者：Zeguan Xiao、Lang Mo、Yun Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17396)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d626cf0a2b4)

> 大语言模型（LLM）遗忘面临的核心矛盾是：在移除敏感知识的同时，必须维持模型在保留集上的通用效用。现有基于参数重要性（如Fisher信息）的低秩适应（LoRA）方法因“超叠加”现象导致参数多义性，难以精准隔离遗忘与保留知识，常引发效用崩溃。本文提出ReGLU，通过表示空间几何解耦替代参数统计量估计，利用平衡协方差矩阵初始化LoRA并引入正交损失约束更新方向。该方法在TOFU和WMDP基准上显著优于FILA和VILA，但其有效性局限于参数高效微调框架，未验证全参数场景下的深层知识擦除能力。

## 研究背景

当LLM执行遗忘任务时，目标是将模型行为调整为仅基于保留集 $\mathcal{D}_r$ 训练的状态，同时彻底移除遗忘集 $\mathcal{D}_f$ 的影响。这一过程通常通过低秩适应（LoRA）实现，即仅更新权重矩阵的低秩增量 $\Delta W = BA$，以规避全参数微调的高昂计算成本。然而，LoRA的初始化策略直接决定了优化轨迹的收敛性与最终性能，传统方法依赖Fisher信息（FI）估计参数重要性，但FI假设参数与单一概念一一对应，这在LLM中并不成立。

LLM参数普遍存在“超叠加”（Superposition）现象，即单个参数同时编码多个语义概念，导致基于FI的参数重要性估计失效：被标记为“遗忘相关”的参数往往对保留集性能至关重要。FILA（Cha et al., 2025）和VILA（Kim et al., 2025）虽通过FI引导初始化改善了LoRA遗忘效果，但仍受限于参数空间的多义性，无法在几何层面解耦遗忘与保留表征。本文切入点在于：参数重要性不可靠，但表示子空间（Representation Subspace）具有可分解性，可通过协方差结构识别遗忘集高方差、保留集低方差的判别方向，从而在初始化与正则化阶段显式控制更新方向。

## 核心方法

### 方法参照系

LoRA-based LLM遗忘的标准流程包含两阶段：（1）基于某种统计量（如FI）初始化LoRA矩阵 $A, B$；（2）在遗忘损失与保留损失加权下优化 $A, B$。本文问题与该流程的关键差异在于：初始化依据从参数梯度统计量（FI）替换为表示空间协方差几何结构，且引入显式正交约束保护保留集主成分。

### RILA：表示引导的LoRA初始化

FILA和VILA通过FI比值 $S = F_\theta(\mathcal{D}_f)/F_\theta(\mathcal{D}_r)$ 确定参数重要性，但FI在非零期望下作为方差度量存在偏差（Kim et al., 2025）。本文提出RILA（Representation-guided Initialization of Low-rank Adaption），直接建模“差分能量”目标：最大化遗忘集输出范数变化，最小化保留集输出范数变化。设计动机是规避参数多义性，转向表示空间几何解耦。具体地，计算遗忘集与保留集输出表征的协方差矩阵 $\text{Cov}_F$ 和 $\text{Cov}_R$，构造平衡协方差矩阵：

$$ \text{Cov}_\Delta = (1-\beta)\text{Cov}_F - \beta\text{Cov}_R $$

其中 $\beta \in [0,1]$ 平衡遗忘与保留权重。提取 $\text{Cov}_\Delta$ 的前 $r$ 个特征向量 $Q_r$，初始化 $B_{\text{init}} = Q_r$，$A_{\text{init}} = Q_r^\top W_0$。该初始化确保LoRA更新 $\Delta W$ 初始对齐于遗忘集高方差、保留集低方差的判别子空间，从源头抑制对保留知识的干扰。

### ROL：表示正交损失

RILA提供初始子空间对齐，但优化过程中LoRA更新可能偏离该子空间，侵入保留集表征区域。本文引入ROL（Representation Orthogonal Loss），通过正交约束限制LoRA上投影矩阵 $B$ 与保留集主成分基 $P_B$ 的夹角。设计动机是防止训练动态中更新方向漂移至保留知识敏感区域。具体地，对保留集输出表征协方差矩阵进行特征分解，提取前 $k$ 个特征向量构成正交基 $P_B \in \mathbb{R}^{d_{\text{out}} \times k}$，定义损失：

$$ \mathcal{L}_{\text{ROL}} = \|B^\top P_B\|_F^2 $$

该损失惩罚 $B$ 的列向量与 $P_B$ 列向量的余弦相似度，迫使LoRA更新 $\Delta h = B(Ax)$ 落在保留集表征子空间的正交补中，从而在几何层面隔离遗忘与保留知识。最终优化目标为 $\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{forget}}(\mathcal{D}_f) + \gamma \mathcal{L}_{\text{retain}}(\mathcal{D}_r) + \lambda \mathcal{L}_{\text{ROL}}$，其中 $\mathcal{L}_{\text{forget}}$ 可选GD或IHL。

## 实验评估

实验在TOFU（200个虚构作者档案）和WMDP（生物安全/网络安全多选题）上进行，模型包括Phi-1.5B、Llama-2-7B和Zephyr-7B-beta。基线覆盖FILA、VILA及GD/IHL损失函数，但缺失NPO、SimNPO等偏好优化类强基线，也未对比全参数微调方法，限制了与领域SOTA的直接可比性。

| 模型 | 方法 | Forget 1% ↑ | Forget 5% ↑ | Forget 10% ↑ | AVG. ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phi-1.5B | GD + ReGLU | -0.8 | -9.9 | -11.2 | -7.3 |
| Phi-1.5B | IHL + ReGLU | -0.1 | -5.4 | -7.7 | -4.4 |
| Llama-2-7B | GD + ReGLU | -0.6 | -12.9 | -13.3 | -8.9 |
| Llama-2-7B | IHL + ReGLU | -0.7 | -5.4 | -1.1 | -2.4 |

TOFU结果显示，IHL + ReGLU在Phi-1.5B上平均FQ达-4.4，显著优于GD + FILA（-7.5）和GD + VILA（-9.3）；Llama-2-7B上IHL + ReGLU平均FQ为-2.4，优于GD + FILA（-9.7）。WMDP上，GD + ReGLU平均准确率35.1%，低于原始模型54.6%，优于GD + VILA（38.1%）；IHL + ReGLU（41.4%）优于IHL + FILA（48.8%）和IHL + VILA（51.0%）。

消融实验表明，RILA和ROL单独使用均优于基线，但组合后效果最佳，验证了初始化与正则化的协同效应。$\beta$ 参数在0.3时达到“甜点”，WMDP-Cyber准确率降至30.1%，TOFU-10% FQ为-2.1；$\beta$ 偏离0.3时性能显著下降，表明平衡子空间识别对超参数敏感。LoRA秩 $r$ 增大至70B时，FILA/VILA的保留集干扰指标（$1-s$）从0.09/0.07升至0.19/0.27，而RILA + ROL保持0.12/0.29，说明表示几何约束对秩变化更鲁棒。

评估边界方面，TOFU的FQ为log-scaled值，与领域综述中BLEU协议不可直接比较；WMDP仅报告准确率，未提供MMLU效用细节（仅声明≥95%）。代码已开源，但超参数搜索范围未完全披露，且未报告置信区间，数值比较需谨慎。

## 关联研究分析

从问题动机看，ReGLU与FILA/VILA同属LoRA初始化优化路线，但根源差异在于对“超叠加”现象的处理方式。FILA/VILA依赖Fisher信息，其理论假设参数与概念一一对应，这在LLM中因多义性而失效；ReGLU转向表示协方差几何，利用子空间可分解性规避参数多义性。这一差异并非任务特性决定，而是论文对FI理论局限的主动修正，但论文未验证表示子空间解耦在分布偏移（如保留集与预训练数据分布差异大）下的鲁棒性，查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，ReGLU与NPO（Zhang et al., 2024）同属“遗忘-保留”双目标优化，但NPO通过偏好优化框架抑制有害内容生成，属于输出级行为抑制；ReGLU通过正交损失约束LoRA更新方向，属于机制级表征干预。NPO未涉及参数初始化，而ReGLU未采用偏好优化损失，二者在优化目标与干预层级上存在根本差异。ReGLU的几何约束是否比NPO的分布约束更彻底地擦除深层知识，论文未提供对抗攻击或重学习测试来验证，这一盲区限制了其鲁棒性评估的完整性。

## 总结

ReGLU解决的核心矛盾是LoRA遗忘中参数多义性导致的遗忘-保留权衡失衡。其切入点在于：参数重要性估计因超叠加失效，但表示子空间几何结构可解耦遗忘与保留知识。方法上，RILA通过平衡协方差矩阵初始化LoRA，ROL通过正交损失约束更新方向，二者协同实现几何层面的知识隔离。实验证明，IHL + ReGLU在TOFU上平均FQ达-4.4（Phi-1.5B），WMDP上准确率降至35.1%，显著优于FILA/VILA。然而，论文仅在LoRA框架内验证，未对比全参数微调，也未提供对抗攻击下的鲁棒性测试，无法确认表示几何解耦是否触及深层表征结构。当保留集与预训练数据分布差异显著时，平衡协方差矩阵的特征向量是否仍能准确捕捉判别方向，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_8d626cf0a2b4)