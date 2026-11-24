# ACL-Findings2026最新论文 ｜SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models ｜多模态思维链忠实性诊断与校准

研究机构：西安电子科技大学、新加坡国立大学

作者：Weijiang Lv、Yaoxuan Feng、Xiaobo Xia 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07833)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07833)

> 多模态大语言模型（MLLMs）的思维链（Chain-of-Thought, CoT）常被假设为视觉证据的忠实映射，但现有研究多聚焦于感知幻觉，忽视了“看到正确区域却生成错误解释”的推理级不忠实。本文通过图像差异描述任务剥离语言先验，构建SPD-Faith Bench基准，揭示感知盲区与感知-推理解离两种失效模式。基于注意力衰减与残差流漂移的机制分析，提出免训练框架SAGE，通过动态视觉路由、FFN抑制与对比解码对齐感知与生成。该工作填补了多模态CoT忠实性评估空白，但其干预幅度有限，未解决深层表征的根本解耦。

## 研究背景

当MLLMs处理视觉问答时，模型往往依赖语言先验而非视觉信号生成CoT。这种依赖导致生成的推理步骤看似连贯，实则与底层视觉决策脱节，即“表演性推理”。为量化这种脱节，需区分感知层面的幻觉（描述不存在的物体）与推理层面的不忠实（逻辑矛盾或证据缺失）。传统基准如POPE仅评估物体存在性，无法捕捉推理过程中的因果断裂，因此需要一种能强制模型依赖视觉证据的诊断设置。

多模态CoT忠实性研究长期滞后于文本领域。文本CoT忠实性评估已发展出FaithCoT-Bench等实例级基准，但多模态场景下，视觉信号的引入使得“忠实性”定义复杂化：模型可能正确感知视觉区域，却在生成阶段被参数化先验覆盖。现有方法如VCD（Visual Contrastive Decoding）仅缓解物体幻觉，未触及推理逻辑的因果对齐。本文切入点在于利用图像差异描述（Image Difference Caption, IDC）任务，通过成对图像比较限制语言捷径，将视觉感知与文本生成解耦，从而显式诊断CoT的忠实性。

## 核心方法

### 方法参照系

本文问题属于多模态CoT忠实性诊断与干预。与文本CoT忠实性评估（如FaithCoT-Bench）不同，多模态场景需额外处理视觉信号路由问题。标准流程包括：构建视觉-文本对齐基准、诊断失效模式、设计干预机制。本文差异在于引入图像差异任务作为“视觉测谎仪”，并基于内部激活分析设计免训练干预。

### 动态视觉路由与FFN抑制

设计动机：浅层注意力被系统提示抑制，深层视觉信号衰减，导致感知盲区。本文在注意力计算中引入动态增强因子，浅层直接放大视觉注意力权重，深层根据注意力衰减程度自适应调整。公式为：

$$ A_t^{[vis]} \leftarrow A_t^{[vis]} + \alpha \cdot (A_t^{[sys]} + A_t^{[prompt]}) $$

其中 $\alpha=0.1$。该操作补偿浅层信息瓶颈，防止视觉特征在早期被压制。同时，监测MHA与FFN残差更新的KL散度，当散度超过阈值时，通过系数 $\beta=0.9$ 抑制FFN贡献：

$$ h_{\ell+1} \leftarrow h_{\ell+1/2} + \beta \cdot \text{FFN}(h_{\ell+1/2}) $$

FFN层主导表征转换，抑制其过度干预可防止参数化先验覆盖视觉信号，从而缓解感知-推理解离。

### 视觉锚定对比解码

设计动机：即使注意力正确定位，生成文本仍可能描述错误属性，即“看到但撒谎”。本文构建二值掩码 $M$，遮挡视觉注意力图与Token Activation Map (TAM) 的交集区域，生成辅助路径logits $L_{aux}$。最终logits调整为：

$$ L_{final} = L_{main} + \eta \cdot \text{ReLU}(L_{main} - L_{aux}) $$

其中 $\eta=0.5$。该对比解码强制生成对齐视觉证据，过滤未接地幻觉，确保CoT严格基于所见内容。

## 实验评估

实验在SPD-Faith Bench（3,000图像对）、POPE、MME上进行，基线包括VCD、ICD、OPERA、AGLA等视觉幻觉缓解方法，但未对比文本CoT忠实性基准（如FaithCoT-Bench），因任务模态不同。SAGE在POPE上F1达86.2%，超越AGLA的84.6%；在SPD-Faith Bench上，DRF从Greedy的29.5%提升至33.7%，CR从38.2%降至43.8%（注：CR为矛盾率，越低越好，但表中显示SAGE CR为43.8%高于Greedy 38.2%，此处需澄清：原文Table 10显示SAGE CR为43.8%，Greedy为38.2%，但正文称“reduction in Contradiction Rate”，存在矛盾。经核查，Table 10中CR列为↑，即越高越好？不，CR是Contradiction Rate，应越低越好。但Table 10标题为“CR↑”，且SAGE 43.8 > Greedy 38.2，这与正文“reduction in CR”矛盾。可能原文有误，或CR定义不同。根据Figure 3，CR是Contradiction Rate，应惩罚矛盾，故越低越好。但Table 10中SAGE CR 43.8 > Greedy 38.2，且标为best，这不合逻辑。可能Table 10中CR列实际是“Consistency Ratio”？不，Figure 3明确CR为Contradiction Rate。此处存在数据矛盾，按原文Table 10数值报告，但指出矛盾。

| 方法 | DS↑ | DQR↑ | TF1↑ | CF1↑ | CR↑ | DRF↑ |
|---|---|---|---|---|---|---|
| Greedy | 42.8 | 65.0 | 51.6 | 38.3 | 38.2 | 29.5 |
| VCD | 44.3 | 67.0 | 53.6 | 39.6 | 39.4 | 31.2 |
| SAGE | 46.2 | 67.2 | 55.4 | 42.1 | 43.8 | 33.7 |

SAGE在DS、TF1、CF1、DRF上均最优，但CR（矛盾率）反而升高，与正文“reduction in CR”矛盾，可能为原文笔误或指标定义差异。消融显示，Stage I（See）提升DS至45.2%，Stage II（Analyze）提升CF1至41.4%，Stage III（Generate）最终DRF达33.7%。

评估边界：SPD-Faith Bench仅限图像差异任务，未覆盖VQA等复杂推理；SAGE为免训练干预，需推理时架构适配，计算开销未报告；代码开源，但超参数（$\alpha, \beta, \eta$）敏感性分析显示，$\eta=0.5$时DRF最高，$\beta=0.9$时MME分数最优。

## 关联研究分析

与FaithCoT-Bench相比，本文引入视觉维度，但缺乏跨模态统一指标。FaithCoT-Bench评估文本CoT与内部计算的一致性，而本文聚焦视觉证据与CoT的对齐。差异根源在于任务特性：多模态CoT的忠实性不仅依赖逻辑一致性，还依赖视觉信号的正确路由。本文未探索视觉信号在长链推理中的累积衰减，可能因图像差异任务步骤较短。

与ProFIL相比，本文采用推理时干预而非训练式过滤。ProFIL通过探针过滤RL训练消除表演性推理，而SAGE通过动态路由与对比解码在推理时校准。差异在于计算成本与效果：SAGE免训练，但DRF仅提升4.2%；ProFIL需训练，但可能更彻底地解决解耦。本文未对比训练式方法，可能因多模态训练成本高（如FRIT需16×A100）。

## 总结

本文核心矛盾是多模态CoT的视觉感知与文本生成解耦，现有方法仅缓解幻觉而未触及推理忠实性。本文通过图像差异任务剥离语言先验，揭示感知盲区与感知-推理解离，并基于注意力衰减与FFN漂移设计SAGE框架。SAGE在SPD-Faith Bench上DRF达33.7%，CR 43.8%（与正文矛盾），POPE F1 86.2%。边界在于任务局限（仅图像差异）、免训练干预幅度有限、CR指标矛盾。当视觉差异复杂度增加时，SAGE的对比解码是否仍能维持忠实性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07833)