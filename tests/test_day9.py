from Day9.day9 import move_head, move_tail, main
from operator import add


def test_move_head():
    # Arrange and Act
    new_head_pos_U = move_head(dir="U", old_head=[0, 0])
    new_head_pos_D = move_head(dir="D", old_head=[0, 0])
    new_head_pos_L = move_head(dir="L", old_head=[0, 0])
    new_head_pos_R = move_head(dir="R", old_head=[0, 0])

    # Assert
    assert new_head_pos_U == [0, 1]
    assert new_head_pos_D == [0, -1]
    assert new_head_pos_L == [-1, 0]
    assert new_head_pos_R == [1, 0]


def test_move_tail():
    # Test all positions when tail doesn't move   
    # Change tail starting position to be in 3x3 grid
    for tail_row in range(-1, 2):
        for tail_col in range(-1, 2):
            tail_pos = [tail_row, tail_col]

            # Check all head positions in 3x3 grid around the tail position.
            for row in range(tail_pos[0] -1, tail_pos[0] + 2):
                for col in range(tail_pos[1] -1, tail_pos[1] + 2):
                    new_tail_pos = move_tail(new_head=[row, col], old_tail=tail_pos)
                    assert new_tail_pos == tail_pos
    
            # Test moving away when inline.

            new_tail_pos_U = move_tail(new_head=list( map(add, tail_pos, [0, 2])), old_tail=tail_pos)
            new_tail_pos_D = move_tail(new_head=list( map(add, tail_pos, [0, -2])), old_tail=tail_pos)
            new_tail_pos_L = move_tail(new_head=list( map(add, tail_pos, [-2, 0])), old_tail=tail_pos)
            new_tail_pos_R = move_tail(new_head=list( map(add, tail_pos, [2, 0])), old_tail=tail_pos)

            assert new_tail_pos_U == list( map(add, tail_pos, [0, 1]))
            assert new_tail_pos_D == list( map(add, tail_pos, [0, -1]))
            assert new_tail_pos_L == list( map(add, tail_pos, [-1, 0]))
            assert new_tail_pos_R == list( map(add, tail_pos, [1, 0]))

            # Test moving diagonally
            assert move_tail(new_head=list( map(add, tail_pos, [1, 2])), old_tail=tail_pos) == move_tail(new_head=list( map(add, tail_pos, [2, 1])), old_tail=tail_pos) == list( map(add, tail_pos, [1, 1]))
            assert move_tail(new_head=list( map(add, tail_pos, [1, -2])), old_tail=tail_pos) == move_tail(new_head=list( map(add, tail_pos, [2, -1])), old_tail=tail_pos) == list( map(add, tail_pos, [1, -1]))
            assert move_tail(new_head=list( map(add, tail_pos, [-1, -2])), old_tail=tail_pos) == move_tail(new_head=list( map(add, tail_pos, [-2, -1])), old_tail=tail_pos) == list( map(add, tail_pos, [-1, -1]))
            assert move_tail(new_head=list( map(add, tail_pos, [-1, 2])), old_tail=tail_pos) == move_tail(new_head=list( map(add, tail_pos, [-2, 1])), old_tail=tail_pos) == list( map(add, tail_pos, [-1, 1]))
    

def test_sample_input1():
    ans = main("Day9/input_test1.txt", 2)
    assert ans == 13
