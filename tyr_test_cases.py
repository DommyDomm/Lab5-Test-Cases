########## All age edge cases ##########
sex:M age:20 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:35 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:M age:45 cho:120 smo:N hdl:60 sbp:100 med:N out:1
sex:M age:55 cho:120 smo:N hdl:60 sbp:100 med:N out:3
sex:M age:65 cho:120 smo:N hdl:60 sbp:100 med:N out:6
sex:M age:75 cho:120 smo:N hdl:60 sbp:100 med:N out:10

sex:F age:20 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:35 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:45 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:55 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:65 cho:120 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:75 cho:120 smo:N hdl:60 sbp:100 med:N out:3

sex:F age:34 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:39 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:44 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:49 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:59 cho:120 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:64 cho:120 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:69 cho:120 smo:N hdl:60 sbp:100 med:N out:1
sex:F age:74 cho:120 smo:N hdl:60 sbp:100 med:N out:2
sex:F age:79 cho:120 smo:N hdl:60 sbp:100 med:N out:3

########## All levels of cholesterol ##########
# Non-smoker
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
## Edge Case
sex:F age:45 cho:105 smo:N hdl:60 sbp:100 med:N out:<1

sex:F age:45 cho:105 smo:N hdl:59 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:50 sbp:100 med:N out:<1

sex:F age:45 cho:105 smo:N hdl:49 sbp:100 med:N out:<1
sex:F age:45 cho:105 smo:N hdl:40 sbp:100 med:N out:<1

# Smoker
## Edge Case
sex:F age:45 cho:105 smo:Y hdl:60 sbp:100 med:N out:1

sex:F age:45 cho:105 smo:Y hdl:59 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:50 sbp:100 med:N out:1

sex:F age:45 cho:105 smo:Y hdl:49 sbp:100 med:N out:1
sex:F age:45 cho:105 smo:Y hdl:40 sbp:100 med:N out:1

############################################################################################

# Edge cases:( beginning and end of sub ranges)
# Sex: M, F
# Age: 20-79
# Cho: 160-280
# Smo: Y, N
# Hdl: 40-60
# Sbp: 120-160
# Med: Y, N
#edge for 34 and cho
sex:F age:34 cho:199 smo:N hdl:40 sbp:130 med:N out:<1 
sex:F age:34 cho:239 smo:N hdl:49 sbp:139 med:Y out:<1

sex:M age:34 cho:199 smo:N hdl:49 sbp:120 med:Y out:<1
sex:M age:34 cho:239 smo:Y hdl:40 sbp:129 med:Y out:4

sex:F age:59 cho:240 smo:N hdl:50 sbp:140 med:N out:4
sex:F age:55 cho:279 smo:N hdl:59 sbp:149 med:Y out:6

sex:M age:59 cho:279 smo:N hdl:59 sbp:140 med:Y out:16
sex:M age:55 cho:240 smo:Y hdl:50 sbp:159 med:Y out:>30


# Corner cases: (at the very end and beginning of every range)
# Sex: it
# Age: 100-10
# Cho:100
# Smo: sometimes
# Hdl:70-30
# Sbp:100-170
# Med: sometimes

# corner cases for age; 20, 79; and cho and F
sex:F age:20 cho:159 smo:N hdl:60 sbp:119 med:N out:<1 
sex:M age:20 cho:285 smo:Y hdl:30 sbp:165 med:Y out:20
sex:F age:79 cho:159 smo:N hdl:60 sbp:100 med:N out:3
sex:M age:79 cho:285 smo:Y hdl:30 sbp:165 med:Y out:>30

#corner cases for  hdl; 60, 39
sex:F age:20 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 
sex:M age:20 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 
sex:F age:34 cho:280 smo:Y hdl:39 sbp:160 med:Y out:22 
sex:M age:34 cho:280 smo:Y hdl:39 sbp:160 med:Y out:20

#corner cases sbp ; 119, 160
sex:M age:50 cho:105 smo:N hdl:60 sbp:119 med:N out:2 
sex:M age:50 cho:285 smo:Y hdl:30 sbp:160 med:Y out:>30


# Typical cases: ( most common or expected input )
# Sex: M, F
# Age: 22, 52, 67

# Cho:220,247
# Smo: Y, N
# Hdl: 54,45
# Sbp: 135,150
# Med: Y, N
##### Male #####
sex:M age:32 cho:220 smo:Y hdl:54 sbp:135 med:Y out:4
sex:M age:32 cho:220 smo:Y hdl:54 sbp:135 med:N out:3
sex:M age:32 cho:220 smo:Y hdl:54 sbp:150 med:Y out:4
sex:M age:32 cho:220 smo:Y hdl:45 sbp:135 med:Y out:5
sex:M age:32 cho:220 smo:N hdl:54 sbp:135 med:Y out:1
sex:M age:32 cho:247 smo:Y hdl:54 sbp:135 med:Y out:6

sex:M age:52 cho:220 smo:Y hdl:54 sbp:135 med:Y out:16
sex:M age:52 cho:220 smo:Y hdl:54 sbp:135 med:N out:12
sex:M age:52 cho:220 smo:Y hdl:54 sbp:150 med:Y out:16
sex:M age:52 cho:220 smo:Y hdl:45 sbp:135 med:Y out:20
sex:M age:52 cho:220 smo:N hdl:54 sbp:135 med:Y out:8
sex:M age:52 cho:247 smo:Y hdl:54 sbp:135 med:Y out:20

sex:M age:67 cho:220 smo:Y hdl:54 sbp:135 med:Y out:20
sex:M age:67 cho:220 smo:Y hdl:54 sbp:135 med:N out:16
sex:M age:67 cho:220 smo:Y hdl:54 sbp:150 med:Y out:20
sex:M age:67 cho:220 smo:Y hdl:45 sbp:135 med:Y out:25
sex:M age:67 cho:220 smo:N hdl:54 sbp:135 med:Y out:16
sex:M age:67 cho:247 smo:Y hdl:54 sbp:135 med:Y out:25

##### Female #####
sex:F age:32 cho:220 smo:Y hdl:54 sbp:135 med:Y out:2
sex:F age:32 cho:220 smo:Y hdl:54 sbp:135 med:N out:1
sex:F age:32 cho:220 smo:Y hdl:54 sbp:150 med:Y out:3
sex:F age:32 cho:220 smo:Y hdl:45 sbp:135 med:Y out:3
sex:F age:32 cho:220 smo:N hdl:54 sbp:135 med:Y out:<1
sex:F age:32 cho:247 smo:Y hdl:54 sbp:135 med:Y out:5

sex:F age:52 cho:220 smo:Y hdl:54 sbp:135 med:Y out:6
sex:F age:52 cho:220 smo:Y hdl:54 sbp:135 med:N out:4
sex:F age:52 cho:220 smo:Y hdl:54 sbp:150 med:Y out:8
sex:F age:52 cho:220 smo:Y hdl:45 sbp:135 med:Y out:8
sex:F age:52 cho:220 smo:N hdl:54 sbp:135 med:Y out:2
sex:F age:52 cho:247 smo:Y hdl:54 sbp:135 med:Y out:8

sex:F age:67 cho:220 smo:Y hdl:54 sbp:135 med:Y out:11
sex:F age:67 cho:220 smo:Y hdl:54 sbp:135 med:N out:6
sex:F age:67 cho:220 smo:Y hdl:54 sbp:150 med:Y out:14
sex:F age:67 cho:220 smo:Y hdl:45 sbp:135 med:Y out:14
sex:F age:67 cho:220 smo:N hdl:54 sbp:135 med:Y out:6
sex:F age:67 cho:247 smo:Y hdl:54 sbp:135 med:Y out:14


#special cases (statistically improbable ex; a healthy 70yo vs a really unhealthy 20 yo)
##can use these to create different combinations####
#test cases for age range/leah
#age 20 low all values
sex:F age:20 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 
sex:F age:20 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:20 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1

sex:M age:20 cho:105 smo:N hdl:60 sbp:100 med:N out:<1 
sex:M age:20 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:M age:20 cho:105 smo:Y hdl:60 sbp:100 med:Y out:<1
####correct###^

#mid range all values
sex:F age:20 cho:200 smo:N hdl:42 sbp:130 med:N out:<1 
sex:F age:20 cho:200 smo:N hdl:42 sbp:130 med:Y out:<1
sex:F age:20 cho:200 smo:Y hdl:42 sbp:130 med:Y out:3 

sex:M age:20 cho:200 smo:N hdl:42 sbp:130 med:N out:1
sex:M age:20 cho:200 smo:N hdl:42 sbp:130 med:Y out:1 
sex:M age:20 cho:200 smo:Y hdl:42 sbp:130 med:Y out:5 
####correct####

#end range
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

#ages 50 mid range
sex:F age:50 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:50 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:50 cho:105 smo:Y hdl:60 sbp:100 med:Y out:1 

sex:M age:50 cho:105 smo:N hdl:60 sbp:100 med:N out:2 
sex:M age:50 cho:105 smo:N hdl:60 sbp:100 med:Y out:2
sex:M age:50 cho:105 smo:Y hdl:60 sbp:100 med:Y out:4 
#####correct###
# mid range values
sex:F age:50 cho:200 smo:N hdl:42 sbp:130 med:N out:2
sex:F age:50 cho:200 smo:N hdl:42 sbp:130 med:Y out:3
sex:F age:50 cho:200 smo:Y hdl:42 sbp:130 med:Y out:8

sex:M age:50 cho:200 smo:N hdl:42 sbp:130 med:N out:8
sex:M age:50 cho:200 smo:N hdl:42 sbp:130 med:Y out:10
sex:M age:50 cho:200 smo:Y hdl:42 sbp:130 med:Y out:20

###correct#####
sex:F age:34 cho:280 smo:N hdl:39 sbp:160 med:N out:1 
sex:F age:34 cho:280 smo:N hdl:39 sbp:160 med:Y out:2 
sex:F age:34 cho:280 smo:Y hdl:39 sbp:160 med:Y out:22 

sex:M age:34 cho:280 smo:N hdl:39 sbp:160 med:N out:2
sex:M age:34 cho:280 smo:N hdl:39 sbp:160 med:Y out:3
sex:M age:34 cho:280 smo:Y hdl:39 sbp:160 med:Y out:20
#correct^
#ages 50 M and F
sex:F age:50 cho:105 smo:N hdl:60 sbp:100 med:N out:<1
sex:F age:50 cho:105 smo:N hdl:60 sbp:100 med:Y out:<1
sex:F age:50 cho:105 smo:Y hdl:60 sbp:100 med:Y out:1 

sex:M age:50 cho:105 smo:N hdl:60 sbp:100 med:N out:2 
sex:M age:50 cho:105 smo:N hdl:60 sbp:100 med:Y out:2
sex:M age:50 cho:105 smo:Y hdl:60 sbp:100 med:Y out:4 
#correct^
# mid age 50(beginning range)
sex:F age:50 cho:200 smo:N hdl:42 sbp:130 med:N out:2
sex:F age:50 cho:200 smo:N hdl:42 sbp:130 med:Y out:3
sex:F age:50 cho:200 smo:Y hdl:42 sbp:130 med:Y out:8

sex:M age:50 cho:200 smo:N hdl:42 sbp:130 med:N out:8
sex:M age:50 cho:200 smo:N hdl:42 sbp:130 med:Y out:10
sex:M age:50 cho:200 smo:Y hdl:42 sbp:130 med:Y out:20
###correct###^

#end of range for all values
sex:F age:50 cho:285 smo:N hdl:30 sbp:165 med:N out:8
sex:F age:50 cho:285 smo:N hdl:30 sbp:165 med:Y out:14
sex:F age:50 cho:285 smo:Y hdl:30 sbp:165 med:Y out:>30 

sex:M age:50 cho:285 smo:N hdl:30 sbp:165 med:N out:20
sex:M age:50 cho:285 smo:N hdl:30 sbp:165 med:Y out:25
sex:M age:50 cho:285 smo:Y hdl:30 sbp:165 med:Y out:>30
####correctttt######
#ages 79 M and F
# beginning of range
sex:F age:79 cho:105 smo:N hdl:60 sbp:100 med:N out:3
sex:F age:79 cho:105 smo:N hdl:60 sbp:100 med:Y out:3
sex:F age:79 cho:105 smo:Y hdl:60 sbp:100 med:Y out:4

sex:M age:79 cho:105 smo:N hdl:60 sbp:100 med:N out:10 
sex:M age:79 cho:105 smo:N hdl:60 sbp:100 med:Y out:10
sex:M age:79 cho:105 smo:Y hdl:60 sbp:100 med:Y out:12
####correct####
# mid range
# mid age 79
sex:F age:79 cho:200 smo:N hdl:42 sbp:130 med:N out:11 
sex:F age:79 cho:200 smo:N hdl:42 sbp:130 med:Y out:17
sex:F age:79 cho:200 smo:Y hdl:42 sbp:130 med:Y out:22

sex:M age:79 cho:200 smo:N hdl:42 sbp:130 med:N out:20
sex:M age:79 cho:200 smo:N hdl:42 sbp:130 med:Y out:25
sex:M age:79 cho:200 smo:Y hdl:42 sbp:130 med:Y out:>30
###correct####

#end of range 
sex:F age:79 cho:285 smo:N hdl:30 sbp:165 med:N out:27
sex:F age:79 cho:285 smo:N hdl:30 sbp:165 med:Y out:>30
sex:F age:79 cho:285 smo:Y hdl:30 sbp:165 med:Y out:>30 

sex:M age:79 cho:285 smo:N hdl:30 sbp:165 med:N out:>30
sex:M age:79 cho:285 smo:N hdl:30 sbp:165 med:Y out:>30
sex:M age:79 cho:285 smo:Y hdl:30 sbp:165 med:Y out:>30
###correct###
