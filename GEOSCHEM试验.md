# GEOSCHEM试验 - Group

# BACKGROUND

PM2.5最主要的成分是有机碳（OC），![图片](https://mmbiz.qpic.cn/mmbiz_png/aVugibaFCcicNcw2vdrpibX1jsbkxQWtJNqxJ7rD4IM0u6teObRibxfI2qrHC1wTpxNaz3iauDyvpFm5ncQzFg2psicw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)，其他成分包括氯化物、钠、镁、钾、钙、土壤和水分子，以及其他未标明成分。这些成分主要来自国内、工业、国际、农业和运输部门。

## 1. 分组分

### 1.1 组分信息 - PM2.5

**组分信息查询 CodeDir/src/GEOS-Chem/GeosCore/aerosol_mod.F90**

! Particulate matter < 2.5um [kg/m3]

​    PM25(I,J,L) = NH4(I,J,L)    * SIA_GROWTH + &

​           NIT(I,J,L)    * SIA_GROWTH + &

​           SO4(I,J,L)    * SIA_GROWTH + &

​           HMS(I,J,L)    * SIA_GROWTH + &  ! (jmm, 06/30/18)

​           BCPI(I,J,L)          + &

​           BCPO(I,J,L)          + &

​           OCPO(I,J,L)          + &

​           OCPI(I,J,L)    * ORG_GROWTH + &

​           SALA(I,J,L)    * SSA_GROWTH + &    ! SSA_GROWTH = 1.86 

​           SOILDUST(I,J,L,1)       + &

​           SOILDUST(I,J,L,2)       + &

​           SOILDUST(I,J,L,3)       + &

​           SOILDUST(I,J,L,4)       + &

​           SOILDUST(I,J,L,5) * 0.3_fp      ! + 30% of DST2

**即：NH4, NIT, SO4, BCPI,BCPO, OCPI, OCPO, SALA, DST1, DST2, DST3, DST4.**

unit: molec/cm3

# . 分源

## 2.1 分源信息

CEDS (人为排放源)：

1. non-combustion **agricultural** sector
2. **energy** transformation and extraction
3. **industrial** combustion
4. residential combustion
5. **commercial** combustion
6. other combustion
7. **international shipping**
8. **solvents**
9. surface **Transportation (Road**, Rail, Other)
10. **waste** disposal and handling
11. **DUST**

Sensitivity By fuel type

12. total coal
12. soild biofuel 
12. Liquid oil and natural gas
12. non-combustion processes
12. Coal from energy
12. Coal from industrial
12. Coal from residential
12. Soild biofuel from residential combustion

GFED4(野火)

17. **non-arg fires** 

    TEMP - 温带森林

    PEAT - 沼泽

    SAVA - 草原

    DEFO - 热带森林

    BORF - 北方针叶林

18. **AGRI - 农业**
19. Others
20. Fugitive, Combustion, Industrial dust (AFCID)
21. Aircraft emission AEIC

### 2.2 实验记录

 20231218-0108

- [x] 01-base 1997-2023
  - 2007 (2024.1.24)
- [x] 02-agrfire 1997-2023 (GFED -2019)
  - 2015 (2024.1.24)
- [x] 03-openfire 1997-2023 (GFED -2019) 
  - 2003/11 broke
  - 2005 (2024.1.24)
- [ ] 04 - dust 1997-2023
  - 2016 (2024.1.24)
- [ ] 05 - other natural (biogenic, seasalt, soilnox) 1997-2023
  - 2010 (2024.1.24)
- [ ] 06 - aircraft emission （AEIC 2019）
  - 1997 (2024.1.24)
- [ ] 07 - rco
  - 1997 (2024.1.24)

# 3 jielan - 臭氧输送路径

- 两个台风外围气流影响下的污染个例：
  - 2021年7月22-25（23-24为臭氧污染日）
  - 2021年9月10-13（11-12为臭氧污染日）
- 模拟要点：
  1. 【污染日和非污染日对比】污染日(7月23-24，9月11-12)与污染出现前后日的气象条件相比，造成污染的原因是台风外围影响下污染物及其前体物的跨边界层输送，即污染物从香港上游城市往下游输送；
  2. 【污染日发现O3和PM2.5都呈现明显日变化，即白天二者都高，入夜后二者都低】

- 模拟目的：

​	证明地表风场（1000hpa）的风场存在逐小时变化，白天珠江口为偏北风，入夜后珠江口转为偏南风；白天	北风条件使得香港上游城市的颗粒物和臭氧前体物输送至香港，从而加剧污染。

111-116E，21-25N
