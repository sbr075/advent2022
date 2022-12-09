def sol(moves : list[str], n_knots : int = 2):
    knots = [(0, 0) for _ in range(n_knots)]

    tiles = []
    for move in moves:
        motion, steps = move.split()
        steps = int(steps)

        for _ in range(steps):
            hY, hX = knots[0]
            match motion:
                case "R": hX += 1
                case "L": hX -= 1
                case "U": hY += 1
                case "D": hY -= 1

            knots[0] = (hY, hX)
            for knot in range(1, n_knots):
                hY, hX = knots[knot - 1]
                tY, tX = knots[knot]

                dY, dX = hY - tY, hX - tX

                # More than two tiles away in Y direction
                if abs(dY) > 1:
                    tY += 1 if dY > 0 else -1

                    # Not on same row
                    if abs(dX) != 0:
                        # Move diagonally
                        tX += 1 if dX > 0 else -1

                # More than two tiles away in X direction
                elif abs(dX) > 1:
                    tX += 1 if dX > 0 else -1

                    # Not on same column
                    if abs(dY) != 0:
                        # Move diagonally
                        tY += 1 if dY > 0 else -1

                knots[knot] = (tY, tX)

                if knot == n_knots - 1:
                    tiles.append((tY, tX))

    return len(set(tiles))

with open("input.txt", "r") as file:
    moves = file.readlines()

print(sol(moves, 2))
print(sol(moves, 10))