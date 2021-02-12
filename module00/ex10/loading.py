from time import sleep, time
import sys
# from sys.stdout import write, flush

def ft_profress(listy: list):
    list_len = len(listy)
    list_d = len(str(list_len))
    start = time()
    for elem, i in enumerate(listy):
        pre = round((i / list_len) * 100)
        t = time() - start
        pred = t * (100 / (pre + 0.1))
        bar_pre = round(pre * 0.2)
        bar = "=" * bar_pre + (">" if bar_pre != 20 else "")
        sys.stdout.write("\rETA: {:>5.2f}s [{:3}%][{:<20}] {:{d}}/{} | elapsed time {:>5.2f}s".format(pred, pre, bar, i + 1, list_len, t, d=list_d))
        sys.stdout.flush()
        yield elem

if __name__ == "__main__":
    listy = range(10000)
    ret = 0

    for elem in ft_profress(listy):
        ret += (elem + 3) % 5
        sleep(0.00001)
    
    print()
    print(ret)