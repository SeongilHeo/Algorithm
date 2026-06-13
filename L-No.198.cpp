#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums)
    {

        int one = 0;
        int two = 0;

        for (int n : nums)
        {
            int current = max(one, two + n);
            two = one;
            one = current;
        }
        return one;
    }
};

int main()
{
    vector<int> nums = { 1,2,3,1 };
    Solution sol;
    int ans = sol.rob(nums);

    cout << ans << endl;

    return 0;
}