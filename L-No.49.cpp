#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        unordered_map<string, vector<string>> mp;

        for (const string& str : strs)
        {
            string temp = str;
            ranges::sort(temp);

            mp[temp].push_back(str);
        }

        vector<vector<string>> ans;

        for (auto& [key, group] : mp)
        {
            ans.push_back(group);
        }

        return ans;
    }
};

int main()
{
    vector<string> strs = { "eat", "tea", "tan", "ate", "nat", "bat" };

    Solution sol;
    vector<vector<string>> result = sol.groupAnagrams(strs);

    for (const auto& group : result)
    {
        cout << "[ ";
        for (const auto& word : group)
        {
            cout << word << " ";
        }
        cout << "]\n";
    }

    return 0;
}