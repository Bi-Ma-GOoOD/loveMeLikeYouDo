im = imread('space2.jpg');

%1
subplot(1, 3, 1);
imshow(im);
title('Original');
%2
h2 = fspecial("average", [3, 3]);
img_space2 = imadjust(im, stretchlim(im), [0.0, 1.0]);
img_space2 = imfilter(img_space2, h2);
subplot(1, 3, 2);
imshow(img_space2);
title('Image 02')
%3
img_space3 = adapthisteq(img_space2);
subplot(1, 3, 3);
imshow(img_space3);
title('Image 03');