from Day10.day10 import main


def test_sample_input2():
    ans = main("Day10/input_test2.txt")
    assert ans[0] == 13140

def test_sample_input2_CRT():
    ans = main("Day10/input_test2.txt")
    assert ans[1].rstrip() == "##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######....."