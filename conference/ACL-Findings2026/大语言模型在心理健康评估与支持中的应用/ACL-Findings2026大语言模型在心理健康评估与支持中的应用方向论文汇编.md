# ACL-Findings2026 · 大语言模型在心理健康评估与支持中的应用方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Auditing LLM Responses to Harmful Stereotypes Targeting Mental Health Groups ｜心理健康刻板印象的显式合理化审计

研究机构：美国罗切斯特理工学院、美国佐治亚理工学院

作者：Arka Dutta、Rijul Magu、Sean Kim 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c4dce0c363a)

> 大语言模型在心理健康领域的应用常聚焦于临床辅助与危机干预，但模型内化的社会偏见如何转化为对弱势群体权利剥夺的合理化论述，长期处于安全评估的盲区。现有通用内容过滤工具仅能识别显性毒性，无法捕捉以“合理建议”为伪装的结构性歧视，导致模型在投票权、居住权等敏感议题上输出有害内容却未被标记。本文通过构建包含15个刻板印象框架与132个身份群体的提示集，对13个开源模型进行零样本审计，揭示模型在显式提示下对权利限制类刻板印象的高比例背书，并证明主流Moderation API对此类细微歧视的漏检率极高。该工作填补了社会偏见审计中“权利合理化”维度的空白，但单轮静态评估能否反映多轮对话中偏见的累积效应，仍存疑。

】

---

【CARE-CR: Context-Aware Routing and Expert Fusion for Multi-Preference Cognitive Restructuring ｜上下文感知路由与专家融合的认知重构

作者：Hongzhi Qi、Liangcheng Wang、Yijing YU 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce3cf009b44e)

> 认知行为疗法中的认知重构旨在通过识别非理性信念并生成辩驳来缓解心理痛苦，但现有大语言模型方法往往陷入表面化的积极改写，缺乏对共情、理性等治疗维度动态权衡的机制。本文指出单一奖励模型无法适应不同情境下的偏好差异，提出CARE-CR框架，通过训练维度特定的专家策略并利用上下文感知路由进行动态融合，实现个性化认知重构。该方法在诊断准确性与临床效度上优于单一对齐基线，但其单轮评估协议与有限的数据规模限制了结论向多轮临床场景的泛化。

】

---

【Like a Therapist, But Not: Reddit Narratives of AI in Mental Health Contexts ｜基于技术接受模型与治疗联盟的AI心理健康话语分析

作者：Elham Aghakhani、Rezvaneh Rezapour

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb4037c0104f)

> 现有LLM心理健康研究聚焦于模型临床能力与安全审计，却忽视了用户在实际使用中的感知、信任与关系建立机制。本文切入点在于将心理学中的技术接受模型（TAM）与治疗联盟理论引入大规模自然主义话语分析，量化用户如何评估AI作为治疗工具的价值与风险。通过构建混合人工-LLM标注流程，对5,126条Reddit帖子进行细粒度编码，揭示了任务对齐而非单纯情感纽带是驱动积极采纳的核心因素。该工作填补了用户侧评估空白，但其结论局限于话语层面，无法直接验证临床有效性。

】

---

【MHSafeEval: Role-Aware Interaction-Level Evaluation of Mental Health Safety in Large Language Models ｜角色感知交互级心理健康安全评估

研究机构：韩国汉阳大学、新加坡管理大学

作者：Suhyun Lee、Palakorn Achananuparp、Neemesh Yadav 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17730)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17730)

> 大语言模型在心理咨询中的安全性评估长期受限于静态、粗粒度的基准，无法捕捉多轮对话中累积的关系性危害。现有方法将安全失效简化为单轮内容毒性检测，忽略了咨询师在对话中扮演的交互角色如何塑造伤害轨迹。本文提出 R-MHSafe 分类法与 MHSafeEval 框架，通过质量多样性搜索动态生成对抗性多轮交互，揭示角色特异性的隐性安全漏洞。该框架在八个主流模型上实现了 0.914 至 0.997 的攻击成功率，证明了动态评估在诊断粒度上的优势，但其依赖 LLM 裁判的可靠性及动态生成的可复现性仍存疑。

】
