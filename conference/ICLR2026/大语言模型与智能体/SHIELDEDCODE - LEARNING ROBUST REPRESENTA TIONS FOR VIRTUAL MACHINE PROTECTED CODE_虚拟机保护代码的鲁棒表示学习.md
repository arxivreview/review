# ICLR2026最新论文 ｜SHIELDEDCODE: LEARNING ROBUST REPRESENTA TIONS FOR VIRTUAL MACHINE PROTECTED CODE ｜虚拟机保护代码的鲁棒表示学习

研究机构：中国科学院大学、美国明尼苏达大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_87671773)

> 传统虚拟机保护（VMP）依赖僵化的规则转换，易被逆向工程破解，且设计成本高。现有大语言模型（LLM）虽能生成代码，但缺乏对虚拟化机器码多态性的语义理解，无法有效生成或评估受保护代码。本文提出 ShieldedCode，通过构建源-虚拟机（VM）配对数据，结合层级依赖建模与功能-保护对比学习，实现保护感知代码生成。该方法在 L0 级别 VM 代码生成上超越 GPT-4o，但在高保护级别下的泛化能力与真实逆向场景的对抗鲁棒性仍存疑。

## 研究背景

逆向工程通过静态与动态分析恢复软件逻辑，威胁知识产权安全。虚拟机保护（Virtual Machine Protection, VMP）将原生指令替换为自定义虚拟指令，由专用解释器执行，旨在增加分析难度。然而，传统 VMP 系统依赖规则基转换，产生高度规律的虚拟机结构，成为自动化逆向工具的目标。

LLM 在代码生成与理解上取得进展，但主要聚焦于标准汇编或中间表示（如 LLVM IR），其结构相对稳定。VMP 字节码经历多态扩展、虚拟寄存器重命名及解释器驱动语义，与标准汇编存在显著领域差距。现有二进制代码表示学习方法（如 jTrans, CodeBERT-Binary）未针对 VMP 的多态性与保护强度分级进行优化，导致模型难以区分不同保护级别的语义等价性。

本文切入点在于将软件保护形式化为表示学习问题。不同于关注漏洞检测或修复，ShieldedCode 旨在通过生成多态 VM 代码最大化逆向难度，同时保持功能等价性。这一视角填补了 LLM 在虚拟化机器码保护领域的空白，从“消除漏洞”转向“增加攻击成本”。

## 核心方法

### 方法参照系

本文问题可置于二进制代码表示学习框架下，但关键差异在于目标对象为多态 VM 字节码而非标准汇编。标准流程通常通过对比学习对齐源-二进制对，但忽略保护强度分级与多态性带来的长距离依赖。本文引入保护感知目标，要求嵌入空间同时反映功能等价性与保护强度差异。

### 层级依赖建模

针对 VM 代码中指令间复杂的执行依赖，本文设计三级注意力掩码。在指令内级别，通过 `[VINST]` 标记聚合局部 token 交互；在前指令级别，当前指令 token 条件化于前一指令标记，捕捉寄存器复用等短程依赖；在指令间级别，当前 token 连接所有先前标记，编码长程上下文。该设计解决了标准因果掩码无法捕捉 VM 多态变换中分散控制流依赖的问题。

$$
\text{Mask}(x_t^{[k]}, x_j^{[l]}) = \begin{cases}
1 & \text{if } l < t \text{ or } (l = t \text{ and } j \le k) \text{ or } (l = t-1 \text{ and } j \in \text{Marker}) \\
0 & \text{otherwise}
\end{cases}
$$

此掩码强制模型在生成当前 token 时，显式参考前指令标记与全局指令标记，从而对齐 VM 代码的结构化依赖。

### 功能-保护对比学习

为克服 LLM 对表面语法模式的过拟合，本文联合优化语言建模损失与两种对比损失。功能对比学习（Functionality Contrastive Learning, FCL）拉近同一函数在不同保护级别下的嵌入，引入指数衰减权重 $w_{s,t} = \exp(-|s-t|/\tau_{fcl})$，使相邻级别对齐更强。保护对比学习（Protection Contrastive Learning, PCL）通过软边距约束，强制嵌入距离随保护级别差线性增长：

$$
\mathcal{L}_{pcl} = \sum_{s < t} \max(0, \beta(t-s) - m - d(e_f^{[s]}, e_f^{[t]}))
$$

其中 $\beta$ 为缩放因子，$m$ 为软边距。FCL 确保语义一致性，PCL 编码保护强度分层，两者协同使嵌入空间既保持功能聚类，又体现保护强度的线性分层。

## 实验评估

实验在 HumanEval-compile 与 BinaryCorp-VirtualAssembly 上进行，基线涵盖通用 LLM（GPT-4o, CodeLlama）及二进制方法（jTrans, BinDiff）。ShieldedCode 在 L0 VM 代码生成 Pass@1 达 26.95%，高于 GPT-4o 的 22.58%；在 O0+L1 二进制相似度检测 Recall@1 达 0.488，显著优于 jTrans (Linear Probe) 的 0.333。

| 方法 | Pass@1 (L0) | Pass@10 (L0) | Recall@1 (O0+L1) | MRR (O0+L1) |
|---|---|---|---|---|
| GPT-4o | 22.58 | 31.47 | 0.333 | 0.575 |
| jTrans (Linear Probe) | - | - | 0.333 | 0.575 |
| ShieldedCode | 26.95 | 35.68 | 0.488 | 0.575 |

消融实验显示，移除多态生成（ShieldedCode[-PG]）使 Pass@1 从 25.17% 降至 21.86%，移除对比学习（ShieldedCode[-CL-PG]）进一步降至 15.78%。这表明对比学习提供基础语义对齐，多态生成则显著提升高保护级别下的生成质量。

评估边界方面，Pass@1 仅验证功能正确性，未量化逆向难度；BinaryCorp 数据集规模有限，且未包含真实商业 VMP 工具的复杂混淆。论文未提供代码与超参数细节，可复现性受限。

## 关联研究分析

从问题动机看，ShieldedCode 与漏洞修复方法（如 ContraFix）均关注代码语义保持，但目标相反：前者增加分析难度，后者消除漏洞。ContraFix 依赖运行时证据反馈，而 ShieldedCode 通过对比学习静态编码保护强度，缺乏动态验证机制。这导致 ShieldedCode 生成的代码可能在静态相似度上表现优异，但在动态执行中暴露保护弱点。

从方法设计看，与 LLMCompiler 等二进制 LLM 相比，ShieldedCode 引入层级依赖建模与保护感知对比损失。LLMCompiler 聚焦 LLVM IR 的结构稳定性，而 ShieldedCode 处理 VM 字节码的多态性。然而，ShieldedCode 未探索检索增强生成（RAG）在保护知识注入中的潜力，对比学习可能难以覆盖所有保护变体，导致长尾保护级别的泛化不足。

## 总结

ShieldedCode 解决了传统 VMP 规则僵化与 LLM 缺乏 VM 语义理解之间的矛盾，通过层级依赖建模与功能-保护对比学习，实现了保护感知代码生成。实验表明其在 L0 级别生成与 O0+L1 相似度检测上优于 GPT-4o 与 jTrans，但高保护级别（L3）下 Pass@1 仅 14.71%，显示泛化瓶颈。当保护级别提升至 L3 时，对比学习的线性距离约束是否仍能准确反映多态变换的非线性复杂度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_87671773)