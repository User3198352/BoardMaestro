import numpy as np
import openvino as ov


class ImageInferencing:
    def __init__(self, model_path, device_name, input_shape):
        '''
        ImageInferencing class init function
        :model_path: model_path must include .xmp file
        :device_name: input 'CPU' or 'GPU'
        :input_shape: input_shape value must be same shape with input image shape
        '''
        # Step 1. Initialize OpenVINO Runtime Core
        core = ov.Core()

        # Step 2. Read a model
        model = core.read_model(model_path)

        # Step 3. Set up input
        input_tensor = np.expand_dims(input_shape, 0)

        # Step 4. Apply preprocessing
        ppp = ov.preprocess.PrePostProcessor(model)
        ppp.input().tensor() \
            .set_shape(input_tensor.shape) \
            .set_element_type(ov.Type.u8) \
            .set_layout(ov.Layout('NHWC'))
        ppp.input().preprocess().resize(ov.preprocess.ResizeAlgorithm.RESIZE_LINEAR)
        ppp.input().model().set_layout(ov.Layout('NCHW'))
        ppp.output().tensor().set_element_type(ov.Type.f32)
        model = ppp.build()

        # Step 5. Loading model to the device
        self.compiled_model = core.compile_model(model, device_name)

    def get_inferencing_result(self, frame):
        '''get inferencing result from image'''
        input_tensor = np.expand_dims(frame, 0)
        results = self.compiled_model.infer_new_request({0: input_tensor})
        return next(iter(results.values()))


'''
:Usage example:
import cv2
import time
import numpy as np

# read frame
frame = cv2.imread('C:/pywork/image/2_1.jpg')

# set model path
model_path = 'C:/pywork/model/openvino.xml'

# select inferencing device
device_name = 'CPU'

# make same shape with input frame shape
input_shape = np.zeros((220, 453, 3))

# start 
init_start_time = time.time()
infer = ImageInferencing(model_path, device_name, input_shape)
print(time.time() - init_start_time)
infer_start_time = time.time()
print(infer.get_inferencing_result(frame))
print(time.time() - infer_start_time)
'''