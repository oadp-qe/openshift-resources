# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field

from ...k8s.apimachinery.pkg.apis.meta import v1


class SecurityContextConstraints(BaseModel):
    allowHostDirVolumePlugin: bool = Field(
        ...,
        description='AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin',
    )
    allowHostIPC: bool = Field(
        ...,
        description='AllowHostIPC determines if the policy allows host ipc in the containers.',
    )
    allowHostNetwork: bool = Field(
        ...,
        description='AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.',
    )
    allowHostPID: bool = Field(
        ...,
        description='AllowHostPID determines if the policy allows host pid in the containers.',
    )
    allowHostPorts: bool = Field(
        ...,
        description='AllowHostPorts determines if the policy allows host ports in the containers.',
    )
    allowPrivilegeEscalation: Optional[Any] = Field(
        None,
        description='AllowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.',
    )
    allowPrivilegedContainer: bool = Field(
        ...,
        description='AllowPrivilegedContainer determines if a container can request to be run as privileged.',
    )
    allowedCapabilities: Optional[Any] = Field(
        None,
        description="AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities. To allow all capabilities you may use '*'.",
    )
    allowedFlexVolumes: Optional[Any] = Field(
        None,
        description='AllowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the "Volumes" field.',
    )
    allowedUnsafeSysctls: Optional[Any] = Field(
        None,
        description='AllowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection. \n Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.',
    )
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    defaultAddCapabilities: Optional[Any] = Field(
        None,
        description='DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.',
    )
    defaultAllowPrivilegeEscalation: Optional[Any] = Field(
        None,
        description='DefaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.',
    )
    forbiddenSysctls: Optional[Any] = Field(
        None,
        description='ForbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. \n Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.',
    )
    fsGroup: Optional[Any] = Field(
        None,
        description='FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.',
    )
    groups: Optional[Any] = Field(
        None,
        description='The groups that have permission to use this security context constraints',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    priority: Optional[Any] = Field(
        None,
        description='Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority. An unset value is considered a 0 priority. If scores for multiple SCCs are equal they will be sorted from most restrictive to least restrictive. If both priorities and restrictions are equal the SCCs will be sorted by name.',
    )
    readOnlyRootFilesystem: bool = Field(
        ...,
        description='ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.',
    )
    requiredDropCapabilities: Optional[Any] = Field(
        None,
        description='RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.',
    )
    runAsUser: Optional[Any] = Field(
        None,
        description='RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.',
    )
    seLinuxContext: Optional[Any] = Field(
        None,
        description='SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.',
    )
    seccompProfiles: Optional[Any] = Field(
        None,
        description="SeccompProfiles lists the allowed profiles that may be set for the pod or container's seccomp annotations.  An unset (nil) or empty value means that no profiles may be specifid by the pod or container.\tThe wildcard '*' may be used to allow all profiles.  When used to generate a value for a pod the first non-wildcard profile will be used as the default.",
    )
    supplementalGroups: Optional[Any] = Field(
        None,
        description='SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.',
    )
    users: Optional[Any] = Field(
        None,
        description='The users who have permissions to use this security context constraints',
    )
    volumes: Optional[Any] = Field(
        None,
        description='Volumes is a white list of allowed volume plugins.  FSType corresponds directly with the field names of a VolumeSource (azureFile, configMap, emptyDir).  To allow all volumes you may use "*". To allow no volumes, set to ["none"].',
    )


class SecurityContextConstraintsList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[SecurityContextConstraints] = Field(
        ...,
        description='List of securitycontextconstraints. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
