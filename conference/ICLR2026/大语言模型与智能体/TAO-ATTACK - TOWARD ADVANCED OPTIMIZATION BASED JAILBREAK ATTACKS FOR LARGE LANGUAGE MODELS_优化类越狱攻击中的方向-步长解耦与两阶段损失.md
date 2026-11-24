# ICLR2026最新论文 ｜TAO-ATTACK: TOWARD ADVANCED OPTIMIZATION BASED JAILBREAK ATTACKS FOR LARGE LANGUAGE MODELS ｜优化类越狱攻击中的方向-步长解耦与两阶段损失

研究机构：大连理工大学

作者：Zhi Xu、Jiaqi Li、Xiaotong Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97164175)

> 优化类越狱攻击旨在通过梯度引导离散token后缀优化，突破大语言模型的安全对齐。现有方法如GCG和I-GCG虽能生成有害前缀，但常陷入拒答残留或伪有害输出，且点积排序混淆了更新方向与步长，导致收敛低效。本文提出TAO-Attack，通过两阶段损失函数抑制拒答与伪有害，并引入方向优先token优化（DPTO）策略解耦方向与步长。该方法在多个开源模型上实现了100%攻击成功率，但闭源模型迁移性仍有限，且未解决生成内容的可读性问题。

## 研究背景

当攻击者试图通过追加后缀诱导模型生成有害内容时，模型往往在生成目标前缀后插入拒答语句，或生成看似有害实则安全的“伪有害”输出。这种失效模式源于安全对齐的浅层性：模型仅在表面特征上表现出拒绝，而在深层推理中仍可能泄露有害内容。为量化这种失效，攻击者需优化后缀以最大化有害前缀的条件概率，同时最小化拒答与伪有害输出的概率。

优化类越狱攻击的主流路线是GCG（Zou et al., 2023），它通过贪心坐标下降算法优化离散token后缀，将越狱攻击形式化为离散文本空间的搜索问题。然而，GCG及其变体MAC、I-GCG存在两个核心瓶颈：一是单一目标前缀优化无法区分真有害与伪有害输出，导致攻击成功率受限于模型的拒答机制；二是点积排序混淆了梯度方向与步长，导致token更新不稳定，收敛速度慢。TAO-Attack的切入点在于解决这两个被忽略的点：通过两阶段损失函数动态切换优化目标，以及通过DPTO策略显式解耦方向与步长，从而提升攻击效率与输出质量。

## 核心方法

### 方法参照系

优化类越狱攻击的标准流程是：给定恶意查询 $x_Q$ 和目标前缀 $x_T$，优化后缀 $x_S$ 以最小化损失 $L(x_Q \oplus x_S) = -\log p(x_T | x_Q \oplus x_S)$。GCG通过计算梯度与token嵌入的点积来排序候选token，选择点积最大的token进行更新。本文问题与该通用流程的关键差异在于：GCG的点积排序无法区分方向对齐与步长大小，且单一损失函数无法处理拒答与伪有害输出。

### 两阶段损失函数

GCG的单一损失函数无法区分拒答与伪有害输出，导致模型在生成目标前缀后仍可能插入拒答语句或安全免责声明。TAO-Attack引入两阶段损失函数，第一阶段使用拒答感知损失 $L_1$ 抑制拒答，第二阶段使用有效性感知损失 $L_2$ 惩罚伪有害输出。

$$
L_1(x_Q \oplus x_S) = -\log p(x_T | x_Q \oplus x_S) + \alpha \log p(r_j | x_Q \oplus x_S)
$$

其中 $r_j$ 是拒答集合 $R$ 中的第 $j$ 个拒答响应，$\alpha > 0$ 平衡有害前缀生成与拒答惩罚。当Rouge-L相似度 $Rouge-L(x_{[1]_T}, x_T) \geq \tau$ 时，切换至第二阶段：

$$
L_2(x_Q \oplus x_S) = -\log p(x_T | x_Q \oplus x_S) + \beta \log p(x_O | x_Q \oplus x_S \oplus x_{[1]_T})
$$

其中 $x_O$ 是目标前缀后的剩余续写，$\beta > 0$ 控制对伪有害续写的惩罚。这一设计解决了GCG无法区分真有害与伪有害输出的问题，确保模型生成真正有害的内容。

### 方向优先token优化（DPTO）

GCG的点积排序混淆了梯度方向与步长，导致token更新不稳定。TAO-Attack提出DPTO策略，先筛选方向对齐的候选token，再评估步长大小。对于候选token $v$，计算其位移与负梯度方向的余弦相似度：

$$
C_{i,v} = \frac{(\mathbf{e}_v - \mathbf{e}_i) \cdot (-\nabla_{\mathbf{e}_i} L)}{\|\mathbf{e}_v - \mathbf{e}_i\| \|\nabla_{\mathbf{e}_i} L\|}
$$

选择余弦相似度最高的top-$k$候选token，再计算投影步长：

$$
S_{i,v} = -\nabla_{\mathbf{e}_i} L \cdot (\mathbf{e}_v - \mathbf{e}_i)
$$

通过温度缩放softmax将步长转换为概率分布，采样更新token。这一设计解决了GCG点积排序导致的更新不稳定问题，提升了收敛效率。

## 实验评估

实验在AdvBench基准上进行，对比GCG、MAC、I-GCG等优化类攻击方法。TAO-Attack在Llama-2-7B-Chat、Mistral-7B-Instruct-0.2和Qwen2.5-7B-Instruct上均达到100%攻击成功率，且迭代数显著低于I-GCG（如Mistral 86 vs 406）。

| 方法 | Llama-2-7B-Chat ASR | Llama-2-7B-Chat Iterations | Mistral-7B-Instruct-0.2 ASR | Mistral-7B-Instruct-0.2 Iterations |
| :--- | :--- | :--- | :--- | :--- |
| I-GCG | 68% | 604 | 80% | 406 |
| TAO-Attack | 92% | 305 | 100% | 86 |

消融实验显示，两阶段损失与DPTO策略均对攻击成功率有显著贡献。移除DPTO后，攻击成功率从100%降至65%，迭代数从243增至620。移除两阶段损失后，攻击成功率从100%降至55%，迭代数从243增至702。

| 组件 | ASR | Iterations |
| :--- | :--- | :--- |
| GCG (Softmax) | 55% | 702 |
| + Stage One | 55% | 687 |
| + Stage Two | 65% | 620 |
| + DPTO | 100% | 261 |
| Full TAO-Attack | 100% | 243 |

评估边界方面，论文未报告闭源模型的详细迭代数，且未提供代码URL。超参数如温度 $\gamma$ 和阈值 $\tau$ 的敏感性未充分讨论，可能影响复现性。

## 关联研究分析

从问题动机看，TAO-Attack与I-GCG（Jia et al., 2025）均旨在提升优化类攻击的效率，但I-GCG通过多模板和自适应多坐标更新解决单一模板限制，而TAO-Attack通过两阶段损失解决拒答与伪有害输出问题。I-GCG的伪有害输出问题源于其单一损失函数无法区分真有害与伪有害，而TAO-Attack的两阶段设计显式处理了这一失效模式。

从方法设计看，TAO-Attack与GCG（Zou et al., 2023）共享离散token优化框架，但GCG的点积排序混淆方向与步长，导致更新不稳定。TAO-Attack的DPTO策略通过余弦相似度筛选方向对齐的候选token，再评估步长大小，解决了GCG的更新不稳定问题。这一设计差异源于GCG的点积排序无法区分方向与步长，而TAO-Attack的解耦设计显式处理了这一几何缺陷。

## 总结

TAO-Attack要解决的核心矛盾是优化类越狱攻击中拒答残留与伪有害输出导致的攻击成功率受限，以及点积排序混淆方向与步长导致的收敛低效。本文抓住的切入点是两阶段损失函数与DPTO策略，通过动态切换优化目标和显式解耦方向与步长，提升了攻击效率与输出质量。实验证明，TAO-Attack在多个开源模型上达到100%攻击成功率，且迭代数显著低于I-GCG。本文的边界在于闭源模型迁移性有限（GPT-3.5 Turbo ASR 82%），且未解决生成内容的可读性问题。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97164175)