#include <iostream>
#include <chrono>
#include <thread>
#include <cstdlib>
using namespace std;

void transmissionDelay()
{
    this_thread::sleep_for(chrono::seconds(2));
}

bool networkLoss()
{
    return (rand() % 2) == 0;
}

void sendPacket(int sequenceNumber, int windowSize)
{
    cout << "Sender: Sending packet with sequence number: " << sequenceNumber << endl;
    transmissionDelay();

    if (networkLoss())
    {
        cout << "Sender: Packet lost!" << endl;
        return;
    }

    cout << "Sender: Packet received at receiver!" << endl;
}

void receiveACK(int sequenceNumber)
{
    cout << "Receiver: Receiving ACK for packet with sequence number: " << sequenceNumber << endl;
    transmissionDelay();

    if (networkLoss())
    {
        cout << "Receiver: ACK lost!" << endl;
        return;
    }

    cout << "Receiver: ACK sent back to sender!" << endl;
}

int main()
{
    const int totalPackets = 5;
    int base = 0;
    int sequenceNumber = 0;
    int transmissionDelay = 2;
    int propagationDelay = 1;

    while (base < totalPackets)
    {
        int windowSize = (transmissionDelay + propagationDelay) / transmissionDelay;

        for (int i = base; i < base + windowSize && i < totalPackets; i++)
        {
            sendPacket(i, windowSize);
        }

        bool timeout = false;
        auto start = chrono::steady_clock::now();

        while (base < totalPackets && !timeout)
        {
            auto end = chrono::steady_clock::now();
            auto duration = chrono::duration_cast<chrono::seconds>(end - start);

            if (duration >= chrono::seconds(transmissionDelay))
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

                if (networkLoss())
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

    cout << "\nDevanshu Gupta [21BCE0597]" << endl;
    cout << endl;
    return 0;
}
