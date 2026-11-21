# ICLR2026最新论文 ｜IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs ｜IceCache：基于语义聚类的动态KV缓存卸载管理

研究机构：加拿大西蒙弗雷泽大学、美国哈佛大学

作者：Yuzhen Mao、Qitong Wang、Martin Ester 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10539)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10539)

> 长上下文推理中，键值缓存（KV Cache）随序列线性增长导致GPU显存溢出，现有卸载方法因静态分页与缺乏动态更新机制，在长生成任务中检索命中率低且性能退化。本文切入点在于将语义聚类引入分页存储，通过层级索引结构实现动态维护与高效检索。具体做法是构建DCI-tree将语义相似Token映射至同一物理页，结合CPU-GPU流水线重叠隐藏延迟。该方法在256 Token预算下保持99%精度，但依赖CPU内存充足假设，且未验证低带宽硬件下的延迟收益。

## 研究背景

自回归生成中，每个新Token需读取历史KV缓存，解码阶段受限于内存带宽而非算力。当序列长度增加，KV缓存大小线性增长，往往超过模型参数本身的显存占用，成为长上下文推理的主要瓶颈。为缓解此压力，主流方案将KV缓存卸载至CPU，仅保留少量关键条目在GPU。然而，现有卸载方法如MagicPig和PQCache依赖静态选择策略或近似注意力计算，缺乏对动态生成上下文的适应机制，导致在思维链（CoT）等长生成任务中，早期Token的量化误差或选择偏差随解码步数累积，性能显著退化。

PagedAttention（Kwon et al., 2023）确立了基于虚拟内存分页的KV缓存管理范式，解决了内存碎片化问题，但其页面按Token原始顺序填充。Quest和ArkVale在此基础上引入查询感知页面选择，但相关Token分散在不同页面，导致检索时需加载大量无关数据，命中率低。本文针对这一“语义局部性缺失”问题，提出IceCache，通过语义聚类重构页面组织方式，并引入动态更新的层级索引结构，旨在提升CPU-GPU传输的带宽利用率与检索精度。

## 核心方法

### 方法参照系

本文问题属于KV缓存卸载管理范畴，标准流程为：预填充阶段构建索引，解码阶段基于查询选择Top-k页面并加载至GPU。关键差异在于，传统方法按Token时序分页，而本文按Key Embedding语义相似度聚类分页，并支持解码时动态插入新Token。

### 语义聚类索引构建

设计动机在于解决按Token顺序分页导致的相关Token分散问题，提升页面选择命中率。IceCache在预填充阶段，对每个注意力头构建DCI-tree。首先，将Key Embedding $k_i$ 和Query Embedding $q_i$ 进行变换，以欧氏距离作为度量：

$$
TK(k_i) = \begin{bmatrix} k_i \\ c - \|k_i\|_2^2 \end{bmatrix}, \quad TQ(q_i) = \begin{bmatrix} q_i \\ c - \|q_i\|_2^2 \end{bmatrix}
$$

其中 $c \ge \max_j \|k_j\|_2^2$。该变换将内积最大化问题转化为欧氏距离最小化问题。随后，利用多级动态连续索引（M-DCI）算法，将Token随机提升至不同层级，形成几何分布的层级结构。每个节点对应一个物理内存页，存储语义相似的Token组。这种组织方式确保了查询相关Token在存储上的局部性，减少了无关数据的加载。

### 动态页面选择与流水线重叠

设计动机在于解决静态索引无法适应解码过程中新Token生成的问题，并隐藏CPU-GPU传输延迟。解码阶段，给定查询 $q$，IceCache在DCI-tree中执行近似最近邻（ANN）搜索，定位Top-k最相关页面。由于DCI-tree支持动态插入，新生成Token的Key Embedding可实时插入树结构，更新对应页面的元数据。同时，设计流水线机制，将CPU上的索引更新与GPU上的注意力计算重叠执行。设加载 $p$ 个页面，每页 $d$ 个条目，则加载Key数量 $N \le pd$。通过语义聚类，$p$ 值显著低于按顺序分页所需的页面数，从而降低内存带宽压力。

## 实验评估

实验在LongBench、GSM8K和Passkey Retrieval上进行，使用Llama3.1-8B、Mistral-7B、Qwen3-32B和LongChat-7B四个模型。基线涵盖驱逐类（SnapKV、StreamingLLM）和卸载类（MagicPig、PQCache、OmniKV、ArkVale），但缺失量化类（如KIVI）和架构类（如MLA）基线，限制了跨路线对比。

| 模型 | 预算 | 方法 | LongBench Avg. | GSM8K Acc. |
| :--- | :--- | :--- | :--- | :--- |
| Llama-3.1-8B | 256 | IceCache | 49.0 | - |
| Llama-3.1-8B | 256 | MagicPig | 44.6 | - |
| Llama-3.1-8B | 256 | PQCache | 47.3 | - |
| Mistral-7B | 256 | IceCache | 41.7 | 47.4 |
| Mistral-7B | 256 | MagicPig | 39.1 | 43.1 |
| Mistral-7B | 256 | PQCache | 49.2 | 46.2 |

在Llama-3.1-8B上，IceCache在256预算下平均准确率49.0%，优于MagicPig（44.6%）和PQCache（47.3%）。在Mistral-7B的GSM8K任务中，IceCache达到47.4%，接近全量KV缓存的48.2%，显著优于PQCache的46.2%。Passkey Retrieval测试显示，IceCache在所有预算（64/128/256）下均实现100%检索准确率，表明语义聚类对关键信息定位的有效性。

消融实验未单独报告，但预算变化显示边际收益递减：Llama-3.1-8B从64到256预算，准确率从47.8%提升至49.0%，仅增加1.2个百分点。这表明在低预算下，语义聚类的检索精度已接近饱和，进一步增加预算主要提升覆盖率而非精度。

评估边界方面，论文未报告延迟（TPOT）的具体数值，仅定性描述优于基线；未提供置信区间；代码已开源，但超参数（如提升比例 $r$）未详细列出。实验主要基于A100 GPU，未验证在低带宽硬件（如消费级GPU）上CPU-GPU传输延迟是否抵消精度收益。

## 关联研究分析

从问题动机看，IceCache与H2O（Zhang et al., 2024b）均基于注意力稀疏性假设，但H2O依赖累积注意力分数进行静态驱逐，无法适应解码过程中上下文语义的动态变化。IceCache通过语义聚类实现查询感知的动态检索，解决了H2O在长CoT任务中因滞后性导致的性能退化。这一差异源于任务特性：H2O适用于短上下文或静态Prompt，而IceCache针对长生成任务中Token重要性随时间演化的场景。

从方法设计看，IceCache与Quest（Tang et al., 2024）同属查询感知页面选择，但Quest基于Key向量特征上界估计页面重要性，而IceCache基于Key Embedding语义距离进行精确ANN检索。Quest的估计方法计算开销低，但精度受限于上界松紧度；IceCache的精确检索精度更高，但需通过流水线隐藏计算延迟。这一设计选择暗示，在CPU-GPU带宽充足时，精确检索的收益大于计算开销；但在带宽受限场景下，Quest的近似方法可能更具优势，论文未对此进行对比验证。

## 总结

IceCache旨在解决长上下文推理中KV缓存卸载的检索效率与动态更新矛盾。现有方法因静态分页和缺乏动态机制，在长生成任务中性能退化；IceCache通过语义聚类重构页面组织，并利用DCI-tree实现动态索引，从而提升检索命中率与带宽利用率。实验表明，在256 Token预算下，IceCache保持99%精度，且在GSM8K上接近全量KV缓存性能。然而，其依赖CPU内存充足假设，且未验证低带宽硬件下的延迟表现。当CPU-GPU带宽降至10GB/s以下时，流水线重叠是否仍能隐藏索引更新延迟，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10539)