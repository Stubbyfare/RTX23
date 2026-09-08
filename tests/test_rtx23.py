"""
Unit tests for RTX23 core functionality
"""

import pytest
import json
from pathlib import Path
from main import RTX23Engine
from graphics.shaders import ShaderConfig, ShaderProcessor, PostProcessor
from game.detector import GameDetector, GameInfo, GameEngine


class TestRTX23Engine:
    """Tests for main RTX23 engine"""
    
    def test_engine_initialization(self):
        engine = RTX23Engine()
        assert engine.is_running == False
        assert engine.active_game is None
    
    def test_default_config_loading(self):
        engine = RTX23Engine()
        config = engine.get_default_config()
        assert config["version"] == "1.0"
        assert "graphics" in config
        assert "profiles" in config
    
    def test_apply_enhancements(self):
        engine = RTX23Engine()
        result = engine.apply_enhancements("TestGame", "balanced")
        assert result == True
        assert engine.active_game == "TestGame"
        assert engine.is_running == True
    
    def test_stop_enhancements(self):
        engine = RTX23Engine()
        engine.apply_enhancements("TestGame", "balanced")
        result = engine.stop_enhancements()
        assert result == True
        assert engine.is_running == False


class TestShaderProcessor:
    """Tests for shader processing"""
    
    def test_shader_config_creation(self):
        config = ShaderConfig(bloom_intensity=1.5)
        assert config.bloom_intensity == 1.5
        assert config.shadow_quality == "medium"
    
    def test_shader_processor_initialization(self):
        config = ShaderConfig()
        processor = ShaderProcessor(config)
        assert processor.config == config
    
    def test_apply_all_effects(self):
        config = ShaderConfig()
        processor = ShaderProcessor(config)
        result = processor.apply_all_effects()
        assert result == True


class TestPostProcessor:
    """Tests for post-processing"""
    
    def test_tone_mapping(self):
        hdr_value = 1.0
        result = PostProcessor.tone_map(hdr_value)
        assert 0 <= result <= 1
    
    def test_contrast_adjustment(self):
        pixel = 0.5
        contrast = 1.2
        result = PostProcessor.adjust_contrast(pixel, contrast)
        assert isinstance(result, float)
    
    def test_saturation_adjustment(self):
        color = (0.5, 0.5, 0.5)
        saturation = 1.2
        result = PostProcessor.adjust_saturation(color, saturation)
        assert len(result) == 3


class TestGameDetector:
    """Tests for game detection"""
    
    def test_detector_initialization(self):
        detector = GameDetector()
        assert detector.detected_games == []
    
    def test_game_info_creation(self):
        game = GameInfo(
            name="TestGame",
            process_id=1234,
            engine=GameEngine.UNITY,
            graphics_api="DirectX11"
        )
        assert game.name == "TestGame"
        assert game.process_id == 1234
        assert game.engine == GameEngine.UNITY


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
