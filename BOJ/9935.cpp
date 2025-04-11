#include <iostream>
#include <string>
#include <vector>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);

    string s_query, s_key;
    vector<char> s_stack;
    cin >> s_query;
    cin >> s_key;
    for (int j=0; j<s_query.length(); j++){
        s_stack.push_back(s_query[j]);
        bool boom_flag = true;
        for (int i=0; i<s_key.length(); i++){
            if (s_stack[s_stack.size()-1-i] != s_key[s_key.length()-i-1]){
                boom_flag=false;
                break;
            }
        }
        if (boom_flag){
            for (int i=0; i<s_key.length(); i++){
                s_stack.pop_back();
            }
        }
        
    }
    if (s_stack.size()==0){
        cout << "FRULA";
    }
    else{
        for (char c : s_stack){
            cout << c ;
        }
    }

   return 0;
}