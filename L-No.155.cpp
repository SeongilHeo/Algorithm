#include <vector>
class MinStack {
private:
    std::vector<int> values_;
    std::vector<int> mins_;

public:
    MinStack()
    {

    }

    void push(int value)
    {
        values_.push_back(value);

        if (mins_.empty() || value <= mins_.back())
        {
            mins_.push_back(value);
        }
    }

    void pop()
    {
        if (values_.back() == mins_.back())
        {
            mins_.pop_back();
        }

        values_.pop_back();
    }

    int top()
    {
        return values_.back();
    }

    int getMin()
    {
        return mins_.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */