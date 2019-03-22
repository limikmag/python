
def power(base: int, to_power: int) -> int:
    if to_power == 0:
        return 1
    if to_power % 2 != 0:
        return base*power(
            base=base, to_power=(to_power - 1))
    if to_power % 2 == 0:
        return power(
            base=base, to_power=to_power/2)*power(base=base, to_power=to_power/2)
