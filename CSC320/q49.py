# Question 49:
# Known background:

# C_r = alpha * F_r + (1 - alpha) * B_r
# C_g = alpha * F_g + (1 - alpha) * B_g
# C_b = alpha * F_b + (1 - alpha) * B_b
# C = alpha * F + (1 - alpha) * known_B
# C - known_B = alpha * (F - known_B)
known_B = imread("some_known_B.jpg")
def known_back(C, B, known_B=known_B):
    # We can use C as the "foreground" since it contains the foreground
    height, width, channels = C.shape[:2]
    alpha = zeros((height, width))
    new_C = zeros((height, width, channels))
    new_B = zeros((height, width, channels))
    foreground = zeros((height, width, channels))

    # Determines alpha
    for i in range(height):
        for j in range(width):
            # If background is the same
            alpha[i, j] = 1
            if (known_back[i, j] == C[i, j]):
                            alpha[i, j] = 0

            # Determine foreground and new background while in the loop
            foreground[i, j, 0] = C[i, j, 0] * alpha[i, j]
            foreground[i, j, 1] = C[i, j, 1] * alpha[i, j]
            foreground[i, j, 2] = C[i, j, 2] * alpha[i, j]

            new_B[i, j, 0] = B[i, j, 0] * (1 - alpha[i, j])
            new_B[i, j, 1] = B[i, j, 1] * (1 - alpha[i, j])
            new_B[i, j, 2] = B[i, j, 2] * (1 - alpha[i, j])

    # Determine new composite
    new_C = foreground + new_B

    return new_C

# Question 50:
# C_r = alpha * F_r
# C_g = alpha * F_g
# C_b = (1 - alpha) * B_b = B_b - alpha * B_b
# F_b = B_r = B_g = 0
blue_B = imread("some_blue_B.jpg");
def blue_back(C, B, blue_B=blue_B):
    # We can use C as the "foreground" since it contains the foreground
    height, width, channels = C.shape[:2]
    alpha = zeros((height, width))
    new_C = zeros((height, width, channels))
    new_B = zeros((height, width, channels))
    foreground = zeros((height, width, channels))

    """
    known_B... B[..., 0] = B[..., 1] = 0
    C[i, j, 0] = alpha[i, j] * F[i, j, 0] => C[i, j, 0] / alpha[i, j] = F[i, j, 0]
    C[i, j, 1] = alpha[i, j] * F[i, j, 1] => C[i, j, 1] / alpha[i, j] = F[i, j, 1]
    C[i, j, 2] = B[i, j, 2] - alpha[i, j] * B[i, j, 2] => (C[i, j, 2] - B[i, j, 2]) / B[i, j, 2] = -alpha[i, j] 
    """

    # Determines alpha
    for i in range(height):
        for j in range(width):
            # Determine alpha
            (blue_B[i, j, 2] - C[i, j, 2]) / blue_B[i, j, 2] = alpha[i, j]

            # Determine non blue foreground
            foreground[i, j, 0] = C[i, j, 0] / alpha[i, j]
            foreground[i, j, 1] = C[i, j, 1] / alpha[i, j]

            # Determine new background
            new_B[i, j, 0] = (1 - alpha[i, j]) * B[i, j, 0]
            new_B[i, j, 1] = (1 - alpha[i, j]) * B[i, j, 1]
            new_B[i, j, 1] = (1 - alpha[i, j]) * B[i, j, 1]

    return new_C