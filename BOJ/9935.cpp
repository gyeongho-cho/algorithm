#include <iostream>
#include <string>
#include <map>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);

    string s, s_query;
    map<char, int> s_map;

    cin >> s;
    cin >> s_query;
    for (int i=0; i<(s.length()-s_query.length()+1); i++){
        int j = 0;
        bool boom_flag = true;
        while (j < s_query.length()){
            if(s[i+j] != s_query[j]){
                boom_flag = false;
                break;
            }
            j++;
        }

        if (!boom_flag){
            cout << s[i];
        }else{
            i+= s_query.length();
        }

    }


    return 0;
}