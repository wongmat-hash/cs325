res = []
def recurrence(n, k, sub_list, vis, last):
    global res
    if k == 0 and n == 0:
        res.append([s for s in sub_list])
        return

    if k < 0 or n < 0:
        return

    for i in range(last, 10):

        if not vis[i]:
            vis[i] = True
            sub_list.append(i)
            recurrence(n - i, k - 1, sub_list, vis, i + 1)
            sub_list.pop()
            vis[i] = False

def combination(n, k):
    if k * 9 < n:
        return []
    sub_list = []
    vis = [False for i in range(10)]
    recurrence(n, k, sub_list, vis, 1)
    return res
    
k = 3
n = 9
print(combination(n, k))
