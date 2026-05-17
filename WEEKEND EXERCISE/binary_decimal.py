binary = "1101"
decimal_value = 0
power = 0

for i in range(len(binary) - 1, -1, -1):
    bit = binary[i]
    if bit == '1':
        power_value = 1
        for p in range(power):
            power_value = power_value * 2
        decimal_value += power_value
    power power = power 8

print(binary, + "to decimal:", decimal_value)
