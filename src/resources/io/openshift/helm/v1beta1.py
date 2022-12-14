# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, conint, constr

from ...k8s.apimachinery.pkg.apis.meta import v1


class Ca(BaseModel):
    name: str = Field(
        ..., description='name is the metadata.name of the referenced config map'
    )


class TlsClientConfig(BaseModel):
    name: str = Field(
        ..., description='name is the metadata.name of the referenced secret'
    )


class ConnectionConfig(BaseModel):
    ca: Optional[Ca] = Field(
        None,
        description='ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this config map is openshift-config.',
    )
    tlsClientConfig: Optional[TlsClientConfig] = Field(
        None,
        description='tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret is openshift-config.',
    )
    url: Optional[constr(regex=r'^https?:\/\/', max_length=2048)] = Field(
        None, description='Chart repository URL'
    )


class Spec(BaseModel):
    connectionConfig: Optional[ConnectionConfig] = Field(
        None, description='Required configuration for connecting to the chart repo'
    )
    description: Optional[constr(min_length=1, max_length=2048)] = Field(
        None,
        description='Optional human readable repository description, it can be used by UI for displaying purposes',
    )
    disabled: Optional[bool] = Field(
        None,
        description='If set to true, disable the repo usage in the cluster/namespace',
    )
    name: Optional[constr(min_length=1, max_length=100)] = Field(
        None,
        description='Optional associated human readable repository name, it can be used by UI for displaying purposes',
    )


class Status(Enum):
    True_ = 'True'
    False_ = 'False'
    Unknown = 'Unknown'


class Condition(BaseModel):
    lastTransitionTime: datetime = Field(
        ...,
        description='lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.',
    )
    message: constr(max_length=32768) = Field(
        ...,
        description='message is a human readable message indicating details about the transition. This may be an empty string.',
    )
    observedGeneration: Optional[conint(ge=0)] = Field(
        None,
        description='observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.',
    )
    reason: constr(
        regex=r'^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$', min_length=1, max_length=1024
    ) = Field(
        ...,
        description="reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.",
    )
    status: Status = Field(
        ..., description='status of the condition, one of True, False, Unknown.'
    )
    type: constr(
        regex=r'^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$',
        max_length=316,
    ) = Field(
        ...,
        description='type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)',
    )


class StatusModel(BaseModel):
    conditions: Optional[List[Condition]] = Field(
        None, description='conditions is a list of conditions and their statuses'
    )


class CaModel(BaseModel):
    name: str = Field(
        ..., description='name is the metadata.name of the referenced config map'
    )


class TlsClientConfigModel(BaseModel):
    name: str = Field(
        ..., description='name is the metadata.name of the referenced secret'
    )


class ConnectionConfigModel(BaseModel):
    ca: Optional[CaModel] = Field(
        None,
        description='ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this config map is openshift-config.',
    )
    tlsClientConfig: Optional[TlsClientConfigModel] = Field(
        None,
        description='tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret is openshift-config.',
    )
    url: Optional[constr(regex=r'^https?:\/\/', max_length=2048)] = Field(
        None, description='Chart repository URL'
    )


class SpecModel(BaseModel):
    connectionConfig: Optional[ConnectionConfigModel] = Field(
        None, description='Required configuration for connecting to the chart repo'
    )
    description: Optional[constr(min_length=1, max_length=2048)] = Field(
        None,
        description='Optional human readable repository description, it can be used by UI for displaying purposes',
    )
    disabled: Optional[bool] = Field(
        None,
        description='If set to true, disable the repo usage in the cluster/namespace',
    )
    name: Optional[constr(min_length=1, max_length=100)] = Field(
        None,
        description='Optional associated human readable repository name, it can be used by UI for displaying purposes',
    )


class StatusModel1(Enum):
    True_ = 'True'
    False_ = 'False'
    Unknown = 'Unknown'


class ConditionModel(BaseModel):
    lastTransitionTime: datetime = Field(
        ...,
        description='lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.',
    )
    message: constr(max_length=32768) = Field(
        ...,
        description='message is a human readable message indicating details about the transition. This may be an empty string.',
    )
    observedGeneration: Optional[conint(ge=0)] = Field(
        None,
        description='observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.',
    )
    reason: constr(
        regex=r'^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$', min_length=1, max_length=1024
    ) = Field(
        ...,
        description="reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.",
    )
    status: StatusModel1 = Field(
        ..., description='status of the condition, one of True, False, Unknown.'
    )
    type: constr(
        regex=r'^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$',
        max_length=316,
    ) = Field(
        ...,
        description='type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)',
    )


class StatusModel2(BaseModel):
    conditions: Optional[List[ConditionModel]] = Field(
        None, description='conditions is a list of conditions and their statuses'
    )


class HelmChartRepository(BaseModel):
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
    spec: Spec = Field(
        ..., description='spec holds user settable values for configuration'
    )
    status: Optional[StatusModel] = Field(
        None, description='Observed status of the repository within the cluster..'
    )


class HelmChartRepositoryList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[HelmChartRepository] = Field(
        ...,
        description='List of helmchartrepositories. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ProjectHelmChartRepository(BaseModel):
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
    spec: SpecModel = Field(
        ..., description='spec holds user settable values for configuration'
    )
    status: Optional[StatusModel2] = Field(
        None, description='Observed status of the repository within the namespace..'
    )


class ProjectHelmChartRepositoryList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ProjectHelmChartRepository] = Field(
        ...,
        description='List of projecthelmchartrepositories. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
