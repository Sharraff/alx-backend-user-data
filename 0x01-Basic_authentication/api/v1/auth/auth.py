#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar
User = TypeVar('User')

class Auth:
    """
    a class to manage API authenticaation
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        this function returns False - path and exclude_paths
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request
        """
        return None