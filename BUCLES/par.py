NUM_PAIRS = 100

print(f"Primeros {NUM_PAIRS} números pares")
print("--------------------------")

num_par = 0
while num_par < NUM_PAIRS:
    num_par += 1
    print(f"Par número {num_par: 3}: {num_par * 2: 3}")