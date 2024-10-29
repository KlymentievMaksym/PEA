// Three states are located on a rectangular map of size n * m.
// From any cell of any state, you can go to any cell of the same state, moving only along its cells horizontally or vertically.
// The cells of each state are marked with one of the numbers (1, 2 or 3).

// There are passable (".") and impassable ("#") cells on the map.

// Build roads on the smallest number of passable cells so that you can go from any cell of one state to any cell of another state.
// You can freely move around the cells of any state. You can only move along the map horizontally or vertically.

// Input
// First line contains the size of the map n and m (1 ≤ n, m ≤ 1000). Each of the next n lines contains m symbols:
//     1, 2, 3 - cells that belong to the states;
//     "." - passable cell, here you can build a road;
//     "#" - impassable cell, here you cannot build a road;

// Output
// Print the smallest number of cells in which roads should be built so that all cells of all states will be connected. If it is impossible to do this, print -1.

#include <iostream>
#include <deque>
#include <cstring>
#include <vector>
using namespace std;

#define INF 0x3F3F3F3F
#define MAXN 1001

int n, m;
string grid[MAXN];
int dist[3][MAXN][MAXN];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

int main()
{
   cin >> n >> m;
   for (int i = 0; i < n; i++)
   {
        cin >> grid[i];
   }

   memset(dist, 0x3F, sizeof(dist));

   for (int state = '1'; state <= '3'; state++)
   {
       deque<pair<int, int>> queue;
       

       for (int i = 0; i < n; i++)
       {
           for (int j = 0; j < m; j++)
           {
               if (grid[i][j] == state)
               {
                   dist[state - '1'][i][j] = 0;
                   queue.push_back({i, j});
               }
           }
       }
       

       while (!queue.empty())
       {
           int x = queue.front().first;
           int y = queue.front().second;
           queue.pop_front();
           
           for (int direction_type = 0; direction_type < 4; direction_type++)
           {
               int nx = x + dx[direction_type];
               int ny = y + dy[direction_type];
               
               if (0 <= nx && nx < n && 0 <= ny && ny < m && grid[nx][ny] != '#')
               {
                   int new_distance = dist[state - '1'][x][y] + (grid[nx][ny] == '.');
                   if (new_distance < dist[state - '1'][nx][ny])
                   {
                       dist[state - '1'][nx][ny] = new_distance;
                       if (grid[nx][ny] == '.')
                           queue.push_back({nx, ny});
                       else
                           queue.push_front({nx, ny});
                   }
               }
           }
       }
   }
   
   int answer = INF;
   

   for (int i = 0; i < n; i++)
   {
       for (int j = 0; j < m; j++)
       {
           if (dist[0][i][j] != INF && dist[1][i][j] != INF && dist[2][i][j] != INF)
           {
               int nval = dist[0][i][j] + dist[1][i][j] + dist[2][i][j] - 2 * (grid[i][j] == '.');
               answer = min(answer, nval);
           }
       }
   }

   if (answer == INF) answer = -1;
   cout << answer << endl;
   
   return 0;
}