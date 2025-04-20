C: int = 299_792_458  # Speed of light in m/s

def formula():
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    energy_in_joules: float = mass_in_kg * (C ** 2)

    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")

    print(f"💥 Energy: {energy_in_joules:.2e} joules!")

formula()
