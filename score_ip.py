import os
import geocoder
import numpy as np

def get_loc(ip):
	return geocoder.ipinfo(ip).latlng

def dist(loc1, loc2):
	R = 3959 # Approx. radius of earth in miles
	lat1 = np.radians(loc1[0])
	lat2 = np.radians(loc2[0])

	lon1 = np.radians(loc1[1])
	lon2 = np.radians(loc2[1])

	# Haversine formula
	return 2 * R * np.sqrt(np.sin((lat2 - lat1)/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin((lon2 - lon1)/2)**2)

# CHANGE THIS ***

data_location = "ip.txt"
test_ip = '1.1.1.1'

# -------

fraud = []
ips = []

# Opens file and stores info in fraud and ips
data = open(data_location, "r").readlines()

for i in range (len(data)):
	linesplit = data[i].replace("\n", "").split(" ")

	# Removes duplicates
	if linesplit[1] not in ips:
		fraud.append(linesplit[0])
		ips.append(linesplit[1])

# Populates locs with all locations
locs = [get_loc(ip) for ip in ips]

test_loc = get_loc(test_ip)

# Finds index of ip with smallest distance
min_index = np.argmin([dist(loc, test_loc) for loc in locs])

ans = round(dist(test_loc, locs[min_index]), 2)
if fraud[min_index] == "FRAUD":
	ans *= 2

print("Score for ip {0}: {1}".format(test_ip, ans))