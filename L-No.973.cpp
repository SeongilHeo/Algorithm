#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k)
    {
        priority_queue<pair<int, int>> max_heap;

        for (int i = 0; i < static_cast<int>(points.size()); i++)
        {
            int x = points[i][0];
            int y = points[i][1];

            int dist = x * x + y * y;

            max_heap.push({ dist, i });

            if (static_cast<int>(max_heap.size()) > k)
                max_heap.pop();
        }

        vector<vector<int>> answer;

        while (!max_heap.empty())
        {
            int index = max_heap.top().second;
            max_heap.pop();
            answer.push_back(points[index]);
        }

        return answer;
    }
};

int main()
{
    vector<vector<int>> points = { {3, 3}, {5, -1}, {-2, 4} };
    int k = 2;

    Solution sol;
    vector<vector<int>> result = sol.kClosest(points, k);

    for (const auto& point : result)
        cout << "[" << point[0] << "," << point[1] << "] ";
    cout << endl;

    return 0;
}