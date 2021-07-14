## Set Operation

# 오늘 구현할 내용은 집합 프로그램을 작성하는 것입니다. 

# - 집합 생성 e.g) Set.new(["a", "b"])
# - 원소 추가 e.g) A.add("b")
# - 원소 제거 e.g) A.delete("a")
# - 합집합 기능 e.g) union(set A, set B)
# - 교집합 기능 e.g) intersection(set A, set B)
# - 원소인지 확인하는 기능 e.g) is_member

s1 = set(["a", "b"])
print(f"집합생성: {s1}")

s1.add("c")
print(f"원소추가: {s1}")

s1.remove("a")
print(f"원소제거: {s1}")

s2 = set(["a", "b", "d"])

union = s1 | s2
print(f"합집합: {union}")

intersect = s1 & s2
print(f"교집합: {intersect}")

print(f"s1에서 a 원소확인 {'a' in s1}")
print(f"s1에서 b 원소확인 {'b' in s1}")
