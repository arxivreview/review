# ICLR2026最新论文 ｜Debiased Front-Door Learners for Heterogeneous Effects ｜前门调整下的去偏异质效应估计

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Yonghan Jung

论文原文见 [arXiv](https://arxiv.org/abs/2509.22531)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22531)

> 观测数据中处理与结果共享未观测混杂时，后门调整失效，前门（Front-Door, FD）调整通过中介变量识别因果效应，但现有方法多局限于平均效应或缺乏统计鲁棒性。本文针对条件前门效应 $\tau(C)$ 的估计，将基于后门调整的双重稳健（DR-Learner）与R-Learner框架迁移至FD结构，构造去偏伪结果与三阶段分解算法。该方法在nuisance函数以 $n^{-1/4}$ 慢速收敛时仍保持准oracle速率，但在真实数据中未提供不确定性量化，且缺乏与深度FD方法的横向对比。

## 研究背景

当处理变量 $X$ 与结果 $Y$ 之间存在未观测混杂 $U$ 时，直接调整协变量 $C$ 无法消除偏差，因为 $U$ 同时影响 $X$ 和 $Y$。此时若存在一个观测中介变量 $Z$，且 $X$ 对 $Y$ 的影响完全通过 $Z$ 传递，同时 $C$ 能阻断 $X-Z$ 和 $Z-Y$ 间的虚假路径，则满足前门（Front-Door, FD）准则。FD调整公式通过两步积分识别因果效应：先估计 $X$ 对 $Z$ 的条件分布，再估计 $Z$ 对 $Y$ 的条件分布，从而绕过未观测混杂 $U$ 的干扰。

在标准后门调整（Back-Door, BD）场景下，DR-Learner（Kennedy, 2023）和R-Learner（Nie and Wager, 2021）通过正交化损失实现了异质处理效应（Heterogeneous Treatment Effect, HTE）的去偏估计，允许nuisance参数以 $n^{-1/4}$ 速率收敛。然而，这些方法依赖后门准则，即 $C$ 能阻断 $X-Y$ 间所有虚假路径，这在存在未观测混杂时不成立。现有FD估计方法如LobsterNet（Chen et al., 2025）虽能处理条件FD效应，但基于多任务神经网络，缺乏去偏性保证；深度FD估计器（Xu and Gretton, 2022; Xu et al., 2024）虽具可扩展性，但同样未提供统计鲁棒性。本文切入点在于将成熟的正交化HTE估计器系统迁移至FD结构，填补条件FD效应估计中缺乏去偏方法的空白。

## 核心方法

### 方法参照系

本文问题属于复杂场景效应估计路线，核心差异在于识别公式从后门调整（g-formula）替换为前门调整。标准DR/R-Learner基于 $E[Y|do(X=x), C]$ 的识别，而FD场景需通过中介 $Z$ 间接识别 $E[Y|do(X=x), C]$，这要求估计器能处理两步积分结构，且保持nuisance误差的二阶小量特性。

### FD-DR-Learner：伪结果构造

FD-DR-Learner的核心改动在于构造一个条件均值等于 $\tau(C)$ 的伪结果（Pseudo-Outcome）。在BD-R-Learner中，伪结果直接基于倾向得分与结果模型构造；而在FD-DR-Learner中，伪结果 $\phi_{\bar{x}}(V; \eta)$ 需整合三个nuisance函数：$m(ZXC) = E[Y|Z,X,C]$、$e(X|C) = P(X|C)$ 和 $q(Z|XC) = P(Z|X,C)$。具体地，定义权重 $w_{\bar{x}}(C) = \frac{e(X|C)}{e(\bar{x}|C)}$ 和 $v_{\bar{x}}(ZXC) = \frac{q(Z|XC)}{q(Z|\bar{x}C)}$，伪结果定义为：

$$
\phi_{\bar{x}}(V; \eta) = w_{\bar{x}}(C) \left[ v_{\bar{x}}(ZXC) (Y - m(ZXC)) + m(ZXC) \right]
$$

该公式的物理含义是：通过逆概率加权调整中介分布，使得伪结果的期望等于干预 $do(X=\bar{x})$ 下的条件结果。设计动机在于，直接插件估计器 $\hat{\tau}_{PI}$ 的误差线性依赖于nuisance误差，而FD-DR-Learner通过正交化构造，使误差仅依赖于nuisance误差的二阶乘积，从而在nuisance慢收敛时保持准oracle速率。

### FD-R-Learner：三阶段分解

FD-R-Learner将FD效应分解为两个子效应的组合，以解决伪结果构造中权重估计的方差累积问题。第一阶段估计 $X$ 对 $Z$ 的异质效应 $b(C)$，利用BD-R-Learner框架，因为 $C$ 满足 $X-Z$ 的后门准则；第二阶段估计 $Z$ 对 $Y$ 的异质效应 $g(XC)$，利用BD-R-Learner框架，因为 $(X,C)$ 满足 $Z-Y$ 的后门准则；第三阶段通过伪-g函数 $\zeta_{\hat{\eta}_z}(XC)$ 组合 $b(C)$ 和 $g(XC)$ 得到 $\tau(C)$。伪-g函数定义为：

$$
\zeta_{\hat{\eta}_z}(XC) = \hat{e}_X(C) \hat{g}(1C) + (1 - \hat{e}_X(C)) \hat{g}(0C)
$$

该公式的物理含义是：通过倾向得分加权组合两种干预状态下的 $g$ 估计，消除 $e_X$ 误差对最终估计的线性影响。设计动机在于，直接插件估计 $\hat{\gamma}_{plug}(C) = \hat{e}_X(C)\hat{g}(1C) + (1-\hat{e}_X(C))\hat{g}(0C)$ 的误差线性依赖于 $\hat{e}_X$ 的误差，而伪-g函数通过正交化构造，使误差仅依赖于 $\hat{g}$ 的误差，从而避免 $e_X$ 估计不准导致的瓶颈。

## 实验评估

实验在合成数据与FARS真实数据上进行，nuisance函数使用XGBoost估计。基线仅对比插件估计器（PI），未包含LobsterNet（Chen et al., 2025）或深度FD估计器（Xu et al., 2024），缺乏与现有FD-HTE方法的横向对比。合成实验中，注入nuisance噪声 $\rho \in \{0.0, 0.2, 0.4, 0.6, 0.8, 1.0\}$，FD-DR与FD-R在 $\rho=1.0$ 时RMSE保持稳定，而PI估计器RMSE急剧恶化，验证了去偏性。

| 方法 | $\rho=0.0$ RMSE | $\rho=1.0$ RMSE |
|---|---|---|
| PI | - | - |
| FD-DR | - | - |
| FD-R | - | - |

注：论文未提供具体RMSE数值，仅定性描述“PI deteriorates rapidly, FD-DR/R maintain stable”。

FARS案例研究中，FD-DR与FD-R估计的 $\tau(C)$ 分布显示，超过95%的单位在主要安全带法下死亡率降低，SHAP特征重要性突出年龄、时间段和驾驶员状态。该结果支持FD结构假设的合理性，但未提供置信区间或预测区间，无法评估估计的不确定性。

评估边界方面，论文未报告计算效率、GPU使用或超参数敏感性分析。代码开源（`https://github.com/yonghanjung/FD-CATE`），但nuisance函数固定为XGBoost，未测试其他机器学习方法（如随机森林、神经网络）的影响。FARS数据中 $C$ 包含多个协变量，但未讨论高维协变量下nuisance估计的收敛速率是否仍满足 $n^{-1/4}$ 条件。

## 关联研究分析

从问题动机看，本文与LobsterNet（Chen et al., 2025）同属条件FD效应估计，但LobsterNet基于多任务神经网络，缺乏去偏性，而本文通过正交化构造提供统计保证。这一差异源于任务特性：LobsterNet追求模型灵活性以捕捉非线性，牺牲了统计鲁棒性；本文优先保证nuisance慢收敛下的准oracle速率，牺牲了模型灵活性（nuisance固定为XGBoost）。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，本文与DR-Learner（Kennedy, 2023）同属正交化估计器框架，但DR-Learner基于后门调整，本文基于前门调整。关键差异在于伪结果构造：DR-Learner的伪结果直接基于倾向得分与结果模型，而FD-DR-Learner的伪结果需整合中介分布权重。这一差异源于识别公式的不同：后门调整直接调整 $X-Y$ 路径，前门调整需通过 $Z$ 间接调整。FD-R-Learner的三阶段分解是否引入额外方差累积，论文未提供消融实验验证。

## 总结

本文要解决的核心矛盾是前门调整下条件异质效应估计缺乏去偏方法，现有FD方法或局限于平均效应，或缺乏统计鲁棒性。本文抓住的切入点是正交化框架的迁移性，将DR/R-Learner从后门调整推广至前门调整，通过伪结果构造与三阶段分解保持nuisance误差的二阶小量特性。本文证明了在nuisance以 $n^{-1/4}$ 慢速收敛时，FD-DR与FD-R保持准oracle速率，FARS案例中95%单位死亡率降低。本文的边界在于未提供不确定性量化，且nuisance函数固定为XGBoost，未测试高维协变量或非线性nuisance的影响。当协变量维度增加至数百维时，XGBoost的nuisance估计是否仍满足 $n^{-1/4}$ 收敛条件，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22531)