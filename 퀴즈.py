import random
number = random.randint(1,45)
def lotto():
    results = []
    for i in range(6):
        while len(results) <= 6 :
            number = random.randint(1,45)
            if number not in results :
                print(f"{results}에 해당 숫자가 없습니다.")
                results.append(number)
    results.sort()
    print(f"생성된 로또번호는 {results} 입니다.")

lotto()
