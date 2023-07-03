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

void sendPacket(int sequenceNumber, const string &packetData)
{
    cout << "Sender: Sending packet with sequence number: " << sequenceNumber << endl;

    // Simulate transmission delay
    transmissionDelay();

    // Simulate network loss
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

    // Simulate transmission delay
    transmissionDelay();

    // Simulate network loss
    if (networkLoss())
    {
        cout << "Receiver: ACK lost!" << endl;
        return;
    }

    cout << "Receiver: ACK sent back to sender!" << endl;
}

int main()
{
    int sequenceNumber = 0;
    string packetData = "Hello, receiver!";

    while (true)
    {
        sendPacket(sequenceNumber, packetData);

        auto start_time = chrono::steady_clock::now();
        while (true)
        {
            auto end_time = chrono::steady_clock::now();
            auto duration = chrono::duration_cast<chrono::seconds>(end_time - start_time);

            if (duration >= chrono::seconds(5))
            {
                cout << "Sender: Timeout occurred. Resending packet with sequence number: " << sequenceNumber << endl;
                break;
            }

            receiveACK(sequenceNumber);

            if (networkLoss())
            {
                cout << "Sender: ACK lost. Resending packet with sequence number: " << sequenceNumber << endl;
                break;
            }

            sequenceNumber++;
            break;
        }

        // Break the loop if all packets have been sent
        if (sequenceNumber > 5)
        {
            break;
        }
    }

    cout << "\nDevanshu Gupta [21BCE0597]" << endl;
    cout << endl;
    return 0;
}
