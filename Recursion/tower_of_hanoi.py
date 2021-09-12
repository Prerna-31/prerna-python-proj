"""
Hypothesis: TOH(N ,pole1, pole2, pole3)   -->  moved N disks from pole1 to pole 2 usng pole3
            TOH(N-1, pole1, pole2, pole3)  --> moved N-1 disks from pole 1 to pole 2 using pole3
Induction:  TOH(N-1,pole1, Pole3, pole2); Move Nth disk from pole 1 to pole2 and the last stp would be, moving n-1 disks from pole3 to pole2 via pole1.
Base Condition: if N== 1, then move N from pole 1 to pole2
"""

def TowerOfHanoi(N, S, D, H):
    if(N == 1):
        print("Moving disk {} from pole {} to pole {}".format(N, S, D))
        return

    TowerOfHanoi(N-1, S, H, D)
    print("Moving {}th disk from pole {} to pole {}".format(N, S, D))
    TowerOfHanoi(N-1, H, D, S )

    return count

N = 3
count = 0
TowerOfHanoi(N, 'Source', 'Destination', 'Helper')
print("The total number of steps required to move {} disks from source to destination pole is {}".format(N,count))