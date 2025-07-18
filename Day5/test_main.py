from main import add
 
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 3

if __name__=="__main__":
    test_add()

    print("All test cases passed")