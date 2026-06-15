#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target)
    {
        ranges::sort(candidates);
        backtrack(candidates, target, 0);
        return result;

    }

    void backtrack(vector<int>& candidates, int remain, int start)
    {
        if (remain == 0)
        {
            result.push_back(path);
            return;
        }
        if (remain < 0)
            return;

        for (int i = start; i < static_cast<int>(candidates.size()); i++)
        {
            if (candidates[i] > remain)
                break;

            path.push_back(candidates[i]);

            backtrack(candidates, remain - candidates[i], i);

            path.pop_back();
        }
    }
};

int main()
{
    vector<int> candidates = { 2,3,6,7 };
    int target = 7;

    Solution sol;
    vector<vector<int>> result = sol.combinationSum(candidates, target);

    for (const auto& set : result)
    {
        cout << "[ ";
        for (int num : set)
            cout << num << ", ";
        cout << "]" << endl;
    }

    return 0;
}