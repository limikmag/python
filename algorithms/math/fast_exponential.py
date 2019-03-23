

# recursion
def power(base: int, to_power: int) -> int:
    if to_power == 0:
        return 1
    if to_power % 2 != 0:
        return base*power(
            base=base, to_power=(to_power - 1))
    if to_power % 2 == 0:
        return power(
            base=base, to_power=to_power/2)*power(base=base, to_power=to_power/2)


#iterative
def fast_power(base: int, to_power: int) -> int:
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """
    result = 1
    while to_power > 0:
        if to_power % 2 == 1:
            result = (result * base)
        to_power = to_power//2
        base = (base * base)

    return result


print(fast_power(2,10))

