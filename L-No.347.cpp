#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k)
    {
        unordered_map<int, int> freq;

        for (int num : nums)
        {
            freq[num]++;
        }

        vector<pair<int, int>> items;
        items.reserve(freq.size());

        for (const auto& [num, count] : freq)
        {
            items.push_back({ num, count });
        }

        ranges::sort(items, [](const auto& a, const auto& b)
            {
                return a.second > b.second;
            });

        vector<int> ans;
        ans.reserve(k);

        for (int i = 0; i < k && i < static_cast<int>(items.size()); i++)
        {
            ans.push_back(items[i].first);
        }

        return ans;
    }
};

int main()
{
    vector<int> nums = { 1, 2, 1, 2, 1, 2, 3, 1, 3, 2 };
    int k = 2;

    Solution sol;
    vector<int> result = sol.topKFrequent(nums, k);

    cout << "[ ";
    for (const auto& num : result)
    {
        cout << num << " ";
    }
    cout << "]\n";

    return 0;
}