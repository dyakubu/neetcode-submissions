class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fives = 0
        tens = 0

        for bill in bills:

            if bill == 5:
                fives += 1

            elif bill == 10:
                if fives <= 0:
                    return False
                else:
                    fives -= 1
                    tens += 1
    
            else: #i.e bill ==20
                if fives <= 0:
                    return False # No way to construct 15 without 5
                else:
                    if tens > 0:
                        tens -= 1
                        fives -= 1
                    else:
                        if fives < 3:
                            return False
                        fives -= 3

        return True



        