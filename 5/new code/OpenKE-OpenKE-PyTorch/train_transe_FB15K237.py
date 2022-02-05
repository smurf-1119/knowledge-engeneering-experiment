import openke
from openke.config import Trainer, Tester
from openke.module.model import TransE
from openke.module.loss import MarginLoss
from openke.module.strategy import NegativeSampling
from openke.data import TrainDataLoader, TestDataLoader
import argparse

def set_interact_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--margin', default=5.0, type=float, required=False, help='Margin loss中margin值')
	parser.add_argument('--nbatches', default=100, type=int, required=False, help='Batch size')
	parser.add_argument('--dim', default=100, type=int, required=False, help='Embedding size')
	parser.add_argument('--p_norm', default=1, type=int, required=False, help='能量函数为1范数形式')
	parser.add_argument('--train_times', default=1, type=int, required=False, help='epoch-训练轮次')
	parser.add_argument('--alpha', default=1, type=float, required=False, help='学习率')
	return parser.parse_args()

def train():
	#get params
	args = set_interact_args()
	margin = args.margin
	nbatches = args.nbatches
	dim = args.dim
	p_norm = args.p_norm
	train_times = args.train_times
	alpha = args.alpha
	# dataloader for training
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
	transe = TransE(
		ent_tot = train_dataloader.get_ent_tot(),
		rel_tot = train_dataloader.get_rel_tot(),
		dim = dim, #Embedding size
		p_norm = p_norm, #能量函数为1范数形式
		norm_flag = True)


	# define the loss function
	model = NegativeSampling(
		model = transe, 
		loss = MarginLoss(margin = margin),
		batch_size = train_dataloader.get_batch_size()
	)

	# train the model
	trainer = Trainer(model = model, data_loader = train_dataloader, train_times = train_times, alpha = alpha, use_gpu = True) 
	# train_times: epoch-训练轮次
	# alpha: 学习率
	# use_gpu: 训练过程是否使用gpu加速
	trainer.run()
	transe.save_checkpoint(f'./checkpoint/transe/{margin,nbatches,dim,p_norm,train_times,alpha}transe-WN18RR.ckpt')

	# test the model
	transe.load_checkpoint(f'./checkpoint/transe/{margin,nbatches,dim,p_norm,train_times,alpha}transe-WN18RR.ckpt')
	tester = Tester(model = transe, data_loader = test_dataloader, use_gpu = True)
	tester.run_link_prediction(type_constrain = False)

if __name__ == '__main__':
	train()