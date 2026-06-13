#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n)
    {

        if (n == 1)
            return 1;
        else if (n == 2)
            return 2;

        vector<int> result = { 1,2 };

        for (int i = 2; i < n; i++)
            result.push_back(result[i - 1] + result[i - 2]);

        return result.back();
    }
};

int main()
{
    int n = 3;
    Solution sol;
    int ans = sol.climbStairs(n);

    cout << ans << endl;

    return 0;
}