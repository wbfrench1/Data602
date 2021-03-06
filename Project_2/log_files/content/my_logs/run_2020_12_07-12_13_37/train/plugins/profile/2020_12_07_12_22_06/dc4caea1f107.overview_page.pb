�	�[1к\@�[1к\@!�[1к\@	Q��<j�?Q��<j�?!Q��<j�?"w
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails6�[1к\@st���?1Q�E��[@A�h����q?Ix�~�~9�?Y-z��y�?*	X9��&Y@2F
Iterator::ModelBȗP��?!      Y@)�����?1���y��N@:Preprocessing2P
Iterator::Model::Prefetch�s�p�̣?![VH�8C@)�s�p�̣?1[VH�8C@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.5% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9Q��<j�?#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	st���?st���?!st���?      ��!       "	Q�E��[@Q�E��[@!Q�E��[@*      ��!       2	�h����q?�h����q?!�h����q?:	x�~�~9�?x�~�~9�?!x�~�~9�?B      ��!       J	-z��y�?-z��y�?!-z��y�?R      ��!       Z	-z��y�?-z��y�?!-z��y�?JGPUYQ��<j�?b �"e
<gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropInputConv2DBackpropInput����?�?!����?�?":
sequential/conv2d_1/Relu_FusedConv2D��ً?�?!-Y�š-�?"g
=gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropFilterConv2DBackpropFilterCK1��-�?!g5�8��?"e
<gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropInputConv2DBackpropInput)��
��?!q`��4��?":
sequential/conv2d_3/Relu_FusedConv2D���%��?!�?/��?"-
IteratorGetNext/_1_Send(�$uά?!�"к�^�?":
sequential/conv2d_5/Relu_FusedConv2D��48+��?!#Z�A��?"g
=gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropFilterConv2DBackpropFilter �7���?!�U]D�a�?"e
<gradient_tape/sequential/conv2d_5/Conv2D/Conv2DBackpropInputConv2DBackpropInput6~DT�t�?!����	��?":
sequential/conv2d_2/Relu_FusedConv2D�����4�?!5�%W\�?Q      Y@Y<ݚ)@a,R�nMW@qp���F&@y�gD�+h?"�	
device�Your program is NOT input-bound because only 0.5% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"O
Mtensorflow_stats (identify the time-consuming operations executed on the GPU)"U
Strace_viewer (look at the activities on the timeline of each GPU in the trace view)*�
�<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2�
=type.googleapis.com/tensorflow.profiler.GenericRecommendation�
nono*�Only 0.0% of device computation is 16 bit. So you might want to replace more 32-bit Ops by 16-bit Ops to improve performance (if the reduced accuracy is acceptable).:
Refer to the TF2 Profiler FAQb�11.138% of Op time on the host used eager execution. Performance could be improved with <a href="https://www.tensorflow.org/guide/function" target="_blank">tf.function.</a>2"GPU(: B 