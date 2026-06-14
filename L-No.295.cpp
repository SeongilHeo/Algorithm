#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

class MedianFinder {
private:
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<int>> large;
public:
    MedianFinder()
    {

    }

    void addNum(int num)
    {
        small.push(num);

        large.push(small.top());
        small.pop();

        if (large.size() > small.size())
        {
            small.push(large.top());
            large.pop();
        }
    }

    double findMedian()
    {
        if (small.size() > large.size())
            return small.top();

        return (static_cast<double>(small.top()) + large.top()) / 2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

int main()
{
    MedianFinder medianFinder;

    medianFinder.addNum(1);
    medianFinder.addNum(2);
    cout << medianFinder.findMedian() << endl; // 1.5

    medianFinder.addNum(3);
    cout << medianFinder.findMedian() << endl; // 2

    return 0;
}