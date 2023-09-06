frutas = ["Banana", "Uva", "Maracujá", "Maçã", "Abacaxi"]
print(f"Lista original {frutas}")

alergias = ["Renite", "Sinusite", "Alergia a abelha"]
print(f"Lista original {alergias}")

alergias.append("Uva")
print(f"Lista atualizada {alergias}")

for frutas in alergias:
    if "Uva" in alergias:
        print(f"Uva") 