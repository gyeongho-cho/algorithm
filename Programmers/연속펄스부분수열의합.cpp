#include <vector>
#include <iostream>
using namespace std;

long long solution(vector<int> sequence) {
    long long answer = 0;
    
    long long max_sum1 = 0;
    long long max_sum2 = 0;
    long long curr1 = 0, curr2 = 0;

    for (int i = 0; i < sequence.size(); ++i) {
        int pulse1 = (i % 2 == 0) ? 1 : -1;
        int pulse2 = -pulse1;

        long long val1 = 1LL * sequence[i] * pulse1;
        long long val2 = 1LL * sequence[i] * pulse2;

        curr1 = max(val1, curr1 + val1);
        curr2 = max(val2, curr2 + val2);

        max_sum1 = max(max_sum1, curr1);
        max_sum2 = max(max_sum2, curr2);
    }

    answer = max(max_sum1, max_sum2);
    
    return answer;
}