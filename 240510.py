import random

def ran_num():
    results = []
    while len(results) < 6 :
        ran_num = random.randint(1,45)
        if ran_num not in results:
            results.append(ran_num)

    return results

results = ran_num()
print("생성된 로또 번호는",ran_num(),"입니다")



