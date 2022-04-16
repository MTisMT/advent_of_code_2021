## Part 1
import numpy as np
with open("day1.txt") as f:
    seq = [int(l.strip()) for l in f]
seq_1step = [0]
seq_1step += seq[:len(seq)-1]
diffs = np.array(seq)-np.array(seq_1step)
answer_1 = sum(diffs>0)-1
print("Answer of part 1",answer_1)

## Part 2
seq_w3 = [seq[i]+seq[i+1]+seq[i+2] for i in range(len(seq)-2)] 
seq_1step_w3 = [0]
seq_1step_w3 += seq_w3[:len(seq_w3)-1]
diffs = np.array(seq_w3)-np.array(seq_1step_w3)
answer_2 = sum(diffs>0)-1
print("Answer of part 2",answer_2)
