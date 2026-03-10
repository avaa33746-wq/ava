# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?
# --- Answers to Questions ---

# 1) Write a function that uses a loop to print the name of each star.
def print_star_names():
    print("--- Question 1: Star Names ---")
    for star in targets:
        print(star)
    print()

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_stars_with_spectral_type():
    print("--- Question 2: Names and Spectral Types ---")
    for star, info in targets.items():
        print(f"{star}: {info['Spectral Type']}")
    print()

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_dim_stars():
    print("--- Question 3: Magnitudes > 0.1 (Dimmer stars) ---")
    for star, info in targets.items():
        if info["Magnitude"] > 0.1:
            print(f"{star} has a magnitude of {info['Magnitude']}")
    print()

# 4) Look up another target, add all the necessary information to the targets list.
# Adding Arcturus (Coordinates from Stellarcatalog.com)
targets["Arcturus"] = {
    "RA": "14h 15m 39.7s",
    "Dec": "+19° 10′ 56″",
    "Magnitude": -0.05,
    "Spectral Type": "K1.5 III"
}

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_specific_star():
    print("--- Question 5: Brightest star closest to 20° Dec ---")
    target_dec = 20.0
    best_star = None
    min_diff = float('inf')
    
    for star, info in targets.items():
        # Simple extraction of the degree part from the Dec string
        # This handles strings like "+38° 47' 01\"" or "−16° 42' 58\""
        clean_dec = info["Dec"].replace("−", "-").replace("+", "")
        deg = float(clean_dec.split('°')[0])
        
        diff = abs(deg - target_dec)
        
        # If it's closer than the previous best, update it
        if diff < min_diff:
            min_diff = diff
            best_star = star
        # If the distance is the same, pick the brightest (lowest magnitude)
        elif diff == min_diff:
            if info["Magnitude"] < targets[best_star]["Magnitude"]:
                best_star = star
                
    print(f"The star closest to 20° is {best_star} (Dec: {targets[best_star]['Dec']})")
    print()

# 6) What is your favorite constellation?
def favorite_constellation():
    print("--- Question 6: Favorite Constellation ---")
    print("My favorite constellation is Orion, because it's easy to spot and contains Rigel and Betelgeuse!")

# --- Execute all functions ---
print_star_names()
print_stars_with_spectral_type()
find_dim_stars()
find_specific_star()
favorite_constellation()

