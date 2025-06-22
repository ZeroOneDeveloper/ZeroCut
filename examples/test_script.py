from zerocut import LifeCut
from zerocut.frames.sample import SimpleWhiteFrame

from PIL import Image

images = [Image.open(f"examples/samples/{i}.png") for i in range(1, 5)]
frame = SimpleWhiteFrame()
life_cut = LifeCut(images, frame)
result_image = life_cut.create()
result_image.save("examples/result.png")
