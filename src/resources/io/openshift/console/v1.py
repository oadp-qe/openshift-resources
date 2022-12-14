# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr

from ...k8s.apimachinery.pkg.apis.meta import v1


class Link(BaseModel):
    href: constr(regex=r'^https://') = Field(
        ..., description='href is the absolute secure URL for the link (must use https)'
    )
    text: Optional[str] = Field(
        None, description='text is the display text for the link'
    )


class Spec(BaseModel):
    description: str = Field(
        ...,
        description='description is the description of the CLI download (can include markdown).',
    )
    displayName: str = Field(
        ..., description='displayName is the display name of the CLI download.'
    )
    links: List[Link] = Field(
        ...,
        description='links is a list of objects that provide CLI download link details.',
    )


class SpecModel(BaseModel):
    hrefTemplate: constr(regex=r'^https://') = Field(
        ...,
        description='hrefTemplate is an absolute secure URL (must use https) for the log link including variables to be replaced. Variables are specified in the URL with the format ${variableName}, for instance, ${containerName} and will be replaced with the corresponding values from the resource. Resource is a pod. Supported variables are: - ${resourceName} - name of the resource which containes the logs - ${resourceUID} - UID of the resource which contains the logs               - e.g. `11111111-2222-3333-4444-555555555555` - ${containerName} - name of the resource\'s container that contains the logs - ${resourceNamespace} - namespace of the resource that contains the logs - ${resourceNamespaceUID} - namespace UID of the resource that contains the logs - ${podLabels} - JSON representation of labels matching the pod with the logs             - e.g. `{"key1":"value1","key2":"value2"}` \n e.g., https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}',
    )
    namespaceFilter: Optional[str] = Field(
        None,
        description='namespaceFilter is a regular expression used to restrict a log link to a matching set of namespaces (e.g., `^openshift-`). The string is converted into a regular expression using the JavaScript RegExp constructor. If not specified, links will be displayed for all the namespaces.',
    )
    text: str = Field(..., description='text is the display text for the link')


class ApplicationMenu(BaseModel):
    imageURL: Optional[str] = Field(
        None,
        description='imageUrl is the URL for the icon used in front of the link in the application menu. The URL must be an HTTPS URL or a Data URI. The image should be square and will be shown at 24x24 pixels.',
    )
    section: str = Field(
        ...,
        description='section is the section of the application menu in which the link should appear. This can be any text that will appear as a subheading in the application menu dropdown. A new section will be created if the text does not match text of an existing section.',
    )


class MatchExpression(BaseModel):
    key: str = Field(
        ..., description='key is the label key that the selector applies to.'
    )
    operator: str = Field(
        ...,
        description="operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.",
    )
    values: Optional[List[str]] = Field(
        None,
        description='values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.',
    )


class NamespaceSelector(BaseModel):
    matchExpressions: Optional[List[MatchExpression]] = Field(
        None,
        description='matchExpressions is a list of label selector requirements. The requirements are ANDed.',
    )
    matchLabels: Optional[Dict[str, str]] = Field(
        None,
        description='matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.',
    )


class NamespaceDashboard(BaseModel):
    namespaceSelector: Optional[NamespaceSelector] = Field(
        None,
        description='namespaceSelector is used to select the Namespaces that should contain dashboard link by label. If the namespace labels match, dashboard link will be shown for the namespaces.',
    )
    namespaces: Optional[List[str]] = Field(
        None,
        description='namespaces is an array of namespace names in which the dashboard link should appear.',
    )


class SpecModel1(BaseModel):
    applicationMenu: Optional[ApplicationMenu] = Field(
        None,
        description='applicationMenu holds information about section and icon used for the link in the application menu, and it is applicable only when location is set to ApplicationMenu.',
    )
    href: constr(regex=r'^https://') = Field(
        ..., description='href is the absolute secure URL for the link (must use https)'
    )
    location: constr(
        regex=r'^(ApplicationMenu|HelpMenu|UserMenu|NamespaceDashboard)$'
    ) = Field(
        ...,
        description='location determines which location in the console the link will be appended to (ApplicationMenu, HelpMenu, UserMenu, NamespaceDashboard).',
    )
    namespaceDashboard: Optional[NamespaceDashboard] = Field(
        None,
        description='namespaceDashboard holds information about namespaces in which the dashboard link should appear, and it is applicable only when location is set to NamespaceDashboard. If not specified, the link will appear in all namespaces.',
    )
    text: str = Field(..., description='text is the display text for the link')


class LinkModel(BaseModel):
    href: constr(regex=r'^https://') = Field(
        ..., description='href is the absolute secure URL for the link (must use https)'
    )
    text: str = Field(..., description='text is the display text for the link')


class SpecModel2(BaseModel):
    backgroundColor: Optional[str] = Field(
        None,
        description='backgroundColor is the color of the background for the notification as CSS data type color.',
    )
    color: Optional[str] = Field(
        None,
        description='color is the color of the text for the notification as CSS data type color.',
    )
    link: Optional[LinkModel] = Field(
        None, description='link is an object that holds notification link details.'
    )
    location: Optional[
        constr(regex=r'^(BannerTop|BannerBottom|BannerTopBottom)$')
    ] = Field(
        None,
        description='location is the location of the notification in the console. Valid values are: "BannerTop", "BannerBottom", "BannerTopBottom".',
    )
    text: str = Field(..., description='text is the visible text of the notification.')


class AccessReviewResource(BaseModel):
    group: Optional[str] = Field(
        None, description='Group is the API Group of the Resource.  "*" means all.'
    )
    name: Optional[str] = Field(
        None,
        description='Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview',
    )
    resource: Optional[str] = Field(
        None,
        description='Resource is one of the existing resource types.  "*" means all.',
    )
    subresource: Optional[str] = Field(
        None,
        description='Subresource is one of the existing resource types.  "" means none.',
    )
    verb: Optional[str] = Field(
        None,
        description='Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all.',
    )
    version: Optional[str] = Field(
        None, description='Version is the API Version of the Resource.  "*" means all.'
    )


class Review(BaseModel):
    failedTaskHelp: constr(min_length=1) = Field(
        ...,
        description='failedTaskHelp contains suggestions for a failed task review and is shown at the end of task. (includes markdown)',
    )
    instructions: constr(min_length=1) = Field(
        ...,
        description='instructions contains steps that user needs to take in order to validate his work after going through a task. (includes markdown)',
    )


class Summary(BaseModel):
    failed: constr(min_length=1, max_length=128) = Field(
        ...,
        description='failed briefly describes the unsuccessfully passed task. (includes markdown)',
    )
    success: constr(min_length=1) = Field(
        ..., description='success describes the succesfully passed task.'
    )


class Task(BaseModel):
    description: constr(min_length=1) = Field(
        ...,
        description='description describes the steps needed to complete the task. (includes markdown)',
    )
    review: Optional[Review] = Field(
        None,
        description="review contains instructions to validate the task is complete. The user will select 'Yes' or 'No'. using a radio button, which indicates whether the step was completed successfully.",
    )
    summary: Optional[Summary] = Field(
        None, description='summary contains information about the passed step.'
    )
    title: constr(min_length=1) = Field(
        ..., description='title describes the task and is displayed as a step heading.'
    )


class SpecModel3(BaseModel):
    accessReviewResources: Optional[List[AccessReviewResource]] = Field(
        None,
        description="accessReviewResources contains a list of resources that the user's access will be reviewed against in order for the user to complete the Quick Start. The Quick Start will be hidden if any of the access reviews fail.",
    )
    conclusion: Optional[str] = Field(
        None,
        description='conclusion sums up the Quick Start and suggests the possible next steps. (includes markdown)',
    )
    description: constr(min_length=1, max_length=256) = Field(
        ...,
        description='description is the description of the Quick Start. (includes markdown)',
    )
    displayName: constr(min_length=1) = Field(
        ..., description='displayName is the display name of the Quick Start.'
    )
    durationMinutes: conint(ge=1) = Field(
        ...,
        description='durationMinutes describes approximately how many minutes it will take to complete the Quick Start.',
    )
    icon: Optional[str] = Field(
        None,
        description='icon is a base64 encoded image that will be displayed beside the Quick Start display name. The icon should be an vector image for easy scaling. The size of the icon should be 40x40.',
    )
    introduction: constr(min_length=1) = Field(
        ...,
        description='introduction describes the purpose of the Quick Start. (includes markdown)',
    )
    nextQuickStart: Optional[List[str]] = Field(
        None,
        description='nextQuickStart is a list of the following Quick Starts, suggested for the user to try.',
    )
    prerequisites: Optional[List[str]] = Field(
        None,
        description='prerequisites contains all prerequisites that need to be met before taking a Quick Start. (includes markdown)',
    )
    tags: Optional[List[str]] = Field(
        None, description='tags is a list of strings that describe the Quick Start.'
    )
    tasks: List[Task] = Field(
        ...,
        description='tasks is the list of steps the user has to perform to complete the Quick Start.',
        min_items=1,
    )


class TargetResource(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class SpecModel4(BaseModel):
    description: constr(regex=r'^(.|\s)*\S(.|\s)*$') = Field(
        ..., description='description of the YAML sample.'
    )
    snippet: Optional[bool] = Field(
        None,
        description="snippet indicates that the YAML sample is not the full YAML resource definition, but a fragment that can be inserted into the existing YAML document at the user's cursor.",
    )
    targetResource: TargetResource = Field(
        ...,
        description='targetResource contains apiVersion and kind of the resource YAML sample is representating.',
    )
    title: constr(regex=r'^(.|\s)*\S(.|\s)*$') = Field(
        ..., description='title of the YAML sample.'
    )
    yaml: constr(regex=r'^(.|\s)*\S(.|\s)*$') = Field(
        ..., description='yaml is the YAML sample to display.'
    )


class ConsoleCLIDownload(BaseModel):
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
        ...,
        description='ConsoleCLIDownloadSpec is the desired cli download configuration.',
    )


class ConsoleCLIDownloadList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ConsoleCLIDownload] = Field(
        ...,
        description='List of consoleclidownloads. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ConsoleExternalLogLink(BaseModel):
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
        ...,
        description='ConsoleExternalLogLinkSpec is the desired log link configuration. The log link will appear on the logs tab of the pod details page.',
    )


class ConsoleExternalLogLinkList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ConsoleExternalLogLink] = Field(
        ...,
        description='List of consoleexternalloglinks. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ConsoleLink(BaseModel):
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
    spec: SpecModel1 = Field(
        ..., description='ConsoleLinkSpec is the desired console link configuration.'
    )


class ConsoleLinkList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ConsoleLink] = Field(
        ...,
        description='List of consolelinks. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ConsoleNotification(BaseModel):
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
    spec: SpecModel2 = Field(
        ...,
        description='ConsoleNotificationSpec is the desired console notification configuration.',
    )


class ConsoleNotificationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ConsoleNotification] = Field(
        ...,
        description='List of consolenotifications. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ConsoleQuickStart(BaseModel):
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
    spec: SpecModel3 = Field(
        ...,
        description='ConsoleQuickStartSpec is the desired quick start configuration.',
    )


class ConsoleQuickStartList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ConsoleQuickStart] = Field(
        ...,
        description='List of consolequickstarts. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class ConsoleYAMLSample(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: v1.ObjectMeta = Field(
        ...,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: SpecModel4 = Field(
        ...,
        description='ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console.',
    )


class ConsoleYAMLSampleList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ConsoleYAMLSample] = Field(
        ...,
        description='List of consoleyamlsamples. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
