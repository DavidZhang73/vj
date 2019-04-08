import support.SDUT

import config

code = '''
#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d %d",&a, &b);
    printf("%d\n",a+b);
    return 0;
}
'''
print(support.SDUT.Runner(config.accounts['SDUT'], 3, 1).judge(1000, 0, code))
