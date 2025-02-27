class Solution:
    #easy
    # sliding windows
    #时间复杂度确实是 O(n)，其中 n 是字符串 blocks 的长度，因为我们只需要遍历字符串一次。
#空间复杂度是 O(1)
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        count_b = 0
        ops = float('inf')

        for right in range(len(blocks)):
            if blocks[right] == 'B':
                count_b += 1

            if right - left + 1 == k:
                ops = min(ops, k - count_b)

                if blocks[left] == 'B':
                    count_b -= 1
                left += 1

        return ops