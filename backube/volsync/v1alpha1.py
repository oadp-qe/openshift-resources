# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr

from ...io.k8s.apimachinery.pkg.apis.meta import v1


class External(BaseModel):
    parameters: Optional[Dict[str, str]] = Field(
        None,
        description='parameters are provider-specific key/value configuration parameters. For more information, please see the documentation of the specific replication provider being used.',
    )
    provider: Optional[str] = Field(
        None,
        description='provider is the name of the external replication provider. The name should be of the form: domain.com/provider.',
    )


class CopyMethod(Enum):
    Direct = 'Direct'
    None_ = 'None'
    Clone = 'Clone'
    Snapshot = 'Snapshot'


class Rclone(BaseModel):
    accessModes: Optional[List[str]] = Field(
        None,
        description='accessModes specifies the access modes for the destination volume.',
        min_items=1,
    )
    capacity: Optional[Any] = Field(
        None, description='capacity is the size of the destination volume to create.'
    )
    copyMethod: Optional[CopyMethod] = Field(
        None,
        description='copyMethod describes how a point-in-time (PiT) image of the destination volume should be created.',
    )
    destinationPVC: Optional[str] = Field(
        None,
        description='destinationPVC is a PVC to use as the transfer destination instead of automatically provisioning one. Either this field or both capacity and accessModes must be specified.',
    )
    rcloneConfig: Optional[str] = Field(
        None, description='RcloneConfig is the rclone secret name'
    )
    rcloneConfigSection: Optional[str] = Field(
        None,
        description='RcloneConfigSection is the section in rclone_config file to use for the current job.',
    )
    rcloneDestPath: Optional[str] = Field(
        None, description='RcloneDestPath is the remote path to sync to.'
    )
    storageClassName: Optional[str] = Field(
        None,
        description='storageClassName can be used to specify the StorageClass of the destination volume. If not set, the default StorageClass will be used.',
    )
    volumeSnapshotClassName: Optional[str] = Field(
        None,
        description='volumeSnapshotClassName can be used to specify the VSC to be used if copyMethod is Snapshot. If not set, the default VSC is used.',
    )


class CopyMethodModel(Enum):
    Direct = 'Direct'
    None_ = 'None'
    Clone = 'Clone'
    Snapshot = 'Snapshot'


class Restic(BaseModel):
    accessModes: Optional[List[str]] = Field(
        None,
        description='accessModes specifies the access modes for the destination volume.',
        min_items=1,
    )
    cacheAccessModes: Optional[List[str]] = Field(
        None,
        description='accessModes can be used to set the accessModes of restic metadata cache volume',
    )
    cacheCapacity: Optional[Any] = Field(
        None,
        description='cacheCapacity can be used to set the size of the restic metadata cache volume',
    )
    cacheStorageClassName: Optional[str] = Field(
        None,
        description='cacheStorageClassName can be used to set the StorageClass of the restic metadata cache volume',
    )
    capacity: Optional[Any] = Field(
        None, description='capacity is the size of the destination volume to create.'
    )
    copyMethod: Optional[CopyMethodModel] = Field(
        None,
        description='copyMethod describes how a point-in-time (PiT) image of the destination volume should be created.',
    )
    destinationPVC: Optional[str] = Field(
        None,
        description='destinationPVC is a PVC to use as the transfer destination instead of automatically provisioning one. Either this field or both capacity and accessModes must be specified.',
    )
    previous: Optional[int] = Field(
        None,
        description='Previous specifies the number of image to skip before selecting one to restore from',
    )
    repository: Optional[str] = Field(
        None, description='Repository is the secret name containing repository info'
    )
    restoreAsOf: Optional[datetime] = Field(
        None,
        description='RestoreAsOf refers to the backup that is most recent as of that time.',
    )
    storageClassName: Optional[str] = Field(
        None,
        description='storageClassName can be used to specify the StorageClass of the destination volume. If not set, the default StorageClass will be used.',
    )
    volumeSnapshotClassName: Optional[str] = Field(
        None,
        description='volumeSnapshotClassName can be used to specify the VSC to be used if copyMethod is Snapshot. If not set, the default VSC is used.',
    )


class CopyMethodModel1(Enum):
    Direct = 'Direct'
    None_ = 'None'
    Clone = 'Clone'
    Snapshot = 'Snapshot'


class Rsync(BaseModel):
    accessModes: Optional[List[str]] = Field(
        None,
        description='accessModes specifies the access modes for the destination volume.',
        min_items=1,
    )
    address: Optional[str] = Field(
        None, description='address is the remote address to connect to for replication.'
    )
    capacity: Optional[Any] = Field(
        None, description='capacity is the size of the destination volume to create.'
    )
    copyMethod: Optional[CopyMethodModel1] = Field(
        None,
        description='copyMethod describes how a point-in-time (PiT) image of the destination volume should be created.',
    )
    destinationPVC: Optional[str] = Field(
        None,
        description='destinationPVC is a PVC to use as the transfer destination instead of automatically provisioning one. Either this field or both capacity and accessModes must be specified.',
    )
    path: Optional[str] = Field(
        None, description='path is the remote path to rsync from. Defaults to "/"'
    )
    port: Optional[conint(ge=0, le=65535)] = Field(
        None,
        description='port is the SSH port to connect to for replication. Defaults to 22.',
    )
    serviceType: Optional[str] = Field(
        None,
        description='serviceType determines the Service type that will be created for incoming SSH connections.',
    )
    sshKeys: Optional[str] = Field(
        None,
        description='sshKeys is the name of a Secret that contains the SSH keys to be used for authentication. If not provided, the keys will be generated.',
    )
    sshUser: Optional[str] = Field(
        None,
        description='sshUser is the username for outgoing SSH connections. Defaults to "root".',
    )
    storageClassName: Optional[str] = Field(
        None,
        description='storageClassName can be used to specify the StorageClass of the destination volume. If not set, the default StorageClass will be used.',
    )
    volumeSnapshotClassName: Optional[str] = Field(
        None,
        description='volumeSnapshotClassName can be used to specify the VSC to be used if copyMethod is Snapshot. If not set, the default VSC is used.',
    )


class Trigger(BaseModel):
    manual: Optional[str] = Field(
        None,
        description='manual is a string value that schedules a manual trigger. Once a sync completes then status.lastManualSync is set to the same string value. A consumer of a manual trigger should set spec.trigger.manual to a known value and then wait for lastManualSync to be updated by the operator to the same value, which means that the manual trigger will then pause and wait for further updates to the trigger.',
    )
    schedule: Optional[
        constr(regex=r'^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$')
    ] = Field(
        None,
        description='schedule is a cronspec (https://en.wikipedia.org/wiki/Cron#Overview) that can be used to schedule replication to occur at regular, time-based intervals.',
    )


class Spec(BaseModel):
    external: Optional[External] = Field(
        None,
        description='external defines the configuration when using an external replication provider.',
    )
    paused: Optional[bool] = Field(
        None,
        description='paused can be used to temporarily stop replication. Defaults to "false".',
    )
    rclone: Optional[Rclone] = Field(
        None,
        description='rclone defines the configuration when using Rclone-based replication.',
    )
    restic: Optional[Restic] = Field(
        None,
        description='restic defines the configuration when using Restic-based replication.',
    )
    rsync: Optional[Rsync] = Field(
        None,
        description='rsync defines the configuration when using Rsync-based replication.',
    )
    trigger: Optional[Trigger] = Field(
        None,
        description='trigger determines if/when the destination should attempt to synchronize data with the source.',
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


class LatestImage(BaseModel):
    apiGroup: Optional[str] = Field(
        None,
        description='APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.',
    )
    kind: str = Field(..., description='Kind is the type of resource being referenced')
    name: str = Field(..., description='Name is the name of resource being referenced')


class RsyncModel(BaseModel):
    address: Optional[str] = Field(
        None,
        description='address is the address to connect to for incoming SSH replication connections.',
    )
    port: Optional[int] = Field(
        None,
        description='port is the SSH port to connect to for incoming SSH replication connections.',
    )
    sshKeys: Optional[str] = Field(
        None,
        description='sshKeys is the name of a Secret that contains the SSH keys to be used for authentication. If not provided in .spec.rsync.sshKeys, SSH keys will be generated and the appropriate keys for the remote side will be placed here.',
    )


class StatusModel(BaseModel):
    conditions: Optional[List[Condition]] = Field(
        None,
        description="conditions represent the latest available observations of the destination's state.",
    )
    external: Optional[Dict[str, str]] = Field(
        None,
        description='external contains provider-specific status information. For more details, please see the documentation of the specific replication provider being used.',
    )
    lastManualSync: Optional[str] = Field(
        None,
        description='lastManualSync is set to the last spec.trigger.manual when the manual sync is done.',
    )
    lastSyncDuration: Optional[str] = Field(
        None,
        description='lastSyncDuration is the amount of time required to send the most recent update.',
    )
    lastSyncStartTime: Optional[datetime] = Field(
        None,
        description='lastSyncStartTime is the time the most recent synchronization started.',
    )
    lastSyncTime: Optional[datetime] = Field(
        None,
        description='lastSyncTime is the time of the most recent successful synchronization.',
    )
    latestImage: Optional[LatestImage] = Field(
        None,
        description='latestImage in the object holding the most recent consistent replicated image.',
    )
    nextSyncTime: Optional[datetime] = Field(
        None,
        description='nextSyncTime is the time when the next volume synchronization is scheduled to start (for schedule-based synchronization).',
    )
    rsync: Optional[RsyncModel] = Field(
        None,
        description='rsync contains status information for Rsync-based replication.',
    )


class ExternalModel(BaseModel):
    parameters: Optional[Dict[str, str]] = Field(
        None,
        description='parameters are provider-specific key/value configuration parameters. For more information, please see the documentation of the specific replication provider being used.',
    )
    provider: Optional[str] = Field(
        None,
        description='provider is the name of the external replication provider. The name should be of the form: domain.com/provider.',
    )


class CopyMethodModel2(Enum):
    Direct = 'Direct'
    None_ = 'None'
    Clone = 'Clone'
    Snapshot = 'Snapshot'


class RcloneModel(BaseModel):
    accessModes: Optional[List[str]] = Field(
        None,
        description='accessModes can be used to override the accessModes of the PiT image.',
        min_items=1,
    )
    capacity: Optional[Any] = Field(
        None,
        description='capacity can be used to override the capacity of the PiT image.',
    )
    copyMethod: Optional[CopyMethodModel2] = Field(
        None,
        description='copyMethod describes how a point-in-time (PiT) image of the source volume should be created.',
    )
    rcloneConfig: Optional[str] = Field(
        None, description='RcloneConfig is the rclone secret name'
    )
    rcloneConfigSection: Optional[str] = Field(
        None,
        description='RcloneConfigSection is the section in rclone_config file to use for the current job.',
    )
    rcloneDestPath: Optional[str] = Field(
        None, description='RcloneDestPath is the remote path to sync to.'
    )
    storageClassName: Optional[str] = Field(
        None,
        description='storageClassName can be used to override the StorageClass of the PiT image.',
    )
    volumeSnapshotClassName: Optional[str] = Field(
        None,
        description='volumeSnapshotClassName can be used to specify the VSC to be used if copyMethod is Snapshot. If not set, the default VSC is used.',
    )


class CopyMethodModel3(Enum):
    Direct = 'Direct'
    None_ = 'None'
    Clone = 'Clone'
    Snapshot = 'Snapshot'


class Retain(BaseModel):
    daily: Optional[int] = Field(
        None, description='Daily defines the number of snapshots to be kept daily'
    )
    hourly: Optional[int] = Field(
        None, description='Hourly defines the number of snapshots to be kept hourly'
    )
    monthly: Optional[int] = Field(
        None, description='Monthly defines the number of snapshots to be kept monthly'
    )
    weekly: Optional[int] = Field(
        None, description='Weekly defines the number of snapshots to be kept weekly'
    )
    within: Optional[str] = Field(
        None,
        description='Within defines the number of snapshots to be kept Within the given time period',
    )
    yearly: Optional[int] = Field(
        None, description='Yearly defines the number of snapshots to be kept yearly'
    )


class ResticModel(BaseModel):
    accessModes: Optional[List[str]] = Field(
        None,
        description='accessModes can be used to override the accessModes of the PiT image.',
        min_items=1,
    )
    cacheAccessModes: Optional[List[str]] = Field(
        None,
        description='CacheAccessModes can be used to set the accessModes of restic metadata cache volume',
    )
    cacheCapacity: Optional[Any] = Field(
        None,
        description='cacheCapacity can be used to set the size of the restic metadata cache volume',
    )
    cacheStorageClassName: Optional[str] = Field(
        None,
        description='cacheStorageClassName can be used to set the StorageClass of the restic metadata cache volume',
    )
    capacity: Optional[Any] = Field(
        None,
        description='capacity can be used to override the capacity of the PiT image.',
    )
    copyMethod: Optional[CopyMethodModel3] = Field(
        None,
        description='copyMethod describes how a point-in-time (PiT) image of the source volume should be created.',
    )
    pruneIntervalDays: Optional[int] = Field(
        None, description='PruneIntervalDays define how often to prune the repository'
    )
    repository: Optional[str] = Field(
        None, description='Repository is the secret name containing repository info'
    )
    retain: Optional[Retain] = Field(
        None, description='ResticRetainPolicy define the retain policy'
    )
    storageClassName: Optional[str] = Field(
        None,
        description='storageClassName can be used to override the StorageClass of the PiT image.',
    )
    volumeSnapshotClassName: Optional[str] = Field(
        None,
        description='volumeSnapshotClassName can be used to specify the VSC to be used if copyMethod is Snapshot. If not set, the default VSC is used.',
    )


class CopyMethodModel4(Enum):
    Direct = 'Direct'
    None_ = 'None'
    Clone = 'Clone'
    Snapshot = 'Snapshot'


class RsyncModel1(BaseModel):
    accessModes: Optional[List[str]] = Field(
        None,
        description='accessModes can be used to override the accessModes of the PiT image.',
        min_items=1,
    )
    address: Optional[str] = Field(
        None, description='address is the remote address to connect to for replication.'
    )
    capacity: Optional[Any] = Field(
        None,
        description='capacity can be used to override the capacity of the PiT image.',
    )
    copyMethod: Optional[CopyMethodModel4] = Field(
        None,
        description='copyMethod describes how a point-in-time (PiT) image of the source volume should be created.',
    )
    path: Optional[str] = Field(
        None, description='path is the remote path to rsync to. Defaults to "/"'
    )
    port: Optional[conint(ge=0, le=65535)] = Field(
        None,
        description='port is the SSH port to connect to for replication. Defaults to 22.',
    )
    serviceType: Optional[str] = Field(
        None,
        description='serviceType determines the Service type that will be created for incoming SSH connections.',
    )
    sshKeys: Optional[str] = Field(
        None,
        description='sshKeys is the name of a Secret that contains the SSH keys to be used for authentication. If not provided, the keys will be generated.',
    )
    sshUser: Optional[str] = Field(
        None,
        description='sshUser is the username for outgoing SSH connections. Defaults to "root".',
    )
    storageClassName: Optional[str] = Field(
        None,
        description='storageClassName can be used to override the StorageClass of the PiT image.',
    )
    volumeSnapshotClassName: Optional[str] = Field(
        None,
        description='volumeSnapshotClassName can be used to specify the VSC to be used if copyMethod is Snapshot. If not set, the default VSC is used.',
    )


class Peer(BaseModel):
    ID: str = Field(..., description="The peer's Syncthing ID.")
    address: str = Field(
        ..., description="The peer's address that our Syncthing node will connect to."
    )
    introducer: bool = Field(
        ...,
        description='A flag that determines whether this peer should introduce us to other peers sharing this volume. It is HIGHLY recommended that two Syncthing peers do NOT set each other as introducers as you will have a difficult time disconnecting the two.',
    )


class Syncthing(BaseModel):
    configAccessModes: Optional[List[str]] = Field(
        None, description='Used to set the accessModes of Syncthing config volume.'
    )
    configCapacity: Optional[Any] = Field(
        None, description='Used to set the size of the Syncthing config volume.'
    )
    configStorageClassName: Optional[str] = Field(
        None, description='Used to set the StorageClass of the Syncthing config volume.'
    )
    peers: Optional[List[Peer]] = Field(
        None, description='List of Syncthing peers to be connected for syncing'
    )
    serviceType: Optional[str] = Field(
        None, description='Type of service to be used when exposing the Syncthing peer'
    )


class TriggerModel(BaseModel):
    manual: Optional[str] = Field(
        None,
        description='manual is a string value that schedules a manual trigger. Once a sync completes then status.lastManualSync is set to the same string value. A consumer of a manual trigger should set spec.trigger.manual to a known value and then wait for lastManualSync to be updated by the operator to the same value, which means that the manual trigger will then pause and wait for further updates to the trigger.',
    )
    schedule: Optional[
        constr(regex=r'^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$')
    ] = Field(
        None,
        description='schedule is a cronspec (https://en.wikipedia.org/wiki/Cron#Overview) that can be used to schedule replication to occur at regular, time-based intervals.',
    )


class SpecModel(BaseModel):
    external: Optional[ExternalModel] = Field(
        None,
        description='external defines the configuration when using an external replication provider.',
    )
    paused: Optional[bool] = Field(
        None,
        description='paused can be used to temporarily stop replication. Defaults to "false".',
    )
    rclone: Optional[RcloneModel] = Field(
        None,
        description='rclone defines the configuration when using Rclone-based replication.',
    )
    restic: Optional[ResticModel] = Field(
        None,
        description='restic defines the configuration when using Restic-based replication.',
    )
    rsync: Optional[RsyncModel1] = Field(
        None,
        description='rsync defines the configuration when using Rsync-based replication.',
    )
    sourcePVC: Optional[str] = Field(
        None,
        description='sourcePVC is the name of the PersistentVolumeClaim (PVC) to replicate.',
    )
    syncthing: Optional[Syncthing] = Field(
        None,
        description='syncthing defines the configuration when using Syncthing-based replication.',
    )
    trigger: Optional[TriggerModel] = Field(
        None,
        description='trigger determines when the latest state of the volume will be captured (and potentially replicated to the destination).',
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


class ResticModel1(BaseModel):
    lastPruned: Optional[datetime] = Field(
        None, description='lastPruned in the object holding the time of last pruned'
    )


class RsyncModel2(BaseModel):
    address: Optional[str] = Field(
        None,
        description='address is the address to connect to for incoming SSH replication connections.',
    )
    port: Optional[int] = Field(
        None,
        description='port is the SSH port to connect to for incoming SSH replication connections.',
    )
    sshKeys: Optional[str] = Field(
        None,
        description='sshKeys is the name of a Secret that contains the SSH keys to be used for authentication. If not provided in .spec.rsync.sshKeys, SSH keys will be generated and the appropriate keys for the remote side will be placed here.',
    )


class PeerModel(BaseModel):
    ID: str = Field(..., description="ID Is the peer's Syncthing ID.")
    address: str = Field(..., description='The address of the Syncthing peer.')
    connected: bool = Field(
        ..., description='Flag indicating whether peer is currently connected.'
    )
    introducedBy: Optional[str] = Field(
        None,
        description='The ID of the Syncthing peer that this one was introduced by.',
    )
    name: Optional[str] = Field(
        None, description='A friendly name to associate the given device.'
    )


class SyncthingModel(BaseModel):
    ID: Optional[str] = Field(
        None, description='Device ID of the current syncthing device'
    )
    address: Optional[str] = Field(
        None,
        description='Service address where Syncthing is exposed to the rest of the world',
    )
    peers: Optional[List[PeerModel]] = Field(
        None, description='List of the Syncthing nodes we are currently connected to.'
    )


class StatusModel2(BaseModel):
    conditions: Optional[List[ConditionModel]] = Field(
        None,
        description="conditions represent the latest available observations of the source's state.",
    )
    external: Optional[Dict[str, str]] = Field(
        None,
        description='external contains provider-specific status information. For more details, please see the documentation of the specific replication provider being used.',
    )
    lastManualSync: Optional[str] = Field(
        None,
        description='lastManualSync is set to the last spec.trigger.manual when the manual sync is done.',
    )
    lastSyncDuration: Optional[str] = Field(
        None,
        description='lastSyncDuration is the amount of time required to send the most recent update.',
    )
    lastSyncStartTime: Optional[datetime] = Field(
        None,
        description='lastSyncStartTime is the time the most recent synchronization started.',
    )
    lastSyncTime: Optional[datetime] = Field(
        None,
        description='lastSyncTime is the time of the most recent successful synchronization.',
    )
    nextSyncTime: Optional[datetime] = Field(
        None,
        description='nextSyncTime is the time when the next volume synchronization is scheduled to start (for schedule-based synchronization).',
    )
    restic: Optional[ResticModel1] = Field(
        None,
        description='restic contains status information for Restic-based replication.',
    )
    rsync: Optional[RsyncModel2] = Field(
        None,
        description='rsync contains status information for Rsync-based replication.',
    )
    syncthing: Optional[SyncthingModel] = Field(
        None,
        description='contains status information when Syncthing-based replication is used.',
    )


class ReplicationDestination(BaseModel):
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
    spec: Optional[Spec] = Field(
        None,
        description='spec is the desired state of the ReplicationDestination, including the replication method to use and its configuration.',
    )
    status: Optional[StatusModel] = Field(
        None,
        description='status is the observed state of the ReplicationDestination as determined by the controller.',
    )


class ReplicationDestinationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ReplicationDestination] = Field(
        ...,
        description='List of replicationdestinations. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ReplicationSource(BaseModel):
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
        description='spec is the desired state of the ReplicationSource, including the replication method to use and its configuration.',
    )
    status: Optional[StatusModel2] = Field(
        None,
        description='status is the observed state of the ReplicationSource as determined by the controller.',
    )


class ReplicationSourceList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ReplicationSource] = Field(
        ...,
        description='List of replicationsources. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
