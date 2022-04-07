from typing import List


class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        bank = {5: 0,
                10: 0,
                20: 0}

        for i in range(n):
            bill = bills[i]

            if bill == 10:
                # Checking if we have enough papers of $5
                if bank[5] < 1:
                    return False
                bank[5] -= 1
            if bill == 20:
                # Checking if we have enough papers of $5 and $10
                if (bank[5]) < 3 and (bank[5] < 1 or bank[10] < 1):
                    return False
                # We always prefer to spend one paper of $5 and one of $10 since we need to save papers of 5
                # for clients who pay with papers of $10
                if bank[5] >= 1 and bank[10] >= 1:
                    bank[5] -= 1
                    bank[10] -= 1
                else:
                    bank[5] -= 3
            # Add the received paper to the bank
            bank[bill] += 1

        return True


o1 = Solution()
result = o1.lemonadeChange([5, 5, 5, 10, 20])
print(result)
