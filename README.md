# Identify-intention-BERT
Debt-collection AI models, includings IdentifyClassifier( 身份环节），IntentionClassifer(意图环节）， Loop3Classifer(追问环节）and ModelService
## 身份环节
### 训练语料:train.csv, dev.csv （private)
##### 1.label 当前q对应的标签
##### 2.text_re 去标点符号后的语料
##### 3.qcat话术分类
##### 4.dup_times语料重复的次数
## 模型文件
#### 1.模型分类任务
run_classifier.py
#### 2.数据处理
get_labels（private)
#### 3.模型持久化
 ckpt2pb.py
## 意愿环节
### 1~3同上
#### 4.dictmap1.py （private)
 ##### 4.1flabel2code:将拼接的tag转化成对应的编码
 ##### 4.2 fcode2label 将编码转化成对应newtag
## 追问环节
### 同意愿环节


## 服务端部署与启动
### 5. bert-base, 来自于项目BERT-BiLSTM-CRF-NER
 #### 5.1 dictmap2.py（private)
### 6.模型准确率
####  6.1classifiction_report
