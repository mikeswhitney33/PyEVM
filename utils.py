#Build Gaussian Pyramid
def build_gaussian_pyramid(src, levels=3):
    s=src.copy()
    pyramid=[s]
    for i in range(levels):
        s=cv2.pyrDown(s)
        pyramid.append(s)
    return pyramid