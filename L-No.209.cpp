#include <algorithm>
#include <limits>
#include <vector>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums)
    {
        int left = 0;
        int sum = 0;
        int min_len = numeric_limits<int>::max();

        for (int right = 0; right < static_cast<int>(nums.size()); right++)
        {
            sum += nums[right];

            while (sum >= target)
            {
                min_len = min(min_len, right - left + 1);
                sum -= nums[left];
                left++;
            }
        }

        return min_len == numeric_limits<int>::max() ? 0 : min_len;
    }
};