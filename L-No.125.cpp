#include <cctype>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s)
    {

        int left = 0;
        int right = static_cast<int>(s.size()) - 1;

        while (left < right)
        {
            while (left < right && !isalnum(static_cast<unsigned char>(s[left])))
            {
                left++;
            }
            while (left < right && !isalnum(static_cast<unsigned char>(s[right])))
            {
                right--;
            }

            char l = static_cast<char>(tolower(static_cast<unsigned char>(s[left])));
            char r = static_cast<char>(tolower(static_cast<unsigned char>(s[right])));

            if (l != r)
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};