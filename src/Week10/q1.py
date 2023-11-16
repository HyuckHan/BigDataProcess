class Camera:
    def __init__(self, pixel, mag):
        self.pixel = pixel
        self.mag = mag

    def takepicture(self):
        print("사진이 저장되었습니다. (화소: {}만, 배율 : {}x)".format(self.pixel, self.mag))


if __name__ == "__main__":
    canon = Camera(2430, 1.0)
    canon.takepicture()
    sony = Camera(2410, 3.0)
    sony.takepicture()
