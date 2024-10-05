// # As you know, Andry Sergeevich is an ardent collector of butterflies.
// # He has a huge collection, the exhibits of which are collected from around the world.
// # We assume that there are 2 * 10^9 species of butterflies in the world.

// # In order not to get confused, Andrei Sergeevich assigned a unique number to each species.
// # Butterfly numbering always starts from one.
// # Now he wants to know if there is a butterfly with a number k in his collection, or he will have to get it, spending a lot of effort and money.

// # Input
// # First line contains the number of species of butterflies n (1 ≤ n ≤ 10^5) in the collection of Andrei Sergeevich.
// # Next line contains n numbers in ascending order - the numbers of butterfly species in the collection.
// # All kinds of butterflies in the collection have different numbers.
// # Third line contains the number of species of butterflies m (1 ≤ m ≤ 10^5), about which Andrei Sergeevich wants to know if he has them in the collection or not.
// # The last line contains m numbers - numbers of species of butterflies, the presence of which must be checked.
// # Output
// # Print m lines. For each query print "YES", if the butterfly with the given number exists in his collection and "NO" otherwise.

#include <iostream>
using namespace std;

string binarySearch(int arr[], int left, int right, int x) 
{
    if (right >= left) { 
        int mid = left + (right - left) / 2; 
        if (arr[mid] == x) 
            return "YES";
        if (arr[mid] > x) 
            return binarySearch(arr, left, mid - 1, x); 
        return binarySearch(arr, mid + 1, right, x); 
    }
    return "NO";
} 

int main()
{
    int n;
    cin >> n;
    int collection[n];
    for (int i = 0; i < n; i++)
    {
        cin >> collection[i];
    }
    int m;
    cin >> m;
    int numbers[m];
    for (int i = 0; i < m; i++)
    {
        cin >> numbers[i];
        cout << binarySearch(collection, 0, n, numbers[i]) << endl;
    }
}
    