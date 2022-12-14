# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field, constr

from ....k8s.apimachinery.pkg.apis.meta import v1


class TlsClientCert(BaseModel):
    name: str = Field(
        ..., description='name is the metadata.name of the referenced secret'
    )


class Spec(BaseModel):
    sourcePod: constr(
        regex=r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$'
    ) = Field(
        ...,
        description='SourcePod names the pod from which the condition will be checked',
    )
    targetEndpoint: constr(regex=r'^\S+:\d*$') = Field(
        ...,
        description='EndpointAddress to check. A TCP address of the form host:port. Note that if host is a DNS name, then the check would fail if the DNS name cannot be resolved. Specify an IP address for host to bypass DNS name lookup.',
    )
    tlsClientCert: Optional[TlsClientCert] = Field(
        None,
        description="TLSClientCert, if specified, references a kubernetes.io/tls type secret with 'tls.crt' and 'tls.key' entries containing an optional TLS client certificate and key to be used when checking endpoints that require a client certificate in order to gracefully preform the scan without causing excessive logging in the endpoint process. The secret must exist in the same namespace as this resource.",
    )


class Condition(BaseModel):
    lastTransitionTime: Optional[Any] = Field(
        None,
        description='Last time the condition transitioned from one status to another.',
    )
    message: Optional[str] = Field(
        None,
        description='Message indicating details about last transition in a human readable format.',
    )
    reason: Optional[str] = Field(
        None,
        description="Reason for the condition's last status transition in a machine readable format.",
    )
    status: str = Field(..., description='Status of the condition')
    type: str = Field(..., description='Type of the condition')


class Failure(BaseModel):
    latency: Optional[Any] = Field(
        None,
        description='Latency records how long the action mentioned in the entry took.',
    )
    message: Optional[str] = Field(
        None, description='Message explaining status in a human readable format.'
    )
    reason: Optional[str] = Field(
        None, description='Reason for status in a machine readable format.'
    )
    success: bool = Field(
        ...,
        description='Success indicates if the log entry indicates a success or failure.',
    )
    time: Optional[Any] = Field(None, description='Start time of check action.')


class EndLog(BaseModel):
    latency: Optional[Any] = Field(
        None,
        description='Latency records how long the action mentioned in the entry took.',
    )
    message: Optional[str] = Field(
        None, description='Message explaining status in a human readable format.'
    )
    reason: Optional[str] = Field(
        None, description='Reason for status in a machine readable format.'
    )
    success: bool = Field(
        ...,
        description='Success indicates if the log entry indicates a success or failure.',
    )
    time: Optional[Any] = Field(None, description='Start time of check action.')


class StartLog(BaseModel):
    latency: Optional[Any] = Field(
        None,
        description='Latency records how long the action mentioned in the entry took.',
    )
    message: Optional[str] = Field(
        None, description='Message explaining status in a human readable format.'
    )
    reason: Optional[str] = Field(
        None, description='Reason for status in a machine readable format.'
    )
    success: bool = Field(
        ...,
        description='Success indicates if the log entry indicates a success or failure.',
    )
    time: Optional[Any] = Field(None, description='Start time of check action.')


class Outage(BaseModel):
    end: Optional[Any] = Field(None, description='End of outage detected')
    endLogs: Optional[List[EndLog]] = Field(
        None,
        description='EndLogs contains log entries related to the end of this outage. Should contain the success entry that resolved the outage and possibly a few of the failure log entries that preceded it.',
    )
    message: Optional[str] = Field(
        None,
        description='Message summarizes outage details in a human readable format.',
    )
    start: Optional[Any] = Field(None, description='Start of outage detected')
    startLogs: Optional[List[StartLog]] = Field(
        None,
        description='StartLogs contains log entries related to the start of this outage. Should contain the original failure, any entries where the failure mode changed.',
    )


class Success(BaseModel):
    latency: Optional[Any] = Field(
        None,
        description='Latency records how long the action mentioned in the entry took.',
    )
    message: Optional[str] = Field(
        None, description='Message explaining status in a human readable format.'
    )
    reason: Optional[str] = Field(
        None, description='Reason for status in a machine readable format.'
    )
    success: bool = Field(
        ...,
        description='Success indicates if the log entry indicates a success or failure.',
    )
    time: Optional[Any] = Field(None, description='Start time of check action.')


class Status(BaseModel):
    conditions: Optional[List[Condition]] = Field(
        None, description='Conditions summarize the status of the check'
    )
    failures: Optional[List[Failure]] = Field(
        None, description='Failures contains logs of unsuccessful check actions'
    )
    outages: Optional[List[Outage]] = Field(
        None, description='Outages contains logs of time periods of outages'
    )
    successes: Optional[List[Success]] = Field(
        None, description='Successes contains logs successful check actions'
    )


class PodNetworkConnectivityCheck(BaseModel):
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
        ..., description='Spec defines the source and target of the connectivity check'
    )
    status: Optional[Status] = Field(
        None,
        description='Status contains the observed status of the connectivity check',
    )


class PodNetworkConnectivityCheckList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[PodNetworkConnectivityCheck] = Field(
        ...,
        description='List of podnetworkconnectivitychecks. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
