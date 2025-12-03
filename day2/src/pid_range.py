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
            if 0 != len(check_pid) % 2:
                continue
            max_substring_len = int(len(check_pid) / 2)
            this_substring = check_pid[:max_substring_len]
            next_substring = check_pid[max_substring_len:]   
            if this_substring == next_substring:
                self.invalid_ids.append(pid)
                print(f"Found [{this_substring}] in [{pid}]")
