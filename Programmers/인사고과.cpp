#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> scores) {
    int n = scores.size();
    int wonho_a = scores[0][0];
    int wonho_b = scores[0][1];
    int wonho_sum = wonho_a + wonho_b;

    sort(scores.begin(), scores.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0]) return a[1] < b[1];
        return a[0] > b[0];
    });

    int max_peer_score = 0;
    bool is_incentive = false;

    vector<int> valid_sums;

    for (const auto& s : scores) {
        int a = s[0];
        int b = s[1];

        if (a < wonho_a && b < wonho_b) {
            continue;
        }

        if (b >= max_peer_score) {
            max_peer_score = b;
            valid_sums.push_back(a + b);

            if (a == wonho_a && b == wonho_b) {
                is_incentive = true;
            }
        }
    }

    if (!is_incentive) return -1;

    // 3. 완호의 석차 계산
    int rank = 1;
    for (int s : valid_sums) {
        if (s > wonho_sum) rank++;
    }

    return rank;
}