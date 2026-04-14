import re

str_to_analyze = "xxyyxxxyxxyxx"

greedy_pattern = re.compile("xx(.*)xx")
reluctant_pattern = re.compile("xx(.*?)xx")
posisesive_pattern = re.compile("xx(.*+)xx")

for m in re.findall(greedy_pattern, str_to_analyze):
    print("greedy: ", m)

for m in re.findall(reluctant_pattern, str_to_analyze):
    print("reluctant: ", m)

for m in re.findall(posisesive_pattern, str_to_analyze):
    print("posisesive: ", m)
