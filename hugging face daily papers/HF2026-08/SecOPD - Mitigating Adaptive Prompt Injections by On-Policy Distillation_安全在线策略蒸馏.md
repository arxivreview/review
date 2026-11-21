# HuggingFace最新推荐论文 ｜SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation ｜安全在线策略蒸馏

研究机构：美国加州大学伯克利分校

作者：Yibo Peng、Long Lian、David Wagner 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.21500)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.21500)

> 提示注入防御的核心矛盾在于，现有模型级微调依赖序列级反馈，无法区分响应中合规与违规的片段，导致面对自适应攻击时鲁棒性崩塌。本文指出，将在线策略蒸馏（On-Policy Distillation, OPD）引入防御训练，通过干净输入教师模型对每个 token 提供独立监督，能精确抑制注入诱导的生成。该方法在 Qwen3.6-27B 上将最强自适应攻击成功率从 94.0% 降至 9.0%，且未牺牲任务效用。其价值在于证明了模型内部对齐可逼近系统级隔离的安全下限，但 9.0% 的残留风险是否可被进一步压缩，仍取决于教师模型对“干净行为”定义的完备性。

## 研究背景

当 LLM 代理从网页或邮件中检索数据时，外部文本中嵌入的“忽略所有先前指令”类字符串会直接劫持模型行为，这一现象即提示注入（Prompt Injection）。防御该威胁的模型级路线，通常通过微调让模型学会区分系统指令与外部数据，但此类微调若仅对完整响应给予单一奖励（序列级反馈），则无法处理“部分回答用户问题、部分执行恶意指令”的混合响应，导致信用分配失效。

模型级防御的主流方案包括基于直接偏好优化（Direct Preference Optimization, DPO）的 Meta-SecAlign 和基于组相对策略优化（Group Relative Policy Optimization, GRPO）的强化学习微调。前者构造偏好对，后者使用 LLM 裁判打分，二者均将响应视为整体，无法定位具体违规 token。这一局限在自适应攻击下被放大：攻击者针对防御模型优化注入策略，使得静态防御的鲁棒性迅速失效。本文切入点在于，利用 OPD 的 token 级监督能力，将防御训练从“整体偏好”转向“逐 token 对齐”，使模型在生成过程中实时抑制注入诱导的 token。

## 核心方法

### 序列级反馈的信用分配失效

模型级提示注入防御的标准流程是构造含注入的攻击输入，并通过偏好优化或强化学习训练模型生成安全响应。Meta-SecAlign 使用 DPO，其损失函数为：

$$
\mathcal{L}_{\text{DPO}}(\theta) = -\log \sigma\left(\beta \Delta_{\text{DPO}}\right), \quad \Delta_{\text{DPO}} = \log \frac{\pi_\theta(y^+ | p_a)}{\pi_0(y^+ | p_a)} - \log \frac{\pi_\theta(y^- | p_a)}{\pi_0(y^- | p_a)}
$$

该公式对完整响应 $y^+$ 和 $y^-$ 赋予整体偏好，无法区分响应中哪些 token 遵循了可信指令、哪些 token 响应了注入。当模型生成混合响应时，DPO 无法将其归类为 $y^+$ 或 $y^-$，导致训练信号缺失。GRPO 同样将响应作为整体评分，混合响应会被标记为“不完美”，但无法提供 token 级的修正方向。

### 跨上下文令牌级蒸馏

本文在训练流程中引入“干净输入教师模型”机制，将 OPD 的 token 级监督迁移至防御场景。具体而言，对每个训练样本，构造干净输入 $p_c = R(I, c)$ 和攻击输入 $p_a = R(I, A(c, g))$，其中 $I$ 为可信指令，$c$ 为良性数据，$g$ 为注入目标。学生模型在 $p_a$ 上生成 rollout $z = (z_1, \dots, z_T)$，教师模型（初始化的冻结 LLM）在 $p_c$ 上对同一 rollout 的每个 token $z_t$ 计算对数概率。token 级优势值定义为：

$$
A_t = \text{sg}\left[\log \pi_{\text{teacher}}(z_t | h_c^t) - \log \pi_\theta(z_t | h_a^t)\right]
$$

其中 $h_c^t = (p_c, z_{<t})$，$h_a^t = (p_a, z_{<t})$，$\text{sg}[\cdot]$ 表示停止梯度。该公式的物理含义是：若教师模型在干净输入下对某 token 赋予更高概率，则该 token 被鼓励；反之则被抑制。这一设计解决了序列级反馈无法定位违规 token 的失效，使模型能精确学习“在注入存在时，仅响应可信指令”的安全策略。

## 实验评估

实验在 SEP（9.1K 样本）和 AgentDojo（949 任务对）上评估，基线包括 Meta-SecAlign（DPO）和 GRPO。主结果如下：

| 防御方法 | SEP Static ASR (%) | SEP Basic Adaptive ASR (%) | SEP PISmith Adaptive ASR (%) | AgentDojo Static ASR (%) |
| :--- | :--- | :--- | :--- | :--- |
| Undefended | 99.4 | 99.0 | 97.9 | 26.7 |
| Meta-SecAlign | 28.9 | 5.5 | 94.0 | 5.5 |
| GRPO | 15.0 | 2.3 | 61.2 | 0.7 |
| SecOPD | 1.3 | 0.2 | 9.0 | 4.7 |

SecOPD 在 PISmith 自适应攻击下 ASR 为 9.0%，较 Meta-SecAlign 的 94.0% 降低一个数量级；在 AgentDojo 上 ASR 为 4.7%，优于 Meta-SecAlign 的 5.5%。效用方面，SecOPD 在 SEP 上效用为 88.6%，与未防御模型的 88.0% 基本持平，而 GRPO 的效用降至 79.5%。

消融实验未单独报告，但论文指出，token 级反馈对混合响应的处理是性能提升的关键。设计决策上，教师模型使用初始化的冻结 LLM，而非外部安全裁判，避免了裁判模型自身的偏差。评估边界方面，PISmith 攻击针对每个防御模型单独训练，但论文未报告攻击训练的计算成本；AgentDojo 仅测试了“重要指令”攻击，未覆盖其他注入类型。代码已开源，但超参数细节未在正文中完整披露。

## 关联研究分析

从问题动机看，SecOPD 与系统级防御（如 CaMeL、IsolateGPT）的根本差异在于信任边界的实现位置。系统级防御通过架构隔离强制区分指令与数据，而 SecOPD 依赖模型内部对齐。这一差异导致 SecOPD 的 ASR 下限为 9.0%，而 CaMeL 可达 0.0%。根源在于，模型级防御无法完全消除 LLM 对文本指令的响应倾向，而系统级防御通过密码学签名或信息流控制从外部阻断注入执行。SecOPD 的价值在于，它在无需修改系统架构的前提下，将模型级防御的鲁棒性提升至接近系统级水平，为资源受限场景提供了替代方案。

从方法设计看，SecOPD 与 Meta-SecAlign 共享数据构造方式，但优化目标从偏好对转向 token 级蒸馏。这一改动源于 OPD 在效用提升中的成功，但将其迁移至防御场景时，教师模型的“干净行为”定义成为关键。若教师模型本身对某些注入模式不敏感，则 SecOPD 的防御上限受限于教师模型的安全对齐程度。论文未探索教师模型的安全微调对防御性能的影响，这一盲区可能限制了 SecOPD 在更复杂注入场景下的泛化能力。

## 总结

SecOPD 要解决的核心矛盾是模型级防御在自适应攻击下的鲁棒性崩塌，其切入点在于利用 OPD 的 token 级监督解决序列级反馈的信用分配失效。通过引入干净输入教师模型，SecOPD 将防御训练从整体偏好转向逐 token 对齐，在 Qwen3.6-27B 上将 PISmith ASR 从 94.0% 降至 9.0%，且保持 88.6% 的 SEP 效用。其边界在于，9.0% 的残留 ASR 仍高于系统级防御的 0.0%，且教师模型的安全对齐程度未经验证。当教师模型本身对某些注入模式不敏感时，SecOPD 的防御上限是否会被进一步压缩，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.21500)