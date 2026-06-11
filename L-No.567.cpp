#include <array>
#include <string>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2)
    {
        if (s1.size() > s2.size())
        {
            return false;
        }

        array<int, 26> need{};
        array<int, 26> window{};

        for (char c : s1)
        {
            need[c - 'a']++;
        }

        int len = static_cast<int>(s1.size());

        for (int i = 0; i < static_cast<int>(s2.size()); i++)
        {
            window[s2[i] - 'a']++;

            if (i >= len)
            {
                window[s2[i - len] - 'a']--;
            }

            if (window == need)
            {
                return true;
            }
        }

        return false;
    }
};