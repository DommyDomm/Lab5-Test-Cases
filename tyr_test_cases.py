# Typical Cases
sex:F age:45 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1

# Edge Case above typical ranges
sex:M age:100 cho:290 smo:Y hdl:12 sbp:200 med:N out:>30
sex:F age:99 cho:300 smo:N hdl:30 sbp:180 med:Y out:>30

# Edge Case below typical ranges
sex:M age:12 cho:100 smo:N hdl:100 sbp:90 med:Y out:<1
sex:F age:16 cho:110 smo:Y hdl:99 sbp:100 med:N out:<1

# Edge Case for invalid inputs
sex:Female age:99 cho:300 smo:N hdl:30 sbp:180 med:Y out:>30
# F, N, N
# F, N, Y
# F, Y, N
# F, Y, Y
# M, N, N
# M, N, Y
# M, Y, N
# M, Y, Y
#different variations of yes or no / t/f
sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:40 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:40 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:40 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:40 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:40 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# different age ranges
# 20-34
# 35-39
# 40-44
# 45-49
# 50-54
# 55-59
# 60-64
# 65-69 
# 70-74 
# 75-79
#age 22
sex:F age:22 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 22
sex:F age:22 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:22 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:22 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:22 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:22 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:22 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:22 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 37
sex:F age:37 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 37
sex:F age:37 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:37 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:37 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:37 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:37 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:37 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:37 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 42 
sex:F age:42 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 42
sex:F age:42 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:42 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:22 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:42 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:42 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:42 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:42 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# 47 
sex:F age:47 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 47
sex:F age:47 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:47 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:47 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:47 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:47 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:47 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:47 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 53
sex:F age:53 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 53
sex:F age:53 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:53 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:53 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:53 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:53 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:53 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:53 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 56
sex:F age:56 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 61
sex:F age:56 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:56 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:56 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:56 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:56 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:56 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:56 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 61
sex:F age:61 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 61
sex:F age:61 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:61 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:61 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:61 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:61 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:61 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:61 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 66
sex:F age:66 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 66
sex:F age:66 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:66 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:66 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:66 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:66 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:66 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:66 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 72
sex:F age:72 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 72
sex:F age:72 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:72 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:72 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:72 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:72 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:72 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:72 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1
# age 76
sex:F age:76 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 # middle value age 76
sex:F age:76 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:76 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:F age:76 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

sex:M age:76 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:76 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:76 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
sex:M age:76 cho:105 smo:Y hdl:60 sbp:100 med:N out:<1

