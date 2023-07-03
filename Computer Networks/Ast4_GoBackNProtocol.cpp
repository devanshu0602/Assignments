#include <iostream>
#include <vector>
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

void sendPacket(int sequenceNumber, const string &packetData)
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
    const int windowSize = 4;
    const int totalPackets = 8;
    int base = 0;
    int nextSeqNum = 0;
    vector<string> packetData = {"Packet 0", "Packet 1", "Packet 2", "Packet 3", "Packet 4", "Packet 5", "Packet 6", "Packet 7", "Packet 8", "Packet 9"};

    while (base < totalPackets)
    {
        for (int i = base; i < base + windowSize && i < totalPackets; i++)
        {
            sendPacket(i, packetData[i]);
            nextSeqNum++;
        }

        bool timeout = false;
        auto start = chrono::steady_clock::now();

        while (base < nextSeqNum && !timeout)
        {
            auto end = chrono::steady_clock::now();
            auto duration = chrono::duration_cast<chrono::seconds>(end - start);

            if (duration >= chrono::seconds(5))
            {
                cout << "Sender: Timeout occurred. Resending packets from base: " << base << endl;
                timeout = true;
                nextSeqNum = base; // Go back to the base packet and resend from there
            }
            else
            {
                for (int i = base; i < nextSeqNum; i++)
                {
                    receiveACK(i);
                }

                if (networkLoss())
                {
                    cout << "Sender: ACK lost. Resending packets from base: " << base << endl;
                    timeout = true;
                    nextSeqNum = base; // Go back to the base packet and resend from there
                }
                else
                {
                    base = nextSeqNum; // Move the base to the next expected ACK
                }
            }
        }
    }

    cout << "\nDevanshu Gupta [21BCE0597]" << endl;
    cout << endl;
    return 0;
}
