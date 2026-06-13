#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones)
    {
        priority_queue<int> max_heap;

        for (auto s : stones)
            max_heap.push(s);

        while (max_heap.size() > 1)
        {
            int a = max_heap.top();
            max_heap.pop();

            int b = max_heap.top();
            max_heap.pop();

            if (a != b)
                max_heap.push(a - b);
        }
        return max_heap.empty() ? 0 : max_heap.top();
    }
};
int main()
{
    vector<int> stones = { 2, 7, 4, 1, 8, 1 };

    Solution sol;
    int result = sol.lastStoneWeight(stones);

    cout << result << endl;

    return 0;
}