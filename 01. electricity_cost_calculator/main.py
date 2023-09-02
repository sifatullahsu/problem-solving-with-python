# Input values
total_unit = float(input("Enter total used unit: "))
kw = float(input("Enter total permissable kw: "))

# Constants
meter_rent = 40
demand_charge = 35 * kw


def calculate_energy_cost(unit):
    prices = [4.35, 4.85, 6.63, 6.95, 7.34, 11.51, 13.26]

    if unit <= 50:
        return unit * prices[0]
    elif unit <= 75:
        return unit * prices[1]
    elif unit <= 200:
        return 75 * prices[1] + (unit - 75) * prices[2]
    elif unit <= 300:
        return 75 * prices[1] + 125 * prices[2] + (unit - 200) * prices[3]
    elif unit <= 400:
        return 75 * prices[1] + 125 * prices[2] + 100 * prices[3] + (unit - 300) * prices[4]
    elif unit <= 600:
        return 75 * prices[1] + 125 * prices[2] + 100 * prices[3] + 100 * prices[4] + (unit - 400) * prices[5]
    else:
        return 75 * prices[1] + 125 * prices[2] + 100 * prices[3] + 100 * prices[4] + 200 * prices[5] + (unit - 600) * prices[6]


# Calculate components
total_energy_cost = calculate_energy_cost(total_unit)
vat = ((meter_rent + demand_charge + total_energy_cost) * 5) / 105
rebate = (total_energy_cost + demand_charge) / 101

# Calculate the total cost
total = meter_rent + demand_charge + total_energy_cost + vat - rebate

# Print the total monthly cost
print('\n'f"Total monthly cost: {total:.2f} TK")
