# generated by datamodel-codegen:
#   filename:  k8s_swagger.json
#   timestamp: 2022-10-29T09:10:36+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class APIResourceReference(BaseModel):
    kind: str
    name: str
    version: str


class ActionDescriptor(BaseModel):
    description: Optional[str] = None
    displayName: Optional[str] = None
    path: str
    value: Optional[str] = None
    x_descriptors: Optional[List[str]] = Field(None, alias='x-descriptors')


class InstallMode(BaseModel):
    supported: bool
    type: str


class SpecDescriptor(BaseModel):
    description: Optional[str] = None
    displayName: Optional[str] = None
    path: str
    value: Optional[str] = None
    x_descriptors: Optional[List[str]] = Field(None, alias='x-descriptors')


class StatusDescriptor(BaseModel):
    description: Optional[str] = None
    displayName: Optional[str] = None
    path: str
    value: Optional[str] = None
    x_descriptors: Optional[List[str]] = Field(None, alias='x-descriptors')


class APIServiceDescription(BaseModel):
    actionDescriptors: Optional[List[ActionDescriptor]] = None
    containerPort: Optional[int] = None
    deploymentName: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    group: str
    kind: str
    name: str
    resources: Optional[List[APIResourceReference]] = None
    specDescriptors: Optional[List[SpecDescriptor]] = None
    statusDescriptors: Optional[List[StatusDescriptor]] = None
    version: str


class CRDDescription(BaseModel):
    actionDescriptors: Optional[List[ActionDescriptor]] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    kind: str
    name: str
    resources: Optional[List[APIResourceReference]] = None
    specDescriptors: Optional[List[SpecDescriptor]] = None
    statusDescriptors: Optional[List[StatusDescriptor]] = None
    version: str


class CustomResourceDefinitions(BaseModel):
    owned: Optional[List[CRDDescription]] = None
    required: Optional[List[CRDDescription]] = None


class APIServiceDefinitions(BaseModel):
    owned: Optional[List[APIServiceDescription]] = None
    required: Optional[List[APIServiceDescription]] = None
