#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> info, int n, int m) {
    const int MAX = 121;
    const int INF = 1e9;

    int len = info.size();
    vector<vector<vector<bool>>> dp(len + 1, vector<vector<bool>>(n, vector<bool>(m, false)));
    dp[0][0][0] = true;

    for (int i = 0; i < len; ++i) {
        int a = info[i][0];
        int b = info[i][1];

        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                if (!dp[i][j][k]) continue;

                if (j + a < n)
                    dp[i + 1][j + a][k] = true;

                if (k + b < m)
                    dp[i + 1][j][k + b] = true;
            }
        }
    }

    int answer = INF;
    for (int j = 0; j < n; ++j) {
        for (int k = 0; k < m; ++k) {
            if (dp[len][j][k])
                answer = min(answer, j);
        }
    }

    return answer == INF ? -1 : answer;
}