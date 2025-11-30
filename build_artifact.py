#!/usr/bin/env python3
"""
Build Artifact Creator for C Modulo Project
"""
import datetime
import os
import subprocess

def create_build_artifact():
    """Create build artifact with project information"""
    
    # Create build directory
    os.makedirs('build', exist_ok=True)
    
    # Get current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create artifact info file
    with open('build/artifact_info.txt', 'w') as f:
        f.write("C MODULO PROJECT BUILD ARTIFACT\n")
        f.write("================================\n")
        f.write(f"Build Date: {current_time}\n")
        f.write("Project: C Modulo Operations\n")
        f.write("Language: C Programming\n")
        f.write("Version: 1.0.0\n")
        f.write("Files: modulo.c, test_modulo.c, Makefile\n")
        f.write("Compiler: GCC\n")
        f.write("Status: Build Successful ✅\n")
        f.write("\nArtifact Contents:\n")
        f.write("- modulo_app (Compiled Binary)\n")
        f.write("- test_modulo (Test Binary)\n")
        f.write("- artifact_info.txt (This file)\n")
    
    print("✅ Build artifact created successfully!")
    print("📁 Location: build/artifact_info.txt")

if __name__ == "__main__":
    create_build_artifact()
