# ACL-Findings2026最新论文 ｜Unlocking the Edge deployment and ondevice acceleration of multi-LoRA enabled one-for-all foundational LLM ｜冻结图约束下的多任务LLM端侧部署与自推测加速

研究机构：三星研究院

作者：Sravanth Kodavanti、Sowmya Vajrala、Srinivas Miriyala 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18655)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18655)

> 移动端LLM部署面临内存、延迟与运行时灵活性的三重硬约束，传统静态合并LoRA或云端协同方案无法在冻结推理图中实现多任务动态切换与低延迟并发生成。本文切入点在于将LoRA权重作为运行时输入注入单一冻结图，结合多流并发解码与无草稿模型的自推测策略，在NPU上实现单图多任务。该框架在三星Galaxy S24/S25上验证了可行性，但LoRA维度固定与静态预测嵌入限制了其泛化边界。

## 研究背景

当LLM从云端迁移至手机NPU时，推理图必须冻结以保障实时性，这导致无法像服务器端那样动态重编译或加载不同任务模型。参数高效微调（PEFT）中的LoRA技术虽能降低适配成本，但传统做法在训练后静态合并权重，使得多任务部署需存储多个完整模型副本，内存开销呈线性增长。为突破此瓶颈，需将LoRA从“权重修改”转变为“运行时输入”，使单一基础模型图能动态响应不同任务指令。

现有端侧推理优化多聚焦于量化压缩或云边协同，前者牺牲精度换取内存，后者依赖网络通信且无法离线运行。主流方案如MobiLlama或SPADE虽解决了单任务部署或云端调用减少问题，但未解决单设备内多任务并发与动态切换的矛盾。本文针对这一空白，提出在冻结图内通过掩码机制与多流解码实现多LoRA复用，将多任务推理从“多模型存储”转化为“单模型多路径执行”，从而在严格内存约束下保持任务灵活性。

## 核心方法

### 方法参照系

端侧LLM部署通常遵循“量化-编译-静态加载”流程，其中LoRA权重在编译前合并至基座模型。本文的关键差异在于打破“权重静态化”假设，将LoRA矩阵视为与Token并列的运行时输入，使推理图结构不变而功能动态变化，解决了冻结图无法重编译导致的任务切换延迟与内存冗余问题。

### LoRA-as-Input动态注入机制

传统LoRA合并后，切换任务需重新加载整个模型权重，内存占用为 $N_{tasks} \times M_{base}$。本文设计将LoRA权重 $W_{lora}$ 作为输入张量传入冻结图，通过掩码选择激活特定LoRA分支。其核心公式为：

$$ Y = W_{base}X + s \cdot (M_{task} \odot W_{lora})X $$

其中 $M_{task}$ 为任务掩码，$s$ 为缩放因子。该设计使内存占用降至 $M_{base} + \sum_{i=1}^{N} M_{lora_i}$，且任务切换仅需更新掩码指针，无需重编译。实验表明，相比静态合并，该方法在2任务场景下内存从1.1 GB降至686 MB，延迟从75 ms降至52 ms，验证了运行时注入在NPU上的可行性。

### 多流并发解码与自推测加速

多流并发解码（CTG）利用风格变体由首Token驱动的特性，在单次前向传播中并行生成8个风格输出。其掩码解码公式为：

$$ P(t_i | t_{<i}, \mathcal{S}_j) = \text{Softmax}(f_\theta(t_{<i}, \mathcal{S}_j) \cdot M_{mask}) $$

其中 $\mathcal{S}_j$ 为第 $j$ 个风格嵌入，$M_{mask}$ 屏蔽非目标风格路径。该机制将8次串行解码压缩为1次并行解码，延迟降低6倍。针对解码阶段内存带宽瓶颈，本文提出动态自推测解码（DS2D），通过Prefix Tuning使模型在单步预测 $1+m$ 个Token，无需独立草稿模型。其树状分支验证公式为：

$$ \text{Accept}(t_{draft}) = \mathbb{I} \left( \frac{p_{target}(t_{draft})}{p_{draft}(t_{draft})} \geq \min(1, \tau) \right) $$

该策略将解码吞吐量提升2.3倍，且兼容冻结图约束，避免了草稿模型带来的额外内存开销。

## 实验评估

实验在Samsung Galaxy S24（SM8650）与S25（SM8750）上进行，基线包括Full Precision、静态LoRA合并及无DS2D的自回归解码。缺失与llama.cpp、T-SAR等通用端侧框架的直接对比，但覆盖了NPU专用优化路径。

| 方法 | 内存 (MB) | 首Token延迟 (ms) | 生成延迟 (ms) |
| :--- | :--- | :--- | :--- |
| Base (1B) | 718 | 45 | 22 |
| LoRA-as-Input (2-tasks) | 686 | 45 | 25 |
| LoRA Masking (2-tasks) | 894 | 45 | 30 |

LoRA-as-Input在内存与延迟上均优于Masking方案，验证了运行时注入的效率优势。3B模型在GS25上，DS2D使Correction任务Tokens/sec从22.3提升至44.84，加速比达2.01倍。

| 任务 | DS2D前 Tokens/sec | DS2D后 Tokens/sec | 加速比 |
| :--- | :--- | :--- | :--- |
| Correction | 22.3 | 44.84 | 2.01 |
| Style | 25.21 | 39.67 | 1.57 |
| Summarization | 24.12 | 41.46 | 1.72 |

DS2D加速效果因任务而异，Summarization任务加速比最高（1.72倍），而Style任务最低（1.57倍），表明推测解码对长文本生成任务的收益更显著。评估协议未报告置信区间，且仅使用内部多语言任务，缺乏ShareGPT等标准基准的泛化性验证。

## 关联研究分析

从问题动机看，本文与SelectInfer同属端侧内存优化路线，但SelectInfer基于神经元激活稀疏性仅加载核心神经元，而本文基于LoRA动态加载实现任务切换。SelectInfer的稀疏性假设在长尾任务中可能失效，而本文的LoRA-as-Input依赖LoRA维度一致性，两者在灵活性上形成互补：前者牺牲任务多样性换取内存节省，后者牺牲LoRA异构性换取任务动态性。

从方法设计看，本文DS2D与SPADE均利用推测解码加速，但SPADE依赖边缘小模型生成草稿，本文通过Prefix Tuning实现自推测。SPADE的草稿模型需额外内存，本文的静态预测嵌入虽节省内存，但无法适应高语义方差输入。这一差异源于任务特性：SPADE面向通用文本生成，本文面向固定风格变体，后者对预测嵌入的静态性容忍度更高。

## 总结

本文核心矛盾在于冻结推理图与多任务动态切换的冲突，切入点是将LoRA从权重修改转为运行时输入，结合多流解码与自推测加速。实验证明该框架在NPU上实现3倍内存节省与2倍Token速率提升，但LoRA维度固定与静态预测嵌入限制了其适用场景。当任务间LoRA维度差异显著或输入语义方差较大时，该框架的内存效率与推测接受率是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18655)