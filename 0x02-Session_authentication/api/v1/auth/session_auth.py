#!/usr/bin/env python3
"""
Sesson Authentication
"""
from flask import abort, jsonify, request
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User

class SessionAuth(Auth):
    """
    """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        create session
        """
        if not user_id or type(user_id) != str:
            return None
        else:
            session_id = str(uuid4())
            SessionAuth.user_id_by_session_id[user_id] = session_id
            return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a Uer ID on a session ID
        """
        if not session_id or type(session_id) != str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id, None)
    
    def current_user(self, request=None):
        """
        current_user
        """
        if request:
            session_cookie = self.session_cookie(request)
            if session_cookie:
                user_id = self.user_id_for_session_id(session_cookie)
                return User.get(user_id)
    
    def destroy_session(self, request=None):
        """
        destroy active user session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True