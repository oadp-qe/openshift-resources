# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr

from ...k8s.apimachinery.pkg.apis.meta import v1


class TunedConfig(BaseModel):
    reapply_sysctl: Optional[bool] = Field(
        None,
        description='turn reapply_sysctl functionality on/off for the TuneD daemon: true/false',
    )


class Config(BaseModel):
    debug: Optional[bool] = Field(
        None, description='option to debug TuneD daemon execution'
    )
    providerName: Optional[str] = Field(
        None,
        description='Name of the cloud provider as taken from the Node providerID: <ProviderName>://<ProviderSpecificNodeID>',
    )
    tunedConfig: Optional[TunedConfig] = Field(
        None,
        description='Global configuration for the TuneD daemon as defined in tuned-main.conf',
    )
    tunedProfile: str = Field(..., description='TuneD profile to apply')


class Spec(BaseModel):
    config: Config


class Condition(BaseModel):
    lastTransitionTime: datetime = Field(
        ...,
        description='lastTransitionTime is the time of the last update to the current status property.',
    )
    message: Optional[str] = Field(
        None,
        description='message provides additional information about the current condition. This is only to be consumed by humans.',
    )
    reason: Optional[str] = Field(
        None,
        description="reason is the CamelCase reason for the condition's current status.",
    )
    status: str = Field(
        ..., description='status of the condition, one of True, False, Unknown.'
    )
    type: str = Field(
        ..., description='type specifies the aspect reported by this condition.'
    )


class Status(BaseModel):
    bootcmdline: Optional[str] = Field(
        None,
        description='kernel parameters calculated by tuned for the active Tuned profile',
    )
    conditions: Optional[List[Condition]] = Field(
        None,
        description='conditions represents the state of the per-node Profile application',
    )
    stalld: Optional[bool] = Field(
        None,
        description='deploy stall daemon: https://git.kernel.org/pub/scm/utils/stalld/stalld.git',
    )
    tunedProfile: str = Field(
        ..., description='the current profile in use by the Tuned daemon'
    )


class ProfileItem(BaseModel):
    data: str = Field(
        ...,
        description='Specification of the Tuned profile to be consumed by the Tuned daemon.',
    )
    name: str = Field(
        ...,
        description='Name of the Tuned profile to be used in the recommend section.',
    )


class Type(Enum):
    node = 'node'
    pod = 'pod'


class MatchItem(BaseModel):
    label: str = Field(..., description='Node or Pod label name.')
    match: Optional[List[Any]] = Field(
        None,
        description='Additional rules governing application of the tuned profile connected by logical AND operator.',
    )
    type: Optional[Type] = Field(
        None, description='Match type: [node/pod]. If omitted, "node" is assumed.'
    )
    value: Optional[str] = Field(
        None,
        description='Node or Pod label value. If omitted, the presence of label name is enough to match.',
    )


class TunedConfigModel(BaseModel):
    reapply_sysctl: Optional[bool] = Field(
        None,
        description='turn reapply_sysctl functionality on/off for the TuneD daemon: true/false',
    )


class Operand(BaseModel):
    debug: Optional[bool] = Field(
        None,
        description='turn debugging on/off for the TuneD daemon: true/false (default is false)',
    )
    tunedConfig: Optional[TunedConfigModel] = Field(
        None,
        description='Global configuration for the TuneD daemon as defined in tuned-main.conf',
    )


class RecommendItem(BaseModel):
    machineConfigLabels: Optional[Dict[str, str]] = Field(
        None,
        description="MachineConfigLabels specifies the labels for a MachineConfig. The MachineConfig is created automatically to apply additional host settings (e.g. kernel boot parameters) profile 'Profile' needs and can only be applied by creating a MachineConfig. This involves finding all MachineConfigPools with machineConfigSelector matching the MachineConfigLabels and setting the profile 'Profile' on all nodes that match the MachineConfigPools' nodeSelectors.",
    )
    match: Optional[List[MatchItem]] = Field(
        None,
        description='Rules governing application of a Tuned profile connected by logical OR operator.',
    )
    operand: Optional[Operand] = Field(
        None, description='Optional operand configuration.'
    )
    priority: conint(ge=0) = Field(
        ..., description='Tuned profile priority. Highest priority is 0.'
    )
    profile: str = Field(..., description='Name of the Tuned profile to recommend.')


class SpecModel(BaseModel):
    managementState: Optional[
        constr(regex=r'^(Managed|Unmanaged|Force|Removed)$')
    ] = Field(
        None,
        description='managementState indicates whether the registry instance represented by this config instance is under operator management or not.  Valid values are Force, Managed, Unmanaged, and Removed.',
    )
    profile: Optional[List[ProfileItem]] = Field(None, description='Tuned profiles.')
    recommend: Optional[List[RecommendItem]] = Field(
        None, description='Selection logic for all Tuned profiles.'
    )


class Profile(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[Spec] = None
    status: Optional[Status] = Field(
        None,
        description='ProfileStatus is the status for a Profile resource; the status is for internal use only and its fields may be changed/removed in the future.',
    )


class ProfileList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Profile] = Field(
        ...,
        description='List of profiles. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class Tuned(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[SpecModel] = Field(
        None,
        description='spec is the specification of the desired behavior of Tuned. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status',
    )
    status: Optional[Dict[str, Any]] = Field(
        None, description='TunedStatus is the status for a Tuned resource.'
    )


class TunedList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Tuned] = Field(
        ...,
        description='List of tuneds. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
