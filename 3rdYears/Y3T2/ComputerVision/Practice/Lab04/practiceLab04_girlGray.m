im = imread('girl_gray.jpg');
%1
h1 = fspecial("average", [3, 3]);
img_girl1 = imfilter(im, h1);
subplot(2, 2, 1);
imshow(img_girl1);
title('Image 01')
%4
h4 = fspecial('average', [3, 3]);
img_girl4 = imadjust(im, stretchlim(im), []);
img_girl4 = imfilter(img_girl4, h4);
subplot(2, 2, 4);
imshow(img_girl4);
title('Image 04');
%2 Salt - and -Paper
img_girl2 = adapthisteq(img_girl4);
subplot(2, 2, 2);
imshow(img_girl2);
title('Image 02');
%3
img_girl3 = histeq(img_girl4);
img_girl3 = imfilter(img_girl3, h4);
img_girl3 = imadjust(img_girl3, stretchlim(img_girl3), []);
h3 = fspecial('gaussian', [3, 3], 0.5);
img_girl3 = imfilter(img_girl3, h3);
subplot(2, 2, 3);
imshow(img_girl3);
title('Image 03');