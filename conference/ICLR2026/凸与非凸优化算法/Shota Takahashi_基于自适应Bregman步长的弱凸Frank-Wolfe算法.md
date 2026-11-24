# ICLR2026最新论文 ｜Shota Takahashi ｜基于自适应Bregman步长的弱凸Frank-Wolfe算法

研究机构：日本东京大学、德国柏林工业大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69700272)

> 导读 高维约束优化中，投影算子计算昂贵且常不可行，Frank-Wolfe (FW) 算法通过线性最小化预言机 (LMO) 替代投影，但传统理论依赖目标函数梯度的Lipschitz连续性（$L$-smoothness）与凸性，限制了其在非光滑或非凸问题中的应用。现有自适应步长策略仅针对欧氏距离设计，无法处理由Bregman距离引入的几何缩放参数 $\nu$，导致在弱凸非凸景观中缺乏线性收敛保证。本文提出一种自适应Bregman步长策略，同时动态估计平滑常数 $L$ 与Bregman距离的缩放指数 $\nu$，并在弱凸函数满足局部二次增长条件下，首次证明了FW算法的局部线性收敛。该工作拓展了FW算法的适用域，但 $\nu$ 的估计依赖对Bregman距离的预先选择，且线性收敛仅在局部成立，其全局鲁棒性有待进一步验证。

## 研究背景

理解本文需串联三个核心概念：Frank-Wolfe (FW) 算法、Bregman距离与弱凸性。FW算法通过LMO替代投影，解决了高维约束集上投影计算瓶颈，但其经典收敛分析要求目标函数 $f$ 的梯度 $\nabla f$ 是Lipschitz连续的（即 $L$-smooth）。然而，许多实际应用（如非负矩阵分解、相位恢复）中的目标函数虽在紧集上 $C^2$，其Lipschitz常数 $L$ 可能过于保守，甚至不满足 $L$-smoothness。此时，Bregman距离 $D_\phi(x,y) = \phi(x) - \phi(y) - \langle \nabla \phi(y), x-y \rangle$ 提供了更灵活的度量，其核心假设是 $(f, \phi)$ 满足 $L$-smooth adaptable ($L$-smad) 性质，即 $L\phi - f$ 与 $L\phi + f$ 均为凸函数。这一性质允许梯度非Lipschitz，但引入了Bregman距离的缩放指数 $\nu$，使得步长设计与收敛分析复杂化。

FW算法的收敛速率长期受限于 $O(\epsilon^{-1})$ 的次线性界限，除非假设强凸性或二次增长条件。现有改进主要沿两条路线：一是自适应步长策略（如Pedregosa et al., 2020），动态估计 $L$ 以避免保守参数；二是Away-step机制（Wolfe, 1970），通过移除活跃顶点中的“慢”原子消除多面体约束下的之字形收敛。然而，这些工作均基于欧氏距离（$\nu=1$），未考虑Bregman距离中 $\nu \neq 1$ 的几何效应。当目标函数弱凸（$f + \frac{\rho}{2}\|\cdot\|_2^2$ 凸）且满足局部二次增长时，现有FW算法缺乏线性收敛保证，这构成了本文的核心切入点：在 $L$-smad 假设下，通过自适应估计 $\nu$ 与 $L$，实现弱凸非凸优化中的局部线性收敛。

## 核心方法

### 方法参照系

本文问题属于凸优化算法改进类别，标准流程为：初始化 $x_0 \in P$，迭代计算 $v_t = \arg\min_{v \in P} \langle \nabla f(x_t), v \rangle$，更新 $x_{t+1} = (1-\gamma_t)x_t + \gamma_t v_t$。关键差异在于：标准FW使用欧氏距离与固定/自适应 $L$，本文使用Bregman距离 $D_\phi$ 并自适应估计 $L$ 与 $\nu$，以处理 $L$-smad 函数。

### 自适应Bregman步长策略

传统短步长策略 $\gamma_t = \frac{\langle \nabla f(x_t), x_t - v_t \rangle}{L\|x_t - v_t\|_2^2}$ 依赖已知 $L$，且仅适用于 $\nu=1$。本文在Bregman框架下，步长需同时依赖 $L$ 与 $\nu$，其最优步长为：

$$
\gamma_t = \left( \frac{\langle \nabla f(x_t), x_t - v_t \rangle}{L(1+\nu)D_\phi(v_t, x_t)} \right)^{1/\nu}
$$

该公式的物理含义是：步长由Bregman距离 $D_\phi$ 的几何缩放（$1+\nu$）与平滑常数 $L$ 共同决定，$\nu$ 控制距离的非线性程度。由于 $L$ 与 $\nu$ 通常未知，本文设计自适应回溯策略（Algorithm 2）：从初始估计 $M = \eta \tilde{L}$ 与 $\kappa = 1$ 开始，若更新后 $D_f(x_+, x) \leq M \gamma^{1+\kappa} D_\phi(v, x)$ 不成立，则放大 $M \leftarrow \tau M$ 并缩小 $\kappa \leftarrow \beta \kappa$，直至条件满足。这一设计解决了此前自适应策略无法处理 $\nu \neq 1$ 导致的步长失效问题，确保算法在 $L$-smad 函数上全局收敛。

### Bregman Away-step FW算法

Away-step机制通过移除活跃顶点集合 $S$ 中与梯度内积最大的顶点 $v_t^A$，消除之字形收敛。传统Away-step FW使用欧氏距离计算步长，本文将其推广至Bregman距离。当选择Away-step时，步长上限 $\gamma_{t,\max}$ 由活跃顶点的权重 $\lambda_{v_t^A, t}$ 决定：

$$
\gamma_{t,\max} = \frac{\lambda_{v_t^A, t}}{1 - \lambda_{v_t^A, t}} \cdot \left( \frac{\langle \nabla f(x_t), x_t - v_t^A \rangle}{L(1+\nu)D_\phi(v_t^A, x_t)} \right)^{1/\nu}
$$

该公式表明，Away-step的步长受限于当前点 $x_t$ 在顶点 $v_t^A$ 上的权重比例，权重越小，可远离该顶点的幅度越大。结合自适应Bregman步长，本文证明了在弱凸 $f$ 满足局部二次增长（$\rho < \mu$）时，算法在 $x^* \in \text{int } P$ 附近实现局部线性收敛，收敛速率依赖于 $\nu$ 与 $\rho/\mu$ 的比值。这一创新突破了此前FW算法在非凸设定下仅有次线性收敛的局限。

## 实验评估

实验在Julia 1.11与FrankWolfe.jl包上进行，测试集包括非负矩阵分解、相位恢复等 $L$-smad 问题，基线覆盖EucFW、ShortFW、OpenFW、MD及ProjGD，但未包含其他Bregman变体（如Vyguzov & Stonyakin, 2025的凸Bregman FW）。主结果显示，BregFW在多数指标上优于EucFW，例如在非负线性逆问题上，BregFW的 primal gap 为 **6.9637e-08** $\pm$ **2.0e-08**，而EucFW为 **3.0287e-07** $\pm$ **9.4e-08**；在相位恢复问题上，BregFW的 primal gap 为 **1.0589e-13** $\pm$ **8.6e-15**，EucFW为 **6.2980e-10** $\pm$ **9.9e-11**。BregAFW在部分问题上优于ShortAFW，如在非负矩阵分解上，BregAFW的 primal gap 为 **4.3430e+00** $\pm$ **1.7e+00**，ShortAFW为 **4.4092e+00** $\pm$ **1.7e+00**，但差异较小。

消融实验未单独报告，但步长策略的自适应机制（Algorithm 2）是核心设计决策。其有效性体现在：当 $\nu$ 未知时，回溯估计避免了因 $\nu$ 误估导致的收敛失败；当 $\nu=1$ 时，算法退化为Pedregosa et al. (2020)的自适应欧氏FW，性能与基线一致。反直觉发现是：在弱凸非凸问题上，BregFW的 primal gap 收敛速度虽快，但远离最优解时（如非负矩阵分解初始阶段），其 primal gap 值（**4.3430e+00**）与EucAFW（**4.3968e+00**）接近，表明Bregman几何的优势主要在局部收敛阶段，而非全局探索。

评估边界存在局限：实验未报告计算时间或LMO调用次数，无法量化Bregman距离计算开销；$\nu$ 的估计依赖对 $\phi$ 的预先选择，若 $\phi$ 不匹配 $f$ 的几何，自适应策略可能失效；代码未公开，仅依赖FrankWolfe.jl包，复现需自行实现Algorithm 2与3。

## 关联研究分析

从问题动机看，本文与PF-AGD (Xiong et al., 2026) 同属参数自由算法，但PF-AGD针对无约束非凸优化，通过自适应回溯估计平滑常数实现 $O(\tilde{O}(\epsilon^{-5/3}))$ 全局收敛；本文针对约束FW，核心差异在于处理Bregman距离的 $\nu$ 参数。PF-AGD的自适应机制仅估计 $L$，而本文需同时估计 $L$ 与 $\nu$，这源于约束优化中LMO与Bregman几何的耦合。本文的局部线性收敛保证在PF-AGD中不存在，后者仅提供全局次线性速率，这反映了约束问题中局部几何结构（如 $x^* \in \text{int } P$）对收敛速率的关键作用。

从方法设计看，本文与Bregman Away-Step FW (Takahashi, ICLR 2026, P13) 同属Bregman FW变体，但P13聚焦凸优化下的全局子线性收敛，本文拓展至弱凸非凸下的局部线性收敛。关键差异在于收敛条件：P13依赖HEB条件与 $x^* \in \text{int } P$，本文额外要求弱凸性与局部二次增长。这一差异源于非凸设定下primal gap与dual gap的不等价性，本文通过Lemma C.2建立弱凸函数下primal gap、dual gap与FW gap的关联，从而推导线性收敛。P13未处理非凸情形，其理论保证在弱凸函数上可能失效，这暗示Bregman几何在非凸景观中的利用需更精细的局部结构假设。

## 总结

本文要解决的核心矛盾是：FW算法在 $L$-smad 弱凸非凸问题中缺乏线性收敛保证，而现有自适应步长策略无法处理Bregman距离的 $\nu$ 参数。本文抓住的切入点是：通过自适应同时估计 $L$ 与 $\nu$，并利用弱凸性与局部二次增长条件，建立Bregman FW算法的局部线性收敛理论。本文实现了自适应Bregman步长策略与Bregman Away-step FW算法，证明了在 $\rho < \mu$ 时局部线性收敛，实验显示BregFW在 primal gap 上优于EucFW（如 **6.9637e-08** vs **3.0287e-07**）。本文的边界在于：$\nu$ 的估计依赖对 $\phi$ 的预先选择，若 $\phi$ 不匹配 $f$ 的几何，自适应策略可能失效；线性收敛仅在 $x^* \in \text{int } P$ 附近局部成立，全局收敛仍为次线性。当 $\phi$ 的选择无法准确反映 $f$ 的局部几何时，自适应估计 $\nu$ 的收敛速率是否仍优于固定 $\nu$ 的欧氏FW，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69700272)