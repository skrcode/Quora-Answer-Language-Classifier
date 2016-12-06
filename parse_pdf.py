from pyPdf import PdfFileReader

def do():

	f = open('one-night-at-call-center.pdf', 'rb')
	reader = PdfFileReader(f)
	print reader
	for i in range(100):
		contents = reader.getPage(i).extractText().decode('utf-8').split('\n')
		print contents
	return contents
	f.close()