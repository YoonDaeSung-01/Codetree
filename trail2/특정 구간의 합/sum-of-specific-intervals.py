# 전역 변수로 사용할 수열과 누적합 배열 선언
# 함수 외부(전역 공간)에 선언하여 어디서든 접근할 수 있도록 합니다.
A = []
prefix_sum = []

def change_to_prefix_sum(n, input_array):
    """
    입력받은 배열을 전역 변수 A에 저장하고,
    O(1)만에 구간 합을 구하기 위한 누적합 배열(prefix_sum)을 생성하는 함수
    """
    global A, prefix_sum
    
    # 1-based index를 위해 맨 앞에 0을 붙여 전역 변수에 저장
    A = [0] + input_array
    
    # 누적합 배열 초기화 (크기는 n + 1)
    prefix_sum = [0] * (n + 1)
    
    # prefix_sum[i]에는 1번째부터 i번째 원소까지의 합이 저장됩니다.
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

def get_range_sum(a1, a2):
    """
    전역 변수 prefix_sum을 이용하여 a1번째부터 a2번째까지의 합을 구하는 함수
    """
    # a1부터 a2까지의 합은 (1~a2까지의 합) - (1~a1-1까지의 합)과 같습니다.
    return prefix_sum[a2] - prefix_sum[a1 - 1]


# --- 메인 코드 영역 ---
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 전역 변수 초기화 및 누적합 계산 함수 호출
change_to_prefix_sum(n, arr)

# M개의 쿼리를 처리하며 결과 출력
for _ in range(m):
    a1, a2 = map(int, input().split())
    print(get_range_sum(a1, a2))