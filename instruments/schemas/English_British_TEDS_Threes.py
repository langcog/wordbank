from django.db import models
from instruments.base import BaseTable


class English_British_TEDS_Threes(BaseTable):
    item_1_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_1 = models.CharField(max_length=7, choices=item_1_choices, null=True)
    item_2_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_2 = models.CharField(max_length=7, choices=item_2_choices, null=True)
    item_3_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_3 = models.CharField(max_length=7, choices=item_3_choices, null=True)
    item_4_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_4 = models.CharField(max_length=7, choices=item_4_choices, null=True)
    item_5_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_5 = models.CharField(max_length=7, choices=item_5_choices, null=True)
    item_6_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_6 = models.CharField(max_length=7, choices=item_6_choices, null=True)
    item_7_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_7 = models.CharField(max_length=7, choices=item_7_choices, null=True)
    item_8_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_8 = models.CharField(max_length=7, choices=item_8_choices, null=True)
    item_9_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_9 = models.CharField(max_length=7, choices=item_9_choices, null=True)
    item_10_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_10 = models.CharField(max_length=7, choices=item_10_choices, null=True)
    item_11_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_11 = models.CharField(max_length=7, choices=item_11_choices, null=True)
    item_12_choices = [('simple', 'simple'), ('complex', 'complex')]
    item_12 = models.CharField(max_length=7, choices=item_12_choices, null=True)
    item_13_choices = [('produces', 'produces')]
    item_13 = models.CharField(max_length=8, choices=item_13_choices, null=True)
    item_14_choices = [('produces', 'produces')]
    item_14 = models.CharField(max_length=8, choices=item_14_choices, null=True)
    item_15_choices = [('produces', 'produces')]
    item_15 = models.CharField(max_length=8, choices=item_15_choices, null=True)
    item_16_choices = [('produces', 'produces')]
    item_16 = models.CharField(max_length=8, choices=item_16_choices, null=True)
    item_17_choices = [('produces', 'produces')]
    item_17 = models.CharField(max_length=8, choices=item_17_choices, null=True)
    item_18_choices = [('produces', 'produces')]
    item_18 = models.CharField(max_length=8, choices=item_18_choices, null=True)
    item_19_choices = [('produces', 'produces')]
    item_19 = models.CharField(max_length=8, choices=item_19_choices, null=True)
    item_20_choices = [('produces', 'produces')]
    item_20 = models.CharField(max_length=8, choices=item_20_choices, null=True)
    item_21_choices = [('produces', 'produces')]
    item_21 = models.CharField(max_length=8, choices=item_21_choices, null=True)
    item_22_choices = [('produces', 'produces')]
    item_22 = models.CharField(max_length=8, choices=item_22_choices, null=True)
    item_23_choices = [('produces', 'produces')]
    item_23 = models.CharField(max_length=8, choices=item_23_choices, null=True)
    item_24_choices = [('produces', 'produces')]
    item_24 = models.CharField(max_length=8, choices=item_24_choices, null=True)
    item_25_choices = [('produces', 'produces')]
    item_25 = models.CharField(max_length=8, choices=item_25_choices, null=True)
    item_26_choices = [('produces', 'produces')]
    item_26 = models.CharField(max_length=8, choices=item_26_choices, null=True)
    item_27_choices = [('produces', 'produces')]
    item_27 = models.CharField(max_length=8, choices=item_27_choices, null=True)
    item_28_choices = [('produces', 'produces')]
    item_28 = models.CharField(max_length=8, choices=item_28_choices, null=True)
    item_29_choices = [('produces', 'produces')]
    item_29 = models.CharField(max_length=8, choices=item_29_choices, null=True)
    item_30_choices = [('produces', 'produces')]
    item_30 = models.CharField(max_length=8, choices=item_30_choices, null=True)
    item_31_choices = [('produces', 'produces')]
    item_31 = models.CharField(max_length=8, choices=item_31_choices, null=True)
    item_32_choices = [('produces', 'produces')]
    item_32 = models.CharField(max_length=8, choices=item_32_choices, null=True)
    item_33_choices = [('produces', 'produces')]
    item_33 = models.CharField(max_length=8, choices=item_33_choices, null=True)
    item_34_choices = [('produces', 'produces')]
    item_34 = models.CharField(max_length=8, choices=item_34_choices, null=True)
    item_35_choices = [('produces', 'produces')]
    item_35 = models.CharField(max_length=8, choices=item_35_choices, null=True)
    item_36_choices = [('produces', 'produces')]
    item_36 = models.CharField(max_length=8, choices=item_36_choices, null=True)
    item_37_choices = [('produces', 'produces')]
    item_37 = models.CharField(max_length=8, choices=item_37_choices, null=True)
    item_38_choices = [('produces', 'produces')]
    item_38 = models.CharField(max_length=8, choices=item_38_choices, null=True)
    item_39_choices = [('produces', 'produces')]
    item_39 = models.CharField(max_length=8, choices=item_39_choices, null=True)
    item_40_choices = [('produces', 'produces')]
    item_40 = models.CharField(max_length=8, choices=item_40_choices, null=True)
    item_41_choices = [('produces', 'produces')]
    item_41 = models.CharField(max_length=8, choices=item_41_choices, null=True)
    item_42_choices = [('produces', 'produces')]
    item_42 = models.CharField(max_length=8, choices=item_42_choices, null=True)
    item_43_choices = [('produces', 'produces')]
    item_43 = models.CharField(max_length=8, choices=item_43_choices, null=True)
    item_44_choices = [('produces', 'produces')]
    item_44 = models.CharField(max_length=8, choices=item_44_choices, null=True)
    item_45_choices = [('produces', 'produces')]
    item_45 = models.CharField(max_length=8, choices=item_45_choices, null=True)
    item_46_choices = [('produces', 'produces')]
    item_46 = models.CharField(max_length=8, choices=item_46_choices, null=True)
    item_47_choices = [('produces', 'produces')]
    item_47 = models.CharField(max_length=8, choices=item_47_choices, null=True)
    item_48_choices = [('produces', 'produces')]
    item_48 = models.CharField(max_length=8, choices=item_48_choices, null=True)
    item_49_choices = [('produces', 'produces')]
    item_49 = models.CharField(max_length=8, choices=item_49_choices, null=True)
    item_50_choices = [('produces', 'produces')]
    item_50 = models.CharField(max_length=8, choices=item_50_choices, null=True)
    item_51_choices = [('produces', 'produces')]
    item_51 = models.CharField(max_length=8, choices=item_51_choices, null=True)
    item_52_choices = [('produces', 'produces')]
    item_52 = models.CharField(max_length=8, choices=item_52_choices, null=True)
    item_53_choices = [('produces', 'produces')]
    item_53 = models.CharField(max_length=8, choices=item_53_choices, null=True)
    item_54_choices = [('produces', 'produces')]
    item_54 = models.CharField(max_length=8, choices=item_54_choices, null=True)
    item_55_choices = [('produces', 'produces')]
    item_55 = models.CharField(max_length=8, choices=item_55_choices, null=True)
    item_56_choices = [('produces', 'produces')]
    item_56 = models.CharField(max_length=8, choices=item_56_choices, null=True)
    item_57_choices = [('produces', 'produces')]
    item_57 = models.CharField(max_length=8, choices=item_57_choices, null=True)
    item_58_choices = [('produces', 'produces')]
    item_58 = models.CharField(max_length=8, choices=item_58_choices, null=True)
    item_59_choices = [('produces', 'produces')]
    item_59 = models.CharField(max_length=8, choices=item_59_choices, null=True)
    item_60_choices = [('produces', 'produces')]
    item_60 = models.CharField(max_length=8, choices=item_60_choices, null=True)
    item_61_choices = [('produces', 'produces')]
    item_61 = models.CharField(max_length=8, choices=item_61_choices, null=True)
    item_62_choices = [('produces', 'produces')]
    item_62 = models.CharField(max_length=8, choices=item_62_choices, null=True)
    item_63_choices = [('produces', 'produces')]
    item_63 = models.CharField(max_length=8, choices=item_63_choices, null=True)
    item_64_choices = [('produces', 'produces')]
    item_64 = models.CharField(max_length=8, choices=item_64_choices, null=True)
    item_65_choices = [('produces', 'produces')]
    item_65 = models.CharField(max_length=8, choices=item_65_choices, null=True)
    item_66_choices = [('produces', 'produces')]
    item_66 = models.CharField(max_length=8, choices=item_66_choices, null=True)
    item_67_choices = [('produces', 'produces')]
    item_67 = models.CharField(max_length=8, choices=item_67_choices, null=True)
    item_68_choices = [('produces', 'produces')]
    item_68 = models.CharField(max_length=8, choices=item_68_choices, null=True)
    item_69_choices = [('produces', 'produces')]
    item_69 = models.CharField(max_length=8, choices=item_69_choices, null=True)
    item_70_choices = [('produces', 'produces')]
    item_70 = models.CharField(max_length=8, choices=item_70_choices, null=True)
    item_71_choices = [('produces', 'produces')]
    item_71 = models.CharField(max_length=8, choices=item_71_choices, null=True)
    item_72_choices = [('produces', 'produces')]
    item_72 = models.CharField(max_length=8, choices=item_72_choices, null=True)
    item_73_choices = [('produces', 'produces')]
    item_73 = models.CharField(max_length=8, choices=item_73_choices, null=True)
    item_74_choices = [('produces', 'produces')]
    item_74 = models.CharField(max_length=8, choices=item_74_choices, null=True)
    item_75_choices = [('produces', 'produces')]
    item_75 = models.CharField(max_length=8, choices=item_75_choices, null=True)
    item_76_choices = [('produces', 'produces')]
    item_76 = models.CharField(max_length=8, choices=item_76_choices, null=True)
    item_77_choices = [('produces', 'produces')]
    item_77 = models.CharField(max_length=8, choices=item_77_choices, null=True)
    item_78_choices = [('produces', 'produces')]
    item_78 = models.CharField(max_length=8, choices=item_78_choices, null=True)
    item_79_choices = [('produces', 'produces')]
    item_79 = models.CharField(max_length=8, choices=item_79_choices, null=True)
    item_80_choices = [('produces', 'produces')]
    item_80 = models.CharField(max_length=8, choices=item_80_choices, null=True)
    item_81_choices = [('produces', 'produces')]
    item_81 = models.CharField(max_length=8, choices=item_81_choices, null=True)
    item_82_choices = [('produces', 'produces')]
    item_82 = models.CharField(max_length=8, choices=item_82_choices, null=True)
    item_83_choices = [('produces', 'produces')]
    item_83 = models.CharField(max_length=8, choices=item_83_choices, null=True)
    item_84_choices = [('produces', 'produces')]
    item_84 = models.CharField(max_length=8, choices=item_84_choices, null=True)
    item_85_choices = [('produces', 'produces')]
    item_85 = models.CharField(max_length=8, choices=item_85_choices, null=True)
    item_86_choices = [('produces', 'produces')]
    item_86 = models.CharField(max_length=8, choices=item_86_choices, null=True)
    item_87_choices = [('produces', 'produces')]
    item_87 = models.CharField(max_length=8, choices=item_87_choices, null=True)
    item_88_choices = [('produces', 'produces')]
    item_88 = models.CharField(max_length=8, choices=item_88_choices, null=True)
    item_89_choices = [('produces', 'produces')]
    item_89 = models.CharField(max_length=8, choices=item_89_choices, null=True)
    item_90_choices = [('produces', 'produces')]
    item_90 = models.CharField(max_length=8, choices=item_90_choices, null=True)
    item_91_choices = [('produces', 'produces')]
    item_91 = models.CharField(max_length=8, choices=item_91_choices, null=True)
    item_92_choices = [('produces', 'produces')]
    item_92 = models.CharField(max_length=8, choices=item_92_choices, null=True)
    item_93_choices = [('produces', 'produces')]
    item_93 = models.CharField(max_length=8, choices=item_93_choices, null=True)
    item_94_choices = [('produces', 'produces')]
    item_94 = models.CharField(max_length=8, choices=item_94_choices, null=True)
    item_95_choices = [('produces', 'produces')]
    item_95 = models.CharField(max_length=8, choices=item_95_choices, null=True)
    item_96_choices = [('produces', 'produces')]
    item_96 = models.CharField(max_length=8, choices=item_96_choices, null=True)
    item_97_choices = [('produces', 'produces')]
    item_97 = models.CharField(max_length=8, choices=item_97_choices, null=True)
    item_98_choices = [('produces', 'produces')]
    item_98 = models.CharField(max_length=8, choices=item_98_choices, null=True)
    item_99_choices = [('produces', 'produces')]
    item_99 = models.CharField(max_length=8, choices=item_99_choices, null=True)
    item_100_choices = [('produces', 'produces')]
    item_100 = models.CharField(max_length=8, choices=item_100_choices, null=True)
    item_101_choices = [('produces', 'produces')]
    item_101 = models.CharField(max_length=8, choices=item_101_choices, null=True)
    item_102_choices = [('produces', 'produces')]
    item_102 = models.CharField(max_length=8, choices=item_102_choices, null=True)
    item_103_choices = [('produces', 'produces')]
    item_103 = models.CharField(max_length=8, choices=item_103_choices, null=True)
    item_104_choices = [('produces', 'produces')]
    item_104 = models.CharField(max_length=8, choices=item_104_choices, null=True)
    item_105_choices = [('produces', 'produces')]
    item_105 = models.CharField(max_length=8, choices=item_105_choices, null=True)
    item_106_choices = [('produces', 'produces')]
    item_106 = models.CharField(max_length=8, choices=item_106_choices, null=True)
    item_107_choices = [('produces', 'produces')]
    item_107 = models.CharField(max_length=8, choices=item_107_choices, null=True)
    item_108_choices = [('produces', 'produces')]
    item_108 = models.CharField(max_length=8, choices=item_108_choices, null=True)
    item_109_choices = [('produces', 'produces')]
    item_109 = models.CharField(max_length=8, choices=item_109_choices, null=True)
    item_110_choices = [('produces', 'produces')]
    item_110 = models.CharField(max_length=8, choices=item_110_choices, null=True)
    item_111_choices = [('produces', 'produces')]
    item_111 = models.CharField(max_length=8, choices=item_111_choices, null=True)
    item_112_choices = [('produces', 'produces')]
    item_112 = models.CharField(max_length=8, choices=item_112_choices, null=True)
    item_113_choices = [('yes', 'yes'), ('no', 'no')]
    item_113 = models.CharField(max_length=3, choices=item_113_choices, null=True)
