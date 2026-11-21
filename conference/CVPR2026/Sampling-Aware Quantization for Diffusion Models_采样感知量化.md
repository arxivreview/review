# CVPR2026最新论文 ｜Sampling-Aware Quantization for Diffusion Models ｜采样感知量化

研究机构：浙江大学

作者：Qian Zeng、Jie Song、Yuanyu Wan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b16c02adea8e)

> 扩散模型加速面临采样步数与网络精度双重瓶颈，现有量化方法忽略噪声对高阶求解器方向估计的累积干扰，导致低比特下轨迹发散。本文切入点是将量化校准目标从张量匹配转向采样方向序列对齐，通过混合阶轨迹对齐策略约束误差界。该方法在8-bit下保持高阶采样器收敛性，但在4-bit极低NFE场景下的有效性及离散扩散适配性尚未验证。

## 研究背景

扩散模型采样过程本质是概率流常微分方程（Probability Flow ODE, PF-ODE）的数值积分，其中噪声估计网络 $\epsilon_\theta(x_t, t)$ 决定每一步的去噪方向。高阶求解器（如DPM-Solver-2）通过在区间内引入中间步 $s_j$ 进行多次方向估计，以减小截断误差并支持稀疏步长采样。后训练量化（Post-Training Quantization, PTQ）将FP32权重转换为低比特定点表示，但截断误差引入的量化噪声 $\Delta\epsilon_\theta$ 会扰动每个中间步的方向估计，且这种扰动在高阶项中呈累积效应，可能将稳定的PF-ODE转化为方差爆炸的随机微分方程（Stochastic Differential Equation, SDE），导致轨迹扩散。

现有量化研究如PTQ4DM、Q-Diffusion主要关注时间步分布匹配或U-Net结构适配，未考虑量化噪声对高阶求解器截断误差控制机制的特异性破坏。当采样步数压缩至10步以下时，高阶求解器依赖的中间步方向估计精度成为质量保持的关键，而传统PTQ的MSE最小化目标无法约束这种方向序列的累积偏差。本文针对这一被忽略的失效场景，提出将采样加速原理融入量化校准，通过混合阶轨迹对齐确保量化模型在高速采样下的方向估计线性化。

## 核心方法

### 方法参照系

标准PTQ流程通过最小化量化前后张量的均方误差确定量化参数，其假设是单步输出误差可控。本文问题的关键差异在于：扩散模型采样是迭代过程，单步方向误差会在高阶求解器的中间步评估中累积，因此校准目标必须从单点张量匹配转向整个采样方向序列的对齐。

### 混合阶轨迹对齐

传统PTQ在校准时仅对齐同一时间步的输入输出，忽略了高阶求解器中中间步 $s_j$ 的方向估计依赖关系。本文在DPM-Solver-2框架下，将量化目标定义为对齐量化模型的一阶方向轨迹与全精度模型的二阶方向轨迹。具体地，对于采样区间 $(t_{i-1}, t_i)$，一阶求解器在 $t_{i-1}$ 评估 $\epsilon_\theta(\tilde{x}_{t_{i-1}}, t_{i-1})$，而二阶求解器在中间步 $s_i$ 评估 $\epsilon_\theta(u_i, s_i)$。量化目标函数为：

$$
\arg\min_{s,z} \mathbb{E}_{(x_t,t)\sim D, (x_s,s)\sim S} \|\hat{\epsilon}_\theta(x_{\lambda_s}, \lambda_s) - \epsilon_\theta(x_{\lambda_t}, \lambda_t)\|^2
$$

其中 $\hat{\epsilon}_\theta = Q(\epsilon_\theta, s, z)$ 为量化后的噪声估计网络，$s$ 和 $z$ 分别为量化尺度和零点。该设计动机在于：通过强制量化模型的一阶方向逼近全精度模型的二阶方向，将量化误差 $\delta$ 约束至 $O(\lambda_t - \lambda_s)$ 量级，从而抑制高阶项中的误差累积，使概率流保持线性化。

### 采样感知后训练量化与QLoRA

对于8-bit量化，本文提出SA-PTQ，基于BRECQ框架，采用双阶轨迹采样策略：使用固定种子 $seed$ 和时间调度 $\{t_i\}$，分别用一阶和二阶求解器生成校准轨迹，然后对每个模块 $f_i$ 独立执行Adaround量化，优化参数 $\alpha$ 以最小化模块输入输出在混合阶轨迹上的偏差：

$$
\arg\min_{\alpha} \mathbb{E}_{(t_j,s_j)} \|f_i(x_{t_j}, t_j, \text{cond}) - \hat{f}_i(x_{s_j}, s_j, \text{cond})\|^2
$$

对于4-bit等低比特需求，本文扩展为SA-QLoRA，在QLoRA框架中同时优化LoRA权重 $w$ 和量化参数 $s, z$，其目标函数为：

$$
\arg\min_{w,s,z} \mathbb{E}_{(x_t,t)\sim D} \|\epsilon_\theta(x_t, t) - \hat{\epsilon}_\theta(x_t, t)\|^2
$$

其中 $\hat{\epsilon}_\theta = \text{QLoRA}(\epsilon_\theta, w, s, z)$。这一设计解决了低比特下纯PTQ精度不足的问题，通过轻量微调补偿量化噪声，同时保持混合阶对齐的约束。

## 实验评估

实验在ImageNet 256×256、LSUN-Churches 256×256、LSUN-Bedroom 256×256和MS-COCO 512×512上进行，使用LDM和SD-v1.4作为骨干，DPM-Solver-1和DPM-Solver-2作为低阶和高阶求解器。基线覆盖PTQ4DM、Q-Diffusion、PTQD和EfficientDM，但缺失与最新特征缓存或蒸馏方法的对比。

| 数据集 | 方法 | FID |
| --- | --- | --- |
| ImageNet 256×256 | SA-PTQ | 9.89 |
| ImageNet 256×256 | PTQD | 10.58 |
| ImageNet 256×256 | Q-diffusion | 11.34 |
| MS-COCO | SA-PTQ | 13.10 |
| MS-COCO | Q-Diffusion | 13.28 |
| MS-COCO | PTQD | 13.65 |

在ImageNet 256×256上，SA-PTQ的FID 9.89优于PTQD的10.58和Q-diffusion的11.34；在MS-COCO上，SA-PTQ的FID 13.10优于Q-Diffusion的13.28和PTQD的13.65。这些结果表明混合阶轨迹对齐在8-bit量化下有效维持了高阶采样器的收敛性。

论文未提供消融实验数据，无法量化混合阶对齐相对于单阶对齐的边际收益，也未验证不同求解器阶数（如DPM-Solver-3）下的性能变化。评估协议使用50k样本计算FID、sFID、IS、precision和recall，文本生成任务额外使用CLIP-Score，但未报告置信区间。代码已公开，但超参数细节如校准集大小、LoRA秩等未在正文中明确列出，可复现性依赖代码仓库。

## 关联研究分析

从问题动机看，本文与PTQ4DM、Q-Diffusion等早期量化工作存在根本差异：后者将量化视为独立的模型压缩问题，仅关注时间步分布或U-Net结构适配，而本文将量化误差视为采样轨迹的扰动源，其根源在于扩散模型采样的迭代性和高阶求解器的方向估计依赖性。这一差异并非任务特性决定，而是早期工作未探索高阶求解器与量化交互的盲区。

从方法设计看，本文与DPM-Solver共享高阶展开理论基础，但DPM-Solver关注截断误差控制，本文则关注量化误差对截断误差的干扰。与特征缓存方法（如DeepCache）相比，本文不依赖时间冗余性，而是通过轨迹对齐约束误差界，这使其在低NFE场景下更具理论保证，但缺乏特征缓存的免训练优势。混合阶对齐是否仅适用于线性化程度高的ODE求解器，论文未给出回答。

## 总结

本文要解决的核心矛盾是量化噪声对高阶采样器方向估计的累积干扰导致低比特下轨迹发散。现有PTQ方法因忽略采样迭代性而无法约束这种干扰，本文凭借混合阶轨迹对齐策略，将量化校准目标从张量匹配转向方向序列对齐，从而抑制误差累积。实验证明在8-bit下，SA-PTQ在ImageNet 256×256上FID 9.89、MS-COCO上FID 13.10，优于PTQD和Q-Diffusion。本文的边界在于未验证4-bit极低NFE场景下的有效性，且混合阶对齐对SDE采样器或离散扩散模型的适配性未探索。当量化比特降至4-bit且采样步数压缩至5步以下时，混合阶轨迹对齐是否仍能维持轨迹稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_b16c02adea8e)