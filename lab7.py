def pad_image(img, pad_h, pad_w):
    h = len(img)
    w = len(img[0])
    
    padded = []
    
    # thêm dòng trên
    for _ in range(pad_h):
        padded.append([0] * (w + 2 * pad_w))
    
    # thêm phần giữa
    for i in range(h):
        row = [0] * pad_w + img[i] + [0] * pad_w
        padded.append(row)
    
    # thêm dòng dưới
    for _ in range(pad_h):
        padded.append([0] * (w + 2 * pad_w))
    
    return padded


def convolution2d(image, kernel):
    img_h = len(image)
    img_w = len(image[0])
    
    k_h = len(kernel)
    k_w = len(kernel[0])
    
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    padded = pad_image(image, pad_h, pad_w)
    
    output = [[0 for _ in range(img_w)] for _ in range(img_h)]
    
    for i in range(img_h):
        for j in range(img_w):
            s = 0
            for ki in range(k_h):
                for kj in range(k_w):
                    s += padded[i + ki][j + kj] * kernel[ki][kj]
            output[i][j] = s
    
    return output


# ===== Ví dụ =====
image = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

kernel = [
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
]

result = convolution2d(image, kernel)

for row in result:
    print(row)