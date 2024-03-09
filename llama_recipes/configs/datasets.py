# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from dataclasses import dataclass

    
@dataclass
class custom_dataset:
    dataset: str = "custom_dataset"
    file: str = "examples/custom_dataset.py"
    train_split: str = "train"
    test_split: str = "validation"


@dataclass
class commsense_dataset:
    dataset: str = "commsense_dataset"
    train_split: str = "train"
    test_split: str = "test"
    file: str = "src/llama_recipes/datasets/commsense_dataset.py"
