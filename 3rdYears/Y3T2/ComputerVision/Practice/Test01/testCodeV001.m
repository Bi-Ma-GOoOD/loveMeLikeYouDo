im = imread('dark02.jpg');

im = rgb2gray(im);

h = histeq(im);
j = adapthisteq(im);
k = adapthisteq(h);
s = imadjust(h, stretchlim(h), []);

subplot(3, 3, 1);
imshow(im);
title('Original');

subplot(3, 3, 2);
imshow(h);
title('Histeq');

subplot(3, 3, 3);
imshow(j);
title('AdapThisTeq - V01');

subplot(3, 3, 4);
imshow(k);
title('AdapThisTeq - V02');

subplot(3, 3, 5);
imshow(s);
title('ImAdjust');