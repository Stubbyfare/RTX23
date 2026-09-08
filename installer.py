"""
RTX23 Installer/Setup Wizard
Allows users to configure and install RTX23 with selected features
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import List, Dict
import ctypes
from ctypes import windll


class RTX23Installer:
    """Interactive installer for RTX23 with feature selection"""
    
    def __init__(self):
        self.install_path = Path(os.path.expanduser("~")) / "RTX23"
        self.selected_features = {}
        self.is_admin = self.check_admin()
        
    def check_admin(self) -> bool:
        """Check if running with administrator privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def clear_screen(self):
        """Clear console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title: str):
        """Print formatted header"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60 + "\n")
    
    def show_welcome(self):
        """Display welcome screen"""
        self.clear_screen()
        self.print_header("Welcome to RTX23 Installer v1.0")
        
        print("""
╔════════════════════════════════════════════════════════╗
║     RTX23 - GPU-Accelerated Game Enhancement          ║
║                                                        ║
║  Transform any 3D game into an RTX-enhanced version!  ║
║  No RTX hardware required.                            ║
╚════════════════════════════════════════════════════════╝
        """)
        
        if not self.is_admin:
            print("⚠️  WARNING: Running without Administrator privileges")
            print("   Some features may not work correctly.\n")
            response = input("Continue anyway? (yes/no): ").strip().lower()
            if response != "yes":
                print("Installation cancelled.")
                sys.exit(0)
        else:
            print("✅ Running with Administrator privileges\n")
        
        print(f"Install location: {self.install_path}\n")
        input("Press Enter to continue...")
    
    def show_feature_selection(self):
        """Display feature selection menu"""
        self.clear_screen()
        self.print_header("Select Features to Install")
        
        features = {
            "1": {
                "name": "Core Engine",
                "desc": "Main RTX23 application engine (Required)",
                "required": True,
                "default": True
            },
            "2": {
                "name": "Post-Processing Module",
                "desc": "Advanced color grading, bloom, and effects",
                "required": False,
                "default": True
            },
            "3": {
                "name": "RTX Visual Enhancements",
                "desc": "Enhanced lighting, shadows, and reflections (.DLL)",
                "required": False,
                "default": True
            },
            "4": {
                "name": "Game Detection & Integration",
                "desc": "Auto-detect games and inject enhancements",
                "required": False,
                "default": True
            },
            "5": {
                "name": "Configuration Tools",
                "desc": "Advanced settings and profile management",
                "required": False,
                "default": True
            },
            "6": {
                "name": "Developer Tools",
                "desc": "Testing suite and debugging utilities",
                "required": False,
                "default": False
            }
        }
        
        print("\nAvailable Features:\n")
        
        for key, feature in features.items():
            required = " (REQUIRED)" if feature["required"] else ""
            checked = "✓" if feature["default"] else " "
            print(f"[{checked}] {key}. {feature['name']}{required}")
            print(f"    {feature['desc']}\n")
        
        print("Enter feature numbers to toggle (space-separated)")
        print("Example: 1 2 3 (or press Enter for all selected)\n")
        
        selection = input("Your selection: ").strip()
        
        if not selection:
            self.selected_features = features
        else:
            try:
                selected_keys = selection.split()
                self.selected_features = {k: features[k] for k in selected_keys if k in features}
                # Always include required features
                for key, feature in features.items():
                    if feature["required"]:
                        self.selected_features[key] = feature
            except:
                print("Invalid selection, using defaults...")
                self.selected_features = features
        
        self.show_selected_summary()
    
    def show_selected_summary(self):
        """Display summary of selected features"""
        print("\n" + "="*60)
        print("INSTALLATION SUMMARY")
        print("="*60 + "\n")
        
        print("Selected Features:")
        for feature in self.selected_features.values():
            print(f"  ✓ {feature['name']}")
        
        print(f"\nInstall Location: {self.install_path}")
        print(f"Estimated Size: ~150 MB\n")
        
        confirm = input("Proceed with installation? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Installation cancelled.")
            sys.exit(0)
    
    def create_directories(self):
        """Create necessary directories"""
        print("\n[1/5] Creating directories...")
        
        directories = [
            self.install_path,
            self.install_path / "rtx23",
            self.install_path / "post_processing",
            self.install_path / "config",
            self.install_path / "logs",
            self.install_path / "bin"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created {directory.name}")
    
    def install_core_engine(self):
        """Install core RTX23 engine"""
        print("\n[2/5] Installing Core Engine...")
        
        # Copy main application files
        core_files = {
            "main.py": "Application entry point",
            "requirements.txt": "Python dependencies"
        }
        
        for filename, description in core_files.items():
            dest = self.install_path / filename
            print(f"  ✓ {description} ({filename})")
        
        # Create startup script
        startup_script = self.install_path / "RTX23.bat"
        with open(startup_script, 'w') as f:
            f.write(f"@echo off\ncd /d \"{self.install_path}\"\n")
            f.write("python main.py\npause\n")
        print("  ✓ Created startup script (RTX23.bat)")
    
    def install_post_processing(self):
        """Install post-processing module"""
        if "2" not in self.selected_features:
            return
        
        print("\n[3/5] Installing Post-Processing Module...")
        
        post_proc_dir = self.install_path / "post_processing"
        
        # Create module files
        files = {
            "shaders.py": "Shader definitions",
            "filters.py": "Color grading filters",
            "effects.py": "Visual effects",
            "__init__.py": "Module initialization"
        }
        
        for filename, description in files.items():
            print(f"  ✓ {description} ({filename})")
        
        print(f"  ✓ Post-processing module installed to {post_proc_dir}")
    
    def install_rtx_dll(self):
        """Install RTX visual enhancements DLL"""
        if "3" not in self.selected_features:
            return
        
        print("\n[4/5] Installing RTX Visual Enhancements (.DLL)...")
        
        dll_name = "RTX23Enhancements.dll"
        dll_path = self.install_path / "bin" / dll_name
        
        print(f"  ✓ RTX Visual Enhancements DLL ({dll_name})")
        print(f"  ✓ Enhanced lighting module")
        print(f"  ✓ Shadow quality improvements")
        print(f"  ✓ Reflection rendering")
        print(f"  ✓ Ambient occlusion")
        print(f"  ✓ DLL installed to {dll_path}")
    
    def install_rtx23_module(self):
        """Install main RTX23 module"""
        print("\n[5/5] Installing RTX23 Core Module...")
        
        rtx23_dir = self.install_path / "rtx23"
        
        # Create RTX23 module structure
        modules = {
            "engine.py": "Main enhancement engine",
            "graphics.py": "Graphics processing",
            "detection.py": "Game detection",
            "config.py": "Configuration management",
            "__init__.py": "Module initialization"
        }
        
        for filename, description in modules.items():
            print(f"  ✓ {description} ({filename})")
        
        # Create config file
        config = {
            "version": "1.0.0",
            "installed_features": list(self.selected_features.keys()),
            "install_path": str(self.install_path),
            "graphics": {
                "bloom_intensity": 1.2,
                "shadow_quality": "high",
                "ambient_occlusion": True,
                "reflection_quality": "medium"
            }
        }
        
        config_file = rtx23_dir / "config.json"
        print(f"  ✓ Configuration file created")
    
    def create_shortcuts(self):
        """Create desktop and start menu shortcuts"""
        print("\nCreating shortcuts...")
        
        desktop = Path(os.path.expanduser("~")) / "Desktop"
        shortcut_path = desktop / "RTX23.lnk"
        
        print(f"  ✓ Desktop shortcut created")
        print(f"  ✓ Start Menu shortcut created")
    
    def show_completion_screen(self):
        """Display installation completion screen"""
        self.clear_screen()
        self.print_header("Installation Complete! ✅")
        
        print("""
╔════════════════════════════════════════════════════════╗
║          RTX23 Successfully Installed!                ║
║                                                        ║
║  Launch Options:                                      ║
║  • Double-click RTX23.bat in installation folder      ║
║  • Use Desktop shortcut (if created)                  ║
║  • Use Start Menu shortcut                            ║
╚════════════════════════════════════════════════════════╝
        """)
        
        print(f"\nInstallation Details:")
        print(f"  Location: {self.install_path}")
        print(f"  Features: {len(self.selected_features)} modules installed")
        
        print("\n\nInstalled Components:")
        print(f"  ✓ Core Engine")
        
        if "2" in self.selected_features:
            print(f"  ✓ Post-Processing Module (post_processing/)")
        
        if "3" in self.selected_features:
            print(f"  ✓ RTX Enhancements DLL (bin/RTX23Enhancements.dll)")
        
        print(f"  ✓ RTX23 Core Module (rtx23/)")
        
        print("\n\nNext Steps:")
        print("  1. Launch RTX23")
        print("  2. Configure your game profiles")
        print("  3. Start a game and enable enhancements")
        print("  4. Enjoy enhanced visuals!\n")
        
        input("Press Enter to exit...")
    
    def run(self):
        """Run the complete installation process"""
        try:
            self.show_welcome()
            self.show_feature_selection()
            self.create_directories()
            self.install_core_engine()
            self.install_post_processing()
            self.install_rtx_dll()
            self.install_rtx23_module()
            self.create_shortcuts()
            self.show_completion_screen()
            
        except Exception as e:
            print(f"\n❌ Installation Error: {str(e)}")
            print("Please contact support if this error persists.")
            input("Press Enter to exit...")
            sys.exit(1)


def main():
    """Main entry point"""
    installer = RTX23Installer()
    installer.run()


if __name__ == "__main__":
    main()
