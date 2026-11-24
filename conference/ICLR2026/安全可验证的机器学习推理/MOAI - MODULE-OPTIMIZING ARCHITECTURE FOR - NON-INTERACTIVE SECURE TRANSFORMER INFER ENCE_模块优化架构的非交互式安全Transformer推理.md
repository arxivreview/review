# ICLR2026最新论文 ｜MOAI: MODULE-OPTIMIZING ARCHITECTURE FOR - NON-INTERACTIVE SECURE TRANSFORMER INFER ENCE ｜模块优化架构的非交互式安全Transformer推理

研究机构：新加坡南洋理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60015589)

> 同态加密（Fully Homomorphic Encryption, FHE）在Transformer推理中面临高昂的计算开销，导致现有方案难以满足实时性需求。MOAI通过设计一致的矩阵打包策略与无旋转非线性评估算法，消除了层间格式转换与密集的HE旋转操作。该方法在BERT-base上实现了2.36分钟/输入的单GPU推理时间，较SOTA方案THOR降低52.8%。其核心价值在于证明了架构级优化可显著缓解FHE瓶颈，但2.36分钟的延迟仍远高于实时交互场景的需求。

## 研究背景

当客户端将敏感数据上传至云服务提供商（CSP）进行模型推理时，数据隐私泄露风险迫使研究者寻求密态计算方案。全同态加密（FHE）允许在密文上直接执行计算，但CKKS方案中的HE旋转操作（HE Rotation）是计算密集型瓶颈，尤其在处理Softmax和LayerNorm等非线性函数时，传统方法需执行大量旋转以完成向量求和，导致推理延迟呈指数级增长。

FHE-based secure transformer inference的主流路线分为两类：一类是保持原始Transformer组件不变，通过优化密文操作降低开销（如NEXUS, THOR）；另一类是替换非线性函数为FHE友好近似（如Powerformer），但需重新训练模型。前者虽免重训，但THOR等方案因密文打包格式不一致，层间需频繁执行昂贵的格式转换与矩阵转置；后者虽效率较高，但通用性受限。MOAI的切入点在于：不修改模型结构，通过重构密文打包流与消除关键路径上的HE旋转，实现端到端的高效非交互式推理。

## 核心方法

### 方法参照系

标准FHE Transformer推理流程包含密文矩阵乘法、Softmax、LayerNorm及Bootstrapping。关键差异在于：传统方案（如THOR）在层间传递时，密文打包格式（行/列/对角）不匹配，需额外转换；而MOAI通过统一打包策略，使各层输出格式直接匹配下一层输入格式，消除转换开销。

### 一致矩阵打包与无旋转Softmax

传统Softmax评估需通过HE旋转累加密文内各slot数据，MOAI利用Lemma 4.1（方阵列和等于对角线和）设计对角打包（Diagonal Packing）下的无旋转算法。输入$QK^\top$采用对角打包，Softmax输出保持对角打包，直接作为下一矩阵乘法输入。该设计消除了Softmax与LayerNorm中的全部HE旋转，在BERT-base中节省2448次旋转。

$$
\sum_{i} \mathbf{c}_i^\top = \sum_{i} \text{Diag}_i(C)
$$

此公式表明，对角打包下无需旋转即可通过向量加法完成求和，物理含义是将求和操作从“单密文内slot移动”转化为“多密文同位置相加”。

### 列打包与交错批处理

矩阵乘法中，明文-密文乘法（如计算$Q,K,V$）采用列打包（Column Packing），避免HE旋转；密文-密文乘法（如$QK^\top$）结合交错批处理（Interleaved Batching），将多个向量交错打包至单密文，利用Lemma 3.2使内部旋转仅需1次HE旋转（传统需2次）。该策略使MOAI在所有矩阵乘法中HE旋转次数至少降低1.7倍。

$$
\text{Rot}_{jN/(2m)}(\tilde{\mathbf{x}}) = \text{Interleave}(\{\text{Rot}_j(\mathbf{x}^{(r)})\}_{r \in [N/(2m)]})
$$

此公式表明，交错批处理下的大步长旋转等价于各子向量的独立小步长旋转，物理含义是通过打包结构优化，将2次旋转合并为1次，直接减少密钥切换开销。

## 实验评估

实验在BERT-base（SST-2, QNLI, RTE）上评估，基线覆盖THOR（CCS'25）、Powerformer（ACL'25）及NEXUS（NDSS'25），未对比MPC路线（如Cheetah）或TEE混合方案。主结果如下：

| 方法 | 环境 | 总时间 (min/input) | 相对THOR降幅 |
|---|---|---|---|
| THOR | A100 GPU | 10.0 | — |
| MOAI | A100 GPU | 2.36 | 52.8% |
| Powerformer | A100 GPU | 5.74 | — |
| MOAI+Powerformer | A100 GPU | 2.55 | 55.7% (vs Powerformer) |

MOAI在相同A100环境下较THOR降低52.8%延迟，较Powerformer降低55.7%。消融显示，Softmax与LayerNorm的无旋转优化贡献最大：Softmax耗时从15.53s降至2.19s，LayerNorm从7.13s降至0.15s，表明非线性层是主要瓶颈。

评估边界：仅报告BERT-base（128 tokens）与LLaMA-3-8B（附录），未覆盖MoE架构；精度分析显示FHE引入误差对GLUE分数影响可忽略（SST-2从93.9降至93.8），但未报告置信区间。代码开源（GitHub: dtc2025ag/MOAI），超参数（$N=2^{16}$, 1743-bit模数）可复现，但GPU结果依赖H200/A100特定硬件。

## 关联研究分析

从问题动机看，MOAI与THOR同属“免重训”路线，但THOR因打包格式不一致需层间转换，MOAI通过统一列/对角打包流消除该开销。根源在于THOR未将打包策略作为全局优化目标，而MOAI将格式一致性纳入架构设计，这是任务特性（Transformer层间数据流固定）决定的优化空间。

从方法设计看，MOAI与Powerformer同属FHE优化，但Powerformer替换Softmax/LayerNorm为近似函数需重训，MOAI保持原始函数通过算法优化降低开销。MOAI将自身打包策略应用于Powerformer后仍获55.7%加速，表明其优化与模型结构解耦。然而，MOAI未探索MoE动态路由下的打包策略，稀疏架构中专家选择的不确定性是否破坏列/对角打包的一致性，论文未给出回答。

## 总结

MOAI解决的核心矛盾是FHE在Transformer推理中HE旋转与格式转换导致的高延迟。其切入点在于：传统方案将打包格式视为局部操作，MOAI将其重构为全局一致的架构约束，通过无旋转Softmax/LayerNorm与交错批处理消除关键路径瓶颈。实验证明，该策略在BERT-base上实现2.36分钟/输入，较THOR降低52.8%。边界在于：2.36分钟仍远高于实时交互需求，且未验证MoE架构下的扩展性。当输入序列长度从128扩展至2048时，对角打包的密文数量与Bootstrapping频率是否呈线性增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60015589)