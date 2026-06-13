#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost)
    {

        int two = cost[0];
        int one = cost[1];

        for (int i = 2; i < cost.size(); i++)
        {
            int current = cost[i] + min(one, two);
            two = one;
            one = current;
        }

        return min(one, two);

    }
};

int main()
{
    vector<int> cost = { 1,100,1,1,1,100,1,1,100,1 };
    Solution sol;
    int ans = sol.minCostClimbingStairs(cost);

    cout << ans << endl;

    return 0;
}