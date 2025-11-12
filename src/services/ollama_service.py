from typing import Dict

import httpx
from loguru import logger

from src.settings import DefaultSettings


class OllamaService:
    """Minial Ollama service"""

    def __init__(self, settings: DefaultSettings):
        self.base_url = settings.OLLAMA_HOST

    async def health_check(self) -> Dict[str, str]:
        """Check if Ollama service is available."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                if response.status_code == 200:
                    return {"status": "healthy", "message": "Ollama service is running"}
                else:
                    return {"status": "unhealthy", "message": f"HTTP {response.status_code}"}
        except Exception as e:
            logger.error("Ollama health check failed")
            return {"status": "unhealthy", "message": str(e)}
