import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise1 = PerlinNoise(octaves=2)
noise2 = PerlinNoise(octaves=4)
noise3 = PerlinNoise(octaves=8)
noise4 = PerlinNoise(octaves=16)

xpix, ypix = 100, 100
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        a = 20
        noise_val =         noise1([i/xpix, j/ypix])*a
        noise_val += 0.5  * noise2([i/xpix, j/ypix])*a
        noise_val += 0.25 * noise3([i/xpix, j/ypix])*a
        noise_val += 0.125* noise4([i/xpix, j/ypix])*a

        row.append(int(noise_val))
    pic.append(row)

plt.imshow(pic, cmap='gray')
plt.show()
