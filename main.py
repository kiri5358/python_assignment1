import loop.while_mission as su
import fileio.fileio_mission as emp

def menu():
    prompt = '''
    1. while 실습문제
    2. fileio 실습문제
    9. 과제 실행 테스트 끝내기
'''
    while True:
        print(prompt)
        no = int(input('원하는 메뉴 번호 입력 : '))

        if no == 1:
            su.sungjuk_process()
        if no == 2:
            emp.emp_process()
        if no == 9:
            break


if __name__=='__main__':
   menu()