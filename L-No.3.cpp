#include <algorithm>
#include <array>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s)
    {
        array<int, 128> last;
        last.fill(-1);

        int max_len = 0;
        int start = 0;

        for (int i = 0; i < static_cast<int>(s.size()); i++)
        {
            char c = s[i];

            if (last[c] >= start)
            {
                start = last[c] + 1;
            }

            last[c] = i;
            max_len = max(max_len, i - start + 1);
        }

        return max_len;
    }
};