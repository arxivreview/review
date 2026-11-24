# ACL-Findings2026 · 大语言模型谈判与议价智能体方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Datamart-Agent: LLM-Driven Game-Theoretic Agent for Data Marketplace Modeling ｜数据市场均衡一致性建模

研究机构：香港理工大学

作者：Pangjing Wu、Peter Q. Chen、Xiaodong Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed702225f89d)

> 数据市场研究长期受限于静态完全信息假设，难以刻画动态演化与买方估值不完全信息下的真实博弈。现有基于强化学习或静态提示的大语言模型（LLM）代理在缺乏参数更新的情况下，难以在解析均衡真值上实现策略一致性。本文提出EvoDM框架与Datamart-Agent，通过动态博弈树记忆与机制引导反思，在无参数更新条件下执行均衡一致决策。该工作验证了非训练式LLM代理在复杂市场模拟中的有效性，但其泛化边界与长程依赖处理能力仍存疑。

】

---

【Nash-Pruned CredMAS: Dynamic Panel Pruning for VLM-MAS using Nash-based Selection and Doubly-Robust Credits ｜纳什剪枝可信多智能体系统

研究机构：中山大学

作者：Yijia Fan、Mingyu Liu、Jing Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1128085fe323)

> 多轮视觉语言模型（VLM）多智能体系统（MAS）面临静态面板导致的 $O(N \times T)$ 通信成本爆炸与低价值代理引入的噪声干扰。现有启发式路由或一次性剪枝方法缺乏理论保证，且无法动态适应上下文依赖的边际效用变化。本文提出 NP-CredMAS，通过离线双重稳健因果价值学习与在线子模最大化拍卖机制，实现推理时的动态资源分配。该方法在保持 SOTA 性能的同时显著降低 Token 消耗，但其因果估计对离线日志分布偏移的鲁棒性尚存疑。

】

---

【Preference Estimation via Opponent Modeling in Multi-Agent Negotiation ｜融合语言信号的贝叶斯对手建模

研究机构：日本京都大学

作者：Yuta Konishi、Kento Yamamoto、Eisuke Sonomoto 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15687)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b2ed3fc887a)

> 导读 多智能体谈判中，私有偏好隐藏在自然语言与数值报价的混合流中，传统仅依赖数值历史的贝叶斯方法无法捕捉话语中的定性线索，导致高不确定性下偏好估计失稳。本文切入点在于将大语言模型（LLM）提取的语言信号转化为概率格式，与数值似然进行贝叶斯融合，实现动态信念跟踪。该方法在稀疏共识空间中提升了全协议率与估计精度，但其对“真诚对话”的强假设限制了在策略性欺骗场景下的适用性。

】

---

【ProMediate: A Simulation Testbed for Evaluating Proactive Mediation in Multi-Party Negotiation ｜ProMediate：多方主动调解的社会认知评估测试床

研究机构：美国南加州大学

作者：Ziyi Liu、Bahareh Sarrafzadeh、Pei Zhou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0536f8e06d5d)

> 多方谈判中的共识构建长期缺乏系统化的量化评估手段，现有基准多聚焦双边经济效率或被动响应式辅助，无法捕捉调解者主动介入时机与策略对社会动态的影响。ProMediate 通过构建基于冲突理论的多方模拟环境，将“何时介入”与“如何介入”解耦，并引入共识追踪与社会认知智能双维度指标，填补了主动调解能力评估的空白。其价值在于提供了可复现的主动代理压力测试框架，但实验仅覆盖单一骨干模型与有限场景，缺乏与强化学习路线的横向对比，其结论的泛化性存疑。

】

---

【RCBSF: A Multi-Agent Framework for Automated Contract Revision via Stackelberg Game ｜风险约束双层斯塔克尔伯格框架

研究机构：重庆大学、英国伦敦玛丽女王大学

作者：Shijia Xu、Yu Wang、Xiaolong Jia 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b000e7eb2efb)

> 法律合同修订面临的核心矛盾是通用大语言模型（LLM）将严格法律约束视为建议而非硬性边界，导致高风险输出。现有单智能体或合作型多智能体方法缺乏对抗性层级控制，无法在生成过程中强制合规。本文提出风险约束双层斯塔克尔伯格框架（RCBSF），通过领导者-跟随者博弈结构实现约束驱动的合同修订。该框架在7B模型上实现了超越72B基线的风险解决率，但其评估依赖LLM裁判，且未验证在动态多议题谈判中的泛化能力。

】
