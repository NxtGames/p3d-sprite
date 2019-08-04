"""
MIT License

Copyright (c) 2019 Nxt Games, LLC
Written by Jordan Maxwell 
08/04/2019

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from direct.showbase.ShowBase import ShowBase
from p3d_sprite import sprite as spritesheet

# Create a new showbase instance
base = ShowBase()

# Load the spritesheet and specify the number of rows and columns in the sheet
sprite = spritesheet.Sprite2D(
    file_path='SaraFullSheet.png',            
    rows=21,
    cols=13)

# Create and run a walking animation
sprite.create_animation('walk-right', 
    frames=[143, 144, 145, 146, 147, 148, 149, 150, 151])
sprite.play_animation('walk-right', loop=True)

# Parent the sprite node to render
sprite.node.reparent_to(base.render)

# Run
base.run()