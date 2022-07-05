#ifdef _WIN32
#define LIBRARY_API __declspec(dllexport)
#else
#define LIBRARY_API 
#endif

#include <stdlib.h>


LIBRARY_API double *add_vec3(double *a, double *b)
{
    double *res = malloc(sizeof(double) * 3);

    for (int i = 0; i < 3; ++i)
    {
        res[i] = a[i] + b[i];
    }

    return res;
}
