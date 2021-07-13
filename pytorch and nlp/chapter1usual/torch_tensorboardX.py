from tensorboardX import SummaryWriter
import tensorflow as tf
import tensorboard
writer = SummaryWriter("log")
for i in range(100):
    writer.add_scalar("a", i, global_step=i)
    writer.add_scalar("b", i*i, global_step=i)
writer.close()
