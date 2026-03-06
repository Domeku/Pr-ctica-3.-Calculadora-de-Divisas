def exchange_money(budget, exchange_rate):
    """Convierte dinero según la tasa de cambio."""
    return budget / exchange_rate


def calculadora_divisas():
    print("=" * 45)
    print("   💱 CALCULADORA DE DIVISAS - Camila & Diego")
    print("=" * 45)

    # Pedir moneda de origen
    moneda_origen = input("\n¿Cuál es tu moneda? (ej: USD, EUR): ").upper()

    # Pedir moneda de destino
    moneda_destino = input("¿A qué moneda quieres convertir? (ej: JPY, MXN): ").upper()

    # Pedir la tasa de cambio
    tasa = float(input(f"¿Cuánto vale 1 {moneda_destino} en {moneda_origen}? "))

    # Pedir la cantidad a convertir
    cantidad = float(input(f"\n¿Cuántos {moneda_origen} deseas convertir? "))

    # Calcular
    resultado = exchange_money(cantidad, tasa)

    # Mostrar resultado
    print("\n" + "=" * 45)
    print(f"  {cantidad:,.2f} {moneda_origen}  →  {resultado:,.2f} {moneda_destino}")
    print("=" * 45)


# Ejecutar el programa
calculadora_divisas()