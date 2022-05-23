
import cv2 as cv

import numpy as np
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog
import PyQt5.QtCore as Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class BiedaInstagram(object):

    def __init__(self):
        self.current_blur_value = 1
        self.doTreshold = False
        self.isErodeOn = False
        self.doNegative = False
        self.sing = False
        self.current_gamma_value = 0
        self.isCannyOn = False
        self.canny = False
        self.isNegativeOn = False
        self.current_contrast_value_beta = -10
        self.current_contrast_value_alpha = 1
        self.current_saturation_value = 50


    def application(self, window):
        title = "Bieda Instagram"
        window.setObjectName("Bieda Instagram")
        window.resize(540, 570)
        window.setWindowTitle(title)

        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("glownywidget")
        window.setCentralWidget(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)

        # najbardziej główny layout po rodzicu - central widget
        self.main_layout = QtWidgets.QGridLayout(self.centralwidget)

        self.gridLayout = QtWidgets.QGridLayout()
        self.title_label = QtWidgets.QLabel("INSTAGRAM JAKBY META BYLA MALA FIRMA")

        self.tile = cv.imread("rick editor.png")
        title_image = cv.resize(self.tile, (550, 50))

        frame = cv.cvtColor(title_image, cv.COLOR_BGR2RGB)
        title_image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.title_label = QtWidgets.QLabel()
        self.title_label.setPixmap(QtGui.QPixmap.fromImage(title_image))

        self.title_label.setStyleSheet("font-weight: bold; font-size: 100")
        self.title_label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)
        self.title_layout = QtWidgets.QVBoxLayout()
        self.title_layout.addWidget(self.title_label)
        self.gridLayout.addLayout(self.title_layout, 0, 0, 1, 1)

        self.upper_layout = QtWidgets.QHBoxLayout()
        self.lower_layout = QtWidgets.QGridLayout()
        self.image = cv.imread("rick.jpg")
        image = cv.resize(self.image, (550, 650))
        self.first_photo = cv.imread("rick.jpg")

        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_image = QtWidgets.QLabel()
        self.label_image.setPixmap(QtGui.QPixmap.fromImage(image))

        self.upper_layout.addWidget(self.label_image, alignment=Qt.AlignCenter)
        self.gridLayout.addLayout(self.upper_layout, 1, 0, 1, 1)

        # HORIZONTAL LAYOUT
        self.parent_sliders_layout = QtWidgets.QVBoxLayout()
        self.parent_sliders_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.sliders_layout = QtWidgets.QVBoxLayout()

        self.text_label = QtWidgets.QLabel("Nasycenie")
        self.text_label2 = QtWidgets.QLabel("Kontrast  ")
        self.text_label3 = QtWidgets.QLabel("Jasność   ")
        self.text_label4 = QtWidgets.QLabel("Rozmycie ")


        # NASYCENIE
        self.sliders_layout_one = QtWidgets.QHBoxLayout()
        self.nasycenie_slider = QtWidgets.QSlider(self.centralwidget)
        self.nasycenie_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sliders_layout_one.addWidget(self.text_label)
        self.sliders_layout_one.addWidget(self.nasycenie_slider)
        self.sliders_layout.addLayout(self.sliders_layout_one)

        # Kontrast
        self.layout = QtWidgets.QHBoxLayout()
        self.slider_contrast_alpha = QtWidgets.QSlider(self.centralwidget)
        self.slider_contrast_alpha.setOrientation(QtCore.Qt.Horizontal)
        self.layout.addWidget(self.text_label2)
        self.layout.addWidget(self.slider_contrast_alpha)
        self.sliders_layout.addLayout(self.layout)

        # Jasność
        self.contrast_slider_beta_layout = QtWidgets.QHBoxLayout()
        self.slider_contrast_beta = QtWidgets.QSlider(self.centralwidget)
        self.slider_contrast_beta.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider_beta_layout.addWidget(self.text_label3)
        self.contrast_slider_beta_layout.addWidget(self.slider_contrast_beta)
        self.sliders_layout.addLayout(self.contrast_slider_beta_layout)

        # Rozmycie
        self.blur_slider_layout = QtWidgets.QHBoxLayout()
        self.blur_slider = QtWidgets.QSlider(self.centralwidget)
        self.blur_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blur_slider_layout.addWidget(self.text_label4)
        self.blur_slider_layout.addWidget(self.blur_slider)
        self.sliders_layout.addLayout(self.blur_slider_layout)


        self.parent_sliders_layout.addLayout(self.sliders_layout)

        self.lower_layout.addLayout(self.parent_sliders_layout, 2, 0, 1, 1)
        self.setSlider()

        self.button_layout = QtWidgets.QHBoxLayout()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_layout.addWidget(self.pushButton, 2)
        self.button_layout.addWidget(self.pushButton2, 2)
        self.lower_layout.addLayout(self.button_layout, 3, 0, 1, 1)

        self.Abutton_layout = QtWidgets.QHBoxLayout()
        self.never_gonna_button = QtWidgets.QPushButton(self.centralwidget)
        self.Abutton_layout.addWidget(self.never_gonna_button, 2)
        self.lower_layout.addLayout(self.Abutton_layout, 3, 1, 1, 1)

        self.right_button_layout = QtWidgets.QVBoxLayout()
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3_right = QtWidgets.QPushButton(self.centralwidget)
        self.right_button_layout.addWidget(self.pushButton_right, 1)
        self.right_button_layout.addWidget(self.pushButton2_right, 1)
        self.right_button_layout.addWidget(self.pushButton3_right, 1)

        # self.gridLayout.addLayout(self.button_layout, 1, 0, 1, 1)
        self.lower_layout.addLayout(self.right_button_layout, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.lower_layout, 3, 0, 1, 1)
        self.main_layout.addLayout(self.gridLayout, 0, 0, 1, 1)

        window.setCentralWidget(self.centralwidget)

        # Laczenie sliderow i przyciskow z funkcjami
        self.nasycenie_slider.valueChanged['int'].connect(self.saturation_value)
        self.slider_contrast_alpha.valueChanged['int'].connect(self.contrast_alpha_value)
        self.slider_contrast_beta.valueChanged['int'].connect(self.contrast_beta_value)
        self.blur_slider.valueChanged['int'].connect(self.blur_value)
        self.pushButton.clicked.connect(self.savePhoto)
        self.pushButton2.clicked.connect(self.resetPhoto)
        self.never_gonna_button.clicked.connect(self.neverGonna)
        self.pushButton_right.clicked.connect(self.doCanny)
        self.pushButton2_right.clicked.connect(self.isNegative)
        self.pushButton3_right.clicked.connect(self.doErode)

        QtCore.QMetaObject.connectSlotsByName(window)

        translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(translate("glownywidget", title))

        self.pushButton.setText(translate("glownywidget", "Zapisz"))
        self.pushButton2.setText(translate("glownywidget", "Powrót"))
        self.pushButton_right.setText(translate("glownywidget", "Filtr Cannyego"))
        self.pushButton2_right.setText(translate("glownywidget", "Negatyw"))
        self.pushButton3_right.setText(translate("glownywidget", "Erozja"))
        self.never_gonna_button.setText(translate("glownywidget", "Never gonna give you up!"))

    def setSlider(self):
        self.nasycenie_slider.setSliderPosition(50)
        self.blur_slider.setSliderPosition(50)
        self.slider_contrast_beta.setSliderPosition(50)
        self.slider_contrast_alpha.setSliderPosition(50)

    def neverGonna(self):

        self.sing = not self.sing
        self.update()

    @staticmethod
    def neverGonnaLetYou(img, sing):
        small_image = cv.imread("let_you_down.png")
        small_image = cv.resize(small_image, (600, 240))
        x_end = small_image.shape[1]
        y_end = small_image.shape[0]
        x_img_end = img.shape[1]

        if sing:
            roi = img[0:y_end, x_img_end - x_end - 100:x_img_end - 100]
            small_img_gray = cv.cvtColor(small_image, cv.COLOR_RGB2GRAY)
            ret, mask = cv.threshold(small_img_gray, 180, 255, cv.THRESH_BINARY)

            mask_inv = cv.bitwise_not(small_img_gray)
            bg = cv.bitwise_and(roi, roi, mask=mask_inv)
            fg = cv.bitwise_and(small_image, small_image, mask=mask)
            final_roi = cv.add(bg, fg)
            small_img = final_roi
            img[0:y_end, x_img_end - x_end - 100:x_img_end - 100] = small_img

        return img

    def setPhoto(self, image):

        image = cv.resize(image, (550, 650))

        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)

        self.label_image.setPixmap(QtGui.QPixmap.fromImage(image))

    def update(self):
        # print("sat: " , self.current_saturation_value)
        # print("alpha: ", self.current_contrast_value_alpha)
        # print("beta: ", self.current_contrast_value_beta)
        # print("blur: ", self.current_blur_value)



        img = self.saturation(self.image, self.current_saturation_value)
        img = self.contrast(img, self.current_contrast_value_alpha, self.current_contrast_value_beta)
        img = self.blur(img, self.current_blur_value)
        img = self.neverGonnaLetYou(img, self.sing)
        img = self.negative(img, self.isNegativeOn)
        img = self.cannyFunction(img, self.isCannyOn)
        img = self.erodeFunction(img, self.isErodeOn)
        self.temp_image = img
        self.setPhoto(img)

    def savePhoto(self):
        print("Saving...")
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        cv.imwrite(filename, self.temp_image)
        print('Successfully saved as', filename)

    def resetPhoto(self):
        print("Reset photo....")
        translate = QtCore.QCoreApplication.translate
        img = self.first_photo
        self.isNegativeOn = False
        self.isErodeOn = False
        self.isCannyOn = False
        self.sing = False
        self.setSlider()
        self.pushButton_right.setText(translate("glownywidget", "Filtr Cannyego"))
        self.pushButton2_right.setText(translate("glownywidget", "Negatyw"))
        self.pushButton3_right.setText(translate("glownywidget", "Erozja"))
        self.setPhoto(img)

    def isNegative(self):
        self.isNegativeOn = not self.isNegativeOn
        self.update()

    def negative(self, img, doNegative):
        translate = QtCore.QCoreApplication.translate
        if self.isNegativeOn:
            if doNegative:
                self.pushButton2_right.setText(translate("glownywidget", "Powrot"))
            return 255 - img if doNegative else img

        else:

            self.pushButton2_right.setText(translate("glownywidget", "Negatyw"))
            return img

    def doCanny(self):
        self.isCannyOn = not self.isCannyOn
        self.update()

    def cannyFunction(self, img, doCanny):
        translate = QtCore.QCoreApplication.translate
        if self.isCannyOn:
            if doCanny:
                self.pushButton_right.setText(translate("glownywidget", "Powrót"))
            return cv.Canny(img, 100, 200) if doCanny else img
        else:
            self.pushButton_right.setText(translate("glownywidget", "Filtr Cannyego"))
            return img

    def doErode(self):
        self.isErodeOn = not self.isErodeOn
        self.update()

    def erodeFunction(self, img, doErode):
        ret, result = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
        translate = QtCore.QCoreApplication.translate
        if self.isErodeOn:
            if doErode:
                self.pushButton3_right.setText(translate("glownywidget", "Powrót"))
            return cv.erode(result, (5, 5)) if doErode else img
        else:
            self.pushButton3_right.setText(translate("glownywidget", "Erozja"))
            return img

    def blur_value(self, value):
        value -= 50
        if value % 2 == 0:
            value += 1
        self.current_blur_value = value
        self.update()

    @staticmethod
    def blur(img, value):
        return cv.GaussianBlur(img, (value, value), 3)

    def contrast_alpha_value(self, value):
        value += 30
        self.current_contrast_value_alpha = value / 100
        self.update()

    def contrast_beta_value(self, value):
        value += 44
        self.current_contrast_value_beta = value - 100
        self.update()

    @staticmethod
    def contrast(img, alpha, beta):
        return cv.convertScaleAbs(img, alpha=alpha, beta=beta)

    def saturation_value(self, value):
        self.current_saturation_value = value
        self.update()

    @staticmethod
    def saturation(img, satur):

        satur = satur / 50
        img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
        img = img.astype('int32')
        tmp = np.ones_like(img[:, :, 1]) * 255
        img[:, :, 1] = np.where(img[:, :, 1] * satur > 255, tmp, img[:, :, 1] * satur)
        img = np.clip(img, 0, 255)
        img = img.astype('uint8')
        img = cv.cvtColor(img, cv.COLOR_HSV2RGB)

        return img


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.jpg'))
    app.setStyle('Fusion')

    window = QtWidgets.QMainWindow()
    # Jakaś magia żeby było na środku
    multiplier_x = 1
    multiplier_y = 2
    cursor_pos = QtWidgets.QApplication.desktop().cursor().pos()
    screen = QtWidgets.QApplication.desktop().screenNumber(cursor_pos)
    pos_x = QtWidgets.QDesktopWidget().screenGeometry(screen).center().x()
    pos_x -= window.frameGeometry().center().x() * multiplier_x
    pos_y = QtWidgets.QDesktopWidget().screenGeometry(screen).center().y()
    pos_y -= window.frameGeometry().center().y() * multiplier_y
    window.move(pos_x, pos_y)

    bi = BiedaInstagram()
    bi.application(window)

    window.show()
    sys.exit(app.exec_())
