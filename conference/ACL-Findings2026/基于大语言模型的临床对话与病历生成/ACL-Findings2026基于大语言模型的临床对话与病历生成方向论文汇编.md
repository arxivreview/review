# ACL-Findings2026 · 基于大语言模型的临床对话与病历生成方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Benchmarking LLMs on Authentic Cases from Medical Journals ｜临床诊断推理基准

研究机构：电子科技大学、香港中文大学

作者：Wanlong Liu、Junying Chen、Yunjin Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9a3f076a4085)

> 临床AI评估长期受困于基准饱和与场景失真，现有考试题导向的基准无法区分模型在复杂真实病例中的推理能力。本文切入点在于将权威医学期刊中的真实病例转化为高难度多选题，强制模型整合长上下文证据而非依赖参数化知识。通过构建覆盖11个专科、含多模态版本的ClinBench，并引入人类专家对照，量化了LLM与专家在专科深度与广度上的能力边界。该基准有效揭示了当前SOTA模型在真实临床场景下的性能瓶颈，但其选择题格式是否掩盖了开放式诊断推理的真实缺陷，仍存疑。

】

---

【EMSDialog: Synthetic Multi-person Emergency Medical Service Dialogue Generation from Electronic Patient Care Reports via Multi-LLM Agents ｜基于多智能体规则约束的急救对话合成与流式诊断预测

研究机构：美国弗吉尼亚大学

作者：Xueren Ge、Sahil Murtaza、Anthony Cortez 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07549)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07549)

> 对话式诊断预测要求模型在证据不完整的流式交互中实时决定何时提交诊断，现有医疗语料多为双人异步对话，缺乏多角色协作与任务对齐标注，导致模型在动态场景下预测波动大且过早自信。本文切入点在于利用电子患者护理报告（ePCR）作为事实锚点，构建包含确定性规则检查器的多智能体生成管道，产出符合急救流程逻辑的多角色合成数据。该方法通过迭代批判-精炼机制强制事实接地与话题流合规，显著提升了小模型在真实急救对话上的预测准确性与稳定性。其价值在于验证了规则约束合成数据对流式诊断任务的增益，但规则覆盖范围与临床变体适应性仍存疑。

】

---

【Experience is the Teacher: Reusing Atomic Thoughts from LLMs to Improve Medical Dialogue ｜原子思维蒸馏框架

作者：Guangya Yu、Hui Luo、Qi Ye 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_acf880749a9b)

> 多轮医疗对话中，静态专家模板僵化且测试时扩展冗余，导致推理既不够灵活也不够高效。本文切入点是将推理过程拆解为可复用的“原子思维”单元，通过教师模型提取并蒸馏至小模型。具体做法是构建基于嵌入去重的经验库，指导生成推理轨迹并微调学生模型。该方法在同等参数量级下显著提升了临床逻辑与准确性，但绝对性能仍低于顶级大模型，且依赖教师模型的质量。

】

---

【ReMedi: Reasoner for Medical Clinical Prediction ｜临床结局预测中的困难样本自优化框架

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Yushi Cao、Yiming Chen、Hongchao Jiang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01474)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a070b414830a)

> 临床结局预测要求模型从电子健康记录（EHR）中推断死亡、再入院等离散标签，但通用大语言模型（LLM）在缺乏外部知识检索时，常因内部知识局限而陷入随机猜测。现有微调方法如KARE依赖专有教师模型蒸馏，限制了部署灵活性，而直接应用自改进算法STaR在临床任务中增益微弱。ReMedi通过引入“困难样本再生成”机制，将模型预测错误的案例转化为高价值训练数据，结合监督微调（SFT）与直接偏好优化（DPO）实现端到端自优化。该方法在MIMIC-IV基准上显著提升了预测精度，但其对开放临床推理任务的适用性仍存疑。

】
