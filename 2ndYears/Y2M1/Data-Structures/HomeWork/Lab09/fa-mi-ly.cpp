#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int id = 0;
    vector<Node> children;
};

void calculateDescendants(Node node) {
    node.id = 0;
    for (const Node& child : node.children) {
        calculateDescendants(child);
        node.id += child.id + 1;
    }
}

int main() {
    int n;
    cin >> n;

    vector<Node> tree(n + 1);

    for (int i = 2; i <= n; ++i) {
        int parent;
        cin >> parent;
        tree[parent].children.push_back(&tree[i]);
    }

    calculateDescendants(tree[1]);

    for (int i = 1; i <= n; ++i) {
        cout << tree[i].id << " ";
    }

    cout << endl;

    return 0;
}

