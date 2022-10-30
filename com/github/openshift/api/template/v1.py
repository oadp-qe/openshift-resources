# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from ......io.k8s.api.core import v1
from ......io.k8s.apimachinery.pkg import runtime
from ......io.k8s.apimachinery.pkg.apis.meta import v1 as v1_1


class Parameter(BaseModel):
    description: Optional[str] = Field(
        None, description='Description of a parameter. Optional.'
    )
    displayName: Optional[str] = Field(
        None,
        description="Optional: The name that will show in UI instead of parameter 'Name'",
    )
    from_: Optional[str] = Field(
        None,
        alias='from',
        description='From is an input value for the generator. Optional.',
    )
    generate: Optional[str] = Field(
        None,
        description='generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.\n\nThe only supported generator is "expression", which accepts a "from" value in the form of a simple regular expression containing the range expression "[a-zA-Z0-9]", and the length expression "a{length}".\n\nExamples:\n\nfrom             | value ----------------------------- "test[0-9]{1}x"  | "test7x" "[0-1]{8}"       | "01001100" "0x[A-F0-9]{4}"  | "0xB3AF" "[a-zA-Z0-9]{8}" | "hW4yQU5i"',
    )
    name: str = Field(
        ...,
        description='Name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required.',
    )
    required: Optional[bool] = Field(
        None,
        description='Optional: Indicates the parameter must have a value.  Defaults to false.',
    )
    value: Optional[str] = Field(
        None,
        description='Value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional.',
    )


class TemplateInstanceRequester(BaseModel):
    extra: Optional[Dict[str, List[str]]] = Field(
        None,
        description='extra holds additional information provided by the authenticator.',
    )
    groups: Optional[List[str]] = Field(
        None, description='groups represent the groups this user is a part of.'
    )
    uid: Optional[str] = Field(
        None,
        description='uid is a unique value that identifies this user across time; if this user is deleted and another user by the same name is added, they will have different UIDs.',
    )
    username: Optional[str] = Field(
        None,
        description='username uniquely identifies this user among all active users.',
    )


class BrokerTemplateInstanceSpec(BaseModel):
    bindingIDs: Optional[List[str]] = Field(
        None,
        description="bindingids is a list of 'binding_id's provided during successive bind calls to the template service broker.",
    )
    secret: v1.ObjectReference = Field(
        ...,
        description='secret is a reference to a Secret object residing in a namespace, containing the necessary template parameters.',
    )
    templateInstance: v1.ObjectReference = Field(
        ...,
        description='templateinstance is a reference to a TemplateInstance object residing in a namespace.',
    )


class TemplateInstanceCondition(BaseModel):
    lastTransitionTime: v1_1.Time = Field(
        ...,
        description='LastTransitionTime is the last time a condition status transitioned from one state to another.',
    )
    message: str = Field(
        ...,
        description='Message is a human readable description of the details of the last transition, complementing reason.',
    )
    reason: str = Field(
        ...,
        description="Reason is a brief machine readable explanation for the condition's last transition.",
    )
    status: str = Field(
        ..., description='Status of the condition, one of True, False or Unknown.'
    )
    type: str = Field(
        ..., description='Type of the condition, currently Ready or InstantiateFailure.'
    )


class TemplateInstanceObject(BaseModel):
    ref: Optional[v1.ObjectReference] = Field(
        None,
        description='ref is a reference to the created object.  When used under .spec, only name and namespace are used; these can contain references to parameters which will be substituted following the usual rules.',
    )


class TemplateInstanceStatus(BaseModel):
    conditions: Optional[List[TemplateInstanceCondition]] = Field(
        None,
        description="conditions represent the latest available observations of a TemplateInstance's current state.",
    )
    objects: Optional[List[TemplateInstanceObject]] = Field(
        None,
        description='Objects references the objects created by the TemplateInstance.',
    )


class BrokerTemplateInstance(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ObjectMetaV2] = None
    spec: BrokerTemplateInstanceSpec = Field(
        ..., description='spec describes the state of this BrokerTemplateInstance.'
    )


class BrokerTemplateInstanceList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[BrokerTemplateInstance] = Field(
        ..., description='items is a list of BrokerTemplateInstances'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMetaV2] = None


class Template(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description='labels is a optional set of labels that are applied to every object during the Template to Config transformation.',
    )
    message: Optional[str] = Field(
        None,
        description='message is an optional instructional message that will be displayed when this template is instantiated. This field should inform the user how to utilize the newly created resources. Parameter substitution will be performed on the message before being displayed so that generated credentials and other parameters can be included in the output.',
    )
    metadata: Optional[v1_1.ObjectMetaV2] = None
    objects: List[runtime.RawExtension] = Field(
        ...,
        description='objects is an array of resources to include in this template. If a namespace value is hardcoded in the object, it will be removed during template instantiation, however if the namespace value is, or contains, a ${PARAMETER_REFERENCE}, the resolved value after parameter substitution will be respected and the object will be created in that namespace.',
    )
    parameters: Optional[List[Parameter]] = Field(
        None,
        description='parameters is an optional array of Parameters used during the Template to Config transformation.',
    )


class TemplateInstanceSpec(BaseModel):
    requester: Optional[TemplateInstanceRequester] = Field(
        None,
        description='requester holds the identity of the agent requesting the template instantiation.',
    )
    secret: Optional[v1.LocalObjectReference] = Field(
        None,
        description='secret is a reference to a Secret object containing the necessary template parameters.',
    )
    template: Template = Field(
        ..., description='template is a full copy of the template for instantiation.'
    )


class TemplateList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Template] = Field(..., description='Items is a list of templates')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMetaV2] = None


class TemplateInstance(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ObjectMetaV2] = None
    spec: TemplateInstanceSpec = Field(
        ..., description='spec describes the desired state of this TemplateInstance.'
    )
    status: Optional[TemplateInstanceStatus] = Field(
        None, description='status describes the current state of this TemplateInstance.'
    )


class TemplateInstanceList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[TemplateInstance] = Field(
        ..., description='items is a list of Templateinstances'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMetaV2] = None
