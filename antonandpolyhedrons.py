n = int(input())
faces = 0

for _ in range(n):
    shape = input()

    if shape == 'Tetrahedron':
        faces += 4
    if shape == 'Cube':
        faces += 6
    if shape == 'Octahedron':
        faces += 8
    if shape == 'Dodecahedron':
        faces += 12
    if shape == 'Icosahedron':
        faces += 20

print(faces)
