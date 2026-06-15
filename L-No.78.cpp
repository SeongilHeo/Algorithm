#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;

public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
        backtrack(nums, 0);
        return result;
    }

    void backtrack(vector<int>& nums, int start)
    {
        result.push_back(path);

        for (int i = start; i < static_cast<int>(nums.size()); i++)
        {
            path.push_back(nums[i]);

            backtrack(nums, i + 1);

            path.pop_back();
        }
    }
};

int main()
{
    vector<int> nums = { 1,2,3 };

    Solution sol;
    vector<vector<int>> result = sol.subsets(nums);

    for (const auto& set : result)
    {
        cout << "[ ";
        for (int num : set)
            cout << num << ", ";
        cout << "]" << endl;
    }

    return 0;
}