from django.db import models
from instruments.base import BaseTable


class Irish_WS(BaseTable):
    item_14_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_14 = models.CharField(max_length=15, choices=item_14_choices, null=True)
    item_16_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_16 = models.CharField(max_length=15, choices=item_16_choices, null=True)
    item_18_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_18 = models.CharField(max_length=15, choices=item_18_choices, null=True)
    item_20_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_20 = models.CharField(max_length=15, choices=item_20_choices, null=True)
    item_21_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_21 = models.CharField(max_length=15, choices=item_21_choices, null=True)
    item_23_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_23 = models.CharField(max_length=15, choices=item_23_choices, null=True)
    item_25_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_25 = models.CharField(max_length=15, choices=item_25_choices, null=True)
    item_27_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_27 = models.CharField(max_length=15, choices=item_27_choices, null=True)
    item_29_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_29 = models.CharField(max_length=15, choices=item_29_choices, null=True)
    item_31_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_31 = models.CharField(max_length=15, choices=item_31_choices, null=True)
    item_32_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_32 = models.CharField(max_length=15, choices=item_32_choices, null=True)
    item_34_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_34 = models.CharField(max_length=15, choices=item_34_choices, null=True)
    item_36_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_36 = models.CharField(max_length=15, choices=item_36_choices, null=True)
    item_38_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_38 = models.CharField(max_length=15, choices=item_38_choices, null=True)
    item_40_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_40 = models.CharField(max_length=15, choices=item_40_choices, null=True)
    item_42_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_42 = models.CharField(max_length=15, choices=item_42_choices, null=True)
    item_44_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_44 = models.CharField(max_length=15, choices=item_44_choices, null=True)
    item_46_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_46 = models.CharField(max_length=15, choices=item_46_choices, null=True)
    item_48_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_48 = models.CharField(max_length=15, choices=item_48_choices, null=True)
    item_49_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_49 = models.CharField(max_length=15, choices=item_49_choices, null=True)
    item_51_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_51 = models.CharField(max_length=15, choices=item_51_choices, null=True)
    item_53_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_53 = models.CharField(max_length=15, choices=item_53_choices, null=True)
    item_55_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_55 = models.CharField(max_length=15, choices=item_55_choices, null=True)
    item_56_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_56 = models.CharField(max_length=15, choices=item_56_choices, null=True)
    item_58_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_58 = models.CharField(max_length=15, choices=item_58_choices, null=True)
    item_60_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_60 = models.CharField(max_length=15, choices=item_60_choices, null=True)
    item_62_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_62 = models.CharField(max_length=15, choices=item_62_choices, null=True)
    item_64_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_64 = models.CharField(max_length=15, choices=item_64_choices, null=True)
    item_66_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_66 = models.CharField(max_length=15, choices=item_66_choices, null=True)
    item_68_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_68 = models.CharField(max_length=15, choices=item_68_choices, null=True)
    item_70_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_70 = models.CharField(max_length=15, choices=item_70_choices, null=True)
    item_72_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_72 = models.CharField(max_length=15, choices=item_72_choices, null=True)
    item_74_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_74 = models.CharField(max_length=15, choices=item_74_choices, null=True)
    item_76_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_76 = models.CharField(max_length=15, choices=item_76_choices, null=True)
    item_77_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_77 = models.CharField(max_length=15, choices=item_77_choices, null=True)
    item_79_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_79 = models.CharField(max_length=15, choices=item_79_choices, null=True)
    item_81_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_81 = models.CharField(max_length=15, choices=item_81_choices, null=True)
    item_83_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_83 = models.CharField(max_length=15, choices=item_83_choices, null=True)
    item_85_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_85 = models.CharField(max_length=15, choices=item_85_choices, null=True)
    item_87_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_87 = models.CharField(max_length=15, choices=item_87_choices, null=True)
    item_89_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_89 = models.CharField(max_length=15, choices=item_89_choices, null=True)
    item_91_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_91 = models.CharField(max_length=15, choices=item_91_choices, null=True)
    item_93_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_93 = models.CharField(max_length=15, choices=item_93_choices, null=True)
    item_95_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_95 = models.CharField(max_length=15, choices=item_95_choices, null=True)
    item_97_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_97 = models.CharField(max_length=15, choices=item_97_choices, null=True)
    item_98_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_98 = models.CharField(max_length=15, choices=item_98_choices, null=True)
    item_100_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_100 = models.CharField(max_length=15, choices=item_100_choices, null=True)
    item_101_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_101 = models.CharField(max_length=15, choices=item_101_choices, null=True)
    item_103_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_103 = models.CharField(max_length=15, choices=item_103_choices, null=True)
    item_105_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_105 = models.CharField(max_length=15, choices=item_105_choices, null=True)
    item_106_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_106 = models.CharField(max_length=15, choices=item_106_choices, null=True)
    item_108_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_108 = models.CharField(max_length=15, choices=item_108_choices, null=True)
    item_110_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_110 = models.CharField(max_length=15, choices=item_110_choices, null=True)
    item_113_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_113 = models.CharField(max_length=15, choices=item_113_choices, null=True)
    item_114_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_114 = models.CharField(max_length=15, choices=item_114_choices, null=True)
    item_117_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_117 = models.CharField(max_length=15, choices=item_117_choices, null=True)
    item_119_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_119 = models.CharField(max_length=15, choices=item_119_choices, null=True)
    item_120_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_120 = models.CharField(max_length=15, choices=item_120_choices, null=True)
    item_122_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_122 = models.CharField(max_length=15, choices=item_122_choices, null=True)
    item_124_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_124 = models.CharField(max_length=15, choices=item_124_choices, null=True)
    item_126_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_126 = models.CharField(max_length=15, choices=item_126_choices, null=True)
    item_128_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_128 = models.CharField(max_length=15, choices=item_128_choices, null=True)
    item_129_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_129 = models.CharField(max_length=15, choices=item_129_choices, null=True)
    item_131_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_131 = models.CharField(max_length=15, choices=item_131_choices, null=True)
    item_132_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_132 = models.CharField(max_length=15, choices=item_132_choices, null=True)
    item_134_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_134 = models.CharField(max_length=15, choices=item_134_choices, null=True)
    item_136_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_136 = models.CharField(max_length=15, choices=item_136_choices, null=True)
    item_138_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_138 = models.CharField(max_length=15, choices=item_138_choices, null=True)
    item_140_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_140 = models.CharField(max_length=15, choices=item_140_choices, null=True)
    item_142_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_142 = models.CharField(max_length=15, choices=item_142_choices, null=True)
    item_145_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_145 = models.CharField(max_length=15, choices=item_145_choices, null=True)
    item_146_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_146 = models.CharField(max_length=15, choices=item_146_choices, null=True)
    item_149_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_149 = models.CharField(max_length=15, choices=item_149_choices, null=True)
    item_151_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_151 = models.CharField(max_length=15, choices=item_151_choices, null=True)
    item_153_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_153 = models.CharField(max_length=15, choices=item_153_choices, null=True)
    item_155_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_155 = models.CharField(max_length=15, choices=item_155_choices, null=True)
    item_157_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_157 = models.CharField(max_length=15, choices=item_157_choices, null=True)
    item_159_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_159 = models.CharField(max_length=15, choices=item_159_choices, null=True)
    item_161_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_161 = models.CharField(max_length=15, choices=item_161_choices, null=True)
    item_163_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_163 = models.CharField(max_length=15, choices=item_163_choices, null=True)
    item_164_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_164 = models.CharField(max_length=15, choices=item_164_choices, null=True)
    item_166_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_166 = models.CharField(max_length=15, choices=item_166_choices, null=True)
    item_168_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_168 = models.CharField(max_length=15, choices=item_168_choices, null=True)
    item_170_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_170 = models.CharField(max_length=15, choices=item_170_choices, null=True)
    item_172_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_172 = models.CharField(max_length=15, choices=item_172_choices, null=True)
    item_173_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_173 = models.CharField(max_length=15, choices=item_173_choices, null=True)
    item_175_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_175 = models.CharField(max_length=15, choices=item_175_choices, null=True)
    item_177_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_177 = models.CharField(max_length=15, choices=item_177_choices, null=True)
    item_178_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_178 = models.CharField(max_length=15, choices=item_178_choices, null=True)
    item_180_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_180 = models.CharField(max_length=15, choices=item_180_choices, null=True)
    item_182_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_182 = models.CharField(max_length=15, choices=item_182_choices, null=True)
    item_184_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_184 = models.CharField(max_length=15, choices=item_184_choices, null=True)
    item_185_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_185 = models.CharField(max_length=15, choices=item_185_choices, null=True)
    item_187_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_187 = models.CharField(max_length=15, choices=item_187_choices, null=True)
    item_189_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_189 = models.CharField(max_length=15, choices=item_189_choices, null=True)
    item_191_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_191 = models.CharField(max_length=15, choices=item_191_choices, null=True)
    item_193_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_193 = models.CharField(max_length=15, choices=item_193_choices, null=True)
    item_195_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_195 = models.CharField(max_length=15, choices=item_195_choices, null=True)
    item_197_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_197 = models.CharField(max_length=15, choices=item_197_choices, null=True)
    item_199_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_199 = models.CharField(max_length=15, choices=item_199_choices, null=True)
    item_200_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_200 = models.CharField(max_length=15, choices=item_200_choices, null=True)
    item_203_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_203 = models.CharField(max_length=15, choices=item_203_choices, null=True)
    item_205_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_205 = models.CharField(max_length=15, choices=item_205_choices, null=True)
    item_207_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_207 = models.CharField(max_length=15, choices=item_207_choices, null=True)
    item_209_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_209 = models.CharField(max_length=15, choices=item_209_choices, null=True)
    item_211_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_211 = models.CharField(max_length=15, choices=item_211_choices, null=True)
    item_213_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_213 = models.CharField(max_length=15, choices=item_213_choices, null=True)
    item_216_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_216 = models.CharField(max_length=15, choices=item_216_choices, null=True)
    item_218_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_218 = models.CharField(max_length=15, choices=item_218_choices, null=True)
    item_220_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_220 = models.CharField(max_length=15, choices=item_220_choices, null=True)
    item_222_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_222 = models.CharField(max_length=15, choices=item_222_choices, null=True)
    item_224_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_224 = models.CharField(max_length=15, choices=item_224_choices, null=True)
    item_226_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_226 = models.CharField(max_length=15, choices=item_226_choices, null=True)
    item_228_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_228 = models.CharField(max_length=15, choices=item_228_choices, null=True)
    item_230_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_230 = models.CharField(max_length=15, choices=item_230_choices, null=True)
    item_232_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_232 = models.CharField(max_length=15, choices=item_232_choices, null=True)
    item_233_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_233 = models.CharField(max_length=15, choices=item_233_choices, null=True)
    item_235_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_235 = models.CharField(max_length=15, choices=item_235_choices, null=True)
    item_236_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_236 = models.CharField(max_length=15, choices=item_236_choices, null=True)
    item_238_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_238 = models.CharField(max_length=15, choices=item_238_choices, null=True)
    item_240_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_240 = models.CharField(max_length=15, choices=item_240_choices, null=True)
    item_242_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_242 = models.CharField(max_length=15, choices=item_242_choices, null=True)
    item_244_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_244 = models.CharField(max_length=15, choices=item_244_choices, null=True)
    item_246_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_246 = models.CharField(max_length=15, choices=item_246_choices, null=True)
    item_248_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_248 = models.CharField(max_length=15, choices=item_248_choices, null=True)
    item_250_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_250 = models.CharField(max_length=15, choices=item_250_choices, null=True)
    item_252_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_252 = models.CharField(max_length=15, choices=item_252_choices, null=True)
    item_254_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_254 = models.CharField(max_length=15, choices=item_254_choices, null=True)
    item_255_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_255 = models.CharField(max_length=15, choices=item_255_choices, null=True)
    item_257_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_257 = models.CharField(max_length=15, choices=item_257_choices, null=True)
    item_259_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_259 = models.CharField(max_length=15, choices=item_259_choices, null=True)
    item_261_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_261 = models.CharField(max_length=15, choices=item_261_choices, null=True)
    item_263_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_263 = models.CharField(max_length=15, choices=item_263_choices, null=True)
    item_265_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_265 = models.CharField(max_length=15, choices=item_265_choices, null=True)
    item_267_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_267 = models.CharField(max_length=15, choices=item_267_choices, null=True)
    item_269_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_269 = models.CharField(max_length=15, choices=item_269_choices, null=True)
    item_271_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_271 = models.CharField(max_length=15, choices=item_271_choices, null=True)
    item_273_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_273 = models.CharField(max_length=15, choices=item_273_choices, null=True)
    item_275_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_275 = models.CharField(max_length=15, choices=item_275_choices, null=True)
    item_277_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_277 = models.CharField(max_length=15, choices=item_277_choices, null=True)
    item_279_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_279 = models.CharField(max_length=15, choices=item_279_choices, null=True)
    item_281_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_281 = models.CharField(max_length=15, choices=item_281_choices, null=True)
    item_283_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_283 = models.CharField(max_length=15, choices=item_283_choices, null=True)
    item_285_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_285 = models.CharField(max_length=15, choices=item_285_choices, null=True)
    item_287_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_287 = models.CharField(max_length=15, choices=item_287_choices, null=True)
    item_289_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_289 = models.CharField(max_length=15, choices=item_289_choices, null=True)
    item_292_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_292 = models.CharField(max_length=15, choices=item_292_choices, null=True)
    item_294_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_294 = models.CharField(max_length=15, choices=item_294_choices, null=True)
    item_296_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_296 = models.CharField(max_length=15, choices=item_296_choices, null=True)
    item_298_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_298 = models.CharField(max_length=15, choices=item_298_choices, null=True)
    item_300_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_300 = models.CharField(max_length=15, choices=item_300_choices, null=True)
    item_302_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_302 = models.CharField(max_length=15, choices=item_302_choices, null=True)
    item_304_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_304 = models.CharField(max_length=15, choices=item_304_choices, null=True)
    item_306_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_306 = models.CharField(max_length=15, choices=item_306_choices, null=True)
    item_308_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_308 = models.CharField(max_length=15, choices=item_308_choices, null=True)
    item_310_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_310 = models.CharField(max_length=15, choices=item_310_choices, null=True)
    item_312_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_312 = models.CharField(max_length=15, choices=item_312_choices, null=True)
    item_314_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_314 = models.CharField(max_length=15, choices=item_314_choices, null=True)
    item_316_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_316 = models.CharField(max_length=15, choices=item_316_choices, null=True)
    item_318_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_318 = models.CharField(max_length=15, choices=item_318_choices, null=True)
    item_320_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_320 = models.CharField(max_length=15, choices=item_320_choices, null=True)
    item_322_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_322 = models.CharField(max_length=15, choices=item_322_choices, null=True)
    item_323_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_323 = models.CharField(max_length=15, choices=item_323_choices, null=True)
    item_325_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_325 = models.CharField(max_length=15, choices=item_325_choices, null=True)
    item_328_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_328 = models.CharField(max_length=15, choices=item_328_choices, null=True)
    item_330_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_330 = models.CharField(max_length=15, choices=item_330_choices, null=True)
    item_332_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_332 = models.CharField(max_length=15, choices=item_332_choices, null=True)
    item_334_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_334 = models.CharField(max_length=15, choices=item_334_choices, null=True)
    item_336_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_336 = models.CharField(max_length=15, choices=item_336_choices, null=True)
    item_338_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_338 = models.CharField(max_length=15, choices=item_338_choices, null=True)
    item_340_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_340 = models.CharField(max_length=15, choices=item_340_choices, null=True)
    item_342_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_342 = models.CharField(max_length=15, choices=item_342_choices, null=True)
    item_344_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_344 = models.CharField(max_length=15, choices=item_344_choices, null=True)
    item_346_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_346 = models.CharField(max_length=15, choices=item_346_choices, null=True)
    item_348_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_348 = models.CharField(max_length=15, choices=item_348_choices, null=True)
    item_350_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_350 = models.CharField(max_length=15, choices=item_350_choices, null=True)
    item_352_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_352 = models.CharField(max_length=15, choices=item_352_choices, null=True)
    item_354_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_354 = models.CharField(max_length=15, choices=item_354_choices, null=True)
    item_356_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_356 = models.CharField(max_length=15, choices=item_356_choices, null=True)
    item_358_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_358 = models.CharField(max_length=15, choices=item_358_choices, null=True)
    item_360_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_360 = models.CharField(max_length=15, choices=item_360_choices, null=True)
    item_362_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_362 = models.CharField(max_length=15, choices=item_362_choices, null=True)
    item_364_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_364 = models.CharField(max_length=15, choices=item_364_choices, null=True)
    item_366_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_366 = models.CharField(max_length=15, choices=item_366_choices, null=True)
    item_368_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_368 = models.CharField(max_length=15, choices=item_368_choices, null=True)
    item_369_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_369 = models.CharField(max_length=15, choices=item_369_choices, null=True)
    item_371_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_371 = models.CharField(max_length=15, choices=item_371_choices, null=True)
    item_373_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_373 = models.CharField(max_length=15, choices=item_373_choices, null=True)
    item_375_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_375 = models.CharField(max_length=15, choices=item_375_choices, null=True)
    item_377_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_377 = models.CharField(max_length=15, choices=item_377_choices, null=True)
    item_379_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_379 = models.CharField(max_length=15, choices=item_379_choices, null=True)
    item_381_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_381 = models.CharField(max_length=15, choices=item_381_choices, null=True)
    item_383_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_383 = models.CharField(max_length=15, choices=item_383_choices, null=True)
    item_385_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_385 = models.CharField(max_length=15, choices=item_385_choices, null=True)
    item_387_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_387 = models.CharField(max_length=15, choices=item_387_choices, null=True)
    item_389_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_389 = models.CharField(max_length=15, choices=item_389_choices, null=True)
    item_391_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_391 = models.CharField(max_length=15, choices=item_391_choices, null=True)
    item_393_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_393 = models.CharField(max_length=15, choices=item_393_choices, null=True)
    item_395_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_395 = models.CharField(max_length=15, choices=item_395_choices, null=True)
    item_397_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_397 = models.CharField(max_length=15, choices=item_397_choices, null=True)
    item_399_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_399 = models.CharField(max_length=15, choices=item_399_choices, null=True)
    item_401_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_401 = models.CharField(max_length=15, choices=item_401_choices, null=True)
    item_403_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_403 = models.CharField(max_length=15, choices=item_403_choices, null=True)
    item_405_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_405 = models.CharField(max_length=15, choices=item_405_choices, null=True)
    item_407_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_407 = models.CharField(max_length=15, choices=item_407_choices, null=True)
    item_409_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_409 = models.CharField(max_length=15, choices=item_409_choices, null=True)
    item_411_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_411 = models.CharField(max_length=15, choices=item_411_choices, null=True)
    item_413_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_413 = models.CharField(max_length=15, choices=item_413_choices, null=True)
    item_415_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_415 = models.CharField(max_length=15, choices=item_415_choices, null=True)
    item_417_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_417 = models.CharField(max_length=15, choices=item_417_choices, null=True)
    item_419_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_419 = models.CharField(max_length=15, choices=item_419_choices, null=True)
    item_420_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_420 = models.CharField(max_length=15, choices=item_420_choices, null=True)
    item_422_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_422 = models.CharField(max_length=15, choices=item_422_choices, null=True)
    item_424_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_424 = models.CharField(max_length=15, choices=item_424_choices, null=True)
    item_426_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_426 = models.CharField(max_length=15, choices=item_426_choices, null=True)
    item_427_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_427 = models.CharField(max_length=15, choices=item_427_choices, null=True)
    item_429_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_429 = models.CharField(max_length=15, choices=item_429_choices, null=True)
    item_431_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_431 = models.CharField(max_length=15, choices=item_431_choices, null=True)
    item_433_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_433 = models.CharField(max_length=15, choices=item_433_choices, null=True)
    item_435_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_435 = models.CharField(max_length=15, choices=item_435_choices, null=True)
    item_437_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_437 = models.CharField(max_length=15, choices=item_437_choices, null=True)
    item_439_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_439 = models.CharField(max_length=15, choices=item_439_choices, null=True)
    item_441_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_441 = models.CharField(max_length=15, choices=item_441_choices, null=True)
    item_443_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_443 = models.CharField(max_length=15, choices=item_443_choices, null=True)
    item_445_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_445 = models.CharField(max_length=15, choices=item_445_choices, null=True)
    item_447_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_447 = models.CharField(max_length=15, choices=item_447_choices, null=True)
    item_448_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_448 = models.CharField(max_length=15, choices=item_448_choices, null=True)
    item_450_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_450 = models.CharField(max_length=15, choices=item_450_choices, null=True)
    item_452_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_452 = models.CharField(max_length=15, choices=item_452_choices, null=True)
    item_454_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_454 = models.CharField(max_length=15, choices=item_454_choices, null=True)
    item_456_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_456 = models.CharField(max_length=15, choices=item_456_choices, null=True)
    item_458_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_458 = models.CharField(max_length=15, choices=item_458_choices, null=True)
    item_461_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_461 = models.CharField(max_length=15, choices=item_461_choices, null=True)
    item_463_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_463 = models.CharField(max_length=15, choices=item_463_choices, null=True)
    item_465_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_465 = models.CharField(max_length=15, choices=item_465_choices, null=True)
    item_467_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_467 = models.CharField(max_length=15, choices=item_467_choices, null=True)
    item_469_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_469 = models.CharField(max_length=15, choices=item_469_choices, null=True)
    item_471_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_471 = models.CharField(max_length=15, choices=item_471_choices, null=True)
    item_473_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_473 = models.CharField(max_length=15, choices=item_473_choices, null=True)
    item_475_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_475 = models.CharField(max_length=15, choices=item_475_choices, null=True)
    item_477_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_477 = models.CharField(max_length=15, choices=item_477_choices, null=True)
    item_479_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_479 = models.CharField(max_length=15, choices=item_479_choices, null=True)
    item_481_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_481 = models.CharField(max_length=15, choices=item_481_choices, null=True)
    item_483_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_483 = models.CharField(max_length=15, choices=item_483_choices, null=True)
    item_485_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_485 = models.CharField(max_length=15, choices=item_485_choices, null=True)
    item_487_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_487 = models.CharField(max_length=15, choices=item_487_choices, null=True)
    item_490_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_490 = models.CharField(max_length=15, choices=item_490_choices, null=True)
    item_492_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_492 = models.CharField(max_length=15, choices=item_492_choices, null=True)
    item_494_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_494 = models.CharField(max_length=15, choices=item_494_choices, null=True)
    item_496_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_496 = models.CharField(max_length=15, choices=item_496_choices, null=True)
    item_498_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_498 = models.CharField(max_length=15, choices=item_498_choices, null=True)
    item_500_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_500 = models.CharField(max_length=15, choices=item_500_choices, null=True)
    item_502_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_502 = models.CharField(max_length=15, choices=item_502_choices, null=True)
    item_504_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_504 = models.CharField(max_length=15, choices=item_504_choices, null=True)
    item_506_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_506 = models.CharField(max_length=15, choices=item_506_choices, null=True)
    item_508_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_508 = models.CharField(max_length=15, choices=item_508_choices, null=True)
    item_510_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_510 = models.CharField(max_length=15, choices=item_510_choices, null=True)
    item_512_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_512 = models.CharField(max_length=15, choices=item_512_choices, null=True)
    item_514_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_514 = models.CharField(max_length=15, choices=item_514_choices, null=True)
    item_516_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_516 = models.CharField(max_length=15, choices=item_516_choices, null=True)
    item_518_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_518 = models.CharField(max_length=15, choices=item_518_choices, null=True)
    item_520_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_520 = models.CharField(max_length=15, choices=item_520_choices, null=True)
    item_522_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_522 = models.CharField(max_length=15, choices=item_522_choices, null=True)
    item_524_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_524 = models.CharField(max_length=15, choices=item_524_choices, null=True)
    item_526_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_526 = models.CharField(max_length=15, choices=item_526_choices, null=True)
    item_528_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_528 = models.CharField(max_length=15, choices=item_528_choices, null=True)
    item_530_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_530 = models.CharField(max_length=15, choices=item_530_choices, null=True)
    item_532_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_532 = models.CharField(max_length=15, choices=item_532_choices, null=True)
    item_534_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_534 = models.CharField(max_length=15, choices=item_534_choices, null=True)
    item_536_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_536 = models.CharField(max_length=15, choices=item_536_choices, null=True)
    item_538_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_538 = models.CharField(max_length=15, choices=item_538_choices, null=True)
    item_540_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_540 = models.CharField(max_length=15, choices=item_540_choices, null=True)
    item_542_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_542 = models.CharField(max_length=15, choices=item_542_choices, null=True)
    item_544_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_544 = models.CharField(max_length=15, choices=item_544_choices, null=True)
    item_546_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_546 = models.CharField(max_length=15, choices=item_546_choices, null=True)
    item_548_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_548 = models.CharField(max_length=15, choices=item_548_choices, null=True)
    item_550_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_550 = models.CharField(max_length=15, choices=item_550_choices, null=True)
    item_552_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_552 = models.CharField(max_length=15, choices=item_552_choices, null=True)
    item_554_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_554 = models.CharField(max_length=15, choices=item_554_choices, null=True)
    item_556_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_556 = models.CharField(max_length=15, choices=item_556_choices, null=True)
    item_558_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_558 = models.CharField(max_length=15, choices=item_558_choices, null=True)
    item_560_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_560 = models.CharField(max_length=15, choices=item_560_choices, null=True)
    item_562_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_562 = models.CharField(max_length=15, choices=item_562_choices, null=True)
    item_564_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_564 = models.CharField(max_length=15, choices=item_564_choices, null=True)
    item_566_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_566 = models.CharField(max_length=15, choices=item_566_choices, null=True)
    item_568_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_568 = models.CharField(max_length=15, choices=item_568_choices, null=True)
    item_570_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_570 = models.CharField(max_length=15, choices=item_570_choices, null=True)
    item_572_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_572 = models.CharField(max_length=15, choices=item_572_choices, null=True)
    item_574_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_574 = models.CharField(max_length=15, choices=item_574_choices, null=True)
    item_576_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_576 = models.CharField(max_length=15, choices=item_576_choices, null=True)
    item_578_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_578 = models.CharField(max_length=15, choices=item_578_choices, null=True)
    item_580_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_580 = models.CharField(max_length=15, choices=item_580_choices, null=True)
    item_582_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_582 = models.CharField(max_length=15, choices=item_582_choices, null=True)
    item_584_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_584 = models.CharField(max_length=15, choices=item_584_choices, null=True)
    item_586_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_586 = models.CharField(max_length=15, choices=item_586_choices, null=True)
    item_588_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_588 = models.CharField(max_length=15, choices=item_588_choices, null=True)
    item_590_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_590 = models.CharField(max_length=15, choices=item_590_choices, null=True)
    item_592_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_592 = models.CharField(max_length=15, choices=item_592_choices, null=True)
    item_594_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_594 = models.CharField(max_length=15, choices=item_594_choices, null=True)
    item_596_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_596 = models.CharField(max_length=15, choices=item_596_choices, null=True)
    item_598_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_598 = models.CharField(max_length=15, choices=item_598_choices, null=True)
    item_600_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_600 = models.CharField(max_length=15, choices=item_600_choices, null=True)
    item_602_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_602 = models.CharField(max_length=15, choices=item_602_choices, null=True)
    item_604_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_604 = models.CharField(max_length=15, choices=item_604_choices, null=True)
    item_606_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_606 = models.CharField(max_length=15, choices=item_606_choices, null=True)
    item_608_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_608 = models.CharField(max_length=15, choices=item_608_choices, null=True)
    item_610_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_610 = models.CharField(max_length=15, choices=item_610_choices, null=True)
    item_612_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_612 = models.CharField(max_length=15, choices=item_612_choices, null=True)
    item_614_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_614 = models.CharField(max_length=15, choices=item_614_choices, null=True)
    item_616_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_616 = models.CharField(max_length=15, choices=item_616_choices, null=True)
    item_618_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_618 = models.CharField(max_length=15, choices=item_618_choices, null=True)
    item_620_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_620 = models.CharField(max_length=15, choices=item_620_choices, null=True)
    item_622_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_622 = models.CharField(max_length=15, choices=item_622_choices, null=True)
    item_624_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_624 = models.CharField(max_length=15, choices=item_624_choices, null=True)
    item_626_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_626 = models.CharField(max_length=15, choices=item_626_choices, null=True)
    item_628_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_628 = models.CharField(max_length=15, choices=item_628_choices, null=True)
    item_630_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_630 = models.CharField(max_length=15, choices=item_630_choices, null=True)
    item_632_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_632 = models.CharField(max_length=15, choices=item_632_choices, null=True)
    item_634_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_634 = models.CharField(max_length=15, choices=item_634_choices, null=True)
    item_636_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_636 = models.CharField(max_length=15, choices=item_636_choices, null=True)
    item_638_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_638 = models.CharField(max_length=15, choices=item_638_choices, null=True)
    item_640_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_640 = models.CharField(max_length=15, choices=item_640_choices, null=True)
    item_642_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_642 = models.CharField(max_length=15, choices=item_642_choices, null=True)
    item_644_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_644 = models.CharField(max_length=15, choices=item_644_choices, null=True)
    item_646_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_646 = models.CharField(max_length=15, choices=item_646_choices, null=True)
    item_648_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_648 = models.CharField(max_length=15, choices=item_648_choices, null=True)
    item_650_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_650 = models.CharField(max_length=15, choices=item_650_choices, null=True)
    item_652_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_652 = models.CharField(max_length=15, choices=item_652_choices, null=True)
    item_654_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_654 = models.CharField(max_length=15, choices=item_654_choices, null=True)
    item_656_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_656 = models.CharField(max_length=15, choices=item_656_choices, null=True)
    item_658_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_658 = models.CharField(max_length=15, choices=item_658_choices, null=True)
    item_661_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_661 = models.CharField(max_length=15, choices=item_661_choices, null=True)
    item_663_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_663 = models.CharField(max_length=15, choices=item_663_choices, null=True)
    item_666_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_666 = models.CharField(max_length=15, choices=item_666_choices, null=True)
    item_668_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_668 = models.CharField(max_length=15, choices=item_668_choices, null=True)
    item_670_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_670 = models.CharField(max_length=15, choices=item_670_choices, null=True)
    item_672_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_672 = models.CharField(max_length=15, choices=item_672_choices, null=True)
    item_674_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_674 = models.CharField(max_length=15, choices=item_674_choices, null=True)
    item_676_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_676 = models.CharField(max_length=15, choices=item_676_choices, null=True)
    item_678_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_678 = models.CharField(max_length=15, choices=item_678_choices, null=True)
    item_680_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_680 = models.CharField(max_length=15, choices=item_680_choices, null=True)
    item_682_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_682 = models.CharField(max_length=15, choices=item_682_choices, null=True)
    item_684_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_684 = models.CharField(max_length=15, choices=item_684_choices, null=True)
    item_686_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_686 = models.CharField(max_length=15, choices=item_686_choices, null=True)
    item_688_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_688 = models.CharField(max_length=15, choices=item_688_choices, null=True)
    item_690_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_690 = models.CharField(max_length=15, choices=item_690_choices, null=True)
    item_692_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_692 = models.CharField(max_length=15, choices=item_692_choices, null=True)
    item_693_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_693 = models.CharField(max_length=15, choices=item_693_choices, null=True)
    item_695_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_695 = models.CharField(max_length=15, choices=item_695_choices, null=True)
    item_697_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_697 = models.CharField(max_length=15, choices=item_697_choices, null=True)
    item_699_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_699 = models.CharField(max_length=15, choices=item_699_choices, null=True)
    item_701_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_701 = models.CharField(max_length=15, choices=item_701_choices, null=True)
    item_703_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_703 = models.CharField(max_length=15, choices=item_703_choices, null=True)
    item_705_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_705 = models.CharField(max_length=15, choices=item_705_choices, null=True)
    item_707_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_707 = models.CharField(max_length=15, choices=item_707_choices, null=True)
    item_709_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_709 = models.CharField(max_length=15, choices=item_709_choices, null=True)
    item_711_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_711 = models.CharField(max_length=15, choices=item_711_choices, null=True)
    item_713_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_713 = models.CharField(max_length=15, choices=item_713_choices, null=True)
    item_715_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_715 = models.CharField(max_length=15, choices=item_715_choices, null=True)
    item_717_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_717 = models.CharField(max_length=15, choices=item_717_choices, null=True)
    item_719_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_719 = models.CharField(max_length=15, choices=item_719_choices, null=True)
    item_721_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_721 = models.CharField(max_length=15, choices=item_721_choices, null=True)
    item_722_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_722 = models.CharField(max_length=15, choices=item_722_choices, null=True)
    item_724_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_724 = models.CharField(max_length=15, choices=item_724_choices, null=True)
    item_726_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_726 = models.CharField(max_length=15, choices=item_726_choices, null=True)
    item_728_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_728 = models.CharField(max_length=15, choices=item_728_choices, null=True)
    item_729_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_729 = models.CharField(max_length=22, choices=item_729_choices, null=True)
    item_731_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_731 = models.CharField(max_length=22, choices=item_731_choices, null=True)
    item_733_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_733 = models.CharField(max_length=22, choices=item_733_choices, null=True)
    item_735_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_735 = models.CharField(max_length=22, choices=item_735_choices, null=True)
    item_737_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_737 = models.CharField(max_length=22, choices=item_737_choices, null=True)
    item_739_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_739 = models.CharField(max_length=22, choices=item_739_choices, null=True)
    item_741_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_741 = models.CharField(max_length=22, choices=item_741_choices, null=True)
    item_743_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_743 = models.CharField(max_length=22, choices=item_743_choices, null=True)
    item_745_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_745 = models.CharField(max_length=22, choices=item_745_choices, null=True)
    item_747_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_747 = models.CharField(max_length=22, choices=item_747_choices, null=True)
    item_749_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_749 = models.CharField(max_length=22, choices=item_749_choices, null=True)
    item_751_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_751 = models.CharField(max_length=22, choices=item_751_choices, null=True)
    item_753_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_753 = models.CharField(max_length=22, choices=item_753_choices, null=True)
    item_755_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_755 = models.CharField(max_length=22, choices=item_755_choices, null=True)
    item_757_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_757 = models.CharField(max_length=22, choices=item_757_choices, null=True)
    item_759_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_759 = models.CharField(max_length=22, choices=item_759_choices, null=True)
    item_761_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_761 = models.CharField(max_length=22, choices=item_761_choices, null=True)
    item_763_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_763 = models.CharField(max_length=22, choices=item_763_choices, null=True)
    item_765_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_765 = models.CharField(max_length=22, choices=item_765_choices, null=True)
    item_767_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_767 = models.CharField(max_length=22, choices=item_767_choices, null=True)
    item_769_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_769 = models.CharField(max_length=22, choices=item_769_choices, null=True)
    item_771_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_771 = models.CharField(max_length=22, choices=item_771_choices, null=True)
    item_773_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_773 = models.CharField(max_length=22, choices=item_773_choices, null=True)
    item_775_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_775 = models.CharField(max_length=22, choices=item_775_choices, null=True)
    item_776_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_776 = models.CharField(max_length=22, choices=item_776_choices, null=True)
    item_778_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_778 = models.CharField(max_length=22, choices=item_778_choices, null=True)
    item_780_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_780 = models.CharField(max_length=22, choices=item_780_choices, null=True)
    item_781_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_781 = models.CharField(max_length=22, choices=item_781_choices, null=True)
    item_783_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_783 = models.CharField(max_length=22, choices=item_783_choices, null=True)
    item_784_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_784 = models.CharField(max_length=22, choices=item_784_choices, null=True)
    item_786_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_786 = models.CharField(max_length=22, choices=item_786_choices, null=True)
    item_788_choices = [(' ROUTINES AND PHRASES"', ' ROUTINES AND PHRASES"')]
    item_788 = models.CharField(max_length=22, choices=item_788_choices, null=True)
    item_790_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_790 = models.CharField(max_length=15, choices=item_790_choices, null=True)
    item_792_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_792 = models.CharField(max_length=15, choices=item_792_choices, null=True)
    item_794_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_794 = models.CharField(max_length=15, choices=item_794_choices, null=True)
    item_796_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_796 = models.CharField(max_length=15, choices=item_796_choices, null=True)
    item_798_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_798 = models.CharField(max_length=15, choices=item_798_choices, null=True)
    item_800_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_800 = models.CharField(max_length=15, choices=item_800_choices, null=True)
    item_802_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_802 = models.CharField(max_length=15, choices=item_802_choices, null=True)
    item_804_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_804 = models.CharField(max_length=15, choices=item_804_choices, null=True)
    item_806_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_806 = models.CharField(max_length=15, choices=item_806_choices, null=True)
    item_808_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_808 = models.CharField(max_length=15, choices=item_808_choices, null=True)
    item_810_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_810 = models.CharField(max_length=15, choices=item_810_choices, null=True)
    item_812_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_812 = models.CharField(max_length=15, choices=item_812_choices, null=True)
    item_814_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_814 = models.CharField(max_length=15, choices=item_814_choices, null=True)
    item_816_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_816 = models.CharField(max_length=15, choices=item_816_choices, null=True)
    item_818_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_818 = models.CharField(max_length=15, choices=item_818_choices, null=True)
    item_820_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_820 = models.CharField(max_length=15, choices=item_820_choices, null=True)
    item_822_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_822 = models.CharField(max_length=15, choices=item_822_choices, null=True)
    item_824_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_824 = models.CharField(max_length=15, choices=item_824_choices, null=True)
    item_826_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_826 = models.CharField(max_length=15, choices=item_826_choices, null=True)
    item_828_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_828 = models.CharField(max_length=15, choices=item_828_choices, null=True)
    item_830_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_830 = models.CharField(max_length=15, choices=item_830_choices, null=True)
    item_832_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_832 = models.CharField(max_length=15, choices=item_832_choices, null=True)
    item_834_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_834 = models.CharField(max_length=15, choices=item_834_choices, null=True)
    item_836_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_836 = models.CharField(max_length=15, choices=item_836_choices, null=True)
    item_838_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_838 = models.CharField(max_length=15, choices=item_838_choices, null=True)
    item_840_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_840 = models.CharField(max_length=15, choices=item_840_choices, null=True)
    item_842_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_842 = models.CharField(max_length=15, choices=item_842_choices, null=True)
    item_844_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_844 = models.CharField(max_length=15, choices=item_844_choices, null=True)
    item_846_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_846 = models.CharField(max_length=15, choices=item_846_choices, null=True)
    item_848_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_848 = models.CharField(max_length=15, choices=item_848_choices, null=True)
    item_850_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_850 = models.CharField(max_length=15, choices=item_850_choices, null=True)
    item_852_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_852 = models.CharField(max_length=15, choices=item_852_choices, null=True)
    item_854_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_854 = models.CharField(max_length=15, choices=item_854_choices, null=True)
    item_856_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_856 = models.CharField(max_length=15, choices=item_856_choices, null=True)
    item_858_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_858 = models.CharField(max_length=15, choices=item_858_choices, null=True)
    item_860_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_860 = models.CharField(max_length=15, choices=item_860_choices, null=True)
    item_862_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_862 = models.CharField(max_length=15, choices=item_862_choices, null=True)
    item_864_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_864 = models.CharField(max_length=15, choices=item_864_choices, null=True)
    item_866_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_866 = models.CharField(max_length=15, choices=item_866_choices, null=True)
    item_868_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_868 = models.CharField(max_length=15, choices=item_868_choices, null=True)
    item_870_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_870 = models.CharField(max_length=15, choices=item_870_choices, null=True)
    item_872_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_872 = models.CharField(max_length=15, choices=item_872_choices, null=True)
    item_874_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_874 = models.CharField(max_length=15, choices=item_874_choices, null=True)
    item_876_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_876 = models.CharField(max_length=15, choices=item_876_choices, null=True)
    item_878_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_878 = models.CharField(max_length=15, choices=item_878_choices, null=True)
    item_880_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_880 = models.CharField(max_length=15, choices=item_880_choices, null=True)
    item_882_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_882 = models.CharField(max_length=15, choices=item_882_choices, null=True)
    item_884_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_884 = models.CharField(max_length=15, choices=item_884_choices, null=True)
    item_886_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_886 = models.CharField(max_length=15, choices=item_886_choices, null=True)
    item_888_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_888 = models.CharField(max_length=15, choices=item_888_choices, null=True)
    item_890_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_890 = models.CharField(max_length=15, choices=item_890_choices, null=True)
    item_892_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_892 = models.CharField(max_length=15, choices=item_892_choices, null=True)
    item_894_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_894 = models.CharField(max_length=15, choices=item_894_choices, null=True)
    item_896_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_896 = models.CharField(max_length=15, choices=item_896_choices, null=True)
    item_898_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_898 = models.CharField(max_length=15, choices=item_898_choices, null=True)
    item_900_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_900 = models.CharField(max_length=15, choices=item_900_choices, null=True)
    item_902_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_902 = models.CharField(max_length=15, choices=item_902_choices, null=True)
    item_904_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_904 = models.CharField(max_length=15, choices=item_904_choices, null=True)
    item_906_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_906 = models.CharField(max_length=15, choices=item_906_choices, null=True)
    item_908_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_908 = models.CharField(max_length=15, choices=item_908_choices, null=True)
    item_910_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_910 = models.CharField(max_length=15, choices=item_910_choices, null=True)
    item_912_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_912 = models.CharField(max_length=15, choices=item_912_choices, null=True)
    item_914_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_914 = models.CharField(max_length=15, choices=item_914_choices, null=True)
    item_916_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_916 = models.CharField(max_length=15, choices=item_916_choices, null=True)
    item_918_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_918 = models.CharField(max_length=15, choices=item_918_choices, null=True)
    item_920_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_920 = models.CharField(max_length=15, choices=item_920_choices, null=True)
    item_922_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_922 = models.CharField(max_length=15, choices=item_922_choices, null=True)
    item_924_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_924 = models.CharField(max_length=15, choices=item_924_choices, null=True)
    item_926_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_926 = models.CharField(max_length=15, choices=item_926_choices, null=True)
    item_928_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_928 = models.CharField(max_length=15, choices=item_928_choices, null=True)
    item_930_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_930 = models.CharField(max_length=15, choices=item_930_choices, null=True)
    item_932_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_932 = models.CharField(max_length=15, choices=item_932_choices, null=True)
    item_934_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_934 = models.CharField(max_length=15, choices=item_934_choices, null=True)
    item_936_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_936 = models.CharField(max_length=15, choices=item_936_choices, null=True)
    item_938_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_938 = models.CharField(max_length=15, choices=item_938_choices, null=True)
    item_940_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_940 = models.CharField(max_length=15, choices=item_940_choices, null=True)
    item_942_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_942 = models.CharField(max_length=15, choices=item_942_choices, null=True)
    item_944_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_944 = models.CharField(max_length=15, choices=item_944_choices, null=True)
    item_946_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_946 = models.CharField(max_length=15, choices=item_946_choices, null=True)
    item_948_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_948 = models.CharField(max_length=15, choices=item_948_choices, null=True)
    item_950_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_950 = models.CharField(max_length=15, choices=item_950_choices, null=True)
    item_952_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_952 = models.CharField(max_length=15, choices=item_952_choices, null=True)
    item_954_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_954 = models.CharField(max_length=15, choices=item_954_choices, null=True)
    item_956_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_956 = models.CharField(max_length=15, choices=item_956_choices, null=True)
    item_958_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_958 = models.CharField(max_length=15, choices=item_958_choices, null=True)
    item_960_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_960 = models.CharField(max_length=15, choices=item_960_choices, null=True)
    item_962_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_962 = models.CharField(max_length=15, choices=item_962_choices, null=True)
    item_964_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_964 = models.CharField(max_length=15, choices=item_964_choices, null=True)
    item_966_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_966 = models.CharField(max_length=15, choices=item_966_choices, null=True)
    item_968_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_968 = models.CharField(max_length=15, choices=item_968_choices, null=True)
    item_970_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_970 = models.CharField(max_length=15, choices=item_970_choices, null=True)
    item_972_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_972 = models.CharField(max_length=15, choices=item_972_choices, null=True)
    item_974_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_974 = models.CharField(max_length=15, choices=item_974_choices, null=True)
    item_976_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_976 = models.CharField(max_length=15, choices=item_976_choices, null=True)
    item_978_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_978 = models.CharField(max_length=15, choices=item_978_choices, null=True)
    item_980_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_980 = models.CharField(max_length=15, choices=item_980_choices, null=True)
    item_982_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_982 = models.CharField(max_length=15, choices=item_982_choices, null=True)
    item_984_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_984 = models.CharField(max_length=15, choices=item_984_choices, null=True)
    item_986_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_986 = models.CharField(max_length=15, choices=item_986_choices, null=True)
    item_988_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_988 = models.CharField(max_length=15, choices=item_988_choices, null=True)
    item_990_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_990 = models.CharField(max_length=15, choices=item_990_choices, null=True)
    item_992_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_992 = models.CharField(max_length=15, choices=item_992_choices, null=True)
    item_994_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_994 = models.CharField(max_length=15, choices=item_994_choices, null=True)
    item_996_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_996 = models.CharField(max_length=15, choices=item_996_choices, null=True)
    item_998_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_998 = models.CharField(max_length=15, choices=item_998_choices, null=True)
    item_1000_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1000 = models.CharField(max_length=15, choices=item_1000_choices, null=True)
    item_1002_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1002 = models.CharField(max_length=15, choices=item_1002_choices, null=True)
    item_1004_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1004 = models.CharField(max_length=15, choices=item_1004_choices, null=True)
    item_1006_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1006 = models.CharField(max_length=15, choices=item_1006_choices, null=True)
    item_1008_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1008 = models.CharField(max_length=15, choices=item_1008_choices, null=True)
    item_1010_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1010 = models.CharField(max_length=15, choices=item_1010_choices, null=True)
    item_1012_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1012 = models.CharField(max_length=15, choices=item_1012_choices, null=True)
    item_1014_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1014 = models.CharField(max_length=15, choices=item_1014_choices, null=True)
    item_1016_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1016 = models.CharField(max_length=15, choices=item_1016_choices, null=True)
    item_1018_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1018 = models.CharField(max_length=15, choices=item_1018_choices, null=True)
    item_1020_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1020 = models.CharField(max_length=15, choices=item_1020_choices, null=True)
    item_1022_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1022 = models.CharField(max_length=15, choices=item_1022_choices, null=True)
    item_1024_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1024 = models.CharField(max_length=15, choices=item_1024_choices, null=True)
    item_1026_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1026 = models.CharField(max_length=15, choices=item_1026_choices, null=True)
    item_1028_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1028 = models.CharField(max_length=15, choices=item_1028_choices, null=True)
    item_1030_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1030 = models.CharField(max_length=15, choices=item_1030_choices, null=True)
    item_1032_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1032 = models.CharField(max_length=15, choices=item_1032_choices, null=True)
    item_1034_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1034 = models.CharField(max_length=15, choices=item_1034_choices, null=True)
    item_1036_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1036 = models.CharField(max_length=15, choices=item_1036_choices, null=True)
    item_1038_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1038 = models.CharField(max_length=15, choices=item_1038_choices, null=True)
    item_1040_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1040 = models.CharField(max_length=15, choices=item_1040_choices, null=True)
    item_1042_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1042 = models.CharField(max_length=15, choices=item_1042_choices, null=True)
    item_1044_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1044 = models.CharField(max_length=15, choices=item_1044_choices, null=True)
    item_1046_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1046 = models.CharField(max_length=15, choices=item_1046_choices, null=True)
    item_1048_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1048 = models.CharField(max_length=15, choices=item_1048_choices, null=True)
    item_1050_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1050 = models.CharField(max_length=15, choices=item_1050_choices, null=True)
    item_1052_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1052 = models.CharField(max_length=15, choices=item_1052_choices, null=True)
    item_1054_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1054 = models.CharField(max_length=15, choices=item_1054_choices, null=True)
    item_1056_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1056 = models.CharField(max_length=15, choices=item_1056_choices, null=True)
    item_1058_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1058 = models.CharField(max_length=15, choices=item_1058_choices, null=True)
    item_1060_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1060 = models.CharField(max_length=15, choices=item_1060_choices, null=True)
    item_1062_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1062 = models.CharField(max_length=15, choices=item_1062_choices, null=True)
    item_1064_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1064 = models.CharField(max_length=15, choices=item_1064_choices, null=True)
    item_1066_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1066 = models.CharField(max_length=15, choices=item_1066_choices, null=True)
    item_1068_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1068 = models.CharField(max_length=15, choices=item_1068_choices, null=True)
    item_1070_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1070 = models.CharField(max_length=15, choices=item_1070_choices, null=True)
    item_1072_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1072 = models.CharField(max_length=15, choices=item_1072_choices, null=True)
    item_1074_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1074 = models.CharField(max_length=15, choices=item_1074_choices, null=True)
    item_1076_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1076 = models.CharField(max_length=15, choices=item_1076_choices, null=True)
    item_1078_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1078 = models.CharField(max_length=15, choices=item_1078_choices, null=True)
    item_1080_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1080 = models.CharField(max_length=15, choices=item_1080_choices, null=True)
    item_1082_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1082 = models.CharField(max_length=15, choices=item_1082_choices, null=True)
    item_1084_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1084 = models.CharField(max_length=15, choices=item_1084_choices, null=True)
    item_1086_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1086 = models.CharField(max_length=15, choices=item_1086_choices, null=True)
    item_1088_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1088 = models.CharField(max_length=15, choices=item_1088_choices, null=True)
    item_1090_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1090 = models.CharField(max_length=15, choices=item_1090_choices, null=True)
    item_1092_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1092 = models.CharField(max_length=15, choices=item_1092_choices, null=True)
    item_1094_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1094 = models.CharField(max_length=15, choices=item_1094_choices, null=True)
    item_1096_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1096 = models.CharField(max_length=15, choices=item_1096_choices, null=True)
    item_1098_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1098 = models.CharField(max_length=15, choices=item_1098_choices, null=True)
    item_1100_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1100 = models.CharField(max_length=15, choices=item_1100_choices, null=True)
    item_1102_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1102 = models.CharField(max_length=15, choices=item_1102_choices, null=True)
    item_1104_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1104 = models.CharField(max_length=15, choices=item_1104_choices, null=True)
    item_1106_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1106 = models.CharField(max_length=15, choices=item_1106_choices, null=True)
    item_1108_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1108 = models.CharField(max_length=15, choices=item_1108_choices, null=True)
    item_1110_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1110 = models.CharField(max_length=15, choices=item_1110_choices, null=True)
    item_1112_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1112 = models.CharField(max_length=15, choices=item_1112_choices, null=True)
    item_1114_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1114 = models.CharField(max_length=15, choices=item_1114_choices, null=True)
    item_1116_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1116 = models.CharField(max_length=15, choices=item_1116_choices, null=True)
    item_1118_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1118 = models.CharField(max_length=15, choices=item_1118_choices, null=True)
    item_1120_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1120 = models.CharField(max_length=15, choices=item_1120_choices, null=True)
    item_1122_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1122 = models.CharField(max_length=15, choices=item_1122_choices, null=True)
    item_1124_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1124 = models.CharField(max_length=15, choices=item_1124_choices, null=True)
    item_1126_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1126 = models.CharField(max_length=15, choices=item_1126_choices, null=True)
    item_1128_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1128 = models.CharField(max_length=15, choices=item_1128_choices, null=True)
    item_1132_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1132 = models.CharField(max_length=15, choices=item_1132_choices, null=True)
    item_1134_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1134 = models.CharField(max_length=15, choices=item_1134_choices, null=True)
    item_1136_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1136 = models.CharField(max_length=15, choices=item_1136_choices, null=True)
    item_1138_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1138 = models.CharField(max_length=15, choices=item_1138_choices, null=True)
    item_1140_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1140 = models.CharField(max_length=15, choices=item_1140_choices, null=True)
    item_1142_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1142 = models.CharField(max_length=15, choices=item_1142_choices, null=True)
    item_1146_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1146 = models.CharField(max_length=15, choices=item_1146_choices, null=True)
    item_1149_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1149 = models.CharField(max_length=15, choices=item_1149_choices, null=True)
    item_1151_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1151 = models.CharField(max_length=15, choices=item_1151_choices, null=True)
    item_1152_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1152 = models.CharField(max_length=15, choices=item_1152_choices, null=True)
    item_1154_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1154 = models.CharField(max_length=15, choices=item_1154_choices, null=True)
    item_1156_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1156 = models.CharField(max_length=15, choices=item_1156_choices, null=True)
    item_1158_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1158 = models.CharField(max_length=15, choices=item_1158_choices, null=True)
    item_1160_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1160 = models.CharField(max_length=15, choices=item_1160_choices, null=True)
    item_1162_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1162 = models.CharField(max_length=15, choices=item_1162_choices, null=True)
    item_1164_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1164 = models.CharField(max_length=15, choices=item_1164_choices, null=True)
    item_1166_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1166 = models.CharField(max_length=15, choices=item_1166_choices, null=True)
    item_1168_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1168 = models.CharField(max_length=15, choices=item_1168_choices, null=True)
    item_1170_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1170 = models.CharField(max_length=15, choices=item_1170_choices, null=True)
    item_1171_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1171 = models.CharField(max_length=15, choices=item_1171_choices, null=True)
    item_1172_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1172 = models.CharField(max_length=15, choices=item_1172_choices, null=True)
    item_1173_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1173 = models.CharField(max_length=15, choices=item_1173_choices, null=True)
    item_1174_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1174 = models.CharField(max_length=15, choices=item_1174_choices, null=True)
    item_1175_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1175 = models.CharField(max_length=15, choices=item_1175_choices, null=True)
    item_1176_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1176 = models.CharField(max_length=15, choices=item_1176_choices, null=True)
    item_1177_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1177 = models.CharField(max_length=15, choices=item_1177_choices, null=True)
    item_1178_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1178 = models.CharField(max_length=15, choices=item_1178_choices, null=True)
    item_1179_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1179 = models.CharField(max_length=15, choices=item_1179_choices, null=True)
    item_1180_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1180 = models.CharField(max_length=15, choices=item_1180_choices, null=True)
    item_1181_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1181 = models.CharField(max_length=15, choices=item_1181_choices, null=True)
    item_1182_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1182 = models.CharField(max_length=15, choices=item_1182_choices, null=True)
    item_1183_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1183 = models.CharField(max_length=15, choices=item_1183_choices, null=True)
    item_1184_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1184 = models.CharField(max_length=15, choices=item_1184_choices, null=True)
    item_1185_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1185 = models.CharField(max_length=15, choices=item_1185_choices, null=True)
    item_1186_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1186 = models.CharField(max_length=15, choices=item_1186_choices, null=True)
    item_1187_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1187 = models.CharField(max_length=15, choices=item_1187_choices, null=True)
    item_1188_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1188 = models.CharField(max_length=15, choices=item_1188_choices, null=True)
    item_1189_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1189 = models.CharField(max_length=15, choices=item_1189_choices, null=True)
    item_1190_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1190 = models.CharField(max_length=15, choices=item_1190_choices, null=True)
    item_1191_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1191 = models.CharField(max_length=15, choices=item_1191_choices, null=True)
    item_1192_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1192 = models.CharField(max_length=15, choices=item_1192_choices, null=True)
    item_1193_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1193 = models.CharField(max_length=15, choices=item_1193_choices, null=True)
    item_1194_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1194 = models.CharField(max_length=15, choices=item_1194_choices, null=True)
    item_1195_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1195 = models.CharField(max_length=15, choices=item_1195_choices, null=True)
    item_1197_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1197 = models.CharField(max_length=15, choices=item_1197_choices, null=True)
    item_1199_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1199 = models.CharField(max_length=15, choices=item_1199_choices, null=True)
    item_1201_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1201 = models.CharField(max_length=15, choices=item_1201_choices, null=True)
    item_1203_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1203 = models.CharField(max_length=15, choices=item_1203_choices, null=True)
    item_1205_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1205 = models.CharField(max_length=15, choices=item_1205_choices, null=True)
    item_1207_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1207 = models.CharField(max_length=15, choices=item_1207_choices, null=True)
    item_1209_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1209 = models.CharField(max_length=15, choices=item_1209_choices, null=True)
    item_1211_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1211 = models.CharField(max_length=15, choices=item_1211_choices, null=True)
    item_1213_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1213 = models.CharField(max_length=15, choices=item_1213_choices, null=True)
    item_1215_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1215 = models.CharField(max_length=15, choices=item_1215_choices, null=True)
    item_1217_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1217 = models.CharField(max_length=15, choices=item_1217_choices, null=True)
    item_1219_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1219 = models.CharField(max_length=15, choices=item_1219_choices, null=True)
    item_1221_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1221 = models.CharField(max_length=15, choices=item_1221_choices, null=True)
    item_1223_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1223 = models.CharField(max_length=15, choices=item_1223_choices, null=True)
    item_1225_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1225 = models.CharField(max_length=15, choices=item_1225_choices, null=True)
    item_1227_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1227 = models.CharField(max_length=15, choices=item_1227_choices, null=True)
    item_1229_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1229 = models.CharField(max_length=15, choices=item_1229_choices, null=True)
    item_1231_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1231 = models.CharField(max_length=15, choices=item_1231_choices, null=True)
    item_1233_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1233 = models.CharField(max_length=15, choices=item_1233_choices, null=True)
    item_1235_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1235 = models.CharField(max_length=15, choices=item_1235_choices, null=True)
    item_1237_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1237 = models.CharField(max_length=15, choices=item_1237_choices, null=True)
    item_1239_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1239 = models.CharField(max_length=15, choices=item_1239_choices, null=True)
    item_1241_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1241 = models.CharField(max_length=15, choices=item_1241_choices, null=True)
    item_1243_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1243 = models.CharField(max_length=15, choices=item_1243_choices, null=True)
    item_1245_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1245 = models.CharField(max_length=15, choices=item_1245_choices, null=True)
    item_1247_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1247 = models.CharField(max_length=15, choices=item_1247_choices, null=True)
    item_1249_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1249 = models.CharField(max_length=15, choices=item_1249_choices, null=True)
    item_1251_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1251 = models.CharField(max_length=15, choices=item_1251_choices, null=True)
    item_1253_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1253 = models.CharField(max_length=15, choices=item_1253_choices, null=True)
    item_1255_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1255 = models.CharField(max_length=15, choices=item_1255_choices, null=True)
    item_1257_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1257 = models.CharField(max_length=15, choices=item_1257_choices, null=True)
    item_1259_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1259 = models.CharField(max_length=15, choices=item_1259_choices, null=True)
    item_1261_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1261 = models.CharField(max_length=15, choices=item_1261_choices, null=True)
    item_1263_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1263 = models.CharField(max_length=15, choices=item_1263_choices, null=True)
    item_1265_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1265 = models.CharField(max_length=15, choices=item_1265_choices, null=True)
    item_1267_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1267 = models.CharField(max_length=15, choices=item_1267_choices, null=True)
    item_1269_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1269 = models.CharField(max_length=15, choices=item_1269_choices, null=True)
    item_1271_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1271 = models.CharField(max_length=15, choices=item_1271_choices, null=True)
    item_1274_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1274 = models.CharField(max_length=15, choices=item_1274_choices, null=True)
    item_1276_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1276 = models.CharField(max_length=15, choices=item_1276_choices, null=True)
    item_1278_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1278 = models.CharField(max_length=15, choices=item_1278_choices, null=True)
    item_1280_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1280 = models.CharField(max_length=15, choices=item_1280_choices, null=True)
    item_1282_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1282 = models.CharField(max_length=15, choices=item_1282_choices, null=True)
    item_1284_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1284 = models.CharField(max_length=15, choices=item_1284_choices, null=True)
    item_1286_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1286 = models.CharField(max_length=15, choices=item_1286_choices, null=True)
    item_1288_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1288 = models.CharField(max_length=15, choices=item_1288_choices, null=True)
    item_1290_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1290 = models.CharField(max_length=15, choices=item_1290_choices, null=True)
    item_1292_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1292 = models.CharField(max_length=15, choices=item_1292_choices, null=True)
    item_1294_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1294 = models.CharField(max_length=15, choices=item_1294_choices, null=True)
    item_1296_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1296 = models.CharField(max_length=15, choices=item_1296_choices, null=True)
    item_1298_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1298 = models.CharField(max_length=15, choices=item_1298_choices, null=True)
    item_1300_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1300 = models.CharField(max_length=15, choices=item_1300_choices, null=True)
    item_1301_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1301 = models.CharField(max_length=15, choices=item_1301_choices, null=True)
    item_1303_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1303 = models.CharField(max_length=15, choices=item_1303_choices, null=True)
    item_1305_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1305 = models.CharField(max_length=15, choices=item_1305_choices, null=True)
    item_1307_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1307 = models.CharField(max_length=15, choices=item_1307_choices, null=True)
    item_1309_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1309 = models.CharField(max_length=15, choices=item_1309_choices, null=True)
    item_1311_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1311 = models.CharField(max_length=15, choices=item_1311_choices, null=True)
    item_1313_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1313 = models.CharField(max_length=15, choices=item_1313_choices, null=True)
    item_1315_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1315 = models.CharField(max_length=15, choices=item_1315_choices, null=True)
    item_1316_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1316 = models.CharField(max_length=15, choices=item_1316_choices, null=True)
    item_1318_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1318 = models.CharField(max_length=15, choices=item_1318_choices, null=True)
    item_1320_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1320 = models.CharField(max_length=15, choices=item_1320_choices, null=True)
    item_1322_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1322 = models.CharField(max_length=15, choices=item_1322_choices, null=True)
    item_1324_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1324 = models.CharField(max_length=15, choices=item_1324_choices, null=True)
    item_1326_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1326 = models.CharField(max_length=15, choices=item_1326_choices, null=True)
    item_1328_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1328 = models.CharField(max_length=15, choices=item_1328_choices, null=True)
    item_1330_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1330 = models.CharField(max_length=15, choices=item_1330_choices, null=True)
    item_1332_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1332 = models.CharField(max_length=15, choices=item_1332_choices, null=True)
    item_1334_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1334 = models.CharField(max_length=15, choices=item_1334_choices, null=True)
    item_1336_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1336 = models.CharField(max_length=15, choices=item_1336_choices, null=True)
    item_1337_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1337 = models.CharField(max_length=15, choices=item_1337_choices, null=True)
    item_1338_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1338 = models.CharField(max_length=15, choices=item_1338_choices, null=True)
    item_1340_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1340 = models.CharField(max_length=15, choices=item_1340_choices, null=True)
    item_1342_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1342 = models.CharField(max_length=15, choices=item_1342_choices, null=True)
    item_1344_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1344 = models.CharField(max_length=15, choices=item_1344_choices, null=True)
    item_1346_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1346 = models.CharField(max_length=15, choices=item_1346_choices, null=True)
    item_1348_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1348 = models.CharField(max_length=15, choices=item_1348_choices, null=True)
    item_1350_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1350 = models.CharField(max_length=15, choices=item_1350_choices, null=True)
    item_1352_choices = [('produces', 'produces'), ("doesn't produce", "doesn't produce")]
    item_1352 = models.CharField(max_length=15, choices=item_1352_choices, null=True)
