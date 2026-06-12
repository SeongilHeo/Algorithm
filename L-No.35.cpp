#include <vector>

class Solution {
public:
    int searchInsert(vector<int>& nums, int target)
    {
        int l = 0;
        int r = static_cast<int>(nums.size());

        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (nums[mid] < target)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
};