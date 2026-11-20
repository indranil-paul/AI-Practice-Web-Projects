import requests
import logging
from typing import Optional, Dict, Any


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    """
    A simple reusable API client to handle HTTP requests with error handling and logging.
    Usage:
        client = APIClient(base_url="http://example.com/api/v1")
        response = client.get("endpoint")
    """
    def __init__(self, base_url: str = "", timeout: int = 30, headers: Optional[Dict[str, str]] = None):
        self.__base_url = base_url.rstrip("/")
        self.__timeout = timeout
        self.__session = requests.Session()
        self.__headers = headers if headers else {"Content-Type": "application/json"}
    
    def __del__(self):
        self.__session.close()

    def __request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> Any:
        """Internal method to handle all HTTP requests."""
        url = f"{self.__base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.__session.request(method=method, url=url, params=params, json=json, timeout=self.__timeout, headers=self.__headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"[{method}] {url} failed: {e}")
            raise

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self.__request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Any:
        return self.__request("POST", endpoint, json=json)
    
    def put(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Any:
        return self.__request("PUT", endpoint, json=json)
    
    def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self.__request("DELETE", endpoint, params=params)
    