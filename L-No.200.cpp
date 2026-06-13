#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid)
    {
        int height = grid.size();
        int width = grid[0].size();
        int ans = 0;

        const int dy[4] = { 1,-1,0,0 };
        const int dx[4] = { 0,0,1,-1 };


        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == '0')
                    continue;

                grid[y][x] = '0';

                queue<pair<int, int>> q;
                q.push({ y,x });

                while (!q.empty())
                {
                    auto [cy, cx] = q.front();
                    q.pop();

                    for (int i = 0; i < 4; i++)
                    {
                        int ny = cy + dy[i];
                        int nx = cx + dx[i];
                        if (ny < 0 || nx < 0 || ny >= height || nx >= width || grid[ny][nx] == '0')
                            continue;

                        grid[ny][nx] = '0';
                        q.push({ ny,nx });
                    }
                }
                ans++;
            }
        }
        return ans;
    }
};

int main()

{

    vector<vector<char>> grid = {

        {'1', '1', '1', '1', '0'},

        {'1', '1', '0', '1', '0'},

        {'1', '1', '0', '0', '0'},

        {'0', '0', '0', '0', '0'}

    };

    Solution sol;

    int result = sol.numIslands(grid);

    cout << "Number of islands: " << result << '\n';

    return 0;

}