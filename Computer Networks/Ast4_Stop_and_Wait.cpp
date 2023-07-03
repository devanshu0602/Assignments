#include <iostream>
#include <chrono>
#include <thread>
#include <cstdlib>
using namespace std;

// generates delay of 2 secs
void transmissionDelay()
{
    this_thread::sleep_for(chrono::seconds(2));
}

// provides netwrok loss randomly
bool networkLoss()
{
    return (rand() % 10) == 0;
}

// message sender
void send(int message)
{
    cout << "Sender: Sending Msg -> " << message << endl;
    transmissionDelay();
    if (networkLoss())
    {
        cout << "Sender: Message sent." << endl;
        return;
    }
    cout << "Sender: Message received." << endl;
}

// message receiver
void receive(int message)
{
    cout << "Receiver: Receiving message -> " << message << endl;
    transmissionDelay();
    if (networkLoss())
    {
        cout << "Receiver: ACK lost." << endl;
        return;
    }
    cout << "Receiver: Message received. ACK sent." << endl;
}

int main()
{
    int message[] = {0, 5, 9, 7};
    int len = sizeof(message) / sizeof(int);

    for (int i = 0; i < len; i++)
    {
        send(message[i]);
        receive(message[i]);
    }

    cout << "\nDevanshu Gupta [21BCE0597]" << endl;
    cout << endl;
    return 0;
}