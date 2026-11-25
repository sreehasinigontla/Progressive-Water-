
# Progressive Water Tariff Analysis

# Tariff Configuration
FIXED_CHARGE = 75
PENALTY_RATE = 0.10
EXCESS_LIMIT = 25


# Function to calculate water charges
def calculate_water_charges(units):

    if units <= 10:
        charges = units * 5

    elif units <= 20:
        charges = (10 * 5) + ((units - 10) * 8)

    elif units <= 30:
        charges = (10 * 5) + (10 * 8) + ((units - 20) * 12)

    else:
        charges = (10 * 5) + (10 * 8) + (10 * 12) + ((units - 30) * 15)

    return charges


# Function to calculate final water bill
def calculate_bill(units):

    energy_charges = calculate_water_charges(units)

    fixed_charge = FIXED_CHARGE

    penalty = 0

    if units > EXCESS_LIMIT:
        penalty = energy_charges * PENALTY_RATE

    total_bill = energy_charges + fixed_charge + penalty

    return energy_charges, fixed_charge, penalty, total_bill


# Function to collect household details
def get_household_details():

    households = []

    while True:
        try:
            n = int(input("Enter number of households: "))

            if n > 0:
                break

            print("Enter at least one household.")

        except ValueError:
            print("Enter a valid whole number.")

    while True:
        try:
            months_count = int(input("Enter number of months: "))

            if months_count > 0:
                break

            print("Enter at least one month.")

        except ValueError:
            print("Enter a valid whole number.")

    for i in range(n):

        print("\n========== HOUSEHOLD", i + 1, "==========")

        household_id = input("Enter Household ID: ")
        name = input("Enter Household Name: ")

        monthly_data = []

        for j in range(months_count):

            print("\nMonth", j + 1)

            month = input("Enter Month Name: ")

            while True:
                try:
                    units = float(
                        input("Enter water consumption (KL): ")
                    )

                    if units >= 0:
                        break

                    print("Consumption cannot be negative.")

                except ValueError:
                    print("Enter a valid number.")

            energy, fixed, penalty, total = calculate_bill(units)

            record = {
                "month": month,
                "units": units,
                "energy": energy,
                "fixed": fixed,
                "penalty": penalty,
                "total": total
            }

            monthly_data.append(record)

        household = {
            "id": household_id,
            "name": name,
            "records": monthly_data
        }

        households.append(household)

    return households


# Function to display individual bills
def display_bills(households):

    print("\n========== WATER BILL REPORT ==========")

    for household in households:

        print("\nHousehold ID:", household["id"])
        print("Household Name:", household["name"])

        for data in household["records"]:

            print("\nMonth:", data["month"])
            print("Consumption:", data["units"], "KL")
            print("Water Charges: Rs.", round(data["energy"], 2))
            print("Fixed Charges: Rs.", round(data["fixed"], 2))
            print("Penalty: Rs.", round(data["penalty"], 2))
            print("Final Bill: Rs.", round(data["total"], 2))


# Function to compare household consumption
def compare_consumption(households):

    print("\n========== CONSUMPTION COMPARISON ==========")

    if not households:
        return

    month_count = len(households[0]["records"])

    for j in range(month_count):

        total_units = 0

        for household in households:
            total_units += household["records"][j]["units"]

        average = total_units / len(households)

        print("\nMonth:", households[0]["records"][j]["month"])
        print("Average Household Consumption:", round(average, 2), "KL")

        for household in households:

            units = household["records"][j]["units"]

            print(household["name"], ":", units, "KL")

            if units > EXCESS_LIMIT:
                print("WARNING: Excessive water usage!")

            if average > 0 and units > average * 1.30:
                print("WARNING: Consumption is 30% above household average!")


# Function to display highest and lowest consumption
def display_summary(households):

    all_records = []

    for household in households:

        for record in household["records"]:

            all_records.append({
                "name": household["name"],
                "month": record["month"],
                "units": record["units"],
                "bill": record["total"]
            })

    if not all_records:
        return

    highest = max(all_records, key=lambda x: x["units"])
    lowest = min(all_records, key=lambda x: x["units"])

    print("\n========== FINAL SUMMARY ==========")

    print("Highest Consumption:")
    print("Household:", highest["name"])
    print("Month:", highest["month"])
    print("Units:", highest["units"], "KL")

    print("\nLowest Consumption:")
    print("Household:", lowest["name"])
    print("Month:", lowest["month"])
    print("Units:", lowest["units"], "KL")


# Main Program
print("========================================")
print("     PROGRESSIVE WATER TARIFF ANALYSIS")
print("========================================")

households = get_household_details()

display_bills(households)

compare_consumption(households)

display_summary(households)

print("\nWater Tariff Analysis Completed!")
