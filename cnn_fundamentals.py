# 1. Manual Convolution

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

# Image dimensions
image_rows = len(image)
image_cols = len(image[0])

# Kernel dimensions
kernel_rows = len(kernel)
kernel_cols = len(kernel[0])

# Output dimensions
output_rows = image_rows - kernel_rows + 1
output_cols = image_cols - kernel_cols + 1

feature_map = []

print("=" * 60)
print("MANUAL CONVOLUTION")
print("=" * 60)

for i in range(output_rows):

    output_row = []

    for j in range(output_cols):

        # Extract region
        region = []

        for r in range(kernel_rows):
            row = []

            for c in range(kernel_cols):
                row.append(image[i + r][j + c])

            region.append(row)

        print("\nRegion:")
        for row in region:
            print(*row)

        print("\nKernel:")
        for row in kernel:
            print(*row)

        # Calculate convolution
        total = 0
        calculations = []

        for r in range(kernel_rows):
            for c in range(kernel_cols):

                value = region[r][c]
                kernel_value = kernel[r][c]

                result = value * kernel_value
                total += result

                calculations.append(
                    f"{value}*{kernel_value}"
                )

        print("\nCalculation:")
        print(" + ".join(calculations))

        print("\nOutput =", total)

        output_row.append(total)

    feature_map.append(output_row)


print("\n" + "=" * 60)
print("FINAL FEATURE MAP")
print("=" * 60)

for row in feature_map:
    print(row)