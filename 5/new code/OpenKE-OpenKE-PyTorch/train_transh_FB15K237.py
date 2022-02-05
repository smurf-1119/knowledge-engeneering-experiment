import openke
from openke.config import Trainer, Tester
from openke.module.model import TransH
from openke.module.loss import MarginLoss
from openke.module.strategy import NegativeSampling
from openke.data import TrainDataLoader, TestDataLoader

import argparse

def set_interact_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--margin', default=4.0, type=float, required=False, help='Margin loss中margin值')
	parser.add_argument('--nbatches', default=100, type=int, required=False, help='Batch size')
	parser.add_argument('--dim', default=100, type=int, required=False, help='Embedding size')
	parser.add_argument('--p_norm', default=1, type=int, required=False, help='能量函数为1范数形式')
	parser.add_argument('--train_times', default=1, type=int, required=False, help='epoch-训练轮次')
	parser.add_argument('--alpha', default=0.5, type=float, required=False, help='学习率')
	return parser.parse_args()

def train():
	# dataloader for training
	#get params
	args = set_interact_args()
	margin = args.margin
	nbatches = args.nbatches
	dim = args.dim
	p_norm = args.p_norm
	train_times = args.train_times
	alpha = args.alpha

	train_dataloader = TrainDataLoader(
		in_path = "./benchmarks/WN18RR/", 
		nbatches = nbatches,
		threads = 8, 
		sampling_mode = "normal", 
		bern_flag = 1, 
		filter_flag = 1, 
		neg_ent = 25,
		neg_rel = 0)

	# dataloader for test
	test_dataloader = TestDataLoader("./benchmarks/WN18RR/", "link")

	# define the model
	transh = TransH(
		ent_tot = train_dataloader.get_ent_tot(),
		rel_tot = train_dataloader.get_rel_tot(),
		dim = dim, 
		p_norm = p_norm, 
		norm_flag = True)

	# define the loss function
	model = NegativeSampling(
		model = transh, 
		loss = MarginLoss(margin = margin),
		batch_size = train_dataloader.get_batch_size()
	)


	# train the model
	trainer = Trainer(model = model, data_loader = train_dataloader, train_times = train_times, alpha = alpha, use_gpu = True)
	trainer.run()
	transh.save_checkpoint(f'./checkpoint/transh/{margin,nbatches,dim,p_norm,train_times,alpha}transh-WN18RR.ckpt')

	# test the model
	transh.load_checkpoint(f'./checkpoint/transh/{margin,nbatches,dim,p_norm,train_times,alpha}transh-WN18RR.ckpt')
	tester = Tester(model = transh, data_loader = test_dataloader, use_gpu = True)
	tester.run_link_prediction(type_constrain = False)
if __name__ == '__main__':
	train()