// Дано N отрезков на числовой прямой и M точек на этой же прямой.
// Для каждой из данных точек определите, скольким отрезкам она принадлежит.
// Точка x считается принадлежащей отрезку с концами a и b, если выполняется двойное неравенство
// min(a, b) ≤ x ≤ max(a, b).

// Input
// Первая строка входного файла содержит два целых числа N – число отрезков и M – число точек (1 ≤ N, M ≤ 10^5). 
// В следующих N строках по два целых числа a_i и b_i – координаты концов соответствующего отрезка.
// В последней строке M целых чисел – координаты точек. Все числа во входном файле не превосходят по модулю 10^9.
// Output
// В выходной файл выведите M чисел – для каждой точки количество отрезков, в которых она содержится.
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Event {
    int coord;
    char type;
    int index;
    
    bool operator<(const Event& other) const {
        if (coord == other.coord) {
            return type < other.type;
        }
        return coord < other.coord;
    }
};

int main() {
    int N, M;
    cin >> N >> M;

    vector<pair<int, int>> segments(N);
    for (int i = 0; i < N; ++i) {
        cin >> segments[i].first >> segments[i].second;
    }

    vector<int> points(M);
    for (int i = 0; i < M; ++i) {
        cin >> points[i];
    }

    vector<Event> events;
    vector<int> result(M, 0);

    for (const auto& segment : segments) {
        int a = min(segment.first, segment.second);
        int b = max(segment.first, segment.second);
        events.push_back({a, 'L', -1});
        events.push_back({b, 'R', -1});
    }
    
    for (int i = 0; i < M; ++i) {
        events.push_back({points[i], 'P', i});
    }
    
    sort(events.begin(), events.end());
    
    int active_segments = 0;
    
    for (const auto& event : events) {
        if (event.type == 'L') {
            active_segments++;
        } else if (event.type == 'R') {
            active_segments--;
        } else {
            result[event.index] = active_segments;
        }
    }

    for (int res : result) {
        cout << res << " ";
    }
    cout << endl;
    return 0;
}