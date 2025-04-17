def calculate_distance(parallax_arcseconds):
    if parallax_arcseconds == 0:
        print(" 연주시차가 0이면 거리를 계산할 수 없어요. (무한대가 되기 때문이죠!)")
        return None
    else:
        distance = 1 / parallax_arcseconds
        print(f" 계산된 별까지의 거리는 약 {distance:.2f} 파섹입니다. ")
        return distance

def verify_accuracy(calculated_distance, true_distance):
    if calculated_distance is None:
        print("오차를 계산할 수 없습니다.")
        return

    error = abs(calculated_distance - true_distance)
    relative_error = (error / true_distance) * 100
    print(f"실제 거리와의 차이는 약 {error:.2f} 파섹입니다.")
    print(f"상대 오차: {relative_error:.2f}%")

def explain_units():
    print("\n단위 설명")
    print("-" * 40)
    print(" '각초' (arcsecond):")
    print("   각도의 단위로, 1도(degree)의 1/3600 크기예요.")
    print("   (예: 시계 바늘이 1도 움직였다고 해도, 그걸 다시 3600등분한 것 중 하나가 '1초각')")

    print("\n '파섹' (parsec):")
    print("   천문학에서 쓰는 거리 단위예요.")
    print("   1파섹은 약 3.26광년 또는 약 30조 km입니다.")
    print("   (빛의 속도로 3년 넘게 가야 도착하는 거리!)")
    print("-" * 40)
    print("이 프로그램은 별이 보이는 위치 변화(연주시차)를 통해 파섹 단위로 거리를 계산해줍니다.\n")

def main():
    print("별까지의 거리 계산기")
    print("-" * 40)
    print("이 프로그램은 별의 '연주시차'를 이용해\n지구에서 그 별까지의 거리를 계산해줍니다.")
    print("연주시차란? 지구가 태양을 한 바퀴 돌 때, 별이 보이는 위치가 조금 바뀌는 현상이에요.")
    explain_units()

    try:
        parallax_input = input("연주시차를 각초(arcseconds) 단위로 입력하세요 (예: 0.379): ")
        parallax_arcseconds = float(parallax_input)
    except ValueError:
        print("❗ 숫자를 정확히 입력해주세요.")
        return

    distance = calculate_distance(parallax_arcseconds)

    try:
        true_input = input("참고용으로, 별의 실제 거리(파섹)를 입력해주세요 (예: 2.64): ")
        true_distance = float(true_input)
    except ValueError:
        print(" 숫자를 정확히 입력해주세요.")
        return

    verify_accuracy(distance, true_distance)

    print("\n감사합니다! 신비로운 우주여행 되세요. ")

if __name__ == "__main__":
     main()