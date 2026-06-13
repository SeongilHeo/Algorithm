#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int coinChange(vector<int>& coins, int amount)
    {

        vector<int> dp(amount + 1, amount + 1);

        dp[0] = 0;

        for (int cur = 1; cur <= amount; cur++)
        {
            for (int coin : coins)
            {
                if (cur < coin)
                    continue;
                dp[cur] = min(dp[cur], dp[cur - coin] + 1);
            }
        }

        if (dp[amount] == amount + 1)
            return -1;

        return dp[amount];

    }
};

int main()
{
    vector<int> coins = { 1,2,5 };
    int amount = 11;

    Solution sol;
    int ans = sol.coinChange(coins, amount);

    cout << ans << endl;

    return 0;
}