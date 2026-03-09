"""Cross-reference types for links between strata and modules."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CrossReference(BaseModel):
    """A directional link between two modules or strata.

    Cross-references are extracted from filesystem paths in comments
    (e.g., /sys/thermodynamics/entropy.daemon) and from explicit
    cross_refs fields in modules.
    """

    source_id: str = Field(description="The module or stratum that references")
    target_id: str = Field(description="The module or stratum being referenced")
    context: str = Field(default="", description="The comment or line where the reference appears")
    relation: str = Field(
        default="references",
        description="Type of relationship: references, depends_on, implements, contains, etc.",
    )
