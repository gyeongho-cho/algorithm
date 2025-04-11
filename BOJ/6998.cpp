#include <iostream>

#include <sstream>
#include <vector>
#include <string>

using namespace std;

struct Node {
    string val;
    vector<Node*> children;
};

int idx = 0;

Node* buildTree(const vector<string>& tokens) {
    if (idx >= tokens.size() || tokens[idx] == "#") {
        idx++;
        return nullptr;
    }

    Node* node = new Node{tokens[idx++], {}};

    while (true) {
        Node* child = buildTree(tokens);
        if (!child) break; // '#'이 나올 때까지 자식 추가
        node->children.push_back(child);
    }

    return node;
}

bool isIsomorphic(Node* a, Node*b){
    if (!a && !b) return true;
    if (!a || !b) return false;

    if (a->children.size() != b->children.size()) return false;

    vector<bool>matched(b->children.size(), false);

    for (Node* childA: a->children){
        bool foundMatch = false;
        for (size_t i=0; i<b->children.size(); ++i){
            if (!matched[i] && isIsomorphic(childA, b->children[i])){
                matched[i]=true;
                foundMatch=true;
                break;
            }
        }
        if (!foundMatch) return false;
    }
    return true;
}


int main(){
    int T;
    cin >> T;
    cin.ignore();
    for (int i=0; i<T; i++){
        string input1, input2;
        getline(cin, input1);
        getline(cin, input2);
        
        vector<string> tokens1, tokens2;
        stringstream ss1(input1), ss2(input2);
        string tok;


        while (ss1 >> tok) tokens1.push_back(tok);
        while (ss2 >> tok) tokens2.push_back(tok);

        idx = 0;
        Node* root1 = buildTree(tokens1);
        idx = 0;
        Node* root2 = buildTree(tokens2);

        if (isIsomorphic(root1, root2)) {
            cout << "The two trees are isomorphic.\n";
        } else {
            cout << "The two trees are not isomorphic.\n";
        }
    }
    return 0;
}