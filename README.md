# RTX23 - GPU-Accelerated Game Enhancement

RTX23 transforms any 3D game into a visually enhanced RTX-like experience without requiring RTX hardware. It provides real-time shader enhancement, improved lighting, and post-processing effects.

## Features

- 🎮 **Game Detection** - Automatic detection of running 3D games
- ✨ **Visual Enhancement** - Real-time shader improvements
- 🎨 **Lighting Enhancements** - Better ambient occlusion, shadows, and reflections
- 🖼️ **Post-Processing** - Color grading, bloom, and contrast enhancement
- ⚙️ **Easy Configuration** - Simple profiles for different game types
- 🚀 **Performance Optimized** - GPU-accelerated processing

## 🚀 Quick Start - Get Your Executable

### Option 1: Use Pre-Built Executable (Easiest)
1. **Fork this repository** (click the "Fork" button at the top right)
2. Go to your forked repository
3. Click on **"Actions"** tab
4. Select **"Build Executable"** workflow
5. Click **"Run workflow"** (keep default version or set your own)
6. Wait for the build to complete (~5 minutes)
7. Download your executable from the artifacts or release page
8. Run it directly - no Python installation needed!

### Option 2: Run from Source (For Developers)

#### System Requirements
- Windows 10/11 or Linux
- Python 3.8+
- GPU with at least 2GB VRAM
- DirectX 11+ / OpenGL 4.3+

#### Installation

```bash
# Clone your forked repository
git clone https://github.com/YOUR-USERNAME/RTX23.git
cd RTX23

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Usage

1. Launch RTX23
2. Select your game from the dropdown or let auto-detect find it
3. Choose a visual preset (Balanced, High Quality, Maximum)
4. Enable and adjust effects as needed
5. Start your game - enhancements apply in real-time

## Configuration

Edit `config/settings.json` to add custom game settings or create new visual profiles.

### Graphics Settings
- **Ambient Occlusion** - Adds depth to scenes
- **Shadow Quality** - Low, Medium, High, Ultra
- **Bloom Intensity** - Enhances bright areas
- **Reflection Quality** - Low, Medium, High
- **Contrast & Saturation** - Color adjustments

## Visual Presets

### 🎯 Balanced
- Best for all games
- Moderate performance impact
- Great visual improvement

### 🎨 High Quality
- Enhanced visuals
- Noticeable performance impact
- Recommended for high-end GPUs

### ✨ Maximum
- Maximum visual enhancement
- Significant performance impact
- Requires high-end GPU (4GB+ VRAM)

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

MIT License - See LICENSE file for details

## Support & Issues

Found a bug or have a suggestion? Please open an issue on GitHub!

---

**RTX23 - Transform Your Games! 🎮✨**
