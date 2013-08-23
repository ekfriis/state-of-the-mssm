# Atlas H+->tau search
#
# https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/HIGG-2012-09/
#
# From mH vs tanBeta exclusion (Fig 8)
#
#

upper_bound_mh_v_tanbeta = [
    (89.73892423637687, 18.69109947643979),
    (100.04636912168667, 16.387434554973822),
    (110.1275444321837, 13.350785340314134),
    (119.87562510271641, 11.465968586387437),
    (129.8567252834973, 12.722513089005234),
    (139.84457539971356, 16.387434554973822),
    (150.07366233888197, 26.12565445026178),
    (160.2267391355387, 48.743455497382215),
]

lower_bound_mh_v_tanbeta = [
    (89.9194116404104, 3.0890052356020954),
    (99.898750968469, 3.7172774869109935),
    (110.10377292043293, 4.86910994764398),
    (120.08369919939896, 5.706806282722502),
    (129.9471157232409, 4.973821989528774),
    (139.9214659685864, 3.821989528795796),
    (149.8943488366633, 2.1465968586387243),
    (152.02087197426806, 0.8900523560209503),
]


# converting to MA - only need to run this once to get the results.
#from convert_mass import convert_mass_tb
#import pprint

#limit = []
#for mhp, tanb in upper_bound_mh_v_tanbeta:
    #ma0 = convert_mass_tb(mhp, tanb)
    #limit.append((ma0, tanb))
#pprint.pprint(limit)
#lower_limit = []
#for mhp, tanb in lower_bound_mh_v_tanbeta:
    #ma0 = convert_mass_tb(mhp, tanb)
    #lower_limit.append((ma0, tanb))
#pprint.pprint(lower_limit)


limit = [(39.87732209, 18.69109947643979),
         (59.55167744, 16.387434554973822),
         (75.26753805, 13.350785340314134),
         (88.92295432, 11.465968586387437),
         (101.97987725, 12.722513089005234),
         (114.42740709, 16.387434554973822),
         (126.72501869, 26.12565445026178),
         (138.59918552, 48.743455497382215)]

lower_limit = [(40.28184443, 3.0890052356020954),
               (59.3033455, 3.7172774869109935),
               (75.23275327, 4.86910994764398),
               (89.20325724, 5.706806282722502),
               (102.09495234, 4.973821989528774),
               (114.52136475, 3.821989528795796),
               (126.51261675, 2.1465968586387243),
               (129.02508229, 0.8900523560209503)]