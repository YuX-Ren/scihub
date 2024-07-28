from scihub import SciHub

sh = SciHub()

# exactly the same thing as fetch except downloads the articles to disk
# if no path given, a unique name will be used as the file name
# result = sh.download('https://doi.org/10.1126/science.aaf9620', path='paper.pdf')

# retrieve 5 articles on Google Scholars related to 'bittorrent'
paper = "Native architecture of a human GBP1 defense complex for cell-autonomous immunity to infection"
results = sh.search_download(paper , 1,path = '11822.pdf')