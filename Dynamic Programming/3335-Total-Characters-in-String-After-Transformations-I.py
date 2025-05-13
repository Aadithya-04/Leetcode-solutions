class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        
        # g[k] = length of string produced by starting from 'z' with k transforms
        g = [0] * (t + 1)
        g[0] = 1
        for k in range(1, t + 1):
            if k <= 25:
                # before either branch ever returns to 'z'
                g[k] = 2
            elif k == 26:
                # first time both branches have stayed non-z long enough
                g[k] = 3
            else:
                # both 'a' and 'b' branches have themselves branched
                g[k] = (g[k - 26] + g[k - 25]) % MOD
        
        ans = 0
        for ch in s:
            dist = ord('z') - ord(ch)
            if t <= dist:
                # never reaches 'z'
                ans = (ans + 1) % MOD
            else:
                # reaches 'z' after dist steps, then g[t − dist] more transforms
                ans = (ans + g[t - dist]) % MOD
        
        return ans
