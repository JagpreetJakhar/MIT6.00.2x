def lecture_activities(N, aLecture):
    ans = []
    for trial in range(N):
        days = 1
        while (random.random() > aLecture.get_listen_prob()) or \
        (random.random() > aLecture.get_sleep_prob()) or \
        (random.random() > aLecture.get_fb_prob()) :
            days += 1
        ans.append(days)
    (mean, std) = get_mean_and_std(ans)
    return (round(mean, 3), round(1.96*std*2, 3))
