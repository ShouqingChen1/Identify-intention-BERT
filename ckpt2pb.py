import tensorflow as tf
#from create_tf_record import *
from tensorflow.python.framework import graph_util

def freeze_graph(input_checkpoint,output_graph):
　　'''
　　:param input_checkpoint:
　　:param output_graph: PB模型保存路径
　　:return:
　　'''
　　# checkpoint = tf.train.get_checkpoint_state(model_folder) #检查目录下ckpt文件状态是否可用
　　# input_checkpoint = checkpoint.model_checkpoint_path #得ckpt文件路径
　　 
　　# 指定输出的节点名称,该节点名称必须是原模型中存在的节点
　　#output_node_names = "InceptionV1/Logits/Predictions/Reshape_1"
　　#output_node_names = "resnet_v1_101/rpn_conv/3x3/weights/Momentum"
　　output_node_names = "resnet_v1_101/bbox_pred/weights"
　　#trainable_scopes = 'InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits'
　　
　　saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=True)
　　graph = tf.get_default_graph() # 获得默认的图
　　input_graph_def = graph.as_graph_def() # 返回一个序列化的图代表当前的图
 
　　with tf.Session() as sess:
　　　　saver.restore(sess, input_checkpoint) #恢复图并得到数据
　　　　output_graph_def = graph_util.convert_variables_to_constants( # 模型持久化，将变量值固定
　　　　　　sess=sess,
　　　　　　input_graph_def=input_graph_def,# 等于:sess.graph_def
　　　　　　output_node_names=output_node_names.split(","))# 如果有多个输出节点，以逗号隔开
 
　　　　with tf.gfile.GFile(output_graph, "wb") as f: #保存模型
　　　　　　f.write(output_graph_def.SerializeToString()) #序列化输出
　　　　print("%d ops in the final graph." % len(output_graph_def.node)) #得到当前图有几个操作节点
 

#input_checkpoint='inceptionv1/model.ckpt-0'
input_checkpoint = "output/res101/voc_2007_trainval+voc_2012_trainval/default/res101_faster_rcnn_iter_110000.ckpt"

#out_pb_path='inceptionv1/frozen_model.pb'
out_pb_path = "output/pb_model/frozen_model_110000_Variable.pb"

freeze_graph(input_checkpoint, out_pb_path)
