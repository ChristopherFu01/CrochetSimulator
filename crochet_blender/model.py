from dataclasses import dataclass
from typing import List, Optional
import mathutils

@dataclass
class Stitch:
    id: int
    kind: str              # "ch", "sc", "dc", etc.
    position: mathutils.Vector
    parent: Optional[int]
    children: List[int]
