from decimal import Decimal


def main():
    float_res = 0.1 + 0.1 + 0.1 #0.30000000000000004
    print(float_res)
    fixed_res = Decimal('0.1') + Decimal('0.1') +Decimal('0.1')
    print(fixed_res)

if __name__ == "__main__":
    main()