# ACL-Findings2026最新论文 ｜TinyAttack: Exploring Stylistic Vulnerabilities in Large Language Models ｜基于Unicode样式变换的大语言模型对抗攻击

作者：Mamta Mamta、Bogdan Grecu、Oana Cocarascu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2eadcea15a32)

> 大语言模型（LLM）在自然语言处理任务中表现优异，但其对输入扰动的脆弱性在安全敏感场景（如仇恨言论检测、事实核查）中构成严重威胁。现有对抗攻击多聚焦于词级同义词替换或字符级增删，忽略了真实用户生成内容中日益普遍的Unicode样式变形（如上标、下标、特殊字体）这一隐蔽攻击向量。TinyAttack提出了一种利用五种Unicode样式变换的黑盒攻击框架，通过LLM自归因机制以极低查询成本定位关键词并实施扰动。该框架揭示了LLM分词器对非标准字符的处理缺陷，但其在不同模型间的鲁棒性差异及防御有效性仍存疑。

## 研究背景

对抗攻击的核心在于寻找满足语义相似度约束 $Sim(x, x') \geq \tau$ 且导致模型预测错误 $f(x') \neq f(x)$ 的扰动 $\delta$。在离散文本空间中，梯度优化失效，攻击通常依赖启发式搜索。传统方法如TextFooler（Jin et al., 2018）通过词重要性排序和同义词替换实现攻击，但这类扰动易被语义检查或拼写校正防御。随着LLM的普及，攻击面扩展至生成式模型，且真实部署中API查询预算受限，要求攻击方法具备高查询效率。

主流黑盒攻击路线分为语义重写与样式变形两类。语义重写依赖LLM生成变体，隐蔽性强但计算成本高；样式变形利用人机感知差异，通过视觉不可见或微弱的字符变化干扰模型，查询效率极高。然而，现有样式攻击研究多聚焦于传统NLP模型或简单的同形异义字（Homoglyphs），缺乏对LLM内部机制（特别是分词器）与复杂Unicode样式交互的系统性评估。TinyAttack的切入点在于：LLM预训练数据中缺乏对非标准Unicode样式字符的覆盖，导致分词器将这些字符拆分为多个子词或字节序列，破坏了语义映射，从而引发性能显著下降。

## 核心方法

### 黑盒词重要性评估参照系

在缺乏梯度访问的黑盒场景中，攻击需先定位对模型预测影响最大的词。标准流程是“词重要性排序”后“迭代扰动”。传统方法如Leave-One-Out（Jin et al., 2020）需对每个词单独查询模型，计算开销随词数线性增长。TinyAttack的关键差异在于引入两种低开销的重要性评估机制：Feature Ablation（特征消融）与LLM Self-Attribution（LLM自归因），旨在将查询次数从 $O(N)$ 降至常数级。

### LLM自归因与Unicode扰动生成

为降低API调用成本，TinyAttack提出LLM Self-Attribution方法。该方法利用LLM的指令跟随能力，仅需两次查询：第一次获取标签预测，第二次提示LLM直接输出各词的重要性分数。其重要性分数 $I(x_i)$ 定义为模型对真实标签 $y$ 的预测概率在移除词 $x_i$ 后的下降幅度：

$$ I(x_i) = P(y | X) - P(y | X \setminus \{x_i\}) $$

此公式物理含义为：词 $x_i$ 对维持正确预测的贡献度。相比Feature Ablation需 $N$ 次查询，Self-Attribution仅需2次，显著提升了黑盒攻击的效率。

基于重要性排序，TinyAttack设计了对抗生成器，应用五种Unicode样式变换：上标（Superscript）、下标（Subscript）、混合上下标（Super-Sub）、波浪钩（Squiggle & Hooks）及勒索信风格（Ransom Note）。这些变换仅改变字符的视觉渲染，不修改底层语义或句法结构。例如，将 "smoothies" 转换为 "ˢᵐᵒᵒᵗʰᶦᵉˢ"。攻击过程迭代扰动重要性最高的词，直至模型误分类或所有重要词被扰动。这种设计利用了分词器对非标准Unicode字符的“未知”处理机制，将其映射为多个子词或字节序列，从而干扰模型对输入语义的理解。

## 实验评估

实验在五个数据集（SST-3, HSOL, Climate-FEVER, UKP, SNLI）上评估了六个LLM（Llama-3-8B, Mistral-7B, Gemma-3-12B, Qwen2-7B, GPT-3.5, Gemini 2.0 Flash）在Zero-shot和Few-shot设置下的鲁棒性。基线包括标准字符扰动（插入、删除、重述、同义词）及随机词序扰动。

| 模型 | 任务 | Orig F1 | Superscript PDF (LSA) | Squiggle&Hooks PDF (LSA) | Ransom PDF (LSA) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Llama | Sent | 69.95 | 91.5 | 90.5 | 91.9 |
| Gemma | FV | 73.65 | 21.6 | 56.4 | 35.6 |
| GPT 3.5 | HS | 39.08 | 78.2 | 84.0 | 81.5 |
| Qwen | AM | 80.29 | 56.3 | 85.0 | 55.3 |

数据显示，所有模型在所有Unicode扰动下均出现显著性能下降。Llama在SST-3上对Ransom扰动的PDF高达91.9%，表明其极度脆弱。相比之下，Gemma在FV任务上对Superscript扰动的PDF仅为21.6%，显示出相对鲁棒性。消融实验表明，LLM Self-Attribution在Few-shot设置下比Feature Ablation更有效，因为上下文示例增强了LLM对词重要性的理解。此外，随机词序扰动的Perturbation Ratio（PR）普遍高于TinyAttack，证明基于重要性的排序策略能更高效地定位攻击目标。

评估边界方面，论文未报告置信区间，且部分模型（如GPT 3.5在NLI任务）仅预测单一类别，限制了结果的可比性。代码已开源，但超参数细节（如提示词模板）需查阅附录。

## 关联研究分析

从问题动机看，TinyAttack与SAD（Zhang et al., 2025）同属样式变形路线，但SAD聚焦于传统NLP模型，利用注意力重要性评分（AIS）和分词不稳定性评分（TIS）定位关键词，而TinyAttack针对LLM，引入LLM Self-Attribution以降低查询成本。这一差异源于LLM的黑盒特性：传统模型可访问内部注意力权重，而LLM API通常仅返回输出，迫使攻击者利用模型自身的推理能力进行归因。TinyAttack的Self-Attribution机制在Few-shot下表现更优，暗示上下文学习可能增强了LLM对语义重要性的元认知，但这一机制在Zero-shot下的稳定性仍需进一步验证。

从方法设计看，TinyAttack与TDOA（Wang et al., 2025）形成互补。TDOA解决动态输出空间（如多标签、生成任务）的攻击问题，通过聚类代理模型将动态标签转化为静态标签；TinyAttack则聚焦静态标签任务下的样式脆弱性。两者共同揭示了LLM在不同维度（输出空间、输入样式）上的鲁棒性缺陷。TinyAttack未对比TDOA，也未评估样式攻击与语义攻击在相同查询预算下的效率权衡，这限制了对其在真实对抗场景下相对优势的判断。

## 总结

TinyAttack旨在解决LLM对Unicode样式扰动的脆弱性问题，抓住了分词器对非标准字符处理不当这一被忽略的机制。通过LLM Self-Attribution降低查询成本，并设计五种Unicode变换，实现了高效黑盒攻击。实验证明，Llama等模型在SST-3上PDF高达91.9%，而Gemma在FV上仅21.6%，揭示了模型间鲁棒性的显著差异。论文边界在于未评估NFKC等归一化预处理对攻击的防御效果，且Few-shot防御的失效表明现有提示工程无法解决根本问题。当分词器词表覆盖度增加时，样式攻击的PDF是否显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2eadcea15a32)