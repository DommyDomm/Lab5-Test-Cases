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
