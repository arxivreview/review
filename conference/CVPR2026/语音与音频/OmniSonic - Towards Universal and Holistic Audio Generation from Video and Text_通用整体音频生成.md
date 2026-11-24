# CVPR2026最新论文 ｜OmniSonic: Towards Universal and Holistic Audio Generation from Video and Text ｜通用整体音频生成

研究机构：美国克莱姆森大学、加拿大多伦多大学

作者：Weiguo Pian、Saksham Singh Kushwaha、Zhimin Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.04348)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04348)

> 视频到音频生成旨在从无声视频中合成高保真声学信号，但现有模型通常局限于屏幕内环境声，无法处理屏幕外语音与环境声混合的复杂听觉场景。本文提出UniHAGen任务，定义屏幕内外多域声音联合生成的三种典型场景，并构建OmniSonic框架，通过TriAttn-DiT架构与MoE门控机制动态融合视觉、环境声文本与语音转录条件。实验表明该方法在混合场景生成质量上优于现有基线，但其时间同步精度受限于视觉特征选择，未达领域最优水平。

## 研究背景

当视频包含说话人与背景鸟鸣时，生成系统需同时合成与唇形同步的语音和提供氛围的环境声。这一需求要求模型区分屏幕内可见声源与屏幕外不可见声源，并跨语音、环境声、音乐等不同声学域进行联合建模。传统视频到音频模型仅关注屏幕内事件，而环境语音生成模型依赖纯文本输入，缺乏视觉接地以区分声源位置，导致无法处理多源混合场景。

视频到音频生成领域的主流路线基于潜在扩散模型，在音频变分自编码器潜空间进行去噪以提升保真度。近期工作如MMAudio和HunyuanVideo-Foley采用多模态扩散Transformer增强语义一致性，但均局限于非语音域；VinTAGe虽引入文本控制屏幕外声音，仍无法生成高质量语音。环境语音模型如VoiceLDM虽能合成语音，但缺乏视觉线索以区分屏幕内外声源。本文切入点在于统一语音与环境声生成，通过联合视频-文本条件建模，解决现有方法在复杂多源场景下的能力缺失。

## 核心方法

### 方法参照系

本文问题属于视频驱动音频生成路线，标准流程为：视觉特征提取→条件编码→潜空间去噪→波形重建。关键差异在于需同时处理屏幕内/外多域声音条件，传统方法采用静态条件拼接，无法动态平衡不同声源贡献。

### 条件编码与视觉对齐

条件编码器将环境声文本、语音转录与视觉帧映射至嵌入空间。环境声文本采用FLAN-T5编码器，语音转录采用SpeechT5加可微时长模块，视觉特征采用CLIP编码器。视觉条件与时间步嵌入融合后，通过帧对齐自适应层归一化调制后续层，实现视听时序对齐。该设计解决了传统方法中视觉特征与音频潜空间时间分辨率不匹配导致的同步误差。

$$\mathbf{c}_{vt} = \mathbf{c}_v \mathbf{W}_{vt} + \mathbf{t}$$

其中$\mathbf{c}_v$为视觉嵌入，$\mathbf{t}$为时间步嵌入，$\mathbf{W}_{vt}$为可学习投影矩阵，融合后的表示通过最近邻插值上采样至音频潜空间时间分辨率。

### TriAttn-DiT与MoE门控

TriAttn-DiT骨干通过三重交叉注意力融合三路条件。视觉特征与对应文本条件拼接，应用旋转位置编码后执行交叉注意力。MoE门控模块基于条件嵌入均值计算动态权重，加权融合三路注意力输出。该机制解决了静态条件拼接无法适应不同场景声源比例变化的问题，实现动态平衡。

$$\mathbf{v}_t = \omega_{sp.}\mathbf{x}_t^{sp.} + \omega_{on}\mathbf{x}_t^{on} + \omega_{off}\mathbf{x}_t^{off}$$

其中$\omega_{sp.}, \omega_{on}, \omega_{off}$为MoE门控权重，$\mathbf{x}_t^{sp.}, \mathbf{x}_t^{on}, \mathbf{x}_t^{off}$为三路交叉注意力输出，$\mathbf{v}_t$为预测速度场。

## 实验评估

实验在自建UniHAGen-Bench上进行，包含1003个样本覆盖三种场景。基线覆盖MMAudio、VinTAGe、HunyuanVideo-Foley等视频到音频模型及VoiceLDM等语音生成模型，但缺失纯文本到音频强基线如AudioLDM 2的完整对比。

| 模型 | FAD↓ | MKL↓ | AT score↑ | AV score↑ | WER↓ | DeSync↓ |
|---|---|---|---|---|---|---|
| MMAudio | 3.58 | 7.65 | 1.99 | 1.46 | - | 0.38 |
| VinTAGe | 9.33 | 24.26 | 0.66 | 0.50 | - | - |
| VoiceLDM | 14.09 | 13.40 | 0.97 | 1.25 | 0.14 | - |
| OmniSonic | 3.07 | 2.79 | 28.07 | 9.01 | 0.14 | 0.72 |

OmniSonic在FAD与MKL上显著优于所有基线，AT与AV分数均值超MMAudio 1.29，但DeSync 0.72劣于MMAudio 0.38。

| 模型 | FAD↓ | MKL↓ | AT/AV Mean↑ | WER↓ | DeSync↓ |
|---|---|---|---|---|---|
| OmniSonic | 3.07 | 2.79 | 18.54 | 0.14 | 0.72 |
| w/o MoE Gating | 6.12 | 5.25 | 15.94 | 0.56 | 1.23 |

移除MoE门控导致FAD增加3.05，WER增加4倍，表明动态权重对混合场景生成至关重要。

评估指标涵盖FAD、MKL、AT/AV、WER、CER、PER、DeSync及主观MOS，但缺乏计算效率指标如实时因子。UniHAGen-Bench为合成数据，SNR随机采样可能引入分布偏差。代码未开源，超参数与GPU配置未报告，可复现性受限。

## 关联研究分析

从问题动机看，OmniSonic与VinTAGe均处理屏幕内外声音，但VinTAGe局限于环境声，无法生成语音。OmniSonic引入语音转录条件与视觉接地，解决语音与环境声混合场景的生成需求。差异根源在于任务定义：VinTAGe假设屏幕外声音仅为环境声，而OmniSonic将语音视为独立声学域，需专门编码器与对齐机制。

从方法设计看，OmniSonic与MMAudio同用多模态扩散Transformer，但MMAudio采用静态条件拼接，OmniSonic引入MoE门控动态加权。MMAudio在DeSync上优于OmniSonic，因其使用Synchformer特征提供细粒度时序线索，而OmniSonic仅用CLIP特征，在静态场景下时序敏感性不足。这一差异揭示视觉特征选择对时间同步精度的决定性影响，MoE门控虽提升生成质量，但无法弥补视觉特征本身的时序局限。

## 总结

本文核心矛盾在于现有视频到音频模型无法处理屏幕内外多域声音混合场景。切入点在于统一语音与环境声生成，通过TriAttn-DiT与MoE门控动态融合多源条件。实验证明OmniSonic在FAD 3.07与MKL 2.79上优于基线，但DeSync 0.72未达MMAudio的0.38。边界在于CLIP视觉特征在静态场景下时序敏感性不足，导致时间同步精度受限。当引入Synchformer等细粒度同步特征时，MoE门控的动态权重能否进一步提升时间同步精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04348)