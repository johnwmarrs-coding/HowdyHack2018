from math import sqrt


white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
orange = [255, 165, 0]
pink = [255, 192, 203]
purple = [160, 32, 240]
black = [0, 0, 0]






color_descriptions = []

colors = []

colors.append(white)
color_descriptions.append("WHITE")
colors.append(red)
color_descriptions.append("RED")
colors.append(green)
color_descriptions.append("GREEN")
colors.append(yellow)
color_descriptions.append("YELLOW")
colors.append(orange)
color_descriptions.append("ORANGE")
colors.append(pink)
color_descriptions.append("PINK")
colors.append(purple)
color_descriptions.append("PURPLE")
colors.append(black)
color_descriptions.append("BLACK")


def calculate_distance(c1, c2):
	distance = 0
	if (len(c1) != len(c2)):
		print("SIZE MISMATCH!!!!!!!")
		return
	for i in range(0, len(c1)):
		distance += (c1[i]-c2[i]) ** 2

	distance = sqrt(distance)
	return distance

def get_color(target):
	dists = []
	for c in colors:
		dists.append(calculate_distance(target, c))

	return color_descriptions[dists.index(min(dists))]










