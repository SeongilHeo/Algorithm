#include <iostream>
#include <vector>
// #include <algorithm>
// #include <ranges>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums)
    {
        vector<int> lis;

        for (int num : nums)
        {
            auto it = ranges::lower_bound(lis, num);

            if (it == lis.end())
                lis.push_back(num);
            else
                *it = num;
        }
        return static_cast<int>(lis.size());
    }
};

int main()
{
    vector<int> nums = { 10,9,2,5,3,7,101,18 };
    Solution sol;
    int ans = sol.lengthOfLIS(nums);

    cout << ans << endl;

    return 0;
}