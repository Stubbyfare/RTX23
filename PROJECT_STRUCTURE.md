# RTX23 - Project Structure

```
RTX23/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
│
├── config/
│   └── settings.json      # Default configuration and visual presets
│
├── graphics/
│   └── shaders.py         # Shader and post-processing implementations
│
├── game/
│   └── detector.py        # Game detection and integration module
│
└── tests/
    └── test_rtx23.py      # Unit tests
```

## Key Components

### main.py - RTX23Engine
- Core application logic
- Configuration management
- Game enhancement control

### graphics/shaders.py
- ShaderProcessor: Handles visual effects
- PostProcessor: Post-processing pipeline
- Color grading and tone mapping

### game/detector.py
- GameDetector: Identifies running games
- GameIntegration: Injects enhancements

### config/settings.json
- Visual presets (Balanced, High Quality, Maximum)
- Graphics settings
- Performance tuning options
