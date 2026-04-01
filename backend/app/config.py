"""
Configuration module — loads settings from .env using pydantic-settings.
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Tuple

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables / .env file."""

    # YOLO
    yolo_model: str = "weights/yolov8n.pt"
    yolo_confidence: float = 0.5
    device: str = "auto"  # auto | cuda | cpu | mps

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Behavior thresholds
    loitering_threshold_seconds: int = 30
    intrusion_zone: str = "0.6,0.0,1.0,1.0"
    unattended_object_seconds: int = 15
    alert_cooldown_seconds: int = 30

    # CORS
    frontend_url: str = "http://localhost:5173"

    # Directories
    snapshots_dir: str = "snapshots"
    uploads_dir: str = "uploads"
    weights_dir: str = "weights"

    @property
    def intrusion_zone_coords(self) -> Tuple[float, float, float, float]:
        """Parse intrusion zone string into (x1, y1, x2, y2) normalized coords."""
        parts = [float(x.strip()) for x in self.intrusion_zone.split(",")]
        if len(parts) != 4:
            return (0.6, 0.0, 1.0, 1.0)
        return (parts[0], parts[1], parts[2], parts[3])

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Cached settings singleton."""
    return Settings()


def ensure_directories() -> None:
    """Create required directories if they don't exist."""
    settings = get_settings()
    os.makedirs(settings.snapshots_dir, exist_ok=True)
    os.makedirs(settings.uploads_dir, exist_ok=True)
    os.makedirs(settings.weights_dir, exist_ok=True)

