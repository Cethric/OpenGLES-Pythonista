# OpenGLES-Pythonista
[OpenGL for Embedded Systems](https://en.wikipedia.org/wiki/OpenGL_ES) bindings for the lastest [Pythonista](http://www.omz-software.com/pythonista) v1.6 beta

---
## What It Does
- This is boilerplate code for OpenGL ES for iOS in Python, with a little bit extra
- Almost all GLES functions that are natively supported on iOS are supported in this. Except for and `GLsync` and `sync` commands
- For most iOS devices running iOS 8 and greater OpenGL ES 3 is supported.
- In Util/GLKit.py there is support for both touch and the accelerometer  
for touch left side handles look and right side handles move  
accelerometer handles look

---
## What it doesn't do
- This is not a game engine, just boilerplate code with limited support to GLKit iOS render system
- It currently does not have any texture loading support (but it can be implimented)

---
## To do
- Improve the physics simulation. This is not important but still nice
- Clean the code up... Alot :/
- Improve the shader utility
- Improve GLKit and EAGL support
- More reliable header parsing
- Create a better example file

---
## Other resources / misc
- ~~3D physics support is done through [Ammo.js](https://github.com/kripken/ammo.js/) which is a javascript port of the [Bullet](http://bulletphysics.org/wordpress/) physics engine~~ Physics is now done with [Cannon.js](https://github.com/schteppe/cannon.js)
- Header parsing code. This was from an example that I found on stackoverflow which I expanded on quite a bit. However I do not remeber what post it was from. So if someone can find it please let me know.
- Inspired by [PyOpenGL](http://pyopengl.sourceforge.net) for python

__Please note the above is NOT affiliated with or in any way related to this, other than where I have made use of the code. I just what to thank them for their projects__
---