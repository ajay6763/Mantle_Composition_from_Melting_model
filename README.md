# Mantle Composition Partial Melting 

Python 脚本，用于计算由于减压熔融而导致的主要氧化物在固相和熔融相中的分布，作为洋壳厚度的函数，或者换句话说，分数熔融的总百分比。 

主要氧化物的分配系数取自 Langmuir 等人，1992 年。

Python script to calculate the distribution of major oxides into solid and melt phases due to decompressional melting as a function of oceanic crust thickness or in other words aggregate percentage of frational melting. 

Distribution coefficients for major oxides are taken from Langmuir et al.,1992. 

## 估算部分熔融总体含量
<!-- Total Amount of Partial Melting  -->

对地幔橄榄岩的部分熔融实验对在特定 P-T 条件下可能产生的部分熔融程度提供了重要的限制。 Klein and Langmuir. (1987)是首次定义了部分熔融程度 $F$ 与洋脊处洋壳厚度 $h_c$ 之间关系。 

![如图所示](/Images/Niu_2021_ESR_F5.jpg)

[如图所示](/Images/Niu_2021_ESR_F5.jpg)定义固相线交点压力为 $P_o$，熔化停止压力为 $P_f$，则单位柱内存在的熔体总量 $F_t$ 为

$$
    F_t=\int_{P_{f}}^{P_{0}}F(P) dP
$$

那么平均部分熔融程度$\bar{F}$为

$$
    \bar{F}=\frac {\int_{P_{f}}^{P_{0}}F(P) dP} {P_0-P_f}
$$


一般来说，部分熔融程度 $F(P)$ 随着压强而改变，应该是 P(depth）的复函数。 然而，它可以通过以下方法进行近似，
在有限压力区间 $n$ 内用固定斜率 $\gamma_{n} =(dF/dP)_S$ （生产率函数 [Langmuir et al., 1992; Phipps Morgan, 2001]），由下式给出
$$
    \gamma_{n} =(dF/dP)_S = 
    
    \frac
    {\frac{\alpha T }{\rho C_p} - (\frac{\partial T_s}{\partial P})_{F}}
    {\frac{H_m }{C_p} + (\frac{\partial T_s}{\partial F})_{P}}

$$

其中 $T_s$ 是固相线温度，$\alpha$ 是 CTE，$C_p$ 是热容，$H_m$ 是熔化热（或熔化潜热）。 

对于这些变量的普遍接受的值，$\gamma$ 的平均值范围在每 GPa 压力释放的 10% 到 20% 之间 [例如，Langmuir et al., 1992]。 任何压力 $P_x$ 下存在的熔体量由所有相关 n 的 $\gamma_n (P_{n-1}-P_n) $ 之和给出，其中 $P_n$ 在最后一个压力区间变为 $P_x$，$P_o$是$P_{n-1}$ 在第一个压力区间，故因此部分熔融程度方程变为

$$
    F_t=\int_{P_{f}}^{P_{0}}\sum_{n=1}^{n} \gamma_n (P_{n-1}-P_n) dP
$$

请注意，在方程中，生产率函数 $\gamma$ 的单位为 $P^{-1}$ （即每单位压力释放产生的熔体）。 因此，$F_t$ 以 $P$ 为单位（例如 GPa）。 


**与洋壳厚度的关系**

假设每次扩散增量产生的熔体总量被分离形成洋壳，则方程给出地壳厚度 $h_c$ （严格来说，高度为 $h_c$  的熔体柱的重量 [Klein and Langmuir，1987；Langmuir et al.，1992]）
$$
    \rho_cgh_c=F_t=\bar{F}(P_0-P_f)
$$
即
$$
    h_c=\bar{F}(P_0-P_f) \frac {10^4}{\rho_cg}
$$
其中开始熔化的压力$P_o$和熔化停止的压力$P_f$单位是$GPa$，地壳密度$\rho_c$单位是 $kg/m^3$，地壳厚度$h_c$ 单位 $km$。

例如，Asimow et al., (1999)中的典型洋壳值$F = \sim 7.2%$，$P_o \sim 2.75 GPa$，$P_f = \sim 0.2 GPa$ 和 $\rho_c = 2880\ kg m^-3$ ，方程给出 $h_c = \sim 6.5 km$。

因此，$\bar{F}$ > ～10% ($F$ > 25%)的值被认为与正常产生的地壳产生量不一致，当然除了活跃的上升流地点外，这里的地壳可能达到异常厚度。 



[ Afonso et al., 2008 ](Images/Afonso_et_al_2008_G3_FA1.png "Degree of partial melting with depth for different melting models.")的地幔部分熔融模型采用了分段函数: 


$F(P) = 25.23-16.19P$ when P > 1.25 

$F(P) = 10.0-4.0P$    when P < 1.25

这里还有其他模型

| Model*   | Rerfence |
| -------- | ------- |
| $F(P) = 0.006 (P_o-P)$  | Klein & Langmuir, 1987    |
| $F(P) = k (P_o-P)$  | Turcotte & Phipps Morgan. (1992)     |
|   曲线   | Asimow et al., 2001    |
| 拟合的分段函数   | Afonso et al., 2008    |


**\*** 其中$P_o$是开始熔化的压力，单位是$GPa$，地壳密度$\rho_c$单位是 $kg/m^3$，地壳厚度$h_c$ 单位 $km$。

**存在的问题**

Klein and Langmuir. (1987)的这种解释简单且有吸引力，但基本假设是错误的(Niu. 2022):

[1] 减压熔融一直持续到莫霍面的假设忽略了CTBL的存在和影响

[2] MORB地幔具有均匀主量元素组成的假设忽略了地幔源非均质性对观测到的MORB化学的影响。

[3] MORB熔体中FeO（或Fe8）直接指示地幔熔化初始深度的假设忽略了熔化地幔中不可避免的熔体-固体平衡。因此，使用单一变量Fe 8计算的P O、T O和T MP没有意义。

[4] 使用MORB Fe 8，对应于Mg# = 0.56-0.68的可变演化MORB熔体来讨论地幔熔融过程，违反了基本的岩石学原理，详情见原文

[5] 因此，基于 MORB Fe 8（或任何其他形式，如 Fe 90）得出的结论是，全球洋脊 T MP变化（最高 ΔT MP  = 250 K）控制着初始深度/压力和融化程度完全是误导。


## 残余物和熔体的化学组分
<!-- Composition of Both Residue (s) and Melt(l) After Partial Melting -->
残余物的最终化学成分基本上由三个参数决定：系统中元素或组分的初始浓度 $C_o$、总分配系数 $D$ 和部分熔融程度(熔体的质量百分数)$F$。三个参数通过以下形式的表达式相互关联（Langmuir et al., 1992）: 
$$
    \frac {C_l} {C_o} = 
    \frac {1} {D } (1-F)^{\frac {1} {D} -1}
$$


由此可以推导出残余物的最终化学成分，见[熔融程度和组分的关系](oxide_variation_due_partial_melting.jpg)。总分配系数可参开Niu. (1997) 的结果。

