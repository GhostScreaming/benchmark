#   Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common_import import *


@benchmark_registry.register("linspace")
class PaddleLinspace(PaddleOpBenchmarkBase):
    def build_graph(self, config):
        result = paddle.linspace(
            start=config.start,
            stop=config.stop,
            num=config.num,
            dtype=config.dtype)

        self.feed_list = []
        self.fetch_list = [result]


@benchmark_registry.register("linspace")
class TorchLinspace(PytorchOpBenchmarkBase):
    def build_graph(self, config):
        result = torch.linspace(
            start=config.start, end=config.stop, steps=config.num)

        self.feed_list = []
        self.fetch_list = [result]


@benchmark_registry.register("linspace")
class TFLinspace(TensorflowOpBenchmarkBase):
    def build_graph(self, config):
        result = tf.linspace(
            start=config.start, stop=config.stop, num=config.num)

        self.feed_list = []
        self.fetch_list = [result]
