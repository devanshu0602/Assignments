#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
    int childPid;

    childPid = fork(); // Create a child process

    if (childPid < 0)
    {
        fprintf(stderr, "Fork failed.\n");
        return 1;
    }
    else if (childPid == 0)
    {
        // Child process
        printf("Child process:\n");
        printf("PID: %d\n", getpid());
        printf("Parent PID: %d\n", getppid());
    }
    else
    {
        // Parent process
        printf("Parent process:\n");
        printf("PID: %d\n", getpid());
        printf("Child PID: %d\n", childPid);
    }

    return 0;
}
