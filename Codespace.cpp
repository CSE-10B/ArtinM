#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    vector<int> value_storage;
    for (int i = 0; i < t; i++) {
        int nums;
        cin >> nums;
        value_storage.push_back(nums);
    }

    vector<int> kept;
    for (int i = 0; i < (int)value_storage.size(); i++) {
        if (i % 2 == 0) kept.push_back(value_storage[i]);
    }
    value_storage = kept;

    for (int x : value_storage) cout << x << " ";
    cout << "\n";
}