#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int>* createGraph(int n);
void addEdge(vector<int>* adjlist, int u, int v);
bool isCyclic(vector<int>* adjlist, int v, vector<bool>& visited, int parent);
bool isTree(vector<int>* adjlist, int vertices);

int main() {
    int vertices, edges, node1, node2;

    scanf("%d %d", &vertices, &edges);

    vector<int>* adjlist = createGraph(vertices);

    for (int i = 0; i < edges; ++i) {
        scanf("%d %d", &node1, &node2);
        addEdge(adjlist, node1, node2);
    }

    if (isTree(adjlist, vertices)) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    delete[] adjlist;
    return 0;
}

vector<int>* createGraph(int n) {
    return new vector<int>[n];
}

void addEdge(vector<int>* adjlist, int u, int v) {
    adjlist[u].push_back(v);
    adjlist[v].push_back(u);  // Add this line for undirected graphs.
}

bool isCyclic(vector<int>* adjlist, int v, vector<bool>& visited, int parent) {
    visited[v] = true;

    for (int neighbor : adjlist[v]) {
        if (!visited[neighbor]) {
            if (isCyclic(adjlist, neighbor, visited, v)) {
                return true;
            }
        } else if (neighbor != parent) {
            return true;
        }
    }

    return false;
}

bool isTree(vector<int>* adjlist, int vertices) {
    vector<bool> visited(vertices, false);

    for (int i = 0; i < vertices; ++i) {
        if (!visited[i] && isCyclic(adjlist, i, visited, -1)) {
            return false; // The graph is not a tree if it contains a cycle.
        }
    }

    // Check if the graph is connected.
    set<int> visited_set;
    visited_set.insert(0); // Start from vertex 0.
    set<int> stack;
    stack.insert(0);

    while (!stack.empty()) {
        int node = *stack.begin();
        stack.erase(stack.begin());

        for (int neighbor : adjlist[node]) {
            if (visited_set.find(neighbor) == visited_set.end()) {
                visited_set.insert(neighbor);
                stack.insert(neighbor);
            }
        }
    }

    return visited_set.size() == vertices; // The graph is a tree if it is connected.
}