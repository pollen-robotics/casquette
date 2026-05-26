"""Configuration management using Pydantic Settings."""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {"env_prefix": "CASQUETTE_", "env_file": ".env"}

    # Server
    host: str = "0.0.0.0"
    port: int = 8001

    # Backend
    backend: str = "auto"  # "auto", "mock", or "rpi"

    # Data
    data_dir: Path = Path.home() / "casquette-data"

    # Camera
    camera_fps: int = 46
    camera_resolution_w: int = 1296
    camera_resolution_h: int = 972

    # IMU
    imu_hz: int = 200
    imu_i2c_bus: int = 1  # Pi Zero 2W: hw bus 1

    # Device identification (for multi-device sync)
    device_id: str = ""

    # Logging
    log_level: str = "INFO"


settings = Settings()
