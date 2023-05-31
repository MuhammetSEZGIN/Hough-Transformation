############################
#### Goruntu Isleme Odev 5
############################

import cv2
import numpy as np

def hough_transform(image):
    # Gri tonlamaya dönüştür
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Kenarları algıla
    edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

    # Hough dönüşümünü uygula
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

    return lines

def detect_lines(image):
    # Hough dönüşümünü uygula
    lines = hough_transform(image)

    # Doğru segmentlerini depolamak için bir liste oluştur
    line_segment = []

    if lines is not None:
        for line in lines:
            alfa, beta = line[0]
            # Doğru denklemine dönüştür
            a = np.cos(beta)
            b = np.sin(beta)
            x0 = a * alfa
            y0 = b * alfa
            # İki nokta bul
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            # Doğru segmentini oluştur ve listeye ekle
            line_segment.append(((x1, y1), (x2, y2)))

    return line_segment

def draw_lines(image, lines):
    # Görüntüyü kopyala
    result_image = np.copy(image)

    # Doğru segmentlerini çiz
    if lines is not None:
        for line in lines:
            pt1, pt2 = line
            cv2.line(result_image, pt1, pt2, (0, 255, 0), 2)

    return result_image

def main():
    # Görüntüyü yükle
    image_path = 'ela_original.jpg'
    image = cv2.imread(image_path)

    # Doğru tespitini yap
    lines = detect_lines(image)

    # Doğruları çiz
    result_image = draw_lines(image, lines)

    # Sonucu göster
    cv2.imshow('First picture', image)
    cv2.imshow('Result', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
