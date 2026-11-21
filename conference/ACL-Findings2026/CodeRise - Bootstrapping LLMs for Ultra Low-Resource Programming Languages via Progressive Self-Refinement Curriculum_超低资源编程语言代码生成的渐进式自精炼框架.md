# ACL-Findings2026最新论文 ｜CodeRise: Bootstrapping LLMs for Ultra Low-Resource Programming Languages via Progressive Self-Refinement Curriculum ｜超低资源编程语言代码生成的渐进式自精炼框架

研究机构：中国科学院大学、中国科学院

作者：Tengfei Wen、Xuanang Chen、Ben He 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dd9054980de6)

> 超低资源编程语言（ULRPLs）因公开语料极度匮乏，导致大语言模型（LLMs）无法通过常规预训练习得其语法与库函数，陷入“冷启动”困境。现有合成数据方法在ULRPLs上失效，因为模型初始能力近乎为零，无法生成任何有效代码样本，且直接提供完整语法文档会导致推理缓慢与数据分布长尾化。CodeRise通过两阶段框架解决此问题：第一阶段利用语法引导与模块加权采样生成种子数据，第二阶段移除语法提示，通过自适应课程学习与多轮自调试生成复杂高质量数据。该方法在Tengo和Janet语言上显著优于基线，但其性能上限受限于骨干模型的通用推理能力，且对完整语法文档的依赖仍是潜在瓶颈。

## 研究背景

当LLM面对Tengo或Janet等ULRPLs时，其训练分布中缺乏这些语言的token序列，导致模型无法生成语法正确的代码片段。这种数据稀缺性不仅体现在代码数量上，更体现在语言特性的覆盖度上，例如ULRPLs往往缺乏独特的文件扩展名，使得自动识别工具无法有效收集语料。为突破这一限制，研究者尝试利用LLM自身生成合成数据，即自指令（Self-Instruct）范式，但该范式假设模型具备目标语言的基础能力，而在ULRPLs场景中，模型初始能力为零，无法产生任何有效样本，导致自举过程无法启动。

主流路线试图通过提供完整语言语法文档作为上下文来缓解冷启动问题，但这带来了两个严重缺陷：一是极长的上下文导致推理速度大幅下降，二是生成的数据呈现严重的长尾分布，任务集中在字符串操作等通用编程模式上，缺乏对语言特定库函数的覆盖。CodeRise的切入点在于将语法引导与数据生成解耦，并通过课程学习机制逐步提升任务复杂度，同时引入跨语言调试策略以弥补模型在目标语言上的推理短板。

## 核心方法

### 方法参照系

CodeRise属于代码生成数据合成路线，其标准流程为：从种子语料提取概念，生成指令-代码对，并通过沙箱验证过滤错误样本。本文问题与该通用流程的关键差异在于，ULRPLs场景下模型无法直接生成有效代码，必须引入外部语法结构作为生成脚手架，且需解决生成数据的分布偏斜问题。

### 语法引导与模块平衡采样

Stage 1旨在解决冷启动问题，其设计动机是克服模型在ULRPLs上无法生成任何有效代码的失效。该阶段通过从开源代码片段提取编程概念，并引入对数逆频率模块采样策略，将标准库模块注入概念集以平衡数据分布。采样权重公式为：

$$ w_i = \log(c_i + 2)^p $$

其中 $c_i$ 是模块 $i$ 在正确解中出现的频率，$p$ 是控制加权强度的超参数。这一设计通过降低高频模块（如text）的采样概率，提升低频模块（如os, hex）的生成比例，从而缓解长尾分布。生成的指令-代码-测试三元组在沙箱中验证，仅保留通过所有测试的样本，确保种子数据集的语法正确性。

### 自适应课程学习与多轮自调试

Stage 2在Stage 1微调后的模型基础上，移除完整语法提示以提升生成效率，其设计动机是解决Stage 1中语法提示导致的推理缓慢与数据多样性不足问题。该阶段引入基于Pass@10的自适应难度控制器，动态调整Easy、Medium、Hard任务的采样概率。未归一化权重计算为：

$$ Weight_{hard} = \alpha \cdot p, \quad Weight_{medium} = C, \quad Weight_{easy} = \alpha \cdot (1 - p) $$

其中 $p$ 为当前Pass@10，$\alpha$ 和 $C$ 为超参数。随后通过softmax函数转换为概率。当代码生成失败时，系统启动多轮自调试机制：对于编译或运行时错误，利用编译器错误信息、调试指南和BM25检索的文档片段进行修正；对于逻辑错误，生成Python伪真值（Pseudo Ground Truth）进行跨语言对比分析，直至代码通过所有测试。这一机制将“失败即丢弃”策略转化为“迭代修正”，显著提升了复杂任务的数据生成成功率。

## 实验评估

实验在Tengo和Janet两种ULRPLs上进行，使用迁移的HumanEval-Tengo、MBPP-Tengo及自建TengoEval、JanetEval基准。基线覆盖无训练方法（Zero-Shot、Full-Syntax Prompting等）和训练方法（SelfCodeAlign、MultiPL-T、SPEAC）。CodeRise在Qwen-2.5-Coder-32B-Instruct上表现最佳，HumanEval-Tengo Pass@1达71.3%，TengoEval达60.0%，JanetEval达36.0%，均显著优于SelfCodeAlign（61.6%, 49.0%, 24.0%）和MultiPL-T（60.4%, 47.0%, 22.0%）。

| 模型 | 方法 | HumanEval Pass@1 | MBPP Pass@1 | TengoEval Pass@1 | JanetEval Pass@1 |
|---|---|---|---|---|---|
| Qwen-2.5-Coder-32B-Instruct | SelfCodeAlign | 61.6 | 65.1 | 49.0 | 24.0 |
| Qwen-2.5-Coder-32B-Instruct | MultiPL-T | 60.4 | 64.6 | 47.0 | 22.0 |
| Qwen-2.5-Coder-32B-Instruct | CodeRise | 71.3 | 75.5 | 60.0 | 36.0 |
| Qwen-2.5-Coder-7B-Instruct | SelfCodeAlign | 39.6 | 41.7 | 31.0 | 12.0 |
| Qwen-2.5-Coder-7B-Instruct | CodeRise | 50.3 | 57.9 | 39.0 | 20.0 |

消融实验未单独报告，但Stage 2移除语法提示后，生成效率提升且数据质量通过自调试机制保证。在7B模型上，CodeRise相比SelfCodeAlign在TengoEval上提升8.0个百分点，表明该方法对小模型同样有效。评估边界方面，论文未报告计算效率指标，且TengoEval和JanetEval为自建基准，缺乏跨语言通用性验证。代码已开源，但超参数 $\alpha, C, T, p$ 的具体取值未在正文中详细列出，可能影响复现性。

## 关联研究分析

从问题动机看，CodeRise与SelfCodeAlign均基于自指令范式，但SelfCodeAlign假设模型具备目标语言基础能力，而CodeRise针对ULRPLs冷启动问题，引入语法引导作为前置条件。这一差异源于ULRPLs数据稀缺性的极端程度，导致常规自举无法启动。从方法设计看，CodeRise与MultiPL-T均使用测试过滤，但MultiPL-T依赖高资源语言翻译，可能引入任务域偏移，而CodeRise直接生成目标语言代码，并通过跨语言伪真值调试弥补推理短板。这种设计选择反映了ULRPLs场景中翻译范式的局限性，即目标语言与源语言在编程范式上的差异（如Janet的栈式结构）可能导致翻译后的代码不符合目标语言惯用法。

## 总结

CodeRise解决了ULRPLs代码生成中因数据稀缺导致的冷启动问题，其切入点在于将语法引导与数据生成解耦，并通过课程学习与自调试机制逐步提升数据质量。该方法在Tengo和Janet上显著优于基线，HumanEval-Tengo Pass@1达71.3%，TengoEval达60.0%。其边界在于对完整语法文档的依赖，以及自建基准的通用性局限。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_dd9054980de6)