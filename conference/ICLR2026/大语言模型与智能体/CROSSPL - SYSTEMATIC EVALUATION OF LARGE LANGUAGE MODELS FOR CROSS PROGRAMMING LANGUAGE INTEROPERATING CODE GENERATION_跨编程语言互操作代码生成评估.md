# ICLR2026最新论文 ｜CROSSPL: SYSTEMATIC EVALUATION OF LARGE LANGUAGE MODELS FOR CROSS PROGRAMMING LANGUAGE INTEROPERATING CODE GENERATION ｜跨编程语言互操作代码生成评估

研究机构：浙江大学、澳大利亚新南威尔士大学

作者：Zhanhang Xiong、Dongxia Wang、Yuekang Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42104021)

> 现有代码生成基准聚焦单语言函数级任务，无法衡量模型在真实多语言系统中处理进程间通信（IPC）与外部函数接口（FFI）的能力。本文通过挖掘19,169个真实GitHub仓库并设计156个有限状态机（FSM），构建了首个包含2,534个CPL互操作任务的基准。实验表明，当前SOTA模型在FFI任务上表现极差，揭示了单语言能力与跨语言互操作能力间的巨大鸿沟。该基准填补了CPL评估空白，但FSM对非标准协议变体的覆盖度存疑。

## 研究背景

现代软件系统普遍采用多编程语言（MPL）架构，超过80%的项目涉及两种及以上语言（Tomassetti & Torchiano, 2014）。这种异构性主要依赖两种机制实现协同：IPC通过Socket、gRPC等协议在独立进程间交换数据，要求严格遵循序列化与同步协议；FFI则允许同一进程内直接调用不同语言函数，需精确管理函数签名、类型转换及内存布局。任何细微错误均可能导致死锁或未定义行为，这对代码生成的鲁棒性提出了极高要求。

主流代码生成基准如HumanEval和SWE-bench均局限于单一语言环境，前者侧重Python函数级正确性，后者虽涉及仓库级上下文但仍限于单语言Bug修复。现有多语言基准如MultiPL-E仅测试同一逻辑在不同语言中的独立翻译能力，未涉及语言间的实际交互。这种评估缺失导致无法量化模型在真实MPL系统中的工程价值，尤其当IPC和FFI代码片段在大型代码库中稀疏分布且隐含于复杂依赖中时，手动收集与评估成本极高。

## 核心方法

### 基准构建参照系

传统基准构建依赖人工设计任务与单元测试，本文将其扩展至CPL场景。关键差异在于：IPC任务需验证协议状态转移的合规性，而非仅功能正确性；FFI任务需构建受控编译执行环境以验证跨语言调用。本文采用“真实仓库挖掘+形式化验证”策略，替代纯人工设计。

### FSM驱动的IPC任务挖掘与评估

针对IPC代码边界模糊与机制多样性的问题，本文设计了156个场景特定FSM。每个FSM基于官方IPC文档抽象出关键状态转移链，用于从真实仓库中自动检测并提取互操作代码片段。评估时，LLM生成的代码被输入对应FSM，若状态转移完整匹配则判定通过。该机制解决了传统单元测试无法捕捉协议违规（如遗漏Close操作或错误同步）的问题。

$$
\text{Pass}_{IPC} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}[\text{FSM}_i(\text{Code}_i) = \text{Accept}]
$$

其中 $\mathbb{I}$ 为指示函数，当生成代码在对应FSM中完成所有必要状态转移时取1。此公式将协议合规性量化为二元判定，避免了LLM-as-a-Judge的主观偏差。

### 受控环境下的FFI任务构建

FFI任务聚焦Python-C互操作，选用GNU Scientific Library（GSL）作为C代码源，因其自包含且可编译。构建流程包括：编译GSL为共享库（.so），LLM生成Python调用代码，在预置.so环境中执行并验证断言。失败案例通过LLM迭代修正，确保基准的可复现性。该设计规避了真实MPL项目依赖复杂导致执行不可行的问题，同时保留了FFI的核心挑战：符号解析、类型匹配与内存管理。

$$
\text{Pass}_{FFI} = \frac{1}{M} \sum_{j=1}^{M} \mathbb{I}[\text{Exec}(\text{Code}_j, \text{Env}_{GSL}) = \text{Success} \land \text{Assert}(\text{Out}_j) = \text{True}]
$$

该公式要求代码不仅执行成功，还需满足预定义断言，确保功能正确性。

## 实验评估

实验覆盖20个SOTA模型，包括GPT-4o、Qwen3系列、DeepSeek-V3等，采用Pass@1（贪心解码）和Pass@5（温度0.2，top-p 0.95）指标。基线覆盖通用模型与代码专用模型，但未对比专门的代码翻译模型。

| 模型 | CrossPL-IPC Pass@1 | CrossPL-FFI Pass@1 | CrossPL-FFI Pass@5 |
|---|---|---|---|
| GLM4-plus | 75.88% | 8.62% | 13.40% |
| GPT-4o | 73.81% | 19.54% | 26.46% |
| Qwen3-235b-a22b | 75.02% | 13.03% | 21.28% |
| Qwen2.5-coder-32b-instruct | 72.50% | 7.28% | 14.38% |

IPC任务中GLM4-plus表现最佳（75.88%），FFI任务中GPT-4o领先（19.54%），但均远低于单语言基准的90%+水平。FFI的Pass@5提升有限，表明多次采样难以弥补底层机制理解的缺失。

消融实验显示，Think Mode对IPC任务无益甚至有害（如Qwen3-235B Java从77.40%降至75.12%），但对FFI任务显著有效（Qwen3-32B从13.22%升至17.81%）。这暗示IPC依赖结构化模式匹配，而FFI需要显式推理处理内存与类型复杂性。替换构建流水线中的Extractor为Qwen3-4B导致样本量从1,982降至1,723，而替换Generator导致FFI有效样本从522骤降至65，表明FFI任务构建对模型能力更敏感。

评估边界方面，FSM仅覆盖156种标准IPC场景，未包含非标准协议变体；FFI仅限Python-C，未扩展至其他语言对。代码已开源，但FSM设计细节与GSL版本未完全披露，可能影响复现性。

## 关联研究分析

与Multi-LCB相比，后者测试同一问题在不同语言中的独立生成能力，而CrossPL测试语言间实际交互。这一差异源于任务本质：Multi-LCB关注语言泛化，CrossPL关注互操作鲁棒性。Multi-LCB未涉及IPC/FFI机制，因此无法揭示模型在协议合规与内存管理上的短板。CrossPL的FSM评估方法引入了形式化验证，而Multi-LCB依赖单元测试，前者能捕捉更细粒度的协议违规。

与SWE-bench相比，两者均从真实仓库挖掘任务，但SWE-bench聚焦单语言Bug修复，CrossPL聚焦跨语言互操作。SWE-bench的评估依赖执行测试，CrossPL的IPC评估依赖FSM状态匹配。这一差异导致SWE-bench无法评估IPC协议合规性，而CrossPL无法评估仓库级全局上下文。CrossPL的FFI任务构建借鉴了SWE-bench的执行验证思路，但通过GSL受控环境降低了依赖复杂性，牺牲了真实MPL项目的多样性。

## 总结

CrossPL旨在解决单语言基准无法评估CPL互操作能力的问题，通过FSM形式化验证与受控FFI环境构建，填补了该领域空白。实验证明FFI任务极具挑战性，最佳模型Pass@1仅19.54%，且Think Mode对IPC无效。其边界在于FSM覆盖度有限且FFI语言对单一。当IPC任务通过率较高时，是否源于训练数据中Socket代码的过拟合，而非真正的协议理解能力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42104021)