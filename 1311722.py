
def sum_digits(a):
	x = sum(a)
	print a, x
	if x >= 10:
		a = [int(d) for d in str(x)]
		return x + sum_digits(a)
	else:
		return x

if __name__ == '__main__':
	a = [11, 23, 9, 17, 20, 8, 5, 6]
	print sum_digits(a)


"""
int sum_digits(const int *a, int count)
{
    int x = 0;
    for (int i = 0; i < count; i++)
        x += a[i];
    if (x >= 10)
    {
        char buf[128];
        sprintf (buf, "%d", x);
        int tmp[128], i = 0;
        for (const char *cp = buf; *cp; cp++)
            tmp[i++] = *cp -'0';
        return x + sum_digits(tmp, i);
    }
    else
        return x;
}

void main()
{
    int result = sum_digits(11, 23, 9, 17, 20, 8, 5, 6);
    printf("%d\n", result);
}
"""
