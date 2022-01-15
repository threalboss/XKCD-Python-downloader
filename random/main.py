import xkcd as xkcd
comic = xkcd.getRandomComic()
comic.download(output='/home/nschwartz/Desktop/xkcd', outputFile='{}.png'.format(comic.number))
