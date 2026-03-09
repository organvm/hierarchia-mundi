"""Core type system for Hierarchia Mundi.

Maps the structure of reality into typed, composable, executable modules.
Each stratum is a file in the hierarchy. Each module is an atomic unit
within a stratum — a law, process, entity, system, signal, or substrate.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class StratumType(str, Enum):
    """The directory level in the hierarchy — each represents a phase of reality."""

    ROOT = "root"       # / — pure information, meta-laws, mathematics
    BOOT = "boot"       # /boot/ — cosmological origin
    SYS = "sys"         # /sys/ — physical reality kernel (immutable laws)
    LIB = "lib"         # /lib/ — chemistry, shared molecular libraries
    BIN = "bin"         # /bin/ — biological executables, self-replicating agents
    USR = "usr"         # /usr/ — human civilization, anthropomorphic constructs
    NET = "net"         # /net/ — emergent collective, networked consciousness
    DEV = "dev"         # /dev/ — peripherals, chaos, entropy source


class ModuleType(str, Enum):
    """The kind of atom within a stratum."""

    LAW = "law"             # Foundational principle (irreducible truth)
    PROCESS = "process"     # Executable mechanism (transforms input → output)
    ENTITY = "entity"       # Thing, person, place, concept (a noun in the system)
    SYSTEM = "system"       # Complex interacting structure (multiple modules coupled)
    SIGNAL = "signal"       # Information or energy flow between modules
    SUBSTRATE = "substrate" # Material or medium that other modules operate on


class Scale(str, Enum):
    """The scope at which a module applies — from quantum to cosmic."""

    QUANTUM = "quantum"         # Planck-scale phenomena
    MOLECULAR = "molecular"     # Atomic and molecular interactions
    CELLULAR = "cellular"       # Single-cell biology
    ORGANISM = "organism"       # Multi-cellular living systems
    ECOSYSTEM = "ecosystem"     # Populations, food webs, biomes
    PLANETARY = "planetary"     # Earth-scale systems, climate, geology
    COSMIC = "cosmic"           # Stars, galaxies, the universe
    META = "meta"               # Applies across all scales (meta-laws)


class Module(BaseModel):
    """An atomic unit within a stratum — the fundamental composable piece.

    Equivalent to Algorithm/Axiom in narratological-algorithmic-lenses.
    Everything in the hierarchy that can be named, described, and cross-referenced
    is a Module: laws, processes, entities, systems, signals, substrates.
    """

    id: str = Field(description="Qualified identifier, e.g. 'sys.gravity.newtonian'")
    name: str = Field(description="Human-readable name")
    module_type: ModuleType = Field(description="What kind of atom this is")
    description: str = Field(description="What this module represents")
    scale: list[Scale] = Field(default_factory=list, description="Scales of applicability")
    inputs: list[str] = Field(default_factory=list, description="What this module requires")
    outputs: list[str] = Field(default_factory=list, description="What this module produces")
    cross_refs: list[str] = Field(
        default_factory=list,
        description="Links to other modules by id or filesystem path",
    )
    properties: dict[str, Any] = Field(
        default_factory=dict,
        description="Type-specific key-value pairs parsed from the hierarchy file",
    )
    pseudocode: str = Field(default="", description="Algorithmic description if present")
    probes: list[str] = Field(
        default_factory=list,
        description="Diagnostic questions — how to test if something exhibits this pattern",
    )


class Stratum(BaseModel):
    """A file in the hierarchy — contains modules.

    Equivalent to Study in narratological-algorithmic-lenses.
    Each stratum models a layer of reality: gravity.conf, entropy.daemon,
    logic_gates.sys, organism_behavior.sh, etc.
    """

    id: str = Field(description="Qualified identifier, e.g. 'sys.gravity'")
    path: str = Field(description="Filesystem path relative to repo root, e.g. 'sys/gravity.conf'")
    name: str = Field(description="Human-readable name")
    stratum_type: StratumType = Field(description="Which directory level this belongs to")
    description: str = Field(default="", description="What this stratum models")
    modules: list[Module] = Field(default_factory=list, description="Atomic units within")
    dependencies: list[str] = Field(
        default_factory=list,
        description="Other strata this depends on (by id or path)",
    )


class Hierarchia(BaseModel):
    """The complete hierarchy — all strata, all modules.

    Equivalent to Compendium in narratological-algorithmic-lenses.
    This is the full filesystem model of reality, structured as typed data.
    """

    version: str = Field(default="2.0", description="Schema version")
    strata: dict[str, Stratum] = Field(
        default_factory=dict,
        description="All strata keyed by id",
    )

    @property
    def module_count(self) -> int:
        return sum(len(s.modules) for s in self.strata.values())

    @property
    def stratum_count(self) -> int:
        return len(self.strata)

    def get_stratum(self, stratum_id: str) -> Stratum | None:
        return self.strata.get(stratum_id)

    def get_module(self, module_id: str) -> Module | None:
        """Find a module by its qualified id across all strata."""
        for stratum in self.strata.values():
            for module in stratum.modules:
                if module.id == module_id:
                    return module
        return None

    def search_modules(self, query: str) -> list[Module]:
        """Search modules by name or description substring."""
        q = query.lower()
        results = []
        for stratum in self.strata.values():
            for module in stratum.modules:
                if q in module.name.lower() or q in module.description.lower():
                    results.append(module)
        return results
