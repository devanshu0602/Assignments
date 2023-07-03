#include <iostream>
#include <chrono>
#include <thread>
#include <cstdlib>
using namespace std;

void simulateTransmissionDelay()
{
    this_thread::sleep_for(chrono::seconds(2));
}

bool simulateNetworkLoss()
{
    return (rand() % 2) == 0;
}

void sendPacket(int sequenceNumber)
{
    cout << "Sender: Sending packet with sequence number: " << sequenceNumber << endl;
    simulateTransmissionDelay();
    if (simulateNetworkLoss())
    {
        cout << "Sender: Packet lost!" << endl;
        return;
    }
    cout << "Sender: Packet received at receiver!" << endl;
}

void receiveACK(int sequenceNumber)
{
    cout << "Receiver: Receiving ACK for packet with sequence number: " << sequenceNumber << endl;
    simulateTransmissionDelay();
    if (simulateNetworkLoss())
    {
        cout << "Receiver: ACK lost!" << endl;
        return;
    }
    cout << "Receiver: ACK sent back to sender!" << endl;
}

int main()
{
    const int windowSize = 4;
    const int totalPackets = 10;
    int base = 0;

    while (base < totalPackets)
    {
        for (int i = base; i < base + windowSize && i < totalPackets; i++)
        {
            sendPacket(i);
        }

        bool timeout = false;
        auto start = chrono::steady_clock::now();

        while (base < totalPackets && !timeout)
        {
            auto end = chrono::steady_clock::now();
            auto duration = chrono::duration_cast<chrono::seconds>(end - start);

            if (duration >= chrono::seconds(5))
            {
                cout << "Sender: Timeout occurred. Resending packets from base: " << base << endl;
                timeout = true;
            }
            else
            {
                for (int i = base; i < base + windowSize && i < totalPackets; i++)
                {
                    receiveACK(i);
                }

                if (simulateNetworkLoss())
                {
                    cout << "Sender: ACK lost. Resending packets from base: " << base << endl;
                    timeout = true;
                }
                else
                {
                    base += windowSize;
                }
            }
        }
    }

    cout << "\nDevanshu Gupta" << endl;
    cout << endl;
    return 0;
}
