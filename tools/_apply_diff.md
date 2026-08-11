# 真实数据写回差异报告（最终核对版）

源: tools/all_aircraft_realdata_verify.md （216 款全联网核对）  
备份原始: tools/\_pnml_backup

## 总览

- 有改动的机型: 214 / 216
- 字段改动次数: 航程 194 · 座级 114 · 巡航 196
- cost_factor(价格系数): 全部保持原值（游戏用相对系数，未存绝对 USD；缺失者保持原估计值）
- 无可靠来源、保持原值的字段: BRITTEN_NORMAN_BN2T 的 range+cruise、DEHAVILLAND_COMET 的 range（共 3 项，按决定值保留）

## 按厂商分布

- 1-11: 4 款 (航程 4 · 座级 3 · 巡航 4)
- 146-100~ARJ70: 1 款 (航程 1 · 座级 1 · 巡航 1)
- 146-200~ARJ85: 1 款 (航程 1 · 座级 1 · 巡航 1)
- 146-300QT: 1 款 (航程 1 · 座级 0 · 巡航 1)
- 146-300~ARJ100: 1 款 (航程 1 · 座级 1 · 巡航 1)
- 208: 1 款 (航程 0 · 座级 1 · 巡航 0)
- 208B: 1 款 (航程 1 · 座级 0 · 巡航 0)
- 402: 1 款 (航程 1 · 座级 1 · 巡航 1)
- 404: 1 款 (航程 1 · 座级 1 · 巡航 1)
- 408: 1 款 (航程 1 · 座级 0 · 巡航 1)
- 414: 1 款 (航程 0 · 座级 1 · 巡航 1)
- 421: 1 款 (航程 0 · 座级 1 · 巡航 1)
- 880: 1 款 (航程 1 · 座级 1 · 巡航 1)
- 990: 1 款 (航程 0 · 座级 1 · 巡航 0)
- A220: 2 款 (航程 1 · 座级 2 · 巡航 2)
- A300: 6 款 (航程 6 · 座级 3 · 巡航 6)
- A320: 8 款 (航程 8 · 座级 2 · 巡航 7)
- A321: 3 款 (航程 2 · 座级 2 · 巡航 2)
- A330: 5 款 (航程 4 · 座级 3 · 巡航 5)
- A340: 3 款 (航程 3 · 座级 1 · 巡航 3)
- A350: 2 款 (航程 2 · 座级 2 · 巡航 2)
- A380: 1 款 (航程 1 · 座级 1 · 巡航 1)
- AN28: 1 款 (航程 1 · 座级 1 · 巡航 0)
- ATR42: 4 款 (航程 3 · 座级 0 · 巡航 4)
- ATR72: 4 款 (航程 2 · 座级 1 · 巡航 3)
- An124: 1 款 (航程 1 · 座级 1 · 巡航 1)
- An148: 1 款 (航程 1 · 座级 1 · 巡航 1)
- An158: 1 款 (航程 1 · 座级 0 · 巡航 1)
- An225: 1 款 (航程 1 · 座级 0 · 巡航 1)
- B707: 2 款 (航程 2 · 座级 0 · 巡航 2)
- B717: 1 款 (航程 1 · 座级 1 · 巡航 1)
- B727: 3 款 (航程 3 · 座级 2 · 巡航 3)
- B737: 16 款 (航程 14 · 座级 14 · 巡航 16)
- B747: 15 款 (航程 15 · 座级 6 · 巡航 15)
- B757: 3 款 (航程 3 · 座级 0 · 巡航 3)
- B767: 6 款 (航程 6 · 座级 1 · 巡航 6)
- B777: 8 款 (航程 8 · 座级 7 · 巡航 8)
- B787: 3 款 (航程 3 · 座级 3 · 巡航 3)
- BN-2B: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Beech1900D: 1 款 (航程 1 · 座级 0 · 巡航 0)
- C909: 1 款 (航程 1 · 座级 1 · 巡航 1)
- C919: 1 款 (航程 1 · 座级 0 · 巡航 1)
- C929: 1 款 (航程 0 · 座级 0 · 巡航 1)
- CRJ: 11 款 (航程 11 · 座级 3 · 巡航 11)
- Caravelle: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Comet: 1 款 (航程 0 · 座级 1 · 巡航 1)
- Concorde: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Constellation: 1 款 (航程 1 · 座级 0 · 巡航 0)
- DC10: 3 款 (航程 3 · 座级 3 · 巡航 3)
- DC3: 1 款 (航程 1 · 座级 1 · 巡航 0)
- DC6: 1 款 (航程 1 · 座级 1 · 巡航 1)
- DC7: 1 款 (航程 1 · 座级 1 · 巡航 1)
- DC8: 5 款 (航程 5 · 座级 0 · 巡航 5)
- DC9: 5 款 (航程 5 · 座级 1 · 巡航 5)
- DHC6-400: 1 款 (航程 1 · 座级 0 · 巡航 0)
- DO228: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Dash_8: 6 款 (航程 6 · 座级 5 · 巡航 6)
- E145: 1 款 (航程 1 · 座级 0 · 巡航 0)
- E170: 2 款 (航程 2 · 座级 2 · 巡航 2)
- E175: 3 款 (航程 2 · 座级 3 · 巡航 3)
- E190: 4 款 (航程 4 · 座级 3 · 巡航 4)
- E195: 4 款 (航程 4 · 座级 4 · 巡航 4)
- ERJ135: 1 款 (航程 1 · 座级 0 · 巡航 1)
- ERJ140: 1 款 (航程 1 · 座级 0 · 巡航 1)
- F100: 1 款 (航程 1 · 座级 1 · 巡航 1)
- F27: 1 款 (航程 1 · 座级 1 · 巡航 1)
- F28: 1 款 (航程 1 · 座级 1 · 巡航 1)
- F70: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Il114: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Il18: 1 款 (航程 0 · 座级 1 · 巡航 0)
- Il62: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Il76: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Il96: 1 款 (航程 1 · 座级 1 · 巡航 1)
- L1011: 1 款 (航程 1 · 座级 0 · 巡航 1)
- L188: 1 款 (航程 1 · 座级 1 · 巡航 1)
- L410: 1 款 (航程 1 · 座级 0 · 巡航 0)
- MA60: 1 款 (航程 1 · 座级 0 · 巡航 0)
- MA600: 1 款 (航程 1 · 座级 0 · 巡航 0)
- MC21: 1 款 (航程 0 · 座级 1 · 巡航 1)
- MD11: 2 款 (航程 2 · 座级 0 · 巡航 2)
- MD80: 4 款 (航程 4 · 座级 0 · 巡航 4)
- MD90: 2 款 (航程 2 · 座级 1 · 巡航 2)
- PC12: 1 款 (航程 1 · 座级 0 · 巡航 0)
- PC24: 1 款 (航程 0 · 座级 1 · 巡航 1)
- SSJ100: 1 款 (航程 0 · 座级 0 · 巡航 1)
- Trident: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Tu134: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Tu154B: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Tu154M: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Tu204: 1 款 (航程 0 · 座级 0 · 巡航 1)
- Tu214: 1 款 (航程 1 · 座级 0 · 巡航 1)
- VC10: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Viscount: 1 款 (航程 1 · 座级 1 · 巡航 1)
- Y7-200: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Yak40: 1 款 (航程 1 · 座级 0 · 巡航 1)
- Yak42: 1 款 (航程 1 · 座级 1 · 巡航 0)

## 逐机型差异

### AIRBUS_A220_100

- seats: 120->116
- cruise: 829->870 km/h

### AIRBUS_A321LR

- range: 1345->1347 (≈7398->7408 km)
- cruise: 830->833 km/h

### AIRBUS_A321XLR

- seats: 210->206
- cruise: 902->833 km/h

### AIRBUS_A330_800NEO

- seats: 264->257
- cruise: 926->871 km/h

### ANTONOV_AN148

- range: 564->800 (≈3102->4400 km)
- seats: 80->68
- cruise: 830->870 km/h

### ANTONOV_AN158

- range: 509->455 (≈2800->2502 km)
- cruise: 886->870 km/h

### ATR_42_300

- range: 165->267 (≈908->1468 km)
- cruise: 491->484 km/h

### ATR_42_300F

- range: 165->421 (≈908->2316 km)
- cruise: 491->495 km/h

### ATR_42_500

- range: 280->245 (≈1540->1348 km)
- cruise: 564->556 km/h

### ATR_42_600

- cruise: 564->535 km/h

### ATR_72_200

- seats: 74->72

### ATR_72_200F

- cruise: 523->517 km/h

### ATR_72_500

- range: 295->260 (≈1622->1430 km)
- cruise: 515->510 km/h

### ATR_72_600

- range: 249->255 (≈1370->1402 km)
- cruise: 515->510 km/h

### AVIC_MA60

- range: 249->291 (≈1370->1600 km)

### AVIC_MA600

- range: 251->260 (≈1380->1430 km)

### AVIC_Y7_200

- range: 282->165 (≈1551->908 km)
- cruise: 420->423 km/h

### Airbus_A220_300

- range: 1090->1195 (≈5995->6572 km)
- seats: 145->141
- cruise: 840->870 km/h

### Airbus_A300_600F

- range: 2565->1364 (≈14108->7502 km)
- cruise: 870->833 km/h

### Airbus_A300_600R

- range: 2230->1364 (≈12265->7502 km)
- seats: 220->247
- cruise: 870->833 km/h

### Airbus_A310_200

- range: 1000->1182 (≈5500->6501 km)
- seats: 218->195
- cruise: 902->870 km/h

### Airbus_A310_200F

- range: 1000->1082 (≈5500->5951 km)
- cruise: 902->871 km/h

### Airbus_A310_300

- range: 1965->1735 (≈10808->9542 km)
- seats: 218->220
- cruise: 902->870 km/h

### Airbus_A310_300F

- range: 1320->1465 (≈7260->8058 km)
- cruise: 902->871 km/h

### Airbus_A318

- range: 665->1044 (≈3658->5742 km)
- cruise: 854->829 km/h

### Airbus_A319

- range: 1230->1262 (≈6765->6941 km)
- cruise: 869->829 km/h

### Airbus_A319neo

- range: 1200->1245 (≈6600->6848 km)
- seats: 160->140

### Airbus_A320_100

- range: 980->875 (≈5390->4812 km)
- cruise: 902->828 km/h

### Airbus_A320_200

- range: 1020->1109 (≈5610->6100 km)
- cruise: 902->828 km/h

### Airbus_A320neo

- range: 1165->1145 (≈6408->6298 km)
- seats: 165->150
- cruise: 833->828 km/h

### Airbus_A321_100

- range: 785->755 (≈4318->4152 km)
- cruise: 902->828 km/h

### Airbus_A321_200

- range: 885->1078 (≈4868->5929 km)
- cruise: 902->828 km/h

### Airbus_A321neo

- range: 1400->1345 (≈7700->7398 km)
- seats: 220->206

### Airbus_A330_200

- range: 2415->2445 (≈13282->13448 km)
- cruise: 878->871 km/h

### Airbus_A330_200F

- range: 1335->1345 (≈7342->7398 km)
- cruise: 878->871 km/h

### Airbus_A330_300

- range: 1950->2136 (≈10725->11748 km)
- seats: 295->277
- cruise: 926->871 km/h

### Airbus_A330_900neo

- range: 2427->2475 (≈13348->13612 km)
- seats: 300->287
- cruise: 926->871 km/h

### Airbus_A340_300

- range: 2465->2255 (≈13558->12402 km)
- cruise: 902->871 km/h

### Airbus_A340_500

- range: 3000->3031 (≈16500->16670 km)
- cruise: 902->871 km/h

### Airbus_A340_600

- range: 2635->2527 (≈14492->13898 km)
- seats: 380->379
- cruise: 902->871 km/h

### Airbus_A350_1000

- range: 2950->3036 (≈16225->16698 km)
- seats: 366->410
- cruise: 945->912 km/h

### Airbus_A350_900

- range: 2700->2864 (≈14850->15752 km)
- seats: 315->325
- cruise: 945->903 km/h

### Airbus_A380_800

- range: 2735->2855 (≈15042->15702 km)
- seats: 652->525
- cruise: 1023->903 km/h

### Antonov_124

- range: 1075->673 (≈5912->3702 km)
- seats: 0->350
- cruise: 862->865 km/h

### Antonov_225

- range: 2770->2800 (≈15235->15400 km)
- cruise: 846->800 km/h

### BAC_1_11_200

- range: 235->244 (≈1292->1342 km)
- seats: 75->89
- cruise: 878->882 km/h

### BAC_1_11_300

- range: 465->371 (≈2558->2040 km)
- seats: 75->89
- cruise: 878->882 km/h

### BAC_1_11_400

- range: 635->371 (≈3492->2040 km)
- cruise: 870->882 km/h

### BAC_1_11_500

- range: 570->499 (≈3135->2744 km)
- seats: 115->119
- cruise: 870->871 km/h

### BAC_CONCORDE

- range: 1230->1196 (≈6765->6578 km)
- seats: 100->128
- cruise: 2337->2154 km/h

### BAe_146_100

- range: 555->704 (≈3052->3872 km)
- seats: 92->82
- cruise: 781->789 km/h

### BAe_146_200

- range: 525->664 (≈2888->3652 km)
- seats: 112->100
- cruise: 781->789 km/h

### BAe_146_300

- range: 495->607 (≈2722->3338 km)
- seats: 128->112
- cruise: 781->789 km/h

### BAe_146_300QT

- range: 495->607 (≈2722->3338 km)
- cruise: 781->789 km/h

### BOEING_737MAX7

- seats: 150->153
- cruise: 975->839 km/h

### BOEING_747SP

- range: 2236->2239 (≈12298->12314 km)
- seats: 320->331
- cruise: 967->1000 km/h

### BOEING_757_300

- range: 1273->1143 (≈7002->6286 km)
- cruise: 934->858 km/h

### BOEING_777_8

- range: 3036->3198 (≈16698->17589 km)


- seats: 365->395
- cruise: 951->905 km/h

### BRITTEN_NORMAN_BN2B

- range: 195->254 (≈1072->1397 km)
- cruise: 257->240 km/h

### Boeing_707_320

- range: 2050->1262 (≈11275->6941 km)
- cruise: 999->972 km/h

### Boeing_707_420

- range: 2210->1627 (≈12155->8948 km)
- cruise: 991->972 km/h

### Boeing_717_200

- range: 870->695 (≈4785->3822 km)
- seats: 117->106
- cruise: 918->811 km/h

### Boeing_727_100

- range: 950->758 (≈5225->4169 km)
- seats: 131->106
- cruise: 999->960 km/h

### Boeing_727_200

- range: 1155->858 (≈6352->4719 km)
- seats: 147->134
- cruise: 999->954 km/h

### Boeing_727_200F

- range: 905->858 (≈4978->4719 km)
- cruise: 905->954 km/h

### Boeing_737_100

- range: 855->518 (≈4702->2849 km)
- seats: 85->118
- cruise: 878->796 km/h

### Boeing_737_200

- range: 945->873 (≈5198->4802 km)
- seats: 97->130
- cruise: 878->796 km/h

### Boeing_737_200C

- range: 845->873 (≈4648->4802 km)
- cruise: 878->796 km/h

### Boeing_737_300

- range: 755->759 (≈4152->4174 km)
- seats: 128->149
- cruise: 910->828 km/h

### Boeing_737_300F

- range: 845->759 (≈4648->4174 km)
- cruise: 910->828 km/h

### Boeing_737_400

- range: 755->695 (≈4152->3822 km)
- seats: 146->188
- cruise: 918->828 km/h

### Boeing_737_500

- seats: 108->132
- cruise: 910->828 km/h

### Boeing_737_600

- range: 1015->1089 (≈5582->5990 km)
- seats: 108->130
- cruise: 959->834 km/h

### Boeing_737_700

- range: 1120->1013 (≈6160->5572 km)
- seats: 128->149
- cruise: 975->834 km/h

### Boeing_737_800

- range: 1020->988 (≈5610->5434 km)
- seats: 160->189
- cruise: 975->837 km/h

### Boeing_737_900

- range: 685->1000 (≈3768->5500 km)
- seats: 180->189
- cruise: 975->828 km/h

### Boeing_737_900ER

- range: 900->1077 (≈4950->5924 km)
- seats: 180->220
- cruise: 975->840 km/h

### Boeing_737_MAX10

- range: 1044->1036 (≈5742->5698 km)
- seats: 195->230
- cruise: 975->842 km/h

### Boeing_737_MAX8

- range: 1205->1182 (≈6628->6501 km)
- seats: 162->189
- cruise: 975->842 km/h

### Boeing_737_MAX9

- range: 1250->1109 (≈6875->6100 km)
- seats: 178->220
- cruise: 975->842 km/h

### Boeing_747_100

- range: 1665->1782 (≈9158->9801 km)
- cruise: 967->900 km/h

### Boeing_747_200

- range: 2000->2209 (≈11000->12150 km)
- cruise: 967->900 km/h

### Boeing_747_200M

- range: 2000->2209 (≈11000->12150 km)
- seats: 258->238
- cruise: 967->900 km/h

### Boeing_747_300

- range: 2235->2131 (≈12292->11720 km)
- cruise: 999->905 km/h

### Boeing_747_300M

- range: 2165->2255 (≈11908->12402 km)
- seats: 245->366
- cruise: 999->905 km/h

### Boeing_747_400

- range: 2420->2445 (≈13310->13448 km)
- cruise: 991->910 km/h

### Boeing_747_400BCF

- range: 1365->1500 (≈7508->8250 km)
- cruise: 991->910 km/h

### Boeing_747_400D

- range: 600->1818 (≈3300->9999 km)
- seats: 560->568
- cruise: 991->957 km/h

### Boeing_747_400ER

- range: 2555->2554 (≈14052->14047 km)
- seats: 524->416
- cruise: 991->899 km/h

### Boeing_747_400ERF

- range: 1655->1678 (≈9102->9229 km)
- cruise: 991->899 km/h

### Boeing_747_400M

- range: 2400->2445 (≈13200->13448 km)
- cruise: 991->957 km/h

### Boeing_747_400SCD

- range: 1480->2444 (≈8140->13442 km)
- seats: 0->450
- cruise: 991->911 km/h

### Boeing_747_8F

- range: 1490->1478 (≈8195->8129 km)
- cruise: 1007->898 km/h

### Boeing_747_8I

- range: 2665->2727 (≈14658->14998 km)
- cruise: 1007->908 km/h

### Boeing_757_200

- range: 1365->1296 (≈7508->7128 km)
- cruise: 934->858 km/h

### Boeing_757_200F

- range: 1050->1060 (≈5775->5830 km)
- cruise: 934->858 km/h

### Boeing_767_200

- range: 1285->1309 (≈7068->7200 km)
- seats: 181->216
- cruise: 910->858 km/h

### Boeing_767_200ER

- range: 2450->2218 (≈13475->12199 km)
- cruise: 910->858 km/h

### Boeing_767_300

- range: 1420->1309 (≈7810->7200 km)
- cruise: 910->858 km/h

### Boeing_767_300ER

- range: 1995->2013 (≈10972->11072 km)
- cruise: 910->858 km/h

### Boeing_767_300F

- range: 1085->1095 (≈5968->6022 km)
- cruise: 910->858 km/h

### Boeing_767_400ER

- range: 1875->1894 (≈10312->10417 km)
- cruise: 941->851 km/h

### Boeing_777X

- range: 2560->2695 (≈14080->14822 km)
- seats: 426->414
- cruise: 905->903 km/h

### Boeing_777_200

- range: 1745->1764 (≈9598->9702 km)
- seats: 400->305
- cruise: 951->896 km/h

### Boeing_777_200ER

- range: 2575->2379 (≈14162->13084 km)
- seats: 314->301
- cruise: 951->896 km/h

### Boeing_777_200F

- range: 1635->3283 (≈8992->18056 km)
- cruise: 951->896 km/h

### Boeing_777_200LR

- range: 3125->2881 (≈17188->15846 km)
- seats: 314->301
- cruise: 951->896 km/h

### Boeing_777_300

- range: 2000->2022 (≈11000->11121 km)
- seats: 451->368
- cruise: 951->896 km/h

### Boeing_777_300ER

- range: 2645->2482 (≈14548->13651 km)
- seats: 386->392
- cruise: 951->916 km/h

### Boeing_787_10

- range: 2165->2131 (≈11908->11720 km)
- seats: 318->336
- cruise: 943->903 km/h

### Boeing_787_8

- range: 2735->2460 (≈15042->13530 km)
- seats: 242->248
- cruise: 943->903 km/h

### Boeing_787_9

- range: 2835->2547 (≈15592->14008 km)
- seats: 280->296
- cruise: 943->903 km/h

### Bombardier_CRJ1000

- range: 475->491 (≈2612->2700 km)
- cruise: 850->829 km/h

### Bombardier_CRJ1000EL

- range: 325->347 (≈1788->1908 km)
- seats: 100->104
- cruise: 850->829 km/h

### Bombardier_CRJ100ER

- range: 540->545 (≈2970->2998 km)
- cruise: 814->786 km/h

### Bombardier_CRJ100LR

- range: 670->675 (≈3685->3712 km)
- cruise: 814->786 km/h

### Bombardier_CRJ200ER

- range: 550->554 (≈3025->3047 km)
- cruise: 814->786 km/h

### Bombardier_CRJ200LR

- range: 670->675 (≈3685->3712 km)
- cruise: 814->786 km/h

### Bombardier_CRJ700

- range: 405->573 (≈2228->3152 km)
- cruise: 830->876 km/h

### Bombardier_CRJ700ER

- range: 500->684 (≈2750->3762 km)
- cruise: 830->876 km/h

### Bombardier_CRJ900

- range: 350->455 (≈1925->2502 km)
- seats: 88->90
- cruise: 846->829 km/h

### Bombardier_CRJ900ER

- range: 430->536 (≈2365->2948 km)
- seats: 88->90
- cruise: 846->829 km/h

### Bombardier_CRJ900LR

- range: 505->615 (≈2778->3382 km)
- cruise: 846->829 km/h

### Bombardier_Dash_8_100

- range: 340->343 (≈1870->1886 km)
- seats: 39->40
- cruise: 499->500 km/h

### Bombardier_Dash_8_200

- range: 310->311 (≈1705->1710 km)
- seats: 39->40
- cruise: 547->535 km/h

### Bombardier_Dash_8_200Q

- range: 310->311 (≈1705->1710 km)
- seats: 39->40
- cruise: 547->535 km/h

### Bombardier_Dash_8_300

- range: 280->283 (≈1540->1556 km)
- seats: 50->56
- cruise: 531->532 km/h

### Bombardier_Dash_8_300Q

- range: 280->283 (≈1540->1556 km)
- seats: 50->56
- cruise: 531->532 km/h

### Bombardier_Dash_8_400Q

- range: 455->371 (≈2502->2040 km)
- cruise: 668->667 km/h

### CESSNA_208

- seats: 13->9

### CESSNA_208B

- range: 360->325 (≈1980->1788 km)

### CESSNA_402

- range: 236->429 (≈1298->2360 km)
- seats: 8->10
- cruise: 380->263 km/h

### CESSNA_404

- range: 436->620 (≈2398->3410 km)
- seats: 9->10
- cruise: 330->302 km/h

### CESSNA_408

- range: 304->309 (≈1672->1700 km)
- cruise: 388->390 km/h

### CESSNA_414

- seats: 7->8
- cruise: 360->339 km/h

### CESSNA_421

- seats: 8->6
- cruise: 420->440 km/h

### COMAC_C909

- range: 673->400 (≈3702->2200 km)
- seats: 90->78
- cruise: 886->828 km/h

### COMAC_C919

- range: 1020->741 (≈5610->4076 km)
- cruise: 902->835 km/h

### COMAC_C929

- cruise: 945->908 km/h

### CONVAIR_880

- range: 1018->832 (≈5599->4576 km)
- seats: 100->110
- cruise: 910->990 km/h

### CONVAIR_990

- seats: 120->149

### DEHAVILLAND_COMET

- seats: 90->81
- cruise: 740->790 km/h

### DEHAVILLAND_DHC6_400

- range: 236->269 (≈1298->1480 km)

### DOUGLAS_DC3

- range: 473->436 (≈2602->2398 km)
- seats: 30->32

### DOUGLAS_DC6

- range: 1527->1341 (≈8398->7376 km)
- seats: 81->68
- cruise: 504->501 km/h

### DOUGLAS_DC7

- range: 1673->1649 (≈9202->9070 km)
- seats: 95->105
- cruise: 504->557 km/h

### Douglas_DC10_10

- range: 1100->1182 (≈6050->6501 km)
- seats: 255->270
- cruise: 983->876 km/h

### Douglas_DC10_30

- range: 1910->1745 (≈10505->9598 km)
- seats: 255->270
- cruise: 983->876 km/h

### Douglas_DC10_40

- range: 1665->1709 (≈9158->9400 km)
- seats: 255->270
- cruise: 983->876 km/h

### Douglas_DC8_10

- range: 1255->1265 (≈6902->6958 km)
- cruise: 902->895 km/h

### Douglas_DC8_20

- range: 1350->1364 (≈7425->7502 km)
- cruise: 902->895 km/h

### Douglas_DC8_30

- range: 1335->1349 (≈7342->7420 km)
- cruise: 902->895 km/h

### Douglas_DC8_40

- range: 1770->1787 (≈9735->9828 km)
- cruise: 902->895 km/h

### Douglas_DC8_50

- range: 1950->1971 (≈10725->10840 km)
- cruise: 902->895 km/h

### Douglas_DC9_10

- range: 530->426 (≈2915->2343 km)
- cruise: 902->903 km/h

### Douglas_DC9_20

- range: 535->489 (≈2942->2690 km)
- cruise: 902->898 km/h

### Douglas_DC9_30

- range: 555->505 (≈3052->2778 km)
- cruise: 918->898 km/h

### Douglas_DC9_40

- range: 520->524 (≈2860->2882 km)
- cruise: 894->898 km/h

### Douglas_DC9_50

- range: 600->438 (≈3300->2409 km)
- seats: 135->139
- cruise: 918->898 km/h

### EMBRAER_E175_E2

- seats: 88->80
- cruise: 886->833 km/h

### EMBRAER_E190_E2

- range: 963->993 (≈5296->5462 km)
- cruise: 886->833 km/h

### EMBRAER_ERJ135

- range: 591->589 (≈3250->3240 km)
- cruise: 834->831 km/h

### EMBRAER_ERJ140

- range: 555->556 (≈3052->3058 km)
- cruise: 834->831 km/h

### Embraer_E170LR

- range: 700->724 (≈3850->3982 km)
- seats: 78->66
- cruise: 886->829 km/h

### Embraer_E170STD

- range: 600->724 (≈3300->3982 km)
- seats: 78->66
- cruise: 886->829 km/h

### Embraer_E175LR

- range: 700->741 (≈3850->4076 km)
- seats: 86->76
- cruise: 886->829 km/h

### Embraer_E175STD

- range: 600->741 (≈3300->4076 km)
- seats: 86->76
- cruise: 886->829 km/h

### Embraer_E190AR

- range: 800->17 (≈4400->94 km)
- seats: 106->100
- cruise: 886->829 km/h

### Embraer_E190LR

- range: 765->825 (≈4208->4538 km)
- seats: 106->100
- cruise: 886->829 km/h

### Embraer_E190STD

- range: 600->809 (≈3300->4450 km)
- seats: 106->100
- cruise: 886->829 km/h

### Embraer_E195AR

- range: 735->741 (≈4042->4076 km)
- seats: 118->100
- cruise: 886->829 km/h

### Embraer_E195LR

- range: 600->606 (≈3300->3333 km)
- seats: 118->100
- cruise: 886->829 km/h

### Embraer_E195STD

- range: 465->472 (≈2558->2596 km)
- seats: 118->100
- cruise: 886->829 km/h

### Embraer_E195_E2

- range: 873->1018 (≈4802->5599 km)
- seats: 132->120
- cruise: 890->833 km/h

### Embraer_ERJ145

- range: 515->673 (≈2832->3702 km)

### FOKKER_F27

- range: 291->473 (≈1600->2602 km)
- seats: 50->52
- cruise: 470->460 km/h

### FOKKER_F28

- range: 364->303 (≈2002->1666 km)
- seats: 75->85
- cruise: 820->848 km/h

### Fokker_F100

- range: 570->576 (≈3135->3168 km)
- seats: 107->122
- cruise: 846->845 km/h

### Fokker_F70

- range: 615->620 (≈3382->3410 km)
- seats: 79->85
- cruise: 838->845 km/h

### GENERAL_ATOMICS_DO228

- range: 187->430 (≈1028->2365 km)
- cruise: 432->413 km/h

### HS_TRIDENT

- range: 701->791 (≈3856->4350 km)
- seats: 150->115
- cruise: 999->980 km/h

### ILYUSHIN_IL114

- range: 218->182 (≈1199->1001 km)
- cruise: 500->470 km/h

### ILYUSHIN_IL18

- seats: 110->100

### ILYUSHIN_IL96

- range: 2000->1818 (≈11000->9999 km)
- seats: 280->262
- cruise: 926->870 km/h

### IRKUT_MC21

- seats: 180->163
- cruise: 902->870 km/h

### Ilyushin_62

- range: 1800->1818 (≈9900->9999 km)
- seats: 168->186
- cruise: 822->900 km/h

### Ilyushin_76

- range: 1200->909 (≈6600->5000 km)
- seats: 0->225
- cruise: 798->852 km/h

### LET_L410

- range: 251->273 (≈1380->1502 km)

### LOCKHEED_L1011

- range: 1799->1800 (≈9894->9900 km)
- cruise: 983->972 km/h

### LOCKHEED_L188

- range: 727->811 (≈3998->4460 km)
- seats: 100->98
- cruise: 515->600 km/h

### Lockheed_L049_Constellation

- range: 1330->1169 (≈7315->6430 km)

### McDonnell_Douglas_MD11

- range: 2280->2265 (≈12540->12458 km)
- cruise: 943->886 km/h

### McDonnell_Douglas_MD11F

- range: 1315->1190 (≈7232->6545 km)
- cruise: 943->886 km/h

### McDonnell_Douglas_MD81

- range: 525->527 (≈2888->2898 km)
- cruise: 814->840 km/h

### McDonnell_Douglas_MD82

- range: 685->691 (≈3768->3800 km)
- cruise: 814->811 km/h

### McDonnell_Douglas_MD83

- range: 835->843 (≈4592->4636 km)
- cruise: 841->811 km/h

### McDonnell_Douglas_MD87

- range: 790->982 (≈4345->5401 km)
- cruise: 814->811 km/h

### McDonnell_Douglas_MD88

- range: 685->843 (≈3768->4636 km)
- cruise: 814->811 km/h

### McDonnell_Douglas_MD90

- range: 930->689 (≈5115->3790 km)
- seats: 155->158
- cruise: 841->812 km/h

### PILATUS_PC12

- range: 544->621 (≈2992->3416 km)

### PILATUS_PC24

- seats: 12->10
- cruise: 787->810 km/h

### PZL_AN28

- range: 264->248 (≈1452->1364 km)
- seats: 19->15

### RAYTHEON_BEECH1900D

- range: 327->419 (≈1798->2304 km)

### SUD_CARAVELLE_III

- range: 655->455 (≈3602->2502 km)
- cruise: 805->845 km/h

### SUKHOI_SSJ100

- cruise: 886->870 km/h

### TUPOLEV_TU204

- cruise: 934->850 km/h

### TUPOLEV_TU214

- range: 1309->789 (≈7200->4340 km)
- cruise: 934->850 km/h

### Tupolev_Tu134

- range: 340->545 (≈1870->2998 km)
- seats: 80->84
- cruise: 902->850 km/h

### Tupolev_Tu154B

- range: 785->960 (≈4318->5280 km)
- cruise: 951->850 km/h

### Tupolev_Tu154M

- range: 785->1200 (≈4318->6600 km)
- cruise: 951->850 km/h

### VICKERS_VC10

- range: 1800->1711 (≈9900->9410 km)
- seats: 145->151
- cruise: 822->890 km/h

### VICKERS_VISCOUNT

- range: 504->404 (≈2772->2222 km)
- seats: 60->75
- cruise: 525->566 km/h

### YAKOVLEV_YAK40

- range: 455->327 (≈2502->1798 km)
- cruise: 500->550 km/h

### YAKOVLEV_YAK42

- range: 527->741 (≈2898->4076 km)
- seats: 120->96
