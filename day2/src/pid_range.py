import math


class PidRange:
    def __init__(self, lower_bound: int, upper_bound: int):
        self.lb = lower_bound
        self.ub = upper_bound
        self.invalid_ids = list()
        self.find_invalid_ids()

    def get_invalid_ids(self):
        return self.invalid_ids

    def find_invalid_ids(self):
        for pid in range(self.lb, self.ub + 1):
            check_pid = str(pid)
            if 1 == len(check_pid):
                continue
            factors = self.get_unique_factors(len(check_pid))
            for divisor in factors:
                this_substring = check_pid[:divisor]
                if check_pid == this_substring * int(len(check_pid) / divisor):
                    self.invalid_ids.append(pid)
                    print(f"Found [{this_substring}] in [{pid}]")
                    break

    @staticmethod
    def get_unique_factors(number):
        factors = list([1])
        max_divisor = math.sqrt(number)
        if 0 != max_divisor % max_divisor:
            max_divisor = int(max_divisor) + 1
        for divisor in range(2, int(max_divisor) + 1):
            if 0 == number % divisor:
                quotient = int(number / divisor)
                factors.append(divisor)
                factors.append(quotient)
        return factors
