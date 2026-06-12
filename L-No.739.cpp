#include <vector>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures)
    {

        const int n = static_cast<int>(temperatures.size());

        vector<int> answer(n, 0);
        vector<int> stack;

        for (int current = 0; current < n; current++)
        {
            while (!stack.empty() && temperatures[current] > temperatures[stack.back()])
            {

                int previous = stack.back();
                stack.pop_back();

                answer[previous] = current - previous;
            }
            stack.push_back(current);
        }
        return answer;
    }
};