// Given a directed graph, that can contain multiple edges and loops.
// Each edge has a weight that is expressed by a number (possibly negative).
// It is guaranteed that there are no cycles of negative weight.

// Calculate the length of the shortest paths from the vertex number 1 to all other vertices.

// Input
// First the number of vertices n (1 ≤ n ≤ 100) is given.
// It is followed by the number of edges m (0 ≤ m ≤ 10000).
// Next m triples describe the edges: beginning of the edge, the end of the edge and its weight (an integer from -100 to 100).
// Output
// Print n numbers - the distance from the vertex number 1 to all other vertices of the graph.
// If the path to the corresponding vertex does not exist, instead of the path length print the number 30000.

// def bellman_ford(n, edges):
//     distance = [30000] * n
//     distance[0] = 0

//     for _ in range(n - 1):
//         for u, v, w in edges:
//             if distance[u - 1] != 30000 and distance[u - 1] + w < distance[v - 1]:
//                 distance[v - 1] = distance[u - 1] + w

//     return distance


// n, m = map(int, input().split())

// edges = [list(map(int, input().split())) for _ in range(m)]

// print(" ".join(map(str, bellman_ford(n, edges))))

#include <iostream>
#include <vector>

using namespace std;

const int INF = 30000;

struct Edge
{
    int from, to, weight;
};

int main()
{
    int n, m;
    cin >> n >> m;

    vector<Edge> edges(m);
    for (int i = 0; i < m; i++)
    {
        cin >> edges[i].from >> edges[i].to >> edges[i].weight;
    }

    vector<int> distance(n + 1, INF);
    distance[1] = 0;

    for (int i = 1; i <= n - 1; i++)
    {
        for (const Edge &edge : edges)
        {
            if (distance[edge.from] < INF)
            {
                distance[edge.to] = min(distance[edge.to], distance[edge.from] + edge.weight);
            }
        }
    }

    for (int i = 1; i <= n; i++) 
    {
        cout << distance[i] << " ";
    }
    cout << endl;

    return 0;
}