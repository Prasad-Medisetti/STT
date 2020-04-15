def nearly_equal(s1, s2):
    l = len(s1) if len(s1) < len(s2) else  len(s2)
    i = 0
    cnt = 0
    for i in range(l):
        if s1[i] == s2[i]:
            continue
        else:
            cnt += 1
    print("Nearly Equal") if cnt == 1 or cnt == 0 else print("Not Nearly Equal")