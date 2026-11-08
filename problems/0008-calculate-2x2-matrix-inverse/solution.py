def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a, b = matrix[0]
    c, d = matrix[1]
    area = a * d - c * b
    if area == 0:
        return None
    return [[d/area, -b/area], [-c/area, a/area]]