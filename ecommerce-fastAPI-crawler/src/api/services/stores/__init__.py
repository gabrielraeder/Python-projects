from typing import List, Type

from .kabum import Kabum
from .pichau import Pichau
from .americanas import Americanas
from .dell import Dell
from .website import Website

WEBSITE_CLASSES: List[Type[Website]] = [
    Pichau,
    Kabum,
    Americanas,
    Dell,
]
