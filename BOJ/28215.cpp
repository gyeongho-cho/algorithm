#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cmath>

using namespace std;

typedef pair<int, int> pii;

int manhattan(const pii& a, const pii& b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int main() {
    int N, K;
    cin >> N >> K;

    vector<pii> houses(N);
    for (int i = 0; i < N; ++i) {
        cin >> houses[i].first >> houses[i].second;
    }

    vector<int> indices(N);
    for (int i = 0; i < N; ++i) indices[i] = i;

    int answer = INT_MAX;

    // 모든 K개의 조합
    vector<bool> choose(N, false);
    fill(choose.end() - K, choose.end(), true);

    do {
        vector<int> shelters;
        for (int i = 0; i < N; ++i) {
            if (choose[i]) shelters.push_back(i);
        }

        int maxDist = 0;
        for (int i = 0; i < N; ++i) {
            int minDist = INT_MAX;
            for (int s : shelters) {
                minDist = min(minDist, manhattan(houses[i], houses[s]));
            }
            maxDist = max(maxDist, minDist);
        }

        answer = min(answer, maxDist);
    } while (next_permutation(choose.begin(), choose.end()));

    cout << answer << "\n";
    return 0;
}