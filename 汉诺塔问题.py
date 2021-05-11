def moveDisk(height, fromPole, toPole):
        print(f"moving disk[{height}] from {fromPole} to {toPole}")


def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, withPole, fromPole, toPole)


moveTower(3, "#1", "#2", "#3")
