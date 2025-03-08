class Solution:
    '''其实这个问题要这么思考，我们只在乎 min(l_max, r_max)。对于上图的情况，我们已经知道 l_max < r_max 了，至于这个 r_max 是不是右边最大的，不重要。重要的是 height[i] 能够装的水只和较低的 l_max 之差有关：'''
    #time:On
    #space:O1
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        l_max = height[left]
        r_max = height[right]

        water = 0

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                water += l_max - height[left]
                

            else:
                right-= 1
                r_max = max(r_max, height[right])
                water += r_max - height[right]
        return water


        '''为什么15,22行代码要先移动指针，这个顺序很重要？让我解释一下原因：

初始状态下，left 指向第一个元素，right 指向最后一个元素。此时我们已经记录了这两个位置的高度作为初始的 l_max 和 r_max。
这两个位置本身不会存水，因为它们是边界。我们需要计算的是中间位置的蓄水量。
移动指针的目的是开始考察新的位置。如果我们不先移动指针，就会重复计算边界位置的蓄水量（而边界位置是不存水的）。
在移动指针后，我们检查新位置是否更新了最大高度，然后计算这个新位置能蓄多少水。
让我们用一个简单例子：[0,1,0,2,1,0,1,3]

初始状态：left=0, right=7, l_max=0, r_max=3
由于 l_max < r_max，我们处理左侧：
应该先 left++，变成 left=1
然后更新 l_max = max(0, 1) = 1
计算水量：1 - 1 = 0（位置1不存水）
如果顺序错误，比如先更新 l_max 再移动指针，就会导致计算错误或逻辑混乱。

这个算法的妙处在于它保证了我们总是移动较小一侧的指针，这样能确保另一侧有足够高的"墙"来储水，而我们只需关心当前这一侧的最大高度与当前高度的差值。




'''