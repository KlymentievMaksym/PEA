#include <algorithm>
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int weight(int i, int j, vector<int> &sum) {
        if (i > j) return 0;
        return sum[j] - sum[i - 1];
    }

    int go(int i, int j, vector<int> &sum, vector<vector<int>> &dp) {
        if (i > j) return 0;

        if (dp[i][j] == INT_MAX) {
            for (int k = i; k <= j; k++) {
                int temp = go(i, k - 1, sum, dp) + go(k + 1, j, sum, dp) + weight(i, k - 1, sum) + weight(k + 1, j, sum);
                if (temp < dp[i][j]) {
                    dp[i][j] = temp;
                }
            }
        }

        return dp[i][j];
    }

int main() {
    vector<vector<int>> dp;
    vector<int> sum;
    int n;
    while (cin >> n) {
        dp.assign(n + 1, vector<int>(n + 1, INT_MAX));
        vector<int> freq(n + 1);
        sum.assign(n + 1, 0);

        for (int i = 1; i <= n; i++) {
            cin >> freq[i];
            dp[i][i] = 0;
        }

        for (int i = 1; i <= n; i++) {
            sum[i] = sum[i - 1] + freq[i];
        }

        go(1, n, sum, dp);
        cout << dp[1][n] << endl;
    }
    return 0;
}

