# CVPR2026最新论文 ｜Out of Sight, Out of Track: Adversarial Attacks on Propagation-based Multi-Object Trackers via Query State Manipulation ｜查询状态操纵下的传播式多目标跟踪对抗攻击

研究机构：美国加州大学尔湾分校

作者：Halima Bouzidi、Haoyu Liu、Yonatan Gizachew Achamyeleh 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.00452)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.00452)

> 传播式多目标跟踪（Tracking-by-Propagation, TBP）通过端到端架构解决了传统检测-关联解耦在复杂遮挡下的失效问题，但其引入的固定查询预算与递归记忆机制构成了新的攻击面。现有针对跟踪系统的对抗攻击均基于传统检测-关联（Tracking-by-Detection, TbD）架构设计，无法有效利用TBP特有的结构漏洞。本文提出FADE框架，通过可微分优化同时生成数字与物理传感器欺骗扰动，专门针对TBP的查询耗尽与记忆污染机制。该工作首次系统揭示了TBP架构的对抗脆弱性，但仅停留在攻击侧，未提供防御方案，且物理攻击的泛化能力受限于特定传感器校准。

## 研究背景

多目标跟踪（Multi-Object Tracking, MOT）的核心挑战在于维持物体跨帧身份一致性。传统TbD范式依赖卡尔曼滤波与重识别（Re-Identification, Re-ID）特征解耦检测与关联，但在密集交互场景中，局部运动预测与外观特征均无法提供足够的判别性，导致身份切换（ID Switch）频发。为突破这一瓶颈，TBP范式将MOT建模为端到端自回归任务，通过传播轨迹查询（Track Query）联合优化检测与关联。轨迹查询是物体的持久化运动与外观表示，其更新依赖递归隐状态或长期记忆库（如MeMOTR的记忆库、Samba的状态空间模型）。这种架构虽提升了全局上下文建模能力，但引入了两个关键结构约束：固定查询预算导致的零和资源分配问题，以及递归状态传播形成的时序依赖链。

现有针对MOT的对抗攻击主要聚焦于TbD架构，分为检测规避、关联破坏与特征操纵三类。检测规避攻击（如Daedalus）通过最大化误检干扰检测器，关联破坏攻击（如Hijack）通过操纵卡尔曼滤波预测距离导致门控拒绝，特征操纵攻击（如BankTweak）直接扰动外观嵌入。然而，这些攻击逻辑与TbD特定组件（如卡尔曼滤波、独立Re-ID库）强耦合，无法迁移至TBP架构。TBP中重复检测通过可微分注意力而非固定交并比（Intersection-over-Union, IoU）规则处理，时序动态通过查询传播而非运动预测学习，检测与重识别共享统一查询表示。因此，TBP特有的查询预算耗尽与记忆污染漏洞此前未被研究，构成了安全部署的关键盲区。

## 核心方法

### 方法参照系

本文问题属于对抗攻击设计，但目标从TbD的检测/关联模块转向TBP的查询状态与记忆机制。与通用对抗攻击（如针对分类器的PGD）不同，FADE需同时优化数字像素扰动与物理传感器参数，且攻击目标不是降低检测置信度，而是破坏时序关联逻辑。

### 时序查询洪泛（Temporal Query Flooding, TQF）

TQF攻击利用固定查询预算的零和特性，生成虚假但时序一致的轨迹以耗尽合法轨迹的查询资源。设计动机在于解决现有攻击无法利用TBP查询分配机制的问题。TQF针对未匹配查询集合 $T_{adv} \subset T_t$，通过复合损失函数实现查询耗尽与身份窃取。其核心公式为：

$$ \mathcal{L}_{TQF} = \lambda_1 \mathcal{L}_{Flood} + \lambda_2 \mathcal{L}_{Cost} + \lambda_3 \mathcal{L}_{Siphon} $$

其中 $\mathcal{L}_{Flood}$ 最大化虚假查询的检测置信度，$\mathcal{L}_{Cost}$ 最小化虚假查询与真实物体的匹配成本以欺骗二分匹配算法，$\mathcal{L}_{Siphon}$ 使虚假查询的隐状态与先前合法轨迹的隐状态不可区分，从而实现身份窃取。该机制确保虚假轨迹不仅被检测，还能被查询更新器识别为已知物体的重现，从而持久占用查询预算，导致合法轨迹因资源不足而被终止。

### 时序记忆污染（Temporal Memory Corruption, TMC）

TMC攻击直接破坏查询更新器中的时序记忆，通过状态去相关与特征擦除切断合法轨迹的时序链。设计动机在于利用TBP递归记忆机制的脆弱性，使攻击效果跨帧传播。TMC针对已匹配查询的隐状态 $H_{matched}^t$，通过两个目标实现记忆污染：

$$ \mathcal{L}_{TMC} = \lambda_4 \mathcal{L}_{Decorr} + \lambda_5 \mathcal{L}_{Erase} $$

其中 $\mathcal{L}_{Decorr}$ 最小化当前帧隐状态 $H^t$ 与前一帧隐状态 $H^{t-1}$ 之间的相似度，切断轨迹与自身历史的关联；$\mathcal{L}_{Erase}$ 最小化已匹配查询嵌入的L2范数平方，迫使特征向量坍缩至零，从而擦除轨迹的身份表示。该机制使合法轨迹在后续帧中变得不可跟踪，导致重关联失败。

## 实验评估

实验在MOT17（平均密度约21物体/帧）与MOT20（平均密度约150物体/帧）上进行，对比MOTR、MOTRv2、MeMOTR、Samba、CO-MOT等TBP跟踪器，基线包括Daedalus、Hijack、F&F等TbD攻击。FADE在数字攻击中显著优于基线，例如在MOT17上，FADE_TMC使MeMOTR的HOTA从67.35降至41.56，IDSW从0.81升至4.63；FADE_TQF使CO-MOT的HOTA从58.16降至37.26，IDSW从1.83升至9.50。

| 跟踪器 | 攻击类型 | HOTA↓ | IDSW↑ |
|---|---|---|---|
| MeMOTR (MOT17) | Clean | 67.35 | 0.81 |
| MeMOTR (MOT17) | FADE_TMC | 41.56 | 4.63 |
| CO-MOT (MOT17) | Clean | 58.16 | 1.83 |
| CO-MOT (MOT17) | FADE_TQF | 37.26 | 9.50 |

消融实验显示，TQF中 $\mathcal{L}_{Siphon}$ 与 $\mathcal{L}_{Cost}$ 的有效性依赖跟踪器架构：在Samba中，移除 $\mathcal{L}_{Cost}$ 使攻击减弱7.6 HOTA点，而移除 $\mathcal{L}_{Siphon}$ 反而使攻击增强（44.96 HOTA），表明SSM记忆机制能过滤身份窃取查询；在CO-MOT中，$\mathcal{L}_{Siphon}$ 有效但 $\mathcal{L}_{Cost}$ 无效，揭示简单查询更新器易受身份混淆欺骗。TMC中 $\mathcal{L}_{Decorr}$ 是最关键组件，移除后攻击效果显著下降，验证了时序去相关对记忆污染的核心作用。

物理攻击实验表明，声学对抗注入（AAI）与电磁对抗干扰（EAI）在密集场景（MOT20）中更有效。例如，AAI使MOTR在MOT20上的AssA下降36点，HOTA下降19点，而在MOT17上HOTA仅下降13.5点。这表明密集场景的频繁遮挡放大了攻击切断时序链的能力。然而，具有强外部检测骨干的跟踪器（如MOTRv2、CO-MOT）表现出一定鲁棒性，HOTA下降7-9点，但AssA仍下降8-9点，证明即使少量噪声泄漏至检测器后，仍能有效污染下游时序查询状态。

评估边界方面，实验仅覆盖MOT17与MOT20，未测试DanceTrack等外观相似场景；物理攻击参数基于特定传感器（如Samsung S20、iPhone 7）校准，泛化能力受限；未报告计算开销与实时性影响；代码未开源，可复现性依赖附录中的参数约束细节。

## 关联研究分析

从问题动机看，FADE与BankTweak等特征操纵攻击均针对外观表示，但FADE利用TBP的统一查询表示，攻击目标从独立Re-ID库转向共享查询状态，根源在于TBP架构消除了检测与重识别的模块边界。从方法设计看，FADE与Poltergeist等物理攻击均使用可微分传感器仿真，但FADE将攻击目标从单帧检测扩展至时序关联，通过优化物理参数（如模糊强度、条纹位置）间接影响查询状态，而非直接操纵像素。与Samba等使用SSM的跟踪器相比，FADE揭示了SSM在对抗下的脆弱性，而Samba的设计初衷是提升时序鲁棒性，这一冲突暗示SSM的递归特性在提升性能的同时引入了新的攻击面。

## 总结

本文要解决的核心矛盾是TBP架构在提升跟踪精度的同时引入了新的对抗脆弱性。现有TbD攻击无法利用TBP特有的查询预算与记忆机制，而FADE通过针对查询耗尽与记忆污染的复合损失函数，首次系统揭示了这一漏洞。实验证明FADE在MOT17/MOT20上可使HOTA下降约30点，IDSW增加10倍以上，验证了TBP架构的结构性脆弱。然而，本文仅聚焦攻击侧，未提供防御方案，且物理攻击的泛化能力受限于特定传感器校准。当跟踪器采用动态查询预算或记忆隔离机制时，FADE的攻击效果是否显著减弱，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.00452)