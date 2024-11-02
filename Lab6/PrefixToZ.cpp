#include <cstring>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> P(N);
    vector<int> Z(N);
    for (int i = 0; i < N; i++)
    {
        cin >> P[i];
    }
    for(int i = 1; i < N; i++)
    {
        if(P[i])
        {
            Z[i - P[i] + 1] = P[i];
        }
    }
    Z[0] = 0;
        
    if(Z[1])
    {
        for(int i = 1; i < Z[1]; i++)
        {
            Z[i + 1] = Z[1] - i;
        }
    }

    int t;
    for(int i = Z[1] + 1; i < N - 1; i++)
    {
        t = i;
        if(Z[i] && !Z[i + 1])
        {
            for(int j = 1; j < Z[i] && Z[i + j] <= Z[j]; j++)
            {
                    Z[i + j] = min(Z[j], Z[i] - j);
                    t = i + j;
            }
        }
        i = t;  
    }
    for (int i = 0; i < N; i++)
    {
        cout << Z[i] << " ";
    }
    cout << endl;
    return 0;
}