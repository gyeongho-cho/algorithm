#include <iostream>
#include <vector>
using namespace std;

int dp(vector<int> &methods, int M, int K) {

    
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

    int M, K;
    cin >> M >> K;

    vector<int> methods;
    methods.reserve(K);

    for (int i=0; i<K; i++){
        int a;
        cin >> a;
        methods.push_back(a);
    }

    

}