#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

const int MAXN = 200000;
vector<int> adj[MAXN + 1];
int descendants[MAXN + 1];

void dfs(int node);

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 2; i <= n; ++i) {
        int parent;
        scanf("%d", &parent);
        adj[parent].push_back(i);
    }

    dfs(1);

    for (int i = 1; i <= n; ++i) {
        printf("%d ",descendants[i]);
    }
    printf("\n");
    return 0;
}

void dfs(int node) {
    descendants[node] = 0;
    for (int child : adj[node]) {
        dfs(child);
        descendants[node] += descendants[child] + 1;
    }
}