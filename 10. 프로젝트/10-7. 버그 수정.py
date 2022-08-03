balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("ball : ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons : ", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            break
    else: # weapons 에서 받아올 값이 없을 때, 바깥 for 문 기능을 유지함 
        continue
    print("바깥 for 문 break")
    break # if 내 break 를 타지 않고선 이 break 를 탈 수 없음