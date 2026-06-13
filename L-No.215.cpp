#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k)
    {
        priority_queue<int, vector<int>, greater<int>> min_heap;

        for (auto num : nums)
        {
            min_heap.push(num);

            if (static_cast<int>(min_heap.size()) > k)
                min_heap.pop();
        }
        return min_heap.top();
    }
};

int main()
{
    vector<int> nums = { 3,2,1,5,6,4 };
    int k = 2;

    Solution sol;
    int result = sol.findKthLargest(nums, k);

    cout << result << endl;

    return 0;

}