**1. 嵌套实验边界场数据**

路径：`/data1/user/lfz/Boundary_dy`

时间精度：3小时一次

frequency：每天一个文件

空间精度：全球2°x2.5°

垂直层数：47层

时间范围：199701-202212

| 实验 | 命名     | 关闭的污染源                                                 |
| :--- | -------- | ------------------------------------------------------------ |
| 01   | agr      | Agriculture (AGR) includes manure management, soil fertilizer emissions, rice  cultivation, enteric fermentation, and other agriculture |
| 02   | ene      | Energy Production (ENE)  Includes electricity and heat production, fuel production and  transformation, oil and gas fugitive/flaring, and fossil fuel fires |
| 03   | ind      | Industry (IND) Includes Industrial combustion (iron and steel, non-ferrous metals,  chemicals, pulp and paper, food and tobacco, non-metallic minerals,  construction, transportation equipment, machinery, mining and  quarrying, wood products, textile and leather, and other industry  combustion) and non-combustion industrial processes and product use  (cement production, lime production, other minerals, chemical  industry, metal production, food, beverage, wood, pulp, and paper, and  other non-combustion industrial emissions) |
| 04   | road     | Road Transportation (ROAD) includes cars, motorcycles, heavy and light duty trucks and buses |
| 05   | nrtr     | Non-Road/Off-Road Transportation (NRTR) Includes Rail, Domestic navigation, Other transportation |
| 06   | rcor     | Residential Combustion (RCO-R) includes residential heating and cooking CEDSGBD-MAPS 2017 |
| 07   | rcoc     | Commercial Combustion (RCO-C) Includes commercial and institutional combustion |
| 08   | rcoo     | Other Combustion (RCO-O) Includes combustion from agriculture, forestry, and fishing |
| 09   | slv      | Solvents (SLV) Includes solvents production and application (degreasing and cleaning,  paint application, chemical products manufacturing and processing,  and other product use) |
| 10   | wst      | Waste (WST) Includes solid waste disposal, waste incineration, waste-water  handling, and other waste handling |
| 11   | ship     | International Shipping (SHP) Includes international shipping and tanker loading |
| 12   | agrfire  | Agricultural Waste Burning (AGBURN)  Includes open fires from agricultural waste burning |
| 13   | openfire | Other Open Fires (OBURN) Includes deforestation, boreal forest, peat, savannah, and temperate  forest fires |
| 14   | afcid    | Fugitive, Combustion, Industrial dust (AFCID)                |
| 15   | dust     | Windblown Dust (WDUST)                                       |
| 16   | natural  | volcanic SO2                                                 |
|      |          | aircraft                                                     |
|      |          | lightning Nox                                                |
|      |          | biogenic Soil NO                                             |
|      |          | ocean                                                        |
|      |          | biogenic emissions                                           |
|      |          | very short-lived iodine and bromine species                  |
|      |          | decaying plants                                              |
| 00   | base     | /（控制实验）                                                |
|      |          |                                                              |

**2. PM2.5及其组分数据**

路径：`/data1/data/pm_composition`

时间精度：每月一次（原始数据为每天一次，做了月平均处理）

frequency：每个实验一个文件

空间精度：全球2°x2.5°

垂直层数：仅地面层

时间范围：199701-202212

变量：PM2.5, OC, BC, SOA, SALA, NO3, NH4

单位：ug m-3



**3. GEOS实验输入场数据**

路径：`/data/GEOSCHEM-INPUT/ExtData`

全球气象输入场数据：`/data/GEOSCHEM-INPUT/ExtData/GEOS_2x2.5`

亚洲气象输入数据（嵌套用）：`/data/GEOSCHEM-INPUT/ExtData/GEOS_0.5x0.625_AS`

污染源数据：`/data/GEOSCHEM-INPUT/ExtData/HEMCO`

输入场数据较大，爬数据可以参考脚本：`download_*.py`（路径：`/share/home/fzli/fchem_2X2.5`）



**4. GEOS实验原始结果数据**

路径：`/share/home/fzli/results_dy`

时间精度：每天一次

frequency：每个实验3个文件（前缀分别为：day_species - 排放气体物、day_pm25 - pm25、day_met - 气象变量）

空间精度：全球2°x2.5°

垂直层数：仅地面层

时间范围：199701-202212



**5. 如何计算pm组分并转换单位为ug m-3**

计算气象系数STP_F

`STP_F = 1013.25x温度/(298x气压)`

`OC =(ocpi x 1.07+ ocpo) x 12.01 x 10^6 x 10^6 x 2.1 x STP_F/(6.022x10^23)`

`DST = (dst1+dst2 x 0.3) x 29 x 10^6 x 10^6 x STP_F/(6.022x10^23)`

`SO4 = so4 x 96.06 x 1.35  x 10^6 x 10^6 x STP_F/(6.022x10^23)`

`BC = (bcpi + bcpo) x 12.01 x 10^6 x 10^6 x STP_F/(6.022x10^23)`

`NO3 = nit x 62.01 x 1.35 x 10^6 x 10^6 x STP_F/(6.022x10^23)`

`NH4 = nh4 x 18.05 x 1.35 x 10^6 x 10^6 x STP_F/(6.022x10^23)`

`SALA = sala x 31.4 x 1.86 x 10^6 x 10^6 x STP_F/(6.022x10^23)`

`SOA = soas x 1.07 x150. x 10^6 x 10^6 x STP_F/(6.022x10^23)`

可以参考脚本`pm_com.ncl`

路径：`/data1/user/lfz`





