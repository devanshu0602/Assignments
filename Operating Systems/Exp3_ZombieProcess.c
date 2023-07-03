// Child becomes Zombie as parent is sleeping when child process exits.

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    // Fork returns process id in parent process
    pid_t child_pid = fork();

    // Parent process
    if (child_pid > 0)
    {
        printf("PID: %d\n", getppid());
        printf("Inside Parent process.\n");
        sleep(50);
    }

    // Child process
    else
    {
        printf("PID: %d\n", getpid());
        printf("Inside Child process.\n");
        exit(0);
    }

    return 0;
}