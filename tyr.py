def calculate_risk(sex, age, cho, smo, hdl, sbp, med):
    """Calculate risk based on NIH Framingham model."""

    # --- Age points ---
    if sex == 'F':
        if 20 <= age <= 34: age_points = -7
        elif 35 <= age <= 39: age_points = -3
        elif 40 <= age <= 44: age_points = 0
        elif 45 <= age <= 49: age_points = 3
        elif 50 <= age <= 54: age_points = 6
        elif 55 <= age <= 59: age_points = 8
        elif 60 <= age <= 64: age_points = 10
        elif 65 <= age <= 69: age_points = 12
        else: age_points = 16
    else:  # Male
        if 20 <= age <= 34: age_points = -9
        elif 35 <= age <= 39: age_points = -4
        elif 40 <= age <= 44: age_points = 0
        elif 45 <= age <= 49: age_points = 3
        elif 50 <= age <= 54: age_points = 6
        elif 55 <= age <= 59: age_points = 8
        elif 60 <= age <= 64: age_points = 10
        elif 65 <= age <= 69: age_points = 11
        else: age_points = 13

    # --- Total cholesterol points ---
    if sex == 'F':
        if age < 40:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 4
            elif cho < 240: cho_points = 8
            elif cho < 280: cho_points = 11
            else: cho_points = 13
        elif age < 50:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 3
            elif cho < 240: cho_points = 6
            elif cho < 280: cho_points = 8
            else: cho_points = 10
        elif age < 60:
            cho_points = 0
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 2
            elif cho < 240: cho_points = 4
            elif cho < 280: cho_points = 5
            else: cho_points = 7
        elif age < 70:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 1
            elif cho < 240: cho_points = 2
            elif cho < 280: cho_points = 3
            else: cho_points = 4
        else:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 1
            elif cho < 240: cho_points = 1
            elif cho < 280: cho_points = 2
            else: cho_points = 2
    else:  # Male
        if age < 40:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 4
            elif cho < 240: cho_points = 7
            elif cho < 280: cho_points = 9
            else: cho_points = 11
        elif age < 50:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 3
            elif cho < 240: cho_points = 5
            elif cho < 280: cho_points = 6
            else: cho_points = 8
        elif age < 60:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 2
            elif cho < 240: cho_points = 3
            elif cho < 280: cho_points = 4
            else: cho_points = 5
        elif age < 70:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 1
            elif cho < 240: cho_points = 1
            elif cho < 280: cho_points = 2
            else: cho_points = 3
        else:
            cho_points = 0 
            if cho < 160: cho_points = 0
            elif cho < 200: cho_points = 0
            elif cho < 240: cho_points = 1
            elif cho < 280: cho_points = 1
            else: cho_points = 2

    # --- HDL points ---
    hdl_points = -1 
    if hdl >= 60: hdl_points = -1
    elif hdl >= 50: hdl_points = 0
    elif hdl >= 40: hdl_points = 1
    else: hdl_points = 2

    # --- Smoking points ---
    if smo == 'Y':
        if sex == 'F':
            smo_points = 3 
            if age < 40: smo_points = 9
            elif age < 50: smo_points = 7
            elif age < 60: smo_points = 4
            elif age < 70: smo_points = 2
            else: smo_points = 1
        else:  # Male
            smo_points = 8
            if age < 40: smo_points = 8
            elif age < 50: smo_points = 5
            elif age < 60: smo_points = 3
            else: smo_points = 1
    else:
        smo_points = 0

    # --- Systolic BP points ---
    if sex == 'F':
        sbp_points = 0 
        if med == 'Y':
            if sbp < 120: sbp_points = 0
            elif sbp < 130: sbp_points = 3
            elif sbp < 140: sbp_points = 4
            elif sbp < 160: sbp_points = 5
            else: sbp_points = 6
        else:
            if sbp < 120: sbp_points = 0
            elif sbp < 130: sbp_points = 1
            elif sbp < 140: sbp_points = 2
            elif sbp < 160: sbp_points = 3
            else: sbp_points = 4
    else:
        if med == 'Y':
            sbp_points = 0 
            if sbp < 120: sbp_points = 0
            elif sbp < 130: sbp_points = 1
            elif sbp < 140: sbp_points = 2
            elif sbp < 160: sbp_points = 2
            else: sbp_points = 3
        else:
            sbp_points = 0 
            if sbp < 120: sbp_points = 0
            elif sbp < 130: sbp_points = 0
            elif sbp < 140: sbp_points = 1
            elif sbp < 160: sbp_points = 1
            else: sbp_points = 2

    total_points = age_points + cho_points + hdl_points + smo_points + sbp_points

    # --- Map total points to 10-year risk ---
    if sex == 'F':
        if total_points < 9: return "<1"
        elif total_points == 9: return "1"
        elif total_points == 10: return "1"
        elif total_points == 11: return "1"
        elif total_points == 12: return "1"
        elif total_points == 13: return "2"
        elif total_points == 14: return "2"
        elif total_points == 15: return "3"
        elif total_points == 16: return "4"
        elif total_points == 17: return "5"
        elif total_points == 18: return "6"
        elif total_points == 19: return "8"
        elif total_points == 20: return "11"
        elif total_points == 21: return "14"
        elif total_points == 22: return "17"
        elif total_points == 23: return "22"
        elif total_points == 24: return "27"
        else: return ">30"
    else:  # Male
        if total_points < 0: return "<1"
        elif total_points == 0: return "1"
        elif total_points == 1: return "1"
        elif total_points == 2: return "1"
        elif total_points == 3: return "1"
        elif total_points == 4: return "1"
        elif total_points == 5: return "2"
        elif total_points == 6: return "2"
        elif total_points == 7: return "3"
        elif total_points == 8: return "4"
        elif total_points == 9: return "5"
        elif total_points == 10: return "6"
        elif total_points == 11: return "8"
        elif total_points == 12: return "10"
        elif total_points == 13: return "12"
        elif total_points == 14: return "16"
        elif total_points == 15: return "20"
        elif total_points == 16: return "25"
        else: return ">30"

# --- Parse input string like "sex:M age:65 cho:280 smo:Y hdl:30 sbp:170 med:Y" ---
def parse_input(input_str):
    parts = input_str.split()
    data = {}
    for p in parts:
        k, v = p.split(':')
        if k in ['age', 'cho', 'hdl', 'sbp']:
            v = int(v)
        data[k] = v
    return data

# --- Main ---
if __name__ == "__main__":
    # Example input
    input_str = input() #"sex:M age:65 cho:280 smo:Y hdl:30 sbp:170 med:Y"
    data = parse_input(input_str)
    risk = calculate_risk(**data)
    print(f"10-year risk: {risk}%")
