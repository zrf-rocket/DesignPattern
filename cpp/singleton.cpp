// ccpp.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
/*
单例模式：确保一个类只有一个实例，而且自行实例化并向整个系统提供这个实例
单例模式的主要作用是确保一个类只有一个实例存在。单例模式可以用在建立目录、数据库连接等需要单线程操作的场合，用于实现对系统资源的控制。





*/

#include <iostream>


int main()
{
    std::cout << "Hello World!\n";
}






//懒汉单例模式 第一次引用类时，才进行对象实例化。
//非线程安全的懒汉单例模式


// 线程安全的懒汉单例模式


//饿汉单例模式
//饿汉式：线程安全，注意一定要在合适的地方去delete它
class Singleton
{
public:
    static Singleton* getInstance();
private:
    Singleton() {};   //构造函数私有化
    Singleton(const Singleton&) = delete; //明确拒绝
    Singleton& operator = (const Singleton) = delete; //明确拒绝

    static Singleton* m_pSingleton;
};

Singleton* Singleton::m_pSingleton = new Singleton();
Singleton* Singleton::getInstance()
{
    return m_pSingleton;
}






















// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
