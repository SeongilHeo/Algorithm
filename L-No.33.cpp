#include <vector>
#include <iostream>
#include <algorithm>
#include <ranges>

using namespace std;

class Solution {
public:
    int getH(vector<int>& piles, int k)
    {
        unsigned int h = 0;
        for (unsigned int p : piles)
            h += (p + k - 1) / k;
        return h;
    }
    int minEatingSpeed(vector<int>& piles, int h)
    {
        ranges::sort(piles);

        int l = 0;
        int r = static_cast<int>(piles.size());
        while (l < r)
        {
            int mid = l + (r - l) / 2;

            int cur = getH(piles, piles[mid]);

            if (h < cur)
                l = mid + 1;
            else
                r = mid;
        }

        r = piles[l];
        l = 1;

        while (l < r)
        {
            int mid = l + (r - l) / 2;

            int cur = getH(piles, mid);

            if (h < cur)
                l = mid + 1;
            else
                r = mid;
        }

        return l;
    }
};


int main()
{
    vector<int> piles = { 4, 5, 6, 7, 0, 1, 2 };
    int h = 8;

    Solution sol;
    int result = sol.minEatingSpeed(piles, h);

    cout << result << endl;

    return 0;
}