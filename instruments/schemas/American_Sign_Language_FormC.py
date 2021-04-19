from django.db import models
from instruments.base import BaseTable


class American_Sign_Language_FormC(BaseTable):
    item_1_choices = [('yes', 'yes'), ('no', 'no')]
    item_1 = models.CharField(max_length=3, choices=item_1_choices, null=True)
    item_2_choices = [('yes', 'yes'), ('no', 'no')]
    item_2 = models.CharField(max_length=3, choices=item_2_choices, null=True)
    item_3_choices = [('yes', 'yes'), ('no', 'no')]
    item_3 = models.CharField(max_length=3, choices=item_3_choices, null=True)
    item_4_choices = [('understands', 'understands')]
    item_4 = models.CharField(max_length=11, choices=item_4_choices, null=True)
    item_5_choices = [('understands', 'understands')]
    item_5 = models.CharField(max_length=11, choices=item_5_choices, null=True)
    item_6_choices = [('understands', 'understands')]
    item_6 = models.CharField(max_length=11, choices=item_6_choices, null=True)
    item_7_choices = [('understands', 'understands')]
    item_7 = models.CharField(max_length=11, choices=item_7_choices, null=True)
    item_8_choices = [('understands', 'understands')]
    item_8 = models.CharField(max_length=11, choices=item_8_choices, null=True)
    item_9_choices = [('understands', 'understands')]
    item_9 = models.CharField(max_length=11, choices=item_9_choices, null=True)
    item_10_choices = [('understands', 'understands')]
    item_10 = models.CharField(max_length=11, choices=item_10_choices, null=True)
    item_11_choices = [('understands', 'understands')]
    item_11 = models.CharField(max_length=11, choices=item_11_choices, null=True)
    item_12_choices = [('understands', 'understands')]
    item_12 = models.CharField(max_length=11, choices=item_12_choices, null=True)
    item_13_choices = [('understands', 'understands')]
    item_13 = models.CharField(max_length=11, choices=item_13_choices, null=True)
    item_14_choices = [('understands', 'understands')]
    item_14 = models.CharField(max_length=11, choices=item_14_choices, null=True)
    item_15_choices = [('understands', 'understands')]
    item_15 = models.CharField(max_length=11, choices=item_15_choices, null=True)
    item_16_choices = [('understands', 'understands')]
    item_16 = models.CharField(max_length=11, choices=item_16_choices, null=True)
    item_17_choices = [('understands', 'understands')]
    item_17 = models.CharField(max_length=11, choices=item_17_choices, null=True)
    item_18_choices = [('understands', 'understands')]
    item_18 = models.CharField(max_length=11, choices=item_18_choices, null=True)
    item_19_choices = [('understands', 'understands')]
    item_19 = models.CharField(max_length=11, choices=item_19_choices, null=True)
    item_20_choices = [('understands', 'understands')]
    item_20 = models.CharField(max_length=11, choices=item_20_choices, null=True)
    item_21_choices = [('understands', 'understands')]
    item_21 = models.CharField(max_length=11, choices=item_21_choices, null=True)
    item_22_choices = [('understands', 'understands')]
    item_22 = models.CharField(max_length=11, choices=item_22_choices, null=True)
    item_23_choices = [('understands', 'understands')]
    item_23 = models.CharField(max_length=11, choices=item_23_choices, null=True)
    item_24_choices = [('understands', 'understands')]
    item_24 = models.CharField(max_length=11, choices=item_24_choices, null=True)
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
    item_113_choices = [('produces', 'produces')]
    item_113 = models.CharField(max_length=8, choices=item_113_choices, null=True)
    item_114_choices = [('produces', 'produces')]
    item_114 = models.CharField(max_length=8, choices=item_114_choices, null=True)
    item_115_choices = [('produces', 'produces')]
    item_115 = models.CharField(max_length=8, choices=item_115_choices, null=True)
    item_116_choices = [('produces', 'produces')]
    item_116 = models.CharField(max_length=8, choices=item_116_choices, null=True)
    item_117_choices = [('produces', 'produces')]
    item_117 = models.CharField(max_length=8, choices=item_117_choices, null=True)
    item_118_choices = [('produces', 'produces')]
    item_118 = models.CharField(max_length=8, choices=item_118_choices, null=True)
    item_119_choices = [('produces', 'produces')]
    item_119 = models.CharField(max_length=8, choices=item_119_choices, null=True)
    item_120_choices = [('produces', 'produces')]
    item_120 = models.CharField(max_length=8, choices=item_120_choices, null=True)
    item_121_choices = [('produces', 'produces')]
    item_121 = models.CharField(max_length=8, choices=item_121_choices, null=True)
    item_122_choices = [('produces', 'produces')]
    item_122 = models.CharField(max_length=8, choices=item_122_choices, null=True)
    item_123_choices = [('produces', 'produces')]
    item_123 = models.CharField(max_length=8, choices=item_123_choices, null=True)
    item_124_choices = [('produces', 'produces')]
    item_124 = models.CharField(max_length=8, choices=item_124_choices, null=True)
    item_125_choices = [('produces', 'produces')]
    item_125 = models.CharField(max_length=8, choices=item_125_choices, null=True)
    item_126_choices = [('produces', 'produces')]
    item_126 = models.CharField(max_length=8, choices=item_126_choices, null=True)
    item_127_choices = [('produces', 'produces')]
    item_127 = models.CharField(max_length=8, choices=item_127_choices, null=True)
    item_128_choices = [('produces', 'produces')]
    item_128 = models.CharField(max_length=8, choices=item_128_choices, null=True)
    item_129_choices = [('produces', 'produces')]
    item_129 = models.CharField(max_length=8, choices=item_129_choices, null=True)
    item_130_choices = [('produces', 'produces')]
    item_130 = models.CharField(max_length=8, choices=item_130_choices, null=True)
    item_131_choices = [('produces', 'produces')]
    item_131 = models.CharField(max_length=8, choices=item_131_choices, null=True)
    item_132_choices = [('produces', 'produces')]
    item_132 = models.CharField(max_length=8, choices=item_132_choices, null=True)
    item_133_choices = [('produces', 'produces')]
    item_133 = models.CharField(max_length=8, choices=item_133_choices, null=True)
    item_134_choices = [('produces', 'produces')]
    item_134 = models.CharField(max_length=8, choices=item_134_choices, null=True)
    item_135_choices = [('produces', 'produces')]
    item_135 = models.CharField(max_length=8, choices=item_135_choices, null=True)
    item_136_choices = [('produces', 'produces')]
    item_136 = models.CharField(max_length=8, choices=item_136_choices, null=True)
    item_137_choices = [('produces', 'produces')]
    item_137 = models.CharField(max_length=8, choices=item_137_choices, null=True)
    item_138_choices = [('produces', 'produces')]
    item_138 = models.CharField(max_length=8, choices=item_138_choices, null=True)
    item_139_choices = [('produces', 'produces')]
    item_139 = models.CharField(max_length=8, choices=item_139_choices, null=True)
    item_140_choices = [('produces', 'produces')]
    item_140 = models.CharField(max_length=8, choices=item_140_choices, null=True)
    item_141_choices = [('produces', 'produces')]
    item_141 = models.CharField(max_length=8, choices=item_141_choices, null=True)
    item_142_choices = [('produces', 'produces')]
    item_142 = models.CharField(max_length=8, choices=item_142_choices, null=True)
    item_143_choices = [('produces', 'produces')]
    item_143 = models.CharField(max_length=8, choices=item_143_choices, null=True)
    item_144_choices = [('produces', 'produces')]
    item_144 = models.CharField(max_length=8, choices=item_144_choices, null=True)
    item_145_choices = [('produces', 'produces')]
    item_145 = models.CharField(max_length=8, choices=item_145_choices, null=True)
    item_146_choices = [('produces', 'produces')]
    item_146 = models.CharField(max_length=8, choices=item_146_choices, null=True)
    item_147_choices = [('produces', 'produces')]
    item_147 = models.CharField(max_length=8, choices=item_147_choices, null=True)
    item_148_choices = [('produces', 'produces')]
    item_148 = models.CharField(max_length=8, choices=item_148_choices, null=True)
    item_149_choices = [('produces', 'produces')]
    item_149 = models.CharField(max_length=8, choices=item_149_choices, null=True)
    item_150_choices = [('produces', 'produces')]
    item_150 = models.CharField(max_length=8, choices=item_150_choices, null=True)
    item_151_choices = [('produces', 'produces')]
    item_151 = models.CharField(max_length=8, choices=item_151_choices, null=True)
    item_152_choices = [('produces', 'produces')]
    item_152 = models.CharField(max_length=8, choices=item_152_choices, null=True)
    item_153_choices = [('produces', 'produces')]
    item_153 = models.CharField(max_length=8, choices=item_153_choices, null=True)
    item_154_choices = [('produces', 'produces')]
    item_154 = models.CharField(max_length=8, choices=item_154_choices, null=True)
    item_155_choices = [('produces', 'produces')]
    item_155 = models.CharField(max_length=8, choices=item_155_choices, null=True)
    item_156_choices = [('produces', 'produces')]
    item_156 = models.CharField(max_length=8, choices=item_156_choices, null=True)
    item_157_choices = [('produces', 'produces')]
    item_157 = models.CharField(max_length=8, choices=item_157_choices, null=True)
    item_158_choices = [('produces', 'produces')]
    item_158 = models.CharField(max_length=8, choices=item_158_choices, null=True)
    item_159_choices = [('produces', 'produces')]
    item_159 = models.CharField(max_length=8, choices=item_159_choices, null=True)
    item_160_choices = [('produces', 'produces')]
    item_160 = models.CharField(max_length=8, choices=item_160_choices, null=True)
    item_161_choices = [('produces', 'produces')]
    item_161 = models.CharField(max_length=8, choices=item_161_choices, null=True)
    item_162_choices = [('produces', 'produces')]
    item_162 = models.CharField(max_length=8, choices=item_162_choices, null=True)
    item_163_choices = [('produces', 'produces')]
    item_163 = models.CharField(max_length=8, choices=item_163_choices, null=True)
    item_164_choices = [('produces', 'produces')]
    item_164 = models.CharField(max_length=8, choices=item_164_choices, null=True)
    item_165_choices = [('produces', 'produces')]
    item_165 = models.CharField(max_length=8, choices=item_165_choices, null=True)
    item_166_choices = [('produces', 'produces')]
    item_166 = models.CharField(max_length=8, choices=item_166_choices, null=True)
    item_167_choices = [('produces', 'produces')]
    item_167 = models.CharField(max_length=8, choices=item_167_choices, null=True)
    item_168_choices = [('produces', 'produces')]
    item_168 = models.CharField(max_length=8, choices=item_168_choices, null=True)
    item_169_choices = [('produces', 'produces')]
    item_169 = models.CharField(max_length=8, choices=item_169_choices, null=True)
    item_170_choices = [('produces', 'produces')]
    item_170 = models.CharField(max_length=8, choices=item_170_choices, null=True)
    item_171_choices = [('produces', 'produces')]
    item_171 = models.CharField(max_length=8, choices=item_171_choices, null=True)
    item_172_choices = [('produces', 'produces')]
    item_172 = models.CharField(max_length=8, choices=item_172_choices, null=True)
    item_173_choices = [('produces', 'produces')]
    item_173 = models.CharField(max_length=8, choices=item_173_choices, null=True)
    item_174_choices = [('produces', 'produces')]
    item_174 = models.CharField(max_length=8, choices=item_174_choices, null=True)
    item_175_choices = [('produces', 'produces')]
    item_175 = models.CharField(max_length=8, choices=item_175_choices, null=True)
    item_176_choices = [('produces', 'produces')]
    item_176 = models.CharField(max_length=8, choices=item_176_choices, null=True)
    item_177_choices = [('produces', 'produces')]
    item_177 = models.CharField(max_length=8, choices=item_177_choices, null=True)
    item_178_choices = [('produces', 'produces')]
    item_178 = models.CharField(max_length=8, choices=item_178_choices, null=True)
    item_179_choices = [('produces', 'produces')]
    item_179 = models.CharField(max_length=8, choices=item_179_choices, null=True)
    item_180_choices = [('produces', 'produces')]
    item_180 = models.CharField(max_length=8, choices=item_180_choices, null=True)
    item_181_choices = [('produces', 'produces')]
    item_181 = models.CharField(max_length=8, choices=item_181_choices, null=True)
    item_182_choices = [('produces', 'produces')]
    item_182 = models.CharField(max_length=8, choices=item_182_choices, null=True)
    item_183_choices = [('produces', 'produces')]
    item_183 = models.CharField(max_length=8, choices=item_183_choices, null=True)
    item_184_choices = [('produces', 'produces')]
    item_184 = models.CharField(max_length=8, choices=item_184_choices, null=True)
    item_185_choices = [('produces', 'produces')]
    item_185 = models.CharField(max_length=8, choices=item_185_choices, null=True)
    item_186_choices = [('produces', 'produces')]
    item_186 = models.CharField(max_length=8, choices=item_186_choices, null=True)
    item_187_choices = [('produces', 'produces')]
    item_187 = models.CharField(max_length=8, choices=item_187_choices, null=True)
    item_188_choices = [('produces', 'produces')]
    item_188 = models.CharField(max_length=8, choices=item_188_choices, null=True)
    item_189_choices = [('produces', 'produces')]
    item_189 = models.CharField(max_length=8, choices=item_189_choices, null=True)
    item_190_choices = [('produces', 'produces')]
    item_190 = models.CharField(max_length=8, choices=item_190_choices, null=True)
    item_191_choices = [('produces', 'produces')]
    item_191 = models.CharField(max_length=8, choices=item_191_choices, null=True)
    item_192_choices = [('produces', 'produces')]
    item_192 = models.CharField(max_length=8, choices=item_192_choices, null=True)
    item_193_choices = [('produces', 'produces')]
    item_193 = models.CharField(max_length=8, choices=item_193_choices, null=True)
    item_194_choices = [('produces', 'produces')]
    item_194 = models.CharField(max_length=8, choices=item_194_choices, null=True)
    item_195_choices = [('produces', 'produces')]
    item_195 = models.CharField(max_length=8, choices=item_195_choices, null=True)
    item_196_choices = [('produces', 'produces')]
    item_196 = models.CharField(max_length=8, choices=item_196_choices, null=True)
    item_197_choices = [('produces', 'produces')]
    item_197 = models.CharField(max_length=8, choices=item_197_choices, null=True)
    item_198_choices = [('produces', 'produces')]
    item_198 = models.CharField(max_length=8, choices=item_198_choices, null=True)
    item_199_choices = [('produces', 'produces')]
    item_199 = models.CharField(max_length=8, choices=item_199_choices, null=True)
    item_200_choices = [('produces', 'produces')]
    item_200 = models.CharField(max_length=8, choices=item_200_choices, null=True)
    item_201_choices = [('produces', 'produces')]
    item_201 = models.CharField(max_length=8, choices=item_201_choices, null=True)
    item_202_choices = [('produces', 'produces')]
    item_202 = models.CharField(max_length=8, choices=item_202_choices, null=True)
    item_203_choices = [('produces', 'produces')]
    item_203 = models.CharField(max_length=8, choices=item_203_choices, null=True)
    item_204_choices = [('produces', 'produces')]
    item_204 = models.CharField(max_length=8, choices=item_204_choices, null=True)
    item_205_choices = [('produces', 'produces')]
    item_205 = models.CharField(max_length=8, choices=item_205_choices, null=True)
    item_206_choices = [('produces', 'produces')]
    item_206 = models.CharField(max_length=8, choices=item_206_choices, null=True)
    item_207_choices = [('produces', 'produces')]
    item_207 = models.CharField(max_length=8, choices=item_207_choices, null=True)
    item_208_choices = [('produces', 'produces')]
    item_208 = models.CharField(max_length=8, choices=item_208_choices, null=True)
    item_209_choices = [('produces', 'produces')]
    item_209 = models.CharField(max_length=8, choices=item_209_choices, null=True)
    item_210_choices = [('produces', 'produces')]
    item_210 = models.CharField(max_length=8, choices=item_210_choices, null=True)
    item_211_choices = [('produces', 'produces')]
    item_211 = models.CharField(max_length=8, choices=item_211_choices, null=True)
    item_212_choices = [('produces', 'produces')]
    item_212 = models.CharField(max_length=8, choices=item_212_choices, null=True)
    item_213_choices = [('produces', 'produces')]
    item_213 = models.CharField(max_length=8, choices=item_213_choices, null=True)
    item_214_choices = [('produces', 'produces')]
    item_214 = models.CharField(max_length=8, choices=item_214_choices, null=True)
    item_215_choices = [('produces', 'produces')]
    item_215 = models.CharField(max_length=8, choices=item_215_choices, null=True)
    item_216_choices = [('produces', 'produces')]
    item_216 = models.CharField(max_length=8, choices=item_216_choices, null=True)
    item_217_choices = [('produces', 'produces')]
    item_217 = models.CharField(max_length=8, choices=item_217_choices, null=True)
    item_218_choices = [('produces', 'produces')]
    item_218 = models.CharField(max_length=8, choices=item_218_choices, null=True)
    item_219_choices = [('produces', 'produces')]
    item_219 = models.CharField(max_length=8, choices=item_219_choices, null=True)
    item_220_choices = [('produces', 'produces')]
    item_220 = models.CharField(max_length=8, choices=item_220_choices, null=True)
    item_221_choices = [('produces', 'produces')]
    item_221 = models.CharField(max_length=8, choices=item_221_choices, null=True)
    item_222_choices = [('produces', 'produces')]
    item_222 = models.CharField(max_length=8, choices=item_222_choices, null=True)
    item_223_choices = [('produces', 'produces')]
    item_223 = models.CharField(max_length=8, choices=item_223_choices, null=True)
    item_224_choices = [('produces', 'produces')]
    item_224 = models.CharField(max_length=8, choices=item_224_choices, null=True)
    item_225_choices = [('produces', 'produces')]
    item_225 = models.CharField(max_length=8, choices=item_225_choices, null=True)
    item_226_choices = [('produces', 'produces')]
    item_226 = models.CharField(max_length=8, choices=item_226_choices, null=True)
    item_227_choices = [('produces', 'produces')]
    item_227 = models.CharField(max_length=8, choices=item_227_choices, null=True)
    item_228_choices = [('produces', 'produces')]
    item_228 = models.CharField(max_length=8, choices=item_228_choices, null=True)
    item_229_choices = [('produces', 'produces')]
    item_229 = models.CharField(max_length=8, choices=item_229_choices, null=True)
    item_230_choices = [('produces', 'produces')]
    item_230 = models.CharField(max_length=8, choices=item_230_choices, null=True)
    item_231_choices = [('produces', 'produces')]
    item_231 = models.CharField(max_length=8, choices=item_231_choices, null=True)
    item_232_choices = [('produces', 'produces')]
    item_232 = models.CharField(max_length=8, choices=item_232_choices, null=True)
    item_233_choices = [('produces', 'produces')]
    item_233 = models.CharField(max_length=8, choices=item_233_choices, null=True)
    item_234_choices = [('produces', 'produces')]
    item_234 = models.CharField(max_length=8, choices=item_234_choices, null=True)
    item_235_choices = [('produces', 'produces')]
    item_235 = models.CharField(max_length=8, choices=item_235_choices, null=True)
    item_236_choices = [('produces', 'produces')]
    item_236 = models.CharField(max_length=8, choices=item_236_choices, null=True)
    item_237_choices = [('produces', 'produces')]
    item_237 = models.CharField(max_length=8, choices=item_237_choices, null=True)
    item_238_choices = [('produces', 'produces')]
    item_238 = models.CharField(max_length=8, choices=item_238_choices, null=True)
    item_239_choices = [('produces', 'produces')]
    item_239 = models.CharField(max_length=8, choices=item_239_choices, null=True)
    item_240_choices = [('produces', 'produces')]
    item_240 = models.CharField(max_length=8, choices=item_240_choices, null=True)
    item_241_choices = [('produces', 'produces')]
    item_241 = models.CharField(max_length=8, choices=item_241_choices, null=True)
    item_242_choices = [('produces', 'produces')]
    item_242 = models.CharField(max_length=8, choices=item_242_choices, null=True)
    item_243_choices = [('produces', 'produces')]
    item_243 = models.CharField(max_length=8, choices=item_243_choices, null=True)
    item_244_choices = [('produces', 'produces')]
    item_244 = models.CharField(max_length=8, choices=item_244_choices, null=True)
    item_245_choices = [('produces', 'produces')]
    item_245 = models.CharField(max_length=8, choices=item_245_choices, null=True)
    item_246_choices = [('produces', 'produces')]
    item_246 = models.CharField(max_length=8, choices=item_246_choices, null=True)
    item_247_choices = [('produces', 'produces')]
    item_247 = models.CharField(max_length=8, choices=item_247_choices, null=True)
    item_248_choices = [('produces', 'produces')]
    item_248 = models.CharField(max_length=8, choices=item_248_choices, null=True)
    item_249_choices = [('produces', 'produces')]
    item_249 = models.CharField(max_length=8, choices=item_249_choices, null=True)
    item_250_choices = [('produces', 'produces')]
    item_250 = models.CharField(max_length=8, choices=item_250_choices, null=True)
    item_251_choices = [('produces', 'produces')]
    item_251 = models.CharField(max_length=8, choices=item_251_choices, null=True)
    item_252_choices = [('produces', 'produces')]
    item_252 = models.CharField(max_length=8, choices=item_252_choices, null=True)
    item_253_choices = [('produces', 'produces')]
    item_253 = models.CharField(max_length=8, choices=item_253_choices, null=True)
    item_254_choices = [('produces', 'produces')]
    item_254 = models.CharField(max_length=8, choices=item_254_choices, null=True)
    item_255_choices = [('produces', 'produces')]
    item_255 = models.CharField(max_length=8, choices=item_255_choices, null=True)
    item_256_choices = [('produces', 'produces')]
    item_256 = models.CharField(max_length=8, choices=item_256_choices, null=True)
    item_257_choices = [('produces', 'produces')]
    item_257 = models.CharField(max_length=8, choices=item_257_choices, null=True)
    item_258_choices = [('produces', 'produces')]
    item_258 = models.CharField(max_length=8, choices=item_258_choices, null=True)
    item_259_choices = [('produces', 'produces')]
    item_259 = models.CharField(max_length=8, choices=item_259_choices, null=True)
    item_260_choices = [('produces', 'produces')]
    item_260 = models.CharField(max_length=8, choices=item_260_choices, null=True)
    item_261_choices = [('produces', 'produces')]
    item_261 = models.CharField(max_length=8, choices=item_261_choices, null=True)
    item_262_choices = [('produces', 'produces')]
    item_262 = models.CharField(max_length=8, choices=item_262_choices, null=True)
    item_263_choices = [('produces', 'produces')]
    item_263 = models.CharField(max_length=8, choices=item_263_choices, null=True)
    item_264_choices = [('produces', 'produces')]
    item_264 = models.CharField(max_length=8, choices=item_264_choices, null=True)
    item_265_choices = [('produces', 'produces')]
    item_265 = models.CharField(max_length=8, choices=item_265_choices, null=True)
    item_266_choices = [('produces', 'produces')]
    item_266 = models.CharField(max_length=8, choices=item_266_choices, null=True)
    item_267_choices = [('produces', 'produces')]
    item_267 = models.CharField(max_length=8, choices=item_267_choices, null=True)
    item_268_choices = [('produces', 'produces')]
    item_268 = models.CharField(max_length=8, choices=item_268_choices, null=True)
    item_269_choices = [('produces', 'produces')]
    item_269 = models.CharField(max_length=8, choices=item_269_choices, null=True)
    item_270_choices = [('produces', 'produces')]
    item_270 = models.CharField(max_length=8, choices=item_270_choices, null=True)
    item_271_choices = [('produces', 'produces')]
    item_271 = models.CharField(max_length=8, choices=item_271_choices, null=True)
    item_272_choices = [('produces', 'produces')]
    item_272 = models.CharField(max_length=8, choices=item_272_choices, null=True)
    item_273_choices = [('produces', 'produces')]
    item_273 = models.CharField(max_length=8, choices=item_273_choices, null=True)
    item_274_choices = [('produces', 'produces')]
    item_274 = models.CharField(max_length=8, choices=item_274_choices, null=True)
    item_275_choices = [('produces', 'produces')]
    item_275 = models.CharField(max_length=8, choices=item_275_choices, null=True)
    item_276_choices = [('produces', 'produces')]
    item_276 = models.CharField(max_length=8, choices=item_276_choices, null=True)
    item_277_choices = [('produces', 'produces')]
    item_277 = models.CharField(max_length=8, choices=item_277_choices, null=True)
    item_278_choices = [('produces', 'produces')]
    item_278 = models.CharField(max_length=8, choices=item_278_choices, null=True)
    item_279_choices = [('produces', 'produces')]
    item_279 = models.CharField(max_length=8, choices=item_279_choices, null=True)
    item_280_choices = [('produces', 'produces')]
    item_280 = models.CharField(max_length=8, choices=item_280_choices, null=True)
    item_281_choices = [('produces', 'produces')]
    item_281 = models.CharField(max_length=8, choices=item_281_choices, null=True)
    item_282_choices = [('produces', 'produces')]
    item_282 = models.CharField(max_length=8, choices=item_282_choices, null=True)
    item_283_choices = [('produces', 'produces')]
    item_283 = models.CharField(max_length=8, choices=item_283_choices, null=True)
    item_284_choices = [('produces', 'produces')]
    item_284 = models.CharField(max_length=8, choices=item_284_choices, null=True)
    item_285_choices = [('produces', 'produces')]
    item_285 = models.CharField(max_length=8, choices=item_285_choices, null=True)
    item_286_choices = [('produces', 'produces')]
    item_286 = models.CharField(max_length=8, choices=item_286_choices, null=True)
    item_287_choices = [('produces', 'produces')]
    item_287 = models.CharField(max_length=8, choices=item_287_choices, null=True)
    item_288_choices = [('produces', 'produces')]
    item_288 = models.CharField(max_length=8, choices=item_288_choices, null=True)
    item_289_choices = [('produces', 'produces')]
    item_289 = models.CharField(max_length=8, choices=item_289_choices, null=True)
    item_290_choices = [('produces', 'produces')]
    item_290 = models.CharField(max_length=8, choices=item_290_choices, null=True)
    item_291_choices = [('produces', 'produces')]
    item_291 = models.CharField(max_length=8, choices=item_291_choices, null=True)
    item_292_choices = [('produces', 'produces')]
    item_292 = models.CharField(max_length=8, choices=item_292_choices, null=True)
    item_293_choices = [('produces', 'produces')]
    item_293 = models.CharField(max_length=8, choices=item_293_choices, null=True)
    item_294_choices = [('produces', 'produces')]
    item_294 = models.CharField(max_length=8, choices=item_294_choices, null=True)
    item_295_choices = [('produces', 'produces')]
    item_295 = models.CharField(max_length=8, choices=item_295_choices, null=True)
    item_296_choices = [('produces', 'produces')]
    item_296 = models.CharField(max_length=8, choices=item_296_choices, null=True)
    item_297_choices = [('produces', 'produces')]
    item_297 = models.CharField(max_length=8, choices=item_297_choices, null=True)
    item_298_choices = [('produces', 'produces')]
    item_298 = models.CharField(max_length=8, choices=item_298_choices, null=True)
    item_299_choices = [('produces', 'produces')]
    item_299 = models.CharField(max_length=8, choices=item_299_choices, null=True)
    item_300_choices = [('produces', 'produces')]
    item_300 = models.CharField(max_length=8, choices=item_300_choices, null=True)
    item_301_choices = [('produces', 'produces')]
    item_301 = models.CharField(max_length=8, choices=item_301_choices, null=True)
    item_302_choices = [('produces', 'produces')]
    item_302 = models.CharField(max_length=8, choices=item_302_choices, null=True)
    item_303_choices = [('produces', 'produces')]
    item_303 = models.CharField(max_length=8, choices=item_303_choices, null=True)
    item_304_choices = [('produces', 'produces')]
    item_304 = models.CharField(max_length=8, choices=item_304_choices, null=True)
    item_305_choices = [('produces', 'produces')]
    item_305 = models.CharField(max_length=8, choices=item_305_choices, null=True)
    item_306_choices = [('produces', 'produces')]
    item_306 = models.CharField(max_length=8, choices=item_306_choices, null=True)
    item_307_choices = [('produces', 'produces')]
    item_307 = models.CharField(max_length=8, choices=item_307_choices, null=True)
    item_308_choices = [('produces', 'produces')]
    item_308 = models.CharField(max_length=8, choices=item_308_choices, null=True)
    item_309_choices = [('produces', 'produces')]
    item_309 = models.CharField(max_length=8, choices=item_309_choices, null=True)
    item_310_choices = [('produces', 'produces')]
    item_310 = models.CharField(max_length=8, choices=item_310_choices, null=True)
    item_311_choices = [('produces', 'produces')]
    item_311 = models.CharField(max_length=8, choices=item_311_choices, null=True)
    item_312_choices = [('produces', 'produces')]
    item_312 = models.CharField(max_length=8, choices=item_312_choices, null=True)
    item_313_choices = [('produces', 'produces')]
    item_313 = models.CharField(max_length=8, choices=item_313_choices, null=True)
    item_314_choices = [('produces', 'produces')]
    item_314 = models.CharField(max_length=8, choices=item_314_choices, null=True)
    item_315_choices = [('produces', 'produces')]
    item_315 = models.CharField(max_length=8, choices=item_315_choices, null=True)
    item_316_choices = [('produces', 'produces')]
    item_316 = models.CharField(max_length=8, choices=item_316_choices, null=True)
    item_317_choices = [('produces', 'produces')]
    item_317 = models.CharField(max_length=8, choices=item_317_choices, null=True)
    item_318_choices = [('produces', 'produces')]
    item_318 = models.CharField(max_length=8, choices=item_318_choices, null=True)
    item_319_choices = [('produces', 'produces')]
    item_319 = models.CharField(max_length=8, choices=item_319_choices, null=True)
    item_320_choices = [('produces', 'produces')]
    item_320 = models.CharField(max_length=8, choices=item_320_choices, null=True)
    item_321_choices = [('produces', 'produces')]
    item_321 = models.CharField(max_length=8, choices=item_321_choices, null=True)
    item_322_choices = [('produces', 'produces')]
    item_322 = models.CharField(max_length=8, choices=item_322_choices, null=True)
    item_323_choices = [('produces', 'produces')]
    item_323 = models.CharField(max_length=8, choices=item_323_choices, null=True)
    item_324_choices = [('produces', 'produces')]
    item_324 = models.CharField(max_length=8, choices=item_324_choices, null=True)
    item_325_choices = [('produces', 'produces')]
    item_325 = models.CharField(max_length=8, choices=item_325_choices, null=True)
    item_326_choices = [('produces', 'produces')]
    item_326 = models.CharField(max_length=8, choices=item_326_choices, null=True)
    item_327_choices = [('produces', 'produces')]
    item_327 = models.CharField(max_length=8, choices=item_327_choices, null=True)
    item_328_choices = [('produces', 'produces')]
    item_328 = models.CharField(max_length=8, choices=item_328_choices, null=True)
    item_329_choices = [('produces', 'produces')]
    item_329 = models.CharField(max_length=8, choices=item_329_choices, null=True)
    item_330_choices = [('produces', 'produces')]
    item_330 = models.CharField(max_length=8, choices=item_330_choices, null=True)
    item_331_choices = [('produces', 'produces')]
    item_331 = models.CharField(max_length=8, choices=item_331_choices, null=True)
    item_332_choices = [('produces', 'produces')]
    item_332 = models.CharField(max_length=8, choices=item_332_choices, null=True)
    item_333_choices = [('produces', 'produces')]
    item_333 = models.CharField(max_length=8, choices=item_333_choices, null=True)
    item_334_choices = [('produces', 'produces')]
    item_334 = models.CharField(max_length=8, choices=item_334_choices, null=True)
    item_335_choices = [('produces', 'produces')]
    item_335 = models.CharField(max_length=8, choices=item_335_choices, null=True)
    item_336_choices = [('produces', 'produces')]
    item_336 = models.CharField(max_length=8, choices=item_336_choices, null=True)
    item_337_choices = [('produces', 'produces')]
    item_337 = models.CharField(max_length=8, choices=item_337_choices, null=True)
    item_338_choices = [('produces', 'produces')]
    item_338 = models.CharField(max_length=8, choices=item_338_choices, null=True)
    item_339_choices = [('produces', 'produces')]
    item_339 = models.CharField(max_length=8, choices=item_339_choices, null=True)
    item_340_choices = [('produces', 'produces')]
    item_340 = models.CharField(max_length=8, choices=item_340_choices, null=True)
    item_341_choices = [('produces', 'produces')]
    item_341 = models.CharField(max_length=8, choices=item_341_choices, null=True)
    item_342_choices = [('produces', 'produces')]
    item_342 = models.CharField(max_length=8, choices=item_342_choices, null=True)
    item_343_choices = [('produces', 'produces')]
    item_343 = models.CharField(max_length=8, choices=item_343_choices, null=True)
    item_344_choices = [('produces', 'produces')]
    item_344 = models.CharField(max_length=8, choices=item_344_choices, null=True)
    item_345_choices = [('produces', 'produces')]
    item_345 = models.CharField(max_length=8, choices=item_345_choices, null=True)
    item_346_choices = [('produces', 'produces')]
    item_346 = models.CharField(max_length=8, choices=item_346_choices, null=True)
    item_347_choices = [('produces', 'produces')]
    item_347 = models.CharField(max_length=8, choices=item_347_choices, null=True)
    item_348_choices = [('produces', 'produces')]
    item_348 = models.CharField(max_length=8, choices=item_348_choices, null=True)
    item_349_choices = [('produces', 'produces')]
    item_349 = models.CharField(max_length=8, choices=item_349_choices, null=True)
    item_350_choices = [('produces', 'produces')]
    item_350 = models.CharField(max_length=8, choices=item_350_choices, null=True)
    item_351_choices = [('produces', 'produces')]
    item_351 = models.CharField(max_length=8, choices=item_351_choices, null=True)
    item_352_choices = [('produces', 'produces')]
    item_352 = models.CharField(max_length=8, choices=item_352_choices, null=True)
    item_353_choices = [('produces', 'produces')]
    item_353 = models.CharField(max_length=8, choices=item_353_choices, null=True)
    item_354_choices = [('produces', 'produces')]
    item_354 = models.CharField(max_length=8, choices=item_354_choices, null=True)
    item_355_choices = [('produces', 'produces')]
    item_355 = models.CharField(max_length=8, choices=item_355_choices, null=True)
    item_356_choices = [('produces', 'produces')]
    item_356 = models.CharField(max_length=8, choices=item_356_choices, null=True)
    item_357_choices = [('produces', 'produces')]
    item_357 = models.CharField(max_length=8, choices=item_357_choices, null=True)
    item_358_choices = [('produces', 'produces')]
    item_358 = models.CharField(max_length=8, choices=item_358_choices, null=True)
    item_359_choices = [('produces', 'produces')]
    item_359 = models.CharField(max_length=8, choices=item_359_choices, null=True)
    item_360_choices = [('produces', 'produces')]
    item_360 = models.CharField(max_length=8, choices=item_360_choices, null=True)
    item_361_choices = [('produces', 'produces')]
    item_361 = models.CharField(max_length=8, choices=item_361_choices, null=True)
    item_362_choices = [('produces', 'produces')]
    item_362 = models.CharField(max_length=8, choices=item_362_choices, null=True)
    item_363_choices = [('produces', 'produces')]
    item_363 = models.CharField(max_length=8, choices=item_363_choices, null=True)
    item_364_choices = [('produces', 'produces')]
    item_364 = models.CharField(max_length=8, choices=item_364_choices, null=True)
    item_365_choices = [('produces', 'produces')]
    item_365 = models.CharField(max_length=8, choices=item_365_choices, null=True)
    item_366_choices = [('produces', 'produces')]
    item_366 = models.CharField(max_length=8, choices=item_366_choices, null=True)
    item_367_choices = [('produces', 'produces')]
    item_367 = models.CharField(max_length=8, choices=item_367_choices, null=True)
    item_368_choices = [('produces', 'produces')]
    item_368 = models.CharField(max_length=8, choices=item_368_choices, null=True)
    item_369_choices = [('produces', 'produces')]
    item_369 = models.CharField(max_length=8, choices=item_369_choices, null=True)
    item_370_choices = [('produces', 'produces')]
    item_370 = models.CharField(max_length=8, choices=item_370_choices, null=True)
    item_371_choices = [('produces', 'produces')]
    item_371 = models.CharField(max_length=8, choices=item_371_choices, null=True)
    item_372_choices = [('produces', 'produces')]
    item_372 = models.CharField(max_length=8, choices=item_372_choices, null=True)
    item_373_choices = [('produces', 'produces')]
    item_373 = models.CharField(max_length=8, choices=item_373_choices, null=True)
    item_374_choices = [('produces', 'produces')]
    item_374 = models.CharField(max_length=8, choices=item_374_choices, null=True)
    item_375_choices = [('produces', 'produces')]
    item_375 = models.CharField(max_length=8, choices=item_375_choices, null=True)
    item_376_choices = [('produces', 'produces')]
    item_376 = models.CharField(max_length=8, choices=item_376_choices, null=True)
    item_377_choices = [('produces', 'produces')]
    item_377 = models.CharField(max_length=8, choices=item_377_choices, null=True)
    item_378_choices = [('produces', 'produces')]
    item_378 = models.CharField(max_length=8, choices=item_378_choices, null=True)
    item_379_choices = [('produces', 'produces')]
    item_379 = models.CharField(max_length=8, choices=item_379_choices, null=True)
    item_380_choices = [('produces', 'produces')]
    item_380 = models.CharField(max_length=8, choices=item_380_choices, null=True)
    item_381_choices = [('produces', 'produces')]
    item_381 = models.CharField(max_length=8, choices=item_381_choices, null=True)
    item_382_choices = [('produces', 'produces')]
    item_382 = models.CharField(max_length=8, choices=item_382_choices, null=True)
    item_383_choices = [('produces', 'produces')]
    item_383 = models.CharField(max_length=8, choices=item_383_choices, null=True)
    item_384_choices = [('produces', 'produces')]
    item_384 = models.CharField(max_length=8, choices=item_384_choices, null=True)
    item_385_choices = [('produces', 'produces')]
    item_385 = models.CharField(max_length=8, choices=item_385_choices, null=True)
    item_386_choices = [('produces', 'produces')]
    item_386 = models.CharField(max_length=8, choices=item_386_choices, null=True)
    item_387_choices = [('produces', 'produces')]
    item_387 = models.CharField(max_length=8, choices=item_387_choices, null=True)
    item_388_choices = [('produces', 'produces')]
    item_388 = models.CharField(max_length=8, choices=item_388_choices, null=True)
    item_389_choices = [('produces', 'produces')]
    item_389 = models.CharField(max_length=8, choices=item_389_choices, null=True)
    item_390_choices = [('produces', 'produces')]
    item_390 = models.CharField(max_length=8, choices=item_390_choices, null=True)
    item_391_choices = [('produces', 'produces')]
    item_391 = models.CharField(max_length=8, choices=item_391_choices, null=True)
    item_392_choices = [('produces', 'produces')]
    item_392 = models.CharField(max_length=8, choices=item_392_choices, null=True)
    item_393_choices = [('produces', 'produces')]
    item_393 = models.CharField(max_length=8, choices=item_393_choices, null=True)
    item_394_choices = [('produces', 'produces')]
    item_394 = models.CharField(max_length=8, choices=item_394_choices, null=True)
    item_395_choices = [('produces', 'produces')]
    item_395 = models.CharField(max_length=8, choices=item_395_choices, null=True)
    item_396_choices = [('produces', 'produces')]
    item_396 = models.CharField(max_length=8, choices=item_396_choices, null=True)
    item_397_choices = [('produces', 'produces')]
    item_397 = models.CharField(max_length=8, choices=item_397_choices, null=True)
    item_398_choices = [('produces', 'produces')]
    item_398 = models.CharField(max_length=8, choices=item_398_choices, null=True)
    item_399_choices = [('produces', 'produces')]
    item_399 = models.CharField(max_length=8, choices=item_399_choices, null=True)
    item_400_choices = [('produces', 'produces')]
    item_400 = models.CharField(max_length=8, choices=item_400_choices, null=True)
    item_401_choices = [('produces', 'produces')]
    item_401 = models.CharField(max_length=8, choices=item_401_choices, null=True)
    item_402_choices = [('produces', 'produces')]
    item_402 = models.CharField(max_length=8, choices=item_402_choices, null=True)
    item_403_choices = [('produces', 'produces')]
    item_403 = models.CharField(max_length=8, choices=item_403_choices, null=True)
    item_404_choices = [('produces', 'produces')]
    item_404 = models.CharField(max_length=8, choices=item_404_choices, null=True)
    item_405_choices = [('produces', 'produces')]
    item_405 = models.CharField(max_length=8, choices=item_405_choices, null=True)
    item_406_choices = [('produces', 'produces')]
    item_406 = models.CharField(max_length=8, choices=item_406_choices, null=True)
    item_407_choices = [('produces', 'produces')]
    item_407 = models.CharField(max_length=8, choices=item_407_choices, null=True)
    item_408_choices = [('produces', 'produces')]
    item_408 = models.CharField(max_length=8, choices=item_408_choices, null=True)
    item_409_choices = [('produces', 'produces')]
    item_409 = models.CharField(max_length=8, choices=item_409_choices, null=True)
    item_410_choices = [('produces', 'produces')]
    item_410 = models.CharField(max_length=8, choices=item_410_choices, null=True)
    item_411_choices = [('produces', 'produces')]
    item_411 = models.CharField(max_length=8, choices=item_411_choices, null=True)
    item_412_choices = [('produces', 'produces')]
    item_412 = models.CharField(max_length=8, choices=item_412_choices, null=True)
    item_413_choices = [('produces', 'produces')]
    item_413 = models.CharField(max_length=8, choices=item_413_choices, null=True)
    item_414_choices = [('produces', 'produces')]
    item_414 = models.CharField(max_length=8, choices=item_414_choices, null=True)
    item_415_choices = [('produces', 'produces')]
    item_415 = models.CharField(max_length=8, choices=item_415_choices, null=True)
    item_416_choices = [('produces', 'produces')]
    item_416 = models.CharField(max_length=8, choices=item_416_choices, null=True)
    item_417_choices = [('produces', 'produces')]
    item_417 = models.CharField(max_length=8, choices=item_417_choices, null=True)
    item_418_choices = [('produces', 'produces')]
    item_418 = models.CharField(max_length=8, choices=item_418_choices, null=True)
    item_419_choices = [('produces', 'produces')]
    item_419 = models.CharField(max_length=8, choices=item_419_choices, null=True)
    item_420_choices = [('produces', 'produces')]
    item_420 = models.CharField(max_length=8, choices=item_420_choices, null=True)
    item_421_choices = [('produces', 'produces')]
    item_421 = models.CharField(max_length=8, choices=item_421_choices, null=True)
    item_422_choices = [('produces', 'produces')]
    item_422 = models.CharField(max_length=8, choices=item_422_choices, null=True)
    item_423_choices = [('produces', 'produces')]
    item_423 = models.CharField(max_length=8, choices=item_423_choices, null=True)
    item_424_choices = [('produces', 'produces')]
    item_424 = models.CharField(max_length=8, choices=item_424_choices, null=True)
    item_425_choices = [('produces', 'produces')]
    item_425 = models.CharField(max_length=8, choices=item_425_choices, null=True)
    item_426_choices = [('produces', 'produces')]
    item_426 = models.CharField(max_length=8, choices=item_426_choices, null=True)
    item_427_choices = [('produces', 'produces')]
    item_427 = models.CharField(max_length=8, choices=item_427_choices, null=True)
    item_428_choices = [('produces', 'produces')]
    item_428 = models.CharField(max_length=8, choices=item_428_choices, null=True)
    item_429_choices = [('produces', 'produces')]
    item_429 = models.CharField(max_length=8, choices=item_429_choices, null=True)
    item_430_choices = [('produces', 'produces')]
    item_430 = models.CharField(max_length=8, choices=item_430_choices, null=True)
    item_431_choices = [('produces', 'produces')]
    item_431 = models.CharField(max_length=8, choices=item_431_choices, null=True)
    item_432_choices = [('produces', 'produces')]
    item_432 = models.CharField(max_length=8, choices=item_432_choices, null=True)
    item_433_choices = [('produces', 'produces')]
    item_433 = models.CharField(max_length=8, choices=item_433_choices, null=True)
    item_434_choices = [('produces', 'produces')]
    item_434 = models.CharField(max_length=8, choices=item_434_choices, null=True)
    item_435_choices = [('produces', 'produces')]
    item_435 = models.CharField(max_length=8, choices=item_435_choices, null=True)
    item_436_choices = [('produces', 'produces')]
    item_436 = models.CharField(max_length=8, choices=item_436_choices, null=True)
    item_437_choices = [('produces', 'produces')]
    item_437 = models.CharField(max_length=8, choices=item_437_choices, null=True)
    item_438_choices = [('produces', 'produces')]
    item_438 = models.CharField(max_length=8, choices=item_438_choices, null=True)
    item_439_choices = [('produces', 'produces')]
    item_439 = models.CharField(max_length=8, choices=item_439_choices, null=True)
    item_440_choices = [('produces', 'produces')]
    item_440 = models.CharField(max_length=8, choices=item_440_choices, null=True)
    item_441_choices = [('produces', 'produces')]
    item_441 = models.CharField(max_length=8, choices=item_441_choices, null=True)
    item_442_choices = [('produces', 'produces')]
    item_442 = models.CharField(max_length=8, choices=item_442_choices, null=True)
    item_443_choices = [('produces', 'produces')]
    item_443 = models.CharField(max_length=8, choices=item_443_choices, null=True)
    item_444_choices = [('produces', 'produces')]
    item_444 = models.CharField(max_length=8, choices=item_444_choices, null=True)
    item_445_choices = [('produces', 'produces')]
    item_445 = models.CharField(max_length=8, choices=item_445_choices, null=True)
    item_446_choices = [('produces', 'produces')]
    item_446 = models.CharField(max_length=8, choices=item_446_choices, null=True)
    item_447_choices = [('produces', 'produces')]
    item_447 = models.CharField(max_length=8, choices=item_447_choices, null=True)
    item_448_choices = [('produces', 'produces')]
    item_448 = models.CharField(max_length=8, choices=item_448_choices, null=True)
    item_449_choices = [('produces', 'produces')]
    item_449 = models.CharField(max_length=8, choices=item_449_choices, null=True)
    item_450_choices = [('produces', 'produces')]
    item_450 = models.CharField(max_length=8, choices=item_450_choices, null=True)
    item_451_choices = [('produces', 'produces')]
    item_451 = models.CharField(max_length=8, choices=item_451_choices, null=True)
    item_452_choices = [('produces', 'produces')]
    item_452 = models.CharField(max_length=8, choices=item_452_choices, null=True)
    item_453_choices = [('produces', 'produces')]
    item_453 = models.CharField(max_length=8, choices=item_453_choices, null=True)
    item_454_choices = [('produces', 'produces')]
    item_454 = models.CharField(max_length=8, choices=item_454_choices, null=True)
    item_455_choices = [('produces', 'produces')]
    item_455 = models.CharField(max_length=8, choices=item_455_choices, null=True)
    item_456_choices = [('produces', 'produces')]
    item_456 = models.CharField(max_length=8, choices=item_456_choices, null=True)
    item_457_choices = [('produces', 'produces')]
    item_457 = models.CharField(max_length=8, choices=item_457_choices, null=True)
    item_458_choices = [('produces', 'produces')]
    item_458 = models.CharField(max_length=8, choices=item_458_choices, null=True)
    item_459_choices = [('produces', 'produces')]
    item_459 = models.CharField(max_length=8, choices=item_459_choices, null=True)
    item_460_choices = [('produces', 'produces')]
    item_460 = models.CharField(max_length=8, choices=item_460_choices, null=True)
    item_461_choices = [('produces', 'produces')]
    item_461 = models.CharField(max_length=8, choices=item_461_choices, null=True)
    item_462_choices = [('produces', 'produces')]
    item_462 = models.CharField(max_length=8, choices=item_462_choices, null=True)
    item_463_choices = [('produces', 'produces')]
    item_463 = models.CharField(max_length=8, choices=item_463_choices, null=True)
    item_464_choices = [('produces', 'produces')]
    item_464 = models.CharField(max_length=8, choices=item_464_choices, null=True)
    item_465_choices = [('produces', 'produces')]
    item_465 = models.CharField(max_length=8, choices=item_465_choices, null=True)
    item_466_choices = [('produces', 'produces')]
    item_466 = models.CharField(max_length=8, choices=item_466_choices, null=True)
    item_467_choices = [('produces', 'produces')]
    item_467 = models.CharField(max_length=8, choices=item_467_choices, null=True)
    item_468_choices = [('produces', 'produces')]
    item_468 = models.CharField(max_length=8, choices=item_468_choices, null=True)
    item_469_choices = [('produces', 'produces')]
    item_469 = models.CharField(max_length=8, choices=item_469_choices, null=True)
    item_470_choices = [('produces', 'produces')]
    item_470 = models.CharField(max_length=8, choices=item_470_choices, null=True)
    item_471_choices = [('produces', 'produces')]
    item_471 = models.CharField(max_length=8, choices=item_471_choices, null=True)
    item_472_choices = [('produces', 'produces')]
    item_472 = models.CharField(max_length=8, choices=item_472_choices, null=True)
    item_473_choices = [('produces', 'produces')]
    item_473 = models.CharField(max_length=8, choices=item_473_choices, null=True)
    item_474_choices = [('produces', 'produces')]
    item_474 = models.CharField(max_length=8, choices=item_474_choices, null=True)
    item_475_choices = [('produces', 'produces')]
    item_475 = models.CharField(max_length=8, choices=item_475_choices, null=True)
    item_476_choices = [('produces', 'produces')]
    item_476 = models.CharField(max_length=8, choices=item_476_choices, null=True)
    item_477_choices = [('produces', 'produces')]
    item_477 = models.CharField(max_length=8, choices=item_477_choices, null=True)
    item_478_choices = [('produces', 'produces')]
    item_478 = models.CharField(max_length=8, choices=item_478_choices, null=True)
    item_479_choices = [('produces', 'produces')]
    item_479 = models.CharField(max_length=8, choices=item_479_choices, null=True)
    item_480_choices = [('produces', 'produces')]
    item_480 = models.CharField(max_length=8, choices=item_480_choices, null=True)
    item_481_choices = [('produces', 'produces')]
    item_481 = models.CharField(max_length=8, choices=item_481_choices, null=True)
    item_482_choices = [('produces', 'produces')]
    item_482 = models.CharField(max_length=8, choices=item_482_choices, null=True)
    item_483_choices = [('produces', 'produces')]
    item_483 = models.CharField(max_length=8, choices=item_483_choices, null=True)
    item_484_choices = [('produces', 'produces')]
    item_484 = models.CharField(max_length=8, choices=item_484_choices, null=True)
    item_485_choices = [('produces', 'produces')]
    item_485 = models.CharField(max_length=8, choices=item_485_choices, null=True)
    item_486_choices = [('produces', 'produces')]
    item_486 = models.CharField(max_length=8, choices=item_486_choices, null=True)
    item_487_choices = [('produces', 'produces')]
    item_487 = models.CharField(max_length=8, choices=item_487_choices, null=True)
    item_488_choices = [('produces', 'produces')]
    item_488 = models.CharField(max_length=8, choices=item_488_choices, null=True)
    item_489_choices = [('produces', 'produces')]
    item_489 = models.CharField(max_length=8, choices=item_489_choices, null=True)
    item_490_choices = [('produces', 'produces')]
    item_490 = models.CharField(max_length=8, choices=item_490_choices, null=True)
    item_491_choices = [('produces', 'produces')]
    item_491 = models.CharField(max_length=8, choices=item_491_choices, null=True)
    item_492_choices = [('produces', 'produces')]
    item_492 = models.CharField(max_length=8, choices=item_492_choices, null=True)
    item_493_choices = [('produces', 'produces')]
    item_493 = models.CharField(max_length=8, choices=item_493_choices, null=True)
    item_494_choices = [('produces', 'produces')]
    item_494 = models.CharField(max_length=8, choices=item_494_choices, null=True)
    item_495_choices = [('produces', 'produces')]
    item_495 = models.CharField(max_length=8, choices=item_495_choices, null=True)
    item_496_choices = [('produces', 'produces')]
    item_496 = models.CharField(max_length=8, choices=item_496_choices, null=True)
    item_497_choices = [('produces', 'produces')]
    item_497 = models.CharField(max_length=8, choices=item_497_choices, null=True)
    item_498_choices = [('produces', 'produces')]
    item_498 = models.CharField(max_length=8, choices=item_498_choices, null=True)
    item_499_choices = [('produces', 'produces')]
    item_499 = models.CharField(max_length=8, choices=item_499_choices, null=True)
    item_500_choices = [('produces', 'produces')]
    item_500 = models.CharField(max_length=8, choices=item_500_choices, null=True)
    item_501_choices = [('produces', 'produces')]
    item_501 = models.CharField(max_length=8, choices=item_501_choices, null=True)
    item_502_choices = [('produces', 'produces')]
    item_502 = models.CharField(max_length=8, choices=item_502_choices, null=True)
    item_503_choices = [('produces', 'produces')]
    item_503 = models.CharField(max_length=8, choices=item_503_choices, null=True)
    item_504_choices = [('produces', 'produces')]
    item_504 = models.CharField(max_length=8, choices=item_504_choices, null=True)
    item_505_choices = [('produces', 'produces')]
    item_505 = models.CharField(max_length=8, choices=item_505_choices, null=True)
    item_506_choices = [('produces', 'produces')]
    item_506 = models.CharField(max_length=8, choices=item_506_choices, null=True)
    item_507_choices = [('produces', 'produces')]
    item_507 = models.CharField(max_length=8, choices=item_507_choices, null=True)
    item_508_choices = [('produces', 'produces')]
    item_508 = models.CharField(max_length=8, choices=item_508_choices, null=True)
    item_509_choices = [('produces', 'produces')]
    item_509 = models.CharField(max_length=8, choices=item_509_choices, null=True)
    item_510_choices = [('produces', 'produces')]
    item_510 = models.CharField(max_length=8, choices=item_510_choices, null=True)
    item_511_choices = [('produces', 'produces')]
    item_511 = models.CharField(max_length=8, choices=item_511_choices, null=True)
    item_512_choices = [('produces', 'produces')]
    item_512 = models.CharField(max_length=8, choices=item_512_choices, null=True)
    item_513_choices = [('produces', 'produces')]
    item_513 = models.CharField(max_length=8, choices=item_513_choices, null=True)
    item_514_choices = [('produces', 'produces')]
    item_514 = models.CharField(max_length=8, choices=item_514_choices, null=True)
    item_515_choices = [('produces', 'produces')]
    item_515 = models.CharField(max_length=8, choices=item_515_choices, null=True)
    item_516_choices = [('produces', 'produces')]
    item_516 = models.CharField(max_length=8, choices=item_516_choices, null=True)
    item_517_choices = [('produces', 'produces')]
    item_517 = models.CharField(max_length=8, choices=item_517_choices, null=True)
    item_518_choices = [('produces', 'produces')]
    item_518 = models.CharField(max_length=8, choices=item_518_choices, null=True)
    item_519_choices = [('produces', 'produces')]
    item_519 = models.CharField(max_length=8, choices=item_519_choices, null=True)
    item_520_choices = [('produces', 'produces')]
    item_520 = models.CharField(max_length=8, choices=item_520_choices, null=True)
    item_521_choices = [('produces', 'produces')]
    item_521 = models.CharField(max_length=8, choices=item_521_choices, null=True)
    item_522_choices = [('produces', 'produces')]
    item_522 = models.CharField(max_length=8, choices=item_522_choices, null=True)
    item_523_choices = [('produces', 'produces')]
    item_523 = models.CharField(max_length=8, choices=item_523_choices, null=True)
    item_524_choices = [('produces', 'produces')]
    item_524 = models.CharField(max_length=8, choices=item_524_choices, null=True)
    item_525_choices = [('produces', 'produces')]
    item_525 = models.CharField(max_length=8, choices=item_525_choices, null=True)
    item_526_choices = [('produces', 'produces')]
    item_526 = models.CharField(max_length=8, choices=item_526_choices, null=True)
    item_527_choices = [('produces', 'produces')]
    item_527 = models.CharField(max_length=8, choices=item_527_choices, null=True)
    item_528_choices = [('produces', 'produces')]
    item_528 = models.CharField(max_length=8, choices=item_528_choices, null=True)
    item_529_choices = [('produces', 'produces')]
    item_529 = models.CharField(max_length=8, choices=item_529_choices, null=True)
    item_530_choices = [('produces', 'produces')]
    item_530 = models.CharField(max_length=8, choices=item_530_choices, null=True)
    item_531_choices = [('produces', 'produces')]
    item_531 = models.CharField(max_length=8, choices=item_531_choices, null=True)
    item_532_choices = [('produces', 'produces')]
    item_532 = models.CharField(max_length=8, choices=item_532_choices, null=True)
    item_533_choices = [('produces', 'produces')]
    item_533 = models.CharField(max_length=8, choices=item_533_choices, null=True)
    item_534_choices = [('produces', 'produces')]
    item_534 = models.CharField(max_length=8, choices=item_534_choices, null=True)
    item_535_choices = [('produces', 'produces')]
    item_535 = models.CharField(max_length=8, choices=item_535_choices, null=True)
    item_536_choices = [('produces', 'produces')]
    item_536 = models.CharField(max_length=8, choices=item_536_choices, null=True)
    item_537_choices = [('produces', 'produces')]
    item_537 = models.CharField(max_length=8, choices=item_537_choices, null=True)
    item_538_choices = [('produces', 'produces')]
    item_538 = models.CharField(max_length=8, choices=item_538_choices, null=True)
    item_539_choices = [('produces', 'produces')]
    item_539 = models.CharField(max_length=8, choices=item_539_choices, null=True)
    item_540_choices = [('produces', 'produces')]
    item_540 = models.CharField(max_length=8, choices=item_540_choices, null=True)
    item_541_choices = [('produces', 'produces')]
    item_541 = models.CharField(max_length=8, choices=item_541_choices, null=True)
    item_542_choices = [('produces', 'produces')]
    item_542 = models.CharField(max_length=8, choices=item_542_choices, null=True)
    item_543_choices = [('produces', 'produces')]
    item_543 = models.CharField(max_length=8, choices=item_543_choices, null=True)
    item_544_choices = [('produces', 'produces')]
    item_544 = models.CharField(max_length=8, choices=item_544_choices, null=True)
    item_545_choices = [('produces', 'produces')]
    item_545 = models.CharField(max_length=8, choices=item_545_choices, null=True)
    item_546_choices = [('produces', 'produces')]
    item_546 = models.CharField(max_length=8, choices=item_546_choices, null=True)
    item_547_choices = [('produces', 'produces')]
    item_547 = models.CharField(max_length=8, choices=item_547_choices, null=True)
    item_548_choices = [('produces', 'produces')]
    item_548 = models.CharField(max_length=8, choices=item_548_choices, null=True)
    item_549_choices = [('produces', 'produces')]
    item_549 = models.CharField(max_length=8, choices=item_549_choices, null=True)
    item_550_choices = [('produces', 'produces')]
    item_550 = models.CharField(max_length=8, choices=item_550_choices, null=True)
    item_551_choices = [('produces', 'produces')]
    item_551 = models.CharField(max_length=8, choices=item_551_choices, null=True)
    item_552_choices = [('produces', 'produces')]
    item_552 = models.CharField(max_length=8, choices=item_552_choices, null=True)
    item_553_choices = [('produces', 'produces')]
    item_553 = models.CharField(max_length=8, choices=item_553_choices, null=True)
    item_554_choices = [('produces', 'produces')]
    item_554 = models.CharField(max_length=8, choices=item_554_choices, null=True)
    item_555_choices = [('produces', 'produces')]
    item_555 = models.CharField(max_length=8, choices=item_555_choices, null=True)
    item_556_choices = [('produces', 'produces')]
    item_556 = models.CharField(max_length=8, choices=item_556_choices, null=True)
    item_557_choices = [('produces', 'produces')]
    item_557 = models.CharField(max_length=8, choices=item_557_choices, null=True)
    item_558_choices = [('produces', 'produces')]
    item_558 = models.CharField(max_length=8, choices=item_558_choices, null=True)
    item_559_choices = [('produces', 'produces')]
    item_559 = models.CharField(max_length=8, choices=item_559_choices, null=True)
    item_560_choices = [('produces', 'produces')]
    item_560 = models.CharField(max_length=8, choices=item_560_choices, null=True)
    item_561_choices = [('produces', 'produces')]
    item_561 = models.CharField(max_length=8, choices=item_561_choices, null=True)
    item_562_choices = [('produces', 'produces')]
    item_562 = models.CharField(max_length=8, choices=item_562_choices, null=True)
    item_563_choices = [('yes', 'yes'), ('no', 'no')]
    item_563 = models.CharField(max_length=3, choices=item_563_choices, null=True)
