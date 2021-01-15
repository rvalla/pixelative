![icon](https://gitlab.com/azarte/pixelative/-/raw/master/assets/img/logo_64.png)

# pixelative: attractortive

There are many ways to draw *strange attractors*. I designed a *canvas* to control color behavior. Basically there
is an *Attractor* object which builds itself and which is painted by *AttracCanvas*. Points are mapped in the canvas
stretching the attractor up to the edges so you can change the attractor's aspect ratio.  
Sometimes two or more points end in the same pixel (depending on attractor's density and the size of the canvas). In
such cases there are two *color modes*. In *fixed mode* color does not change, in *additive mode* a pixel in which
more than one point are located the color is the result of the sum of the succession c/2^p (p is the number of points
located en the pixel).  

![attractors](https://gitlab.com/azarte/pixelative/-/raw/master/assets/img/attractor_aspect.jpg)

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).
