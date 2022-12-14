# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from src.resources.io.k8s.api.core import v1 as v1_1
from src.resources.io.k8s.api.rbac import v1 as v1_2
from src.resources.io.k8s.apimachinery.pkg import runtime
from src.resources.io.k8s.apimachinery.pkg.apis.meta import v1


class SelfSubjectRulesReviewSpec(BaseModel):
    scopes: List[str] = Field(
        ...,
        description='Scopes to use for the evaluation.  Empty means "use the unscoped (full) permissions of the user/groups". Nil means "use the scopes on this request".',
    )


class SubjectRulesReviewSpec(BaseModel):
    groups: List[str] = Field(
        ...,
        description='Groups is optional.  Groups is the list of groups to which the User belongs.  At least one of User and Groups must be specified.',
    )
    scopes: List[str] = Field(
        ...,
        description='Scopes to use for the evaluation.  Empty means "use the unscoped (full) permissions of the user/groups".',
    )
    user: str = Field(
        ...,
        description='User is optional.  At least one of User and Groups must be specified.',
    )


class LocalResourceAccessReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    content: Optional[runtime.RawExtension] = Field(
        None,
        description='Content is the actual content of the request for create and update',
    )
    isNonResourceURL: bool = Field(
        ...,
        description='IsNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy)',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    namespace: str = Field(
        ...,
        description='Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces',
    )
    path: str = Field(..., description='Path is the path of a non resource URL')
    resource: str = Field(
        ..., description='Resource is one of the existing resource types'
    )
    resourceAPIGroup: str = Field(
        ...,
        description="Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined",
    )
    resourceAPIVersion: str = Field(
        ...,
        description='Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined',
    )
    resourceName: str = Field(
        ...,
        description='ResourceName is the name of the resource being requested for a "get" or deleted for a "delete"',
    )
    verb: str = Field(
        ..., description='Verb is one of: get, list, watch, create, update, delete'
    )


class LocalSubjectAccessReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    content: Optional[runtime.RawExtension] = Field(
        None,
        description='Content is the actual content of the request for create and update',
    )
    groups: List[str] = Field(
        ...,
        description='Groups is optional.  Groups is the list of groups to which the User belongs.',
    )
    isNonResourceURL: bool = Field(
        ...,
        description='IsNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy)',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    namespace: str = Field(
        ...,
        description='Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces',
    )
    path: str = Field(..., description='Path is the path of a non resource URL')
    resource: str = Field(
        ..., description='Resource is one of the existing resource types'
    )
    resourceAPIGroup: str = Field(
        ...,
        description="Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined",
    )
    resourceAPIVersion: str = Field(
        ...,
        description='Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined',
    )
    resourceName: str = Field(
        ...,
        description='ResourceName is the name of the resource being requested for a "get" or deleted for a "delete"',
    )
    scopes: List[str] = Field(
        ...,
        description='Scopes to use for the evaluation.  Empty means "use the unscoped (full) permissions of the user/groups". Nil for a self-SAR, means "use the scopes on this request". Nil for a regular SAR, means the same as empty.',
    )
    user: str = Field(
        ...,
        description='User is optional.  If both User and Groups are empty, the current authenticated user is used.',
    )
    verb: str = Field(
        ..., description='Verb is one of: get, list, watch, create, update, delete'
    )


class PolicyRule(BaseModel):
    apiGroups: Optional[List[str]] = Field(
        None,
        description='APIGroups is the name of the APIGroup that contains the resources.  If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed',
    )
    attributeRestrictions: Optional[runtime.RawExtension] = Field(
        None,
        description='AttributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error.',
    )
    nonResourceURLs: Optional[List[str]] = Field(
        None,
        description='NonResourceURLsSlice is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different.',
    )
    resourceNames: Optional[List[str]] = Field(
        None,
        description='ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.',
    )
    resources: List[str] = Field(
        ...,
        description='Resources is a list of resources this rule applies to.  ResourceAll represents all resources.',
    )
    verbs: List[str] = Field(
        ...,
        description='Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.',
    )


class ResourceAccessReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    content: Optional[runtime.RawExtension] = Field(
        None,
        description='Content is the actual content of the request for create and update',
    )
    isNonResourceURL: bool = Field(
        ...,
        description='IsNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy)',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    namespace: str = Field(
        ...,
        description='Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces',
    )
    path: str = Field(..., description='Path is the path of a non resource URL')
    resource: str = Field(
        ..., description='Resource is one of the existing resource types'
    )
    resourceAPIGroup: str = Field(
        ...,
        description="Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined",
    )
    resourceAPIVersion: str = Field(
        ...,
        description='Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined',
    )
    resourceName: str = Field(
        ...,
        description='ResourceName is the name of the resource being requested for a "get" or deleted for a "delete"',
    )
    verb: str = Field(
        ..., description='Verb is one of: get, list, watch, create, update, delete'
    )


class SubjectAccessReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    content: Optional[runtime.RawExtension] = Field(
        None,
        description='Content is the actual content of the request for create and update',
    )
    groups: List[str] = Field(
        ...,
        description='GroupsSlice is optional. Groups is the list of groups to which the User belongs.',
    )
    isNonResourceURL: bool = Field(
        ...,
        description='IsNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy)',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    namespace: str = Field(
        ...,
        description='Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces',
    )
    path: str = Field(..., description='Path is the path of a non resource URL')
    resource: str = Field(
        ..., description='Resource is one of the existing resource types'
    )
    resourceAPIGroup: str = Field(
        ...,
        description="Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined",
    )
    resourceAPIVersion: str = Field(
        ...,
        description='Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined',
    )
    resourceName: str = Field(
        ...,
        description='ResourceName is the name of the resource being requested for a "get" or deleted for a "delete"',
    )
    scopes: List[str] = Field(
        ...,
        description='Scopes to use for the evaluation.  Empty means "use the unscoped (full) permissions of the user/groups". Nil for a self-SAR, means "use the scopes on this request". Nil for a regular SAR, means the same as empty.',
    )
    user: str = Field(
        ...,
        description='User is optional. If both User and Groups are empty, the current authenticated user is used.',
    )
    verb: str = Field(
        ..., description='Verb is one of: get, list, watch, create, update, delete'
    )


class SubjectRulesReviewStatus(BaseModel):
    evaluationError: Optional[str] = Field(
        None,
        description='EvaluationError can appear in combination with Rules.  It means some error happened during evaluation that may have prevented additional rules from being populated.',
    )
    rules: List[PolicyRule] = Field(
        ...,
        description='Rules is the list of rules (no particular sort) that are allowed for the subject',
    )


class ClusterRoleBinding(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    groupNames: Optional[List[str]] = Field(
        None,
        description='GroupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMetaV2] = None
    roleRef: v1_1.ObjectReference = Field(
        ...,
        description='RoleRef can only reference the current namespace and the global namespace. If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role.',
    )
    subjects: List[v1_1.ObjectReference] = Field(
        ...,
        description='Subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames.',
    )
    userNames: Optional[List[str]] = Field(
        None,
        description='UserNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.',
    )


class ClusterRoleBindingList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ClusterRoleBinding] = Field(
        ..., description='Items is a list of ClusterRoleBindings'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMetaV2] = None


class Role(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMetaV2] = None
    rules: List[PolicyRule] = Field(
        ..., description='Rules holds all the PolicyRules for this Role'
    )


class RoleBinding(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    groupNames: Optional[List[str]] = Field(
        None,
        description='GroupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMetaV2] = None
    roleRef: v1_1.ObjectReference = Field(
        ...,
        description='RoleRef can only reference the current namespace and the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role.',
    )
    subjects: List[v1_1.ObjectReference] = Field(
        ...,
        description='Subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames.',
    )
    userNames: Optional[List[str]] = Field(
        None,
        description='UserNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.',
    )


class RoleBindingList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[RoleBinding] = Field(..., description='Items is a list of RoleBindings')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMetaV2] = None


class RoleList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Role] = Field(..., description='Items is a list of Roles')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMetaV2] = None


class SelfSubjectRulesReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    spec: SelfSubjectRulesReviewSpec = Field(
        ..., description='Spec adds information about how to conduct the check'
    )
    status: Optional[SubjectRulesReviewStatus] = Field(
        None,
        description='Status is completed by the server to tell which permissions you have',
    )


class SubjectRulesReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    spec: SubjectRulesReviewSpec = Field(
        ..., description='Spec adds information about how to conduct the check'
    )
    status: Optional[SubjectRulesReviewStatus] = Field(
        None,
        description='Status is completed by the server to tell which permissions you have',
    )


class ClusterRole(BaseModel):
    aggregationRule: Optional[v1_2.AggregationRule] = Field(
        None,
        description='AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.',
    )
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMetaV2] = None
    rules: List[PolicyRule] = Field(
        ..., description='Rules holds all the PolicyRules for this ClusterRole'
    )


class ClusterRoleList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ClusterRole] = Field(..., description='Items is a list of ClusterRoles')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMetaV2] = None
