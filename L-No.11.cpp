class Solution {
public:
    int maxArea(vector<int>& height)
    {

        int l = 0;
        int r = static_cast<int>(height.size()) - 1;

        int ans = 0;

        while (l < r)
        {
            int w = r - l;
            int size = w * min(height[l], height[r]);
            if (size > ans)
            {
                ans = size;
            }

            if (height[l] > height[r])
            {
                r--;
            }
            else
            {
                l++;
            }
        }
        return ans;
    }
};