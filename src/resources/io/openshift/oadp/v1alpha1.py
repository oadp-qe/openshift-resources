# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr

from ...k8s.apimachinery.pkg.apis.meta import v1


class CreationSecret(BaseModel):
    key: str = Field(
        ...,
        description='The key of the secret to select from.  Must be a valid secret key.',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?',
    )
    optional: Optional[bool] = Field(
        None, description='Specify whether the Secret or its key must be defined'
    )


class Provider(Enum):
    aws = 'aws'


class Spec(BaseModel):
    creationSecret: CreationSecret = Field(
        ...,
        description='creationSecret is the secret that is needed to be used while creating the bucket.',
    )
    enableSharedConfig: Optional[bool] = Field(
        None,
        description='enableSharedConfig enable the use of shared config loading for AWS Buckets',
    )
    name: str = Field(
        ...,
        description='name is the name requested for the bucket (aws, gcp) or container (azure)',
    )
    provider: Provider = Field(
        ..., description='provider is the provider of the cloud storage'
    )
    region: Optional[str] = Field(
        None,
        description='region` for the bucket to be in, will be us-east-1 if not set.',
    )
    tags: Optional[Dict[str, str]] = Field(None, description='tags` for the bucket')


class Status(BaseModel):
    lastSyncTimestamp: Optional[datetime] = None
    name: str


class CloudStorageRef(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?',
    )


class Credential(BaseModel):
    key: str = Field(
        ...,
        description='The key of the secret to select from.  Must be a valid secret key.',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?',
    )
    optional: Optional[bool] = Field(
        None, description='Specify whether the Secret or its key must be defined'
    )


class Bucket(BaseModel):
    backupSyncPeriod: Optional[Any] = Field(
        None,
        description='backupSyncPeriod defines how frequently to sync backup API objects from object storage. A value of 0 disables sync.',
    )
    cloudStorageRef: CloudStorageRef = Field(
        ...,
        description='LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.',
    )
    config: Optional[Dict[str, str]] = Field(
        None, description='config is for provider-specific configuration fields.'
    )
    credential: Optional[Credential] = Field(
        None,
        description='credential contains the credential information intended to be used with this location',
    )
    default: Optional[bool] = Field(
        None,
        description='default indicates this location is the default backup storage location.',
    )


class AccessMode(Enum):
    ReadOnly = 'ReadOnly'
    ReadWrite = 'ReadWrite'


class CredentialModel(BaseModel):
    key: str = Field(
        ...,
        description='The key of the secret to select from.  Must be a valid secret key.',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid?',
    )
    optional: Optional[bool] = Field(
        None, description='Specify whether the Secret or its key must be defined'
    )


class ObjectStorage(BaseModel):
    bucket: str = Field(
        ..., description='Bucket is the bucket to use for object storage.'
    )
    caCert: Optional[str] = Field(
        None,
        description='CACert defines a CA bundle to use when verifying TLS connections to the provider.',
    )
    prefix: Optional[str] = Field(
        None,
        description='Prefix is the path inside a bucket to use for Velero storage. Optional.',
    )


class Velero(BaseModel):
    accessMode: Optional[AccessMode] = Field(
        None,
        description='AccessMode defines the permissions for the backup storage location.',
    )
    backupSyncPeriod: Optional[Any] = Field(
        None,
        description='BackupSyncPeriod defines how frequently to sync backup API objects from object storage. A value of 0 disables sync.',
    )
    config: Optional[Dict[str, str]] = Field(
        None, description='Config is for provider-specific configuration fields.'
    )
    credential: Optional[CredentialModel] = Field(
        None,
        description='Credential contains the credential information intended to be used with this location',
    )
    default: Optional[bool] = Field(
        None,
        description='Default indicates this location is the default backup storage location.',
    )
    objectStorage: ObjectStorage = Field(
        ...,
        description="ObjectStorageLocation specifies the settings necessary to connect to a provider's object storage.",
    )
    provider: str = Field(
        ..., description='Provider is the provider of the backup storage.'
    )
    validationFrequency: Optional[Any] = Field(
        None,
        description='ValidationFrequency defines how frequently to validate the corresponding object storage. A value of 0 disables validation.',
    )


class BackupLocation(BaseModel):
    bucket: Optional[Bucket] = None
    velero: Optional[Velero] = Field(
        None,
        description='BackupStorageLocationSpec defines the desired state of a Velero BackupStorageLocation',
    )


class Toleration(BaseModel):
    effect: Optional[str] = Field(
        None,
        description='Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.',
    )
    key: Optional[str] = Field(
        None,
        description='Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.',
    )
    operator: Optional[str] = Field(
        None,
        description="Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.",
    )
    tolerationSeconds: Optional[int] = Field(
        None,
        description='TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.',
    )
    value: Optional[str] = Field(
        None,
        description='Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.',
    )


class PodConfig(BaseModel):
    labels: Optional[Dict[str, str]] = Field(None, description='labels to add to pods')
    nodeSelector: Optional[Dict[str, str]] = Field(
        None,
        description='nodeSelector defines the nodeSelector to be supplied to Restic podSpec',
    )
    resourceAllocations: Optional[Any] = Field(
        None,
        description='resourceAllocations defines the CPU and Memory resource allocations for the restic Pod',
    )
    tolerations: Optional[List[Toleration]] = Field(
        None,
        description='tolerations defines the list of tolerations to be applied to Restic daemonset',
    )


class Restic(BaseModel):
    enable: Optional[bool] = Field(
        None,
        description='enable defines a boolean pointer whether we want the daemonset to exist or not',
    )
    podConfig: Optional[PodConfig] = Field(
        None, description='Pod specific configuration'
    )
    supplementalGroups: Optional[List[int]] = Field(
        None,
        description='supplementalGroups defines the linux groups to be applied to the Restic Pod',
    )
    timeout: Optional[str] = Field(
        None, description='timeout defines the Restic timeout, default value is 1h'
    )


class CustomPlugin(BaseModel):
    image: str
    name: str


class LogLevel(Enum):
    trace = 'trace'
    debug = 'debug'
    info = 'info'
    warning = 'warning'
    error = 'error'
    fatal = 'fatal'
    panic = 'panic'


class TolerationModel(BaseModel):
    effect: Optional[str] = Field(
        None,
        description='Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.',
    )
    key: Optional[str] = Field(
        None,
        description='Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.',
    )
    operator: Optional[str] = Field(
        None,
        description="Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.",
    )
    tolerationSeconds: Optional[int] = Field(
        None,
        description='TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.',
    )
    value: Optional[str] = Field(
        None,
        description='Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.',
    )


class PodConfigModel(BaseModel):
    labels: Optional[Dict[str, str]] = Field(None, description='labels to add to pods')
    nodeSelector: Optional[Dict[str, str]] = Field(
        None,
        description='nodeSelector defines the nodeSelector to be supplied to Restic podSpec',
    )
    resourceAllocations: Optional[Any] = Field(
        None,
        description='resourceAllocations defines the CPU and Memory resource allocations for the restic Pod',
    )
    tolerations: Optional[List[TolerationModel]] = Field(
        None,
        description='tolerations defines the list of tolerations to be applied to Restic daemonset',
    )


class VeleroModel(BaseModel):
    customPlugins: Optional[List[CustomPlugin]] = Field(
        None,
        description='customPlugins defines the custom plugin to be installed with Velero',
    )
    defaultPlugins: Optional[List[str]] = None
    featureFlags: Optional[List[str]] = Field(
        None,
        description='featureFlags defines the list of features to enable for Velero instance',
    )
    logLevel: Optional[LogLevel] = Field(
        None,
        description='Velero server???s log level (use debug for the most logging, leave unset for velero default)',
    )
    noDefaultBackupLocation: Optional[bool] = Field(
        None,
        description='If you need to install Velero without a default backup storage location noDefaultBackupLocation flag is required for confirmation',
    )
    podConfig: Optional[PodConfigModel] = Field(
        None, description='Pod specific configuration'
    )
    restoreResourcesVersionPriority: Optional[str] = Field(
        None,
        description='restoreResourceVersionPriority represents a configmap that will be created if defined for use in conjunction with EnableAPIGroupVersions feature flag Defining this field automatically add EnableAPIGroupVersions to the velero server feature flag',
    )


class Configuration(BaseModel):
    restic: Optional[Restic] = Field(
        None, description='ResticConfig is the configuration for restic server'
    )
    velero: Optional[VeleroModel] = None


class DataMover(BaseModel):
    credentialName: Optional[str] = Field(
        None, description='User supplied Restic Secret name'
    )
    enable: Optional[bool] = Field(
        None,
        description='enable flag is used to specify whether you want to deploy the volume snapshot mover controller',
    )
    timeout: Optional[str] = Field(
        None,
        description='User supplied timeout to be used for VolumeSnapshotBackup and VolumeSnapshotRestore to complete, default value is 10m',
    )


class Features(BaseModel):
    dataMover: Optional[DataMover] = Field(
        None, description='Contains data mover specific configurations'
    )


class Option(BaseModel):
    name: Optional[str] = Field(None, description='Required.')
    value: Optional[str] = None


class PodDnsConfig(BaseModel):
    nameservers: Optional[List[str]] = Field(
        None,
        description='A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.',
    )
    options: Optional[List[Option]] = Field(
        None,
        description='A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.',
    )
    searches: Optional[List[str]] = Field(
        None,
        description='A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.',
    )


class VeleroModel1(BaseModel):
    config: Optional[Dict[str, str]] = Field(
        None, description='Config is for provider-specific configuration fields.'
    )
    provider: str = Field(
        ..., description='Provider is the provider of the volume storage.'
    )


class SnapshotLocation(BaseModel):
    velero: VeleroModel1 = Field(
        ...,
        description='VolumeSnapshotLocationSpec defines the specification for a Velero VolumeSnapshotLocation.',
    )


class SpecModel(BaseModel):
    backupImages: Optional[bool] = Field(
        None,
        description='backupImages is used to specify whether you want to deploy a registry for enabling backup and restore of images',
    )
    backupLocations: Optional[List[BackupLocation]] = Field(
        None,
        description='backupLocations defines the list of desired configuration to use for BackupStorageLocations',
    )
    configuration: Configuration = Field(
        ...,
        description="configuration is used to configure the data protection application's server config",
    )
    features: Optional[Features] = Field(
        None,
        description='features defines the configuration for the DPA to enable the OADP tech preview features',
    )
    podAnnotations: Optional[Dict[str, str]] = Field(
        None, description='add annotations to pods deployed by operator'
    )
    podDnsConfig: Optional[PodDnsConfig] = Field(
        None,
        description='podDnsConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy. https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-dns-config',
    )
    podDnsPolicy: Optional[str] = Field(
        None,
        description="podDnsPolicy defines how a pod's DNS will be configured. https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy",
    )
    snapshotLocations: Optional[List[SnapshotLocation]] = Field(
        None,
        description='snapshotLocations defines the list of desired configuration to use for VolumeSnapshotLocations',
    )
    unsupportedOverrides: Optional[Dict[str, str]] = Field(
        None,
        description='unsupportedOverrides can be used to override images used in deployments. Available keys are:   - veleroImageFqin   - awsPluginImageFqin   - openshiftPluginImageFqin   - azurePluginImageFqin   - gcpPluginImageFqin   - csiPluginImageFqin   - dataMoverImageFqin   - resticRestoreImageFqin   - kubevirtPluginImageFqin',
    )


class StatusModel(Enum):
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
    status: StatusModel = Field(
        ..., description='status of the condition, one of True, False, Unknown.'
    )
    type: constr(
        regex=r'^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$',
        max_length=316,
    ) = Field(
        ...,
        description='type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)',
    )


class StatusModel1(BaseModel):
    conditions: Optional[List[Condition]] = None


class CloudStorage(BaseModel):
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
    status: Optional[Status] = None


class CloudStorageList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[CloudStorage] = Field(
        ...,
        description='List of cloudstorages. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class DataProtectionApplication(BaseModel):
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
        description='DataProtectionApplicationSpec defines the desired state of Velero',
    )
    status: Optional[StatusModel1] = Field(
        None,
        description='DataProtectionApplicationStatus defines the observed state of DataProtectionApplication',
    )


class DataProtectionApplicationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[DataProtectionApplication] = Field(
        ...,
        description='List of dataprotectionapplications. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
