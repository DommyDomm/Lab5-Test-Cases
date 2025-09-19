########## All levels of cholesterol ##########

# Non-smoker
## Typical Case
sex:F age:45 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:180 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:220 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:260 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:45 cho:300 smo:N hdl:60 sbp:100 med:N out:1

## Edge Case
sex:F age:45 cho:159 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:160 smo:N hdl:60 sbp:100 med:N out:<1

sex:F age:45 cho:199 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:200 smo:N hdl:60 sbp:100 med:N out:<1

sex:F age:45 cho:239 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:240 smo:N hdl:60 sbp:100 med:N out:1

sex:F age:45 cho:279 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:45 cho:280 smo:N hdl:60 sbp:100 med:N out:1


# Smoker
## Typical Case
sex:F age:45 cho:120 smo:Y hdl:60 sbp:100 med:N out:1
sex:F age:45 cho:180 smo:Y hdl:60 sbp:100 med:N out:1
sex:F age:45 cho:220 smo:Y hdl:60 sbp:100 med:N out:3
sex:F age:45 cho:260 smo:Y hdl:60 sbp:100 med:N out:5
sex:F age:45 cho:300 smo:Y hdl:60 sbp:100 med:N out:8

## Edge Case
sex:F age:45 cho:159 smo:Y hdl:60 sbp:100 med:N out:1
sex:F age:45 cho:160 smo:Y hdl:60 sbp:100 med:N out:1

sex:F age:45 cho:199 smo:Y hdl:60 sbp:100 med:N out:1
sex:F age:45 cho:200 smo:Y hdl:60 sbp:100 med:N out:3

sex:F age:45 cho:239 smo:Y hdl:60 sbp:100 med:N out:3
sex:F age:45 cho:240 smo:Y hdl:60 sbp:100 med:N out:5

sex:F age:45 cho:279 smo:Y hdl:60 sbp:100 med:N out:5
sex:F age:45 cho:280 smo:Y hdl:60 sbp:100 med:N out:8

########## All levels of HDL ##########

# Non-Smoker
## Typical Case
sex:F age:45 cho:105 smo:N hdl:65 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:55 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:45 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:30 sbp:100 med:N out:<1

## Edge Case
sex:F age:45 cho:105 smo:N hdl:60 sbp:100 med:N out:<1

sex:F age:45 cho:105 smo:N hdl:59 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:50 sbp:100 med:N out:<1

sex:F age:45 cho:105 smo:N hdl:49 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:40 sbp:100 med:N out:<1


# Smoker
## Typical Case
sex:F age:45 cho:105 smo:Y hdl:65 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:55 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:45 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:30 sbp:100 med:N out:1

## Edge Case
sex:F age:45 cho:105 smo:Y hdl:60 sbp:100 med:N out:1

sex:F age:45 cho:105 smo:Y hdl:59 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:50 sbp:100 med:N out:1

sex:F age:45 cho:105 smo:Y hdl:49 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:40 sbp:100 med:N out:1

#test cases for age range/leah
sex:F age:20 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 
sex:F age:20 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:20 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1

sex:M age:20 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 
sex:M age:20 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:20 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
####correct###^

# mid age 20
sex:F age:20 cho:200 smo:N hdl:42 sbp:130 med:N out:<1 
sex:F age:20 cho:200 smo:N hdl:42 sbp:130 med:Y out:<1
sex:F age:20 cho:200 smo:Y hdl:42 sbp:130 med:Y out:3 

sex:M age:20 cho:200 smo:N hdl:42 sbp:130 med:N out:1
sex:M age:20 cho:200 smo:N hdl:42 sbp:130 med:Y out:1 
sex:M age:20 cho:200 smo:Y hdl:42 sbp:130 med:Y out:5 
####correct####

#edge
sex:F age:20 cho:285 smo:N hdl:30 sbp:165 med:N out:1 
sex:F age:20 cho:285 smo:N hdl:30 sbp:165 med:Y out:2 
sex:F age:20 cho:285 smo:Y hdl:30 sbp:165 med:Y out:22 

sex:M age:20 cho:285 smo:N hdl:30 sbp:165 med:N out:2
sex:M age:20 cho:285 smo:N hdl:30 sbp:165 med:Y out:3
sex:M age:20 cho:285 smo:Y hdl:30 sbp:165 med:Y out:20

####correct###
#edge of range#
sex:F age:34 cho:280 smo:N hdl:39 sbp:160 med:N out:1 
sex:F age:34 cho:280 smo:N hdl:39 sbp:160 med:Y out:2 
sex:F age:34 cho:280 smo:Y hdl:39 sbp:160 med:Y out:22 

sex:M age:34 cho:280 smo:N hdl:39 sbp:160 med:N out:2
sex:M age:34 cho:280 smo:N hdl:39 sbp:160 med:Y out:3
sex:M age:34 cho:280 smo:Y hdl:39 sbp:160 med:Y out:20
###correct####

#ages 50 M and F/age 50 b of range, 60 edge
sex:F age:50 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:50 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:50 cho:105 smo:Y hdl:60 sbp:100 med:Y out:1 

sex:M age:50 cho:105 smo:N hdl:60 sbp:100 med:N out:2 
sex:M age:50 cho:105 smo:N hdl:60 sbp:100 med:Y out:2
sex:M age:50 cho:105 smo:Y hdl:60 sbp:100 med:Y out:4 
#####correct###
# mid age 50(beginng range) 
sex:F age:50 cho:200 smo:N hdl:42 sbp:130 med:N out:2
sex:F age:50 cho:200 smo:N hdl:42 sbp:130 med:Y out:3
sex:F age:50 cho:200 smo:Y hdl:42 sbp:130 med:Y out:8

sex:M age:50 cho:200 smo:N hdl:42 sbp:130 med:N out:8
sex:M age:50 cho:200 smo:N hdl:42 sbp:130 med:Y out:10
sex:M age:50 cho:200 smo:Y hdl:42 sbp:130 med:Y out:20
###correct#####
























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


