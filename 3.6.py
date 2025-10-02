from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 28
getcontext().rounding = ROUND_HALF_UP

def financial_calculator():
    initial_amount = Decimal(input("Введите начальную сумму вклада (например, 1000.50): ").strip())
    annual_rate = Decimal(input("Введите годовую процентную ставку (например, 7.5): ").strip())
    years = Decimal(input("Введите срок вклада в годах (например, 3): ").strip())

    # Месячная процентная ставка
    monthly_rate = annual_rate / Decimal('12') / Decimal('100')
    months = years * Decimal('12')

    # Формула с ежемесячной капитализацией процентов
    final_amount = initial_amount * ( (Decimal('1') + monthly_rate) ** months )
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount

    print(f"Итоговая сумма вклада: {final_amount} руб.")
    print(f"Общая прибыль: {profit.quantize(Decimal('0.01'))} руб.")

if __name__ == "__main__":
    financial_calculator()
