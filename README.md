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

crt example : https://www.youtube.com/watch?v=2ekJdkXC4i

my works using this class :

Myth of Charlie ：https://jingshing.itch.io/myth-of-charlie

DragonCastle：https://jingshing.itch.io/dragoncastle

我的OpenGL啟蒙者。ModernGL在很多方面都方便很多，不過這也是弊端，雖然和pygame的兼容性很高，不過不是一條長遠的道路。

想要過過shader的癮可以嘗試，但最好淺嘗，ModernGL本身的缺陷很多，打包時很痛苦。

如果只是要做pygame項目是完全夠用的。歡迎參考我有使用這個shader的作品：

Myth of Charlie ：https://jingshing.itch.io/myth-of-charlie

DragonCastle：https://jingshing.itch.io/dragoncastle

