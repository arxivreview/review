# Others2026 · 人脸防欺骗与变形攻击检测方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【基于伪影解耦与局部多任务学习的域泛化面部反欺骗

作者：Seungjin Jung、Yonghyun Jeong、Minha Kim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09018)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09018)

> 面部反欺骗（Face Anti-Spoofing, FAS）旨在区分真实人脸与物理呈现攻击，其核心挑战在于训练数据中身份与环境多样性不足导致的跨域泛化失效。现有域泛化方法多依赖全局风格迁移或单一方向的数据增强，难以捕捉攻击介质特有的局部伪影分布。本文提出模式转换生成对抗网络（Pattern Conversion GAN, PCGAN）与基于补丁的多任务网络（Patch-based Multi-tasking Network, PMN），通过显式解耦伪影与面部内容实现可控数据增强，并结合局部区域监督缓解身份过拟合。该框架在多个基准上验证了性能优势，但其对生成器训练成本的依赖及未覆盖最新视觉基础模型基线，限制了其在实时部署场景中的直接适用性。

】
