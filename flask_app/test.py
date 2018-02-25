def print_betas(recall, precision):
	betas = [0.1, 1, 10]
	for b in betas:
		f_beta = (1 + b**2) * (recall * precision) / (b**2 * precision + recall)
		print('beta: {}, recall: {}, precision: {}, score: {}'.format(b, recall, precision, f_beta))


print_betas(0.5, 0.5)
print_betas(0.8, 0.2)
print_betas(0.2, 0.8)
