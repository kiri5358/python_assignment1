# path : loop\\while_mission.py
# module : loop.while_mission

def sungjuk_process():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
    
    prompt = '''
            *** 원하는 메뉴 번호를 선택하세요. ***
            1. 추가
            2. 삭제
            3. 출력
            4. 끝내기
        '''
    while True:
        print(prompt)
        menu = input('번호 : ')

        if menu == '1':
            sno = int(input('번호 : '))
            sname = input('이름 : ')
            score = int(input('점수 : '))

            sungjuk_list.append([sno, sname, score])
            print('학생정보를 추가했습니다.')

        if menu == '2':
            count = len(sungjuk_list)
            print(f"현재 저장된 아이템의 갯수는 {count}개 입니다.")
            idx = int(input("제거할 아이템의 순번 : "))
            
            if 0 < idx < 4:
                sungjuk_list.pop(idx)
                print(f'{idx}번 위치의 아이템이 제거되었습니다.')
                print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)} 입니다.')

            if 4 <= idx:
                print("순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.")

        if menu == '3':
            for i in range(len(sungjuk_list)):
                print(f'{i} : {sungjuk_list[i]}')

        if menu == '4':
            print('성적관리 프로그램이 종료되었습니다.')
            break
    
    
    
    return