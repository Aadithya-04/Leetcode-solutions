from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  
        length = len(flowerbed)
        
        i = 0
        while i < length:
            
            if flowerbed[i] == 0:
                
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1  
                    count += 1
                    if count >= n:
                        return True
           
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        
        return count >= n
