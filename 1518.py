class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sol = 0
        rest = 0
        while numBottles >= 1:
            sol += numBottles
            rest += numBottles % numExchange
            numBottles = (numBottles // numExchange) + (rest // numExchange)
            rest %= numExchange
        sol += rest // numExchange
        return sol
# Water Bottles, maximum to drink
