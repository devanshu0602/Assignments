#include <iostream>
#include <vector>
using namespace std;

// Function to check if the current state is safe
bool isSafe(vector<vector<int>> &allocated, vector<vector<int>> &maximum, vector<int> &available, vector<int> &work)
{
    int numOfProcesses = allocated.size();
    int numOfResources = available.size();
    vector<bool> finish(numOfProcesses, false);

    // Copy the available resources into the work vector
    for (int i = 0; i < numOfResources; i++)
    {
        work[i] = available[i];
    }

    // Find an unfinished process whose needs can be satisfied with the available resources
    int count = 0;
    while (count < numOfProcesses)
    {
        bool found = false;
        for (int i = 0; i < numOfProcesses; i++)
        {
            if (!finish[i])
            {
                bool canAllocate = true;
                for (int j = 0; j < numOfResources; j++)
                {
                    if (maximum[i][j] - allocated[i][j] > work[j])
                    {
                        canAllocate = false;
                        break;
                    }
                }
                if (canAllocate)
                {
                    // Allocate the resources of process i
                    for (int j = 0; j < numOfResources; j++)
                    {
                        work[j] += allocated[i][j];
                    }
                    finish[i] = true;
                    found = true;
                    count++;
                    cout << "P" << i << " ";
                }
            }
        }
        // If no process can be allocated, the state is unsafe
        if (!found)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    cout << "\nDevanshu Gupta 21BCE0597" << endl;

    int numOfProcesses, numOfResources;
    cout << "\nEnter the number of processes: ";
    cin >> numOfProcesses;
    cout << "\nEnter the number of resources: ";
    cin >> numOfResources;

    vector<vector<int>> allocated(numOfProcesses, vector<int>(numOfResources));
    vector<vector<int>> maximum(numOfProcesses, vector<int>(numOfResources));
    vector<int> available(numOfResources);
    vector<int> work(numOfResources);

    // Allocated matrix
    cout << "\nEnter the allocation matrix:\n";
    for (int i = 0; i < numOfProcesses; i++)
    {
        for (int j = 0; j < numOfResources; j++)
        {
            cin >> allocated[i][j];
        }
    }

    // Maximum matrix
    cout << "\nEnter the maximum matrix:\n";
    for (int i = 0; i < numOfProcesses; i++)
    {
        for (int j = 0; j < numOfResources; j++)
        {
            cin >> maximum[i][j];
        }
    }

    // Available resources
    cout << "\nEnter the available resources:\n";
    for (int i = 0; i < numOfResources; i++)
    {
        cin >> available[i];
    }

    // Check if current state is safe
    if (isSafe(allocated, maximum, available, work))
    {
        cout << "\nThe system is in a safe state.\n";

        // Additional request after safe state
        cout << "\nEnter the additional request for a process (P_i):\n";
        int process;
        vector<int> request(numOfResources);
        cin >> process;
        cout << "\nEnter the resource request for P" << process << ":\n";
        for (int i = 0; i < numOfResources; i++)
        {
            cin >> request[i];
        }

        // Check if additional request can be granted
        bool canAllocate = true;
        for (int i = 0; i < numOfResources; i++)
        {
            if (request[i] > available[i] || request[i] > maximum[process][i] - allocated[process][i])
            {
                canAllocate = false;
                break;
            }
        }

        if (canAllocate)
        {
            // Simulate the allocation of the additional request
            for (int i = 0; i < numOfResources; i++)
            {
                available[i] -= request[i];
                allocated[process][i] += request[i];
            }

            // Check if the resulting state is still safe
            if (isSafe(allocated, maximum, available, work))
            {
                cout << "The additional request can be granted. The resulting state is safe.\n";
            }
            else
            {
                cout << "The additional request can be granted, but the resulting state is unsafe.\n";
            }
        }
        else
        {
            cout << "The additional request cannot be granted.\n";
        }
    }
    else
    {
        cout << "\nThe system is in an unsafe state.\n";
    }

    return 0;
}