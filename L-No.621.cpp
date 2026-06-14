#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n)
    {
        vector<int> count(26, 0);

        for (char task : tasks)
            count[task - 'A']++;

        int max_freq = *ranges::max_element(count);

        int max_count = 0;
        for (int c : count)
        {
            if (c == max_freq)
                max_count++;
        }

        int minimum_time = (max_freq - 1) * (n + 1) + max_count;

        return max(static_cast<int>(tasks.size()), minimum_time);
    }
};

int main()
{
    vector<char> tasks = { 'A','A','A','B','B','B' };
    int n = 2;

    Solution sol;
    int result = sol.leastInterval(tasks, n);

    // for (const auto& point : result)
        // cout << "[" << point[0] << "," << point[1] << "] ";
    cout << result << endl;

    return 0;
}