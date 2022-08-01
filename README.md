# ModernGL-Shader-with-pygame
I had put a crt shader as example in shaders folder. you can write your own shader.
you can use this class to give pygame a shader to render screen. it is easy to use.

I will add tutorial later I have free time.

it's easy to use.
I had put example file in it. You can experiment with it and try something new.

1. replace your display variable with a Surface. and blit everything you want to show on that Surface.
2. display set mode with OPENGL and DOUBLEBUF flag. 
3. import my shader class. And init a new shader for your game. Remember to pass your display Surface to init it.
4. Replace all display.update with your new shader render function.

Enjoy crt shader in your game.

crt example : https://www.youtube.com/watch?v=2ekJdkXC4iM
