import math
import numpy as np
from PIL import Image


outImgPath = '../images/result/'
imgPath    = '../images/'


def imgNormalization(src_img):
	norm_img = (src_img - np.min(src_img)) / (np.max(src_img) - np.min(src_img))
	return norm_img


def mergeImg(cA, cH_V_D):
	cH, cV, cD = cH_V_D
	# cH = imgNormalization(cH)  # 外してもok
	# cV = imgNormalization(cV)  # 外してもok
	# cD = imgNormalization(cD)  # 外してもok
	cA = cA[0:cH.shape[0], 0:cV.shape[1]]  # 元画像が2の累乗ピクセルでない場合の端数調整。小さい方に
	return np.vstack((np.hstack((cA, cH)), np.hstack((cV, cD))))  # [cA, cH]を[cV, cD]縦にくっつける[低周波，y方向高周波],[x方向高周波，xy方向高周波]


def coeffsShow(coeffs):
	coeffs0 = coeffs[0]
	# coeffs0 = imgNormalization(coeffs0) # 外してもok
	merge = coeffs0
	for i in range(1, len(coeffs)):
		merge = mergeImg(merge, coeffs[i])  # ４つの画像を合わせていく
	Image.fromarray(np.uint8(merge)).show()


def listToTextfile(lst, name):
	f = open(name, 'w')
	for i in lst:
		f.write(str(i)+'\n')
	f.close()


def psnr(cover, stego):
	mse = np.mean((cover-stego)**2)
	if mse == 0:
		return 100
	PIXEL_MAX = 255.0

	return 20 * math.log10(PIXEL_MAX/math.sqrt(mse))


def getYcbcrArray(name):
	pil_img = Image.open(imgPath+name)
	pil_y, pil_cr, pil_cb = pil_img.convert('YCbCr').split()
	y = np.asarray(pil_y)
	cr = np.asarray(pil_cr)
	cb = np.asarray(pil_cb)
	y.flags.writeable = True
	cr.flags.writeable = True
	cb.flags.writeable = True
	return [y, cr, cb]


def saveYcbcrAsImg(name: str, y, cr, cb):
	pil_y = Image.fromarray(np.uint8(y))
	pil_cr = Image.fromarray(np.uint8(cr))
	pil_cb = Image.fromarray(np.uint8(cb))
	pil_img = Image.merge('YCbCr', (pil_y, pil_cr, pil_cb)).convert('RGB')
	pil_img.save(outImgPath+name)


def getImgSizeAndData(imgname):
	img = np.array(Image.open(imgPath+imgname), 'f')
	img_y, img_cr, img_cb = getYcbcrArray(imgname)
	width = img.shape[1]
	height = img.shape[0]
	return width, height, img_y, img_cr, img_cb



