	���]�@���]�@!���]�@	 �ţ@�? �ţ@�?! �ţ@�?"w
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails6���]�@��9�@1C���i�@A,�`p��?I��P��K@Y`��8��?*	��� �?�@2g
0Iterator::Model::Prefetch::FlatMap[0]::Generator�����W@!�X-��X@)�����W@1�X-��X@:Preprocessing2F
Iterator::Model��f�|�?!p�����?)�*øD�?18 �0;�?:Preprocessing2P
Iterator::Model::Prefetch%�c\qq�?!���1yw�?)%�c\qq�?1���1yw�?:Preprocessing2Y
"Iterator::Model::Prefetch::FlatMapE�>�'�W@!���&!�X@)�\�	�}?1~���[�~?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.moderate"�9.5 % of the total step time sampled is spent on 'Kernel Launch'. It could be due to CPU contention with tf.data. In this case, you may try to set the environment variable TF_GPU_THREAD_MODE=gpu_private.*no9 �ţ@�?#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	��9�@��9�@!��9�@      ��!       "	C���i�@C���i�@!C���i�@*      ��!       2	,�`p��?,�`p��?!,�`p��?:	��P��K@��P��K@!��P��K@B      ��!       J	`��8��?`��8��?!`��8��?R      ��!       Z	`��8��?`��8��?!`��8��?JGPUY �ţ@�?b 