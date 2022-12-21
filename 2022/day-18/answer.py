import argparse


DELTA = [
    (-1, 0, 0),     # top face
    (0, -1, 0),     # left face
    (0, 0, -1),     # back face
    (1, 0, 0),      # bottom face
    (0, 1, 0),      # right face
    (0, 0, 1)       # front face
]


def get_faces(x, y, z):
    # faces are identified by their diagonals
    faces = [
        ((x, y, z), (x, y+1, z+1)),      # top face
        ((x, y, z), (x+1, y, z+1)),      # left face
        ((x, y, z), (x+1, y+1, z)),      # back face
        ((x+1, y+1, z+1), (x+1, y, z)),  # bottom face
        ((x+1, y+1, z+1), (x, y+1, z)),  # right face
        ((x+1, y+1, z+1), (x, y, z+1)),  # front face
    ]

    return [tuple(sorted(f)) for f in faces]


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        cubes = [map(int, line.split(',')) for line in lines]
        faces = set()
        for cube in cubes:
            for f in get_faces(*cube):
                if f in faces:
                    faces.remove(f)
                else:
                    faces.add(f)
        print(len(faces))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        cubes = set([tuple(map(int, line.split(','))) for line in lines])
        faces = set(f for c in cubes for f in get_faces(*c))
        points = [p for f in faces for p in f]

        x_min = min(points, key=lambda p: p[0])[0]-1
        x_max = max(points, key=lambda p: p[0])[0]

        y_min = min(points, key=lambda p: p[1])[1]-1
        y_max = max(points, key=lambda p: p[1])[1]

        z_min = min(points, key=lambda p: p[2])[2]-1
        z_max = max(points, key=lambda p: p[2])[2]

        def is_in_range(x, y, z):
            return (
                x_min <= x <= x_max and
                y_min <= y <= y_max and
                z_min <= z <= z_max
            )

        water = set()
        exterior_faces = set()
        q = [(x_min, y_min, z_min)]

        # Simulate water flow and track which cube faces it can reach
        while q != []:
            p = q.pop()
            if p in water or not is_in_range(*p):
                continue
            water.add(p)
            for d, water_face in zip(DELTA, get_faces(*p)):
                if water_face in faces:
                    # The water has reached one of the cube faces
                    exterior_faces.add(water_face)
                else:
                    # Otherwise, the water can keep traveling in the direction of this face
                    q.append(tuple(a + b for a, b in zip(p, d)))

        print(len(exterior_faces))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
