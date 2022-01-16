import xkcd as xkcd
comic = xkcd.getRandomComic()
comic.download(output='/Documents/XKCD', outputFile='{}.png'.format(comic.number))
