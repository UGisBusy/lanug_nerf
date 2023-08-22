"""
Lanug Model File

Currently this subclasses the Nerfacto model. Consider subclassing from the base Model.
"""
from dataclasses import dataclass, field
from typing import Type

from nerfstudio.models.nerfacto import NerfactoModel, NerfactoModelConfig  # for subclassing Nerfacto model
from nerfstudio.models.base_model import Model, ModelConfig  # for custom Model


@dataclass
class LanugModelConfig(NerfactoModelConfig):
    """Lanug Model Configuration.

    Add your custom model config parameters here.
    """

    _target: Type = field(default_factory=lambda: LanugModel)


class LanugModel(NerfactoModel):
    """Lanug Model."""

    config: LanugModelConfig

    def populate_modules(self):
        super().populate_modules()

    # TODO: Override any potential functions/methods to implement your own method
    # or subclass from "Model" and define all mandatory fields.