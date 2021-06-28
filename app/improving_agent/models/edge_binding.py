# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent import util


class EdgeBinding(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None):  # noqa: E501
        """EdgeBinding - a model defined in OpenAPI

        :param id: The id of this EdgeBinding.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'EdgeBinding':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EdgeBinding of this EdgeBinding.  # noqa: E501
        :rtype: EdgeBinding
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EdgeBinding.

        The key identifier of a specific KnowledgeGraph Edge.  # noqa: E501

        :return: The id of this EdgeBinding.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeBinding.

        The key identifier of a specific KnowledgeGraph Edge.  # noqa: E501

        :param id: The id of this EdgeBinding.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id
