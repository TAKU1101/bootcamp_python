from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

if __name__ == '__main__':
    l = ft_map(lambda x: x + 2, [2, 3])
    print(l)

    l = ft_filter(lambda x: x < 0, [2, -3, -4, 1, 0])
    print(l)

    l = ft_reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print(l)
