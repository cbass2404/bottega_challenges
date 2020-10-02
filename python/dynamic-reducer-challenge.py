import math
import operator
from functools import reduce

liner, stroke, spm = 4, 10, (180 * .95)

sur_id, sur_depth = 20, 1500

inter_id, inter_depth = 15, 3500

pay_id, pay_depth = 10, 4000

bpm = (0.000243 * float(liner) * float(stroke))

sur_vol = (sur_id ** 2 / 1029.4) * sur_depth

inter_vol = (inter_id ** 2 / 1029.4) * inter_depth

pay_vol = (pay_id ** 2 / 1029.4) * pay_depth

tot_strk = round(reduce(lambda x, y: x/y, [reduce(lambda x, y: x+y, [sur_vol, inter_vol, pay_vol]), bpm]))

pump_hour = reduce(lambda x, y: x/y, [spm, 60])

print("Bottoms up is " + str(tot_strk) + " strokes. It will take " + str(pump_hour) + " hours.")