from typing import Literal

from pydantic import BaseModel, Field


class GivenClause(BaseModel):
    description: str
    setup: dict = Field(default_factory=dict)


class WhenClause(BaseModel):
    description: str
    action: dict = Field(default_factory=dict)


class ThenAssertion(BaseModel):
    description: str
    check: dict = Field(default_factory=dict)


class SLO(BaseModel):
    p95_latency_ms: int | None = None
    availability: float | None = Field(default=None, ge=0, le=1)


class Spec(BaseModel):
    feature: str
    priority: Literal["P0", "P1", "P2", "P3"] = "P2"
    category: str
    description: str
    kpi_links: list[str] = Field(default_factory=list)
    slo: SLO | None = None
    given: list[GivenClause]
    when: list[WhenClause]
    then: list[ThenAssertion]
    invariants: list[str] = Field(default_factory=list)
    failure_modes: list[str] = Field(default_factory=list)
