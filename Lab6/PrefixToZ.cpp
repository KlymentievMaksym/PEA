#include <cstring>
#include <vector>
#include <iostream>

using namespace std;

vector<int> prefix_to_z_function(const vector<int>& pi) {
    int n = pi.size();
    vector<int> z(n, 0);
    for (int i = 1; i < n; i++) {
        if (pi[i] > 0) {
            int j = i - pi[i] + 1;
            z[j] = max(z[j], pi[i]);
        }
    }
    for (int i = 1; i < n; i++) {
        if (z[i] > 0) {
            for (int j = 1; j < z[i] && i + j < n; j++) {
                if (z[i + j] < z[i] - j) {
                    z[i + j] = z[i] - j;
                } else {
                    break;
                }
            }
        }
    }
    return z;
}

int main() {
    int n;
    cin >> n;
    vector<int> pi(n);
    for (int i = 0; i < n; i++) {
        cin >> pi[i];
    }
    vector<int> z = prefix_to_z_function(pi);
    for (int i = 0; i < n; i++) {
        cout << z[i] << " ";
    }
    cout << endl;
    return 0;
}
