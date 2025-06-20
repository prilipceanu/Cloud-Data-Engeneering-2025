## V1
def fibonacci(n):
    if n <= 0:
        return "Numărul trebuie să fie pozitiv."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def test_fibonacci():
    # Teste pentru valori cunoscute
    assert fibonacci(1) == 0, "Testul pentru n=1 a eșuat"
    assert fibonacci(2) == 1, "Testul pentru n=2 a eșuat"
    assert fibonacci(3) == 1, "Testul pentru n=3 a eșuat"
    assert fibonacci(4) == 2, "Testul pentru n=4 a eșuat"
    assert fibonacci(5) == 3, "Testul pentru n=5 a eșuat"
    assert fibonacci(6) == 5, "Testul pentru n=6 a eșuat"
    assert fibonacci(10) == 34, "Testul pentru n=10 a eșuat"
    print("Toate testele au trecut cu succes!")

test_fibonacci()