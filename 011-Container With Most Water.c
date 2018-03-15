int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}

int maxArea(int* height, int heightSize) {
    int maximum_area = 0;
    int left = 0;
    int right = heightSize - 1;

    while (left < right)
    {
        maximum_area = max(maximum_area, min(height[left], height[right])*(right-left));
        if (height[left] > height[right])
            right--;
        else
            left++;
    }

    return maximum_area;
}