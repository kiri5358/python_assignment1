# path : fileio\\fileio_mission.py
# module : fileio.fileio_misson

import os

def emp_process():
    emp_dict = {}

    prompt = '''
        *** 직원 정보 관리 서비스 ***
        1. 새 직원정보 추가
        2. 직원정보 삭제
        3. 전체 출력
        4. 파일에 저장
        5. 파일로 부터 직원정보 읽어오기
        9. 서비스 끝내기
    '''
    
    while True:
        print(prompt)
        menu = input("메뉴 번호 선택 : ")

        if menu == 1:
            empid = input("사번 : ")
            empname = input("이름 : ")
            empno = input("주민번호 : ")
            email = input("이메일 : ")
            phone = input("전화번호 : ")
            salary = int(input("급여 : "))
            job = input("직급 : ")
            dept = input("부서 : ")

            emp_dict[empid] = [empid, empname, empno, email, phone, salary, job, dept]
            print(f"==> {empid}번 사원 정보가 추가되었습니다.")

        if menu == 2:
            del_id = input("삭제할 사번 : ")
            if del_id in emp_dict:
                del emp_dict[del_id]
                print(f"==> {del_id} 번 사번의 직원 정보가 삭제되었습니다.")

        if menu == 3:
            print("--- 전체 직원 정보 ---")
            for eid in emp_dict:
                print(f"{eid} : {emp_dict[eid]}")
        
        if menu == '4':
           filename = "employees.dat"
           with open(filename, "w", encoding="utf-8") as f:
                f.write(str(emp_dict))
                print(f"==> {filename} 파일에 성공적으로 저장되었습니다.")

        if menu == '5':
            filename = "employees.dat"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                    emp_dict = eval(content)
            print(f"==> {filename} 파일을 성공적으로 읽어왔습니다.")
            for eid in emp_dict:
                print(f"{eid} : {emp_dict[eid]}")

        if menu == '9':
            print("직원 관리 프로그램을 종료합니다.")
            break

    return